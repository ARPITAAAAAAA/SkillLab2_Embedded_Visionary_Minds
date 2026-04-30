import serial
import time
import RPi.GPIO as GPIO

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

GPIO.setmode(GPIO.BCM)
Ir_PIN = 22
GPIO.setup(Ir_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("FORCE TEST: Hold the ir sensor to spin motors...")

try:
    while True:
        # If holding the sensor makes it move, logic is working
        if GPIO.input(Ir_PIN) == 0: 
            ser.write(b'F')
            print("\rDRIVING...", end="")
        else:
            ser.write(b'S')
            print("\rIDLE   ", end="")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
