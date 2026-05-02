import serial
import time
import sys
import tty
import termios
import threading
import os

# --- 1. SETUP & LIBRARY CHECK ---
try:
    import RPi.GPIO as GPIO
    import cv2
except ImportError:
    print("ERROR: Missing libraries. Run: sudo apt-get install python3-rpi.gpio python3-opencv")
    sys.exit()

# Set working directory for AI model files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Setup Serial for Arduino
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except:
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    except:
        print("CRITICAL ERROR: Arduino not found.")
        sys.exit()

# Wait for Serial to stabilize
time.sleep(2)

# GPIO Setup for IR Sensors
GPIO.setmode(GPIO.BCM)
IR_LEFT, IR_RIGHT = 17, 27
GPIO.setup(IR_LEFT, GPIO.IN)
GPIO.setup(IR_RIGHT, GPIO.IN)

# --- 2. AI MODELS (LOCAL PATHS) ---
cascade_path = os.path.join(base_dir, "haarcascade_frontalface_default.xml")
proto_path = os.path.join(base_dir, "deploy_age.prototxt")
model_path = os.path.join(base_dir, "age_net.caffemodel")

# Safety Check: Ensure all files exist
for f in [cascade_path, proto_path, model_path]:
    if not os.path.exists(f):
        print(f"CRITICAL ERROR: File missing -> {f}")
        sys.exit()

face_cascade = cv2.CascadeClassifier(cascade_path)
age_net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# State Variables
mode = "manual"  # 'manual' or 'auto'
is_stalled = False

# --- 3. INPUT & CAMERA LOGIC ---

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def keyboard_monitor():
    global mode
    print("\n--- CONTROL SCHEME ---")
    print("M = MANUAL Mode | K = AUTO (IR) Mode")
    print("W/A/S/D = Manual Drive | SPACE = Stop | Q = Quit\n")
    
    while True:
        key = getch().lower()
        
        if key == 'k':
            mode = "auto"
            print("\n[MODE] Switched to AUTO (IR Path Following)")
        elif key == 'm':
            mode = "manual"
            ser.write(b'S')
            print("\n[MODE] Switched to MANUAL Control")
        
        # Manual Overrides (only if in manual mode)
        elif mode == "manual":
            if key == 'w': ser.write(b'F')
            elif key == 's': ser.write(b'B')
            elif key == 'a': ser.write(b'L')
            elif key == 'd': ser.write(b'R')
            elif key == ' ': ser.write(b'S')
        
        if key == 'q':
            ser.write(b'S')
            os._exit(0)

def camera_brain():
    global is_stalled
    # Primary HD Camera on /dev/video0
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(3, 320)
    cap.set(4, 240)
    
    while True:
        ret, frame = cap.read()
        if not ret: continue
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Human Detection Logic
        if len(faces) > 0 and not is_stalled:
            is_stalled = True
            ser.write(b'S') # Stop motors for identification
            print("\n[AI] FACE DETECTED!")
            
            (x, y, w, h) = faces[0]
            face_img = frame[y:y+h, x:x+w].copy()
            blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), (78.4, 87.7, 114.8), swapRB=False)
            
            # Predict Age
            age_net.setInput(blob)
            age = AGE_LIST[age_net.forward()[0].argmax()]
            
            # Show Age in Green Text on Frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Age: {age}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow('Car Vision', frame)
            cv2.waitKey(1)
            
            print(f"[AI] Estimated Age: {age}. Stalling 2s...")
            time.sleep(2) # 2-second stall as requested
            
            is_stalled = False
            print("[AI] Resuming...")
            time.sleep(1) # Cooldown
            
        cv2.imshow('Car Vision', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cap.release()

# --- 4. MAIN NAVIGATION LOOP ---
threading.Thread(target=keyboard_monitor, daemon=True).start()
threading.Thread(target=camera_brain, daemon=True).start()

try:
    while True:
        # Auto-Drive Mode with IR Sensors
        if mode == "auto" and not is_stalled:
            l_val = GPIO.input(IR_LEFT) == 0
            r_val = GPIO.input(IR_RIGHT) == 0

            if l_val and r_val:
                ser.write(b'F')
            elif l_val:
                ser.write(b'L')
            elif r_val:
                ser.write(b'R')
            else:
                ser.write(b'S')
        
        time.sleep(0.05)

except KeyboardInterrupt:
    ser.write(b'S')
    GPIO.cleanup()
