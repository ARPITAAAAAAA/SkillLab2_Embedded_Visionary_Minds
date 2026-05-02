#include <AFMotor.h>

AF_DCMotor motor1(1); AF_DCMotor motor2(2);
AF_DCMotor motor3(3); AF_DCMotor motor4(4);

void setup() {
  Serial.begin(9600); // Start the "listening" channel at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read(); // Read the character sent from the Pi
    if (cmd == 'F') {
      motor1.setSpeed(200); motor1.run(FORWARD);
      motor2.setSpeed(200); motor2.run(FORWARD);
      motor3.setSpeed(200); motor3.run(FORWARD);
      motor4.setSpeed(200); motor4.run(FORWARD);
    } 
    else if (cmd == 'S') {
      motor1.run(RELEASE); motor2.run(RELEASE);
      motor3.run(RELEASE); motor4.run(RELEASE);
    }
  }
}
