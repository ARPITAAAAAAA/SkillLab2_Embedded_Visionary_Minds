import serial
import time
import sys
import tty
import termios
import threading

# These are the ones you asked for:
try:
    import RPi.GPIO as GPIO
    import cv2
except ImportError as e:
    print(f"ERROR: {e}")
    print("Run: sudo apt-get install python3-rpi.gpio python3-opencv")
    sys.exit()

# --- 1. SETUP ---
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# GPIO Setup
GPIO.setmode(GPIO.BCM)
IR_LEFT, IR_RIGHT = 17, 27
GPIO.setup(IR_LEFT, GPIO.IN)
GPIO.setup(IR_RIGHT, GPIO.IN)

# AI Models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
age_net = cv2.dnn.readNetFromCaffe("deploy_age.prototxt", "age_net.caffemodel")
AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# State Control
is_running = False
is_stalled = False

# --- 2. KEYBOARD LISTENER ---
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
    global is_running
    while True:
        k = getch().lower()
        if k == 'w': 
            is_running = True
            print("\n[SYSTEM] STARTING AUTO-DRIVE...")
        elif k == 's': 
            is_running = False
            ser.write(b'S')
            print("\n[SYSTEM] STOPPED")
        elif k == 'q':
            is_running = False
            ser.write(b'S')
            os._exit(0)

# --- 3. CAMERA AI LOGIC ---
def camera_brain():
    global is_stalled
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0 and is_running and not is_stalled:
            is_stalled = True
            ser.write(b'S') # Stop for scan
            print("\n[AI] HUMAN DETECTED!")
            
            # Age analysis
            (x, y, w, h) = faces[0]
            blob = cv2.dnn.blobFromImage(frame[y:y+h, x:x+w], 1.0, (227, 227), (78.4, 87.7, 114.8))
            age_net.setInput(blob)
            age = AGE_LIST[age_net.forward()[0].argmax()]
            
            print(f"[AI] Estimated Age: {age}. Stalling 5s...")
            time.sleep(5)
            is_stalled = False
            print("[AI] Resuming...")
            
        cv2.imshow('Vision', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cap.release()

# --- 4. EXECUTION ---
# Launch background tasks
threading.Thread(target=keyboard_monitor, daemon=True).start()
threading.Thread(target=camera_brain, daemon=True).start()

print("Ready. Press 'W' to begin.")

try:
    while True:
        if is_running and not is_stalled:
            l_val = GPIO.input(IR_LEFT) == 0  # 0 is usually path/light
            r_val = GPIO.input(IR_RIGHT) == 0

            if l_val and r_val: ser.write(b'F')
            elif l_val: ser.write(b'L')
            elif r_val: ser.write(b'R')
            else: ser.write(b'S')
        
        time.sleep(0.05)

except KeyboardInterrupt:
    ser.write(b'S')
    GPIO.cleanup()
