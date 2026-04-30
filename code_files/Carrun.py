import serial
import time
import sys
import tty
import termios

# Setup Serial - Try both common ports
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

time.sleep(2) # Wait for Arduino to wake up

def getch():
    """ Function to read a single keypress from the terminal """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Control your 4WD Car!")
print("W = Forward, S = Backward, A = Left, D = Right, Space = Stop, Q = Quit")

try:
    while True:
        key = getch().lower()
        
        if key == 'w':
            ser.write(b'F')
            print("\rMoving Forward ", end="")
        elif key == 's':
            ser.write(b'B')
            print("\rMoving Backward", end="")
        elif key == 'a':
            ser.write(b'L')
            print("\rTurning Left   ", end="")
        elif key == 'd':
            ser.write(b'R')
            print("\rTurning Right  ", end="")
        elif key == ' ':
            ser.write(b'S')
            print("\rSTOPPED        ", end="")
        elif key == 'q':
            ser.write(b'S')
            print("\rQuitting...    ")
            break
except KeyboardInterrupt:
    ser.write(b'S')
finally:
    ser.close()
