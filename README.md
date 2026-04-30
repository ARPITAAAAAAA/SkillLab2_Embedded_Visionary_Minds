# SKILL LAB PRATICAL HACKATHON

## Final Project README

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`SKILLLAB_PROR-2026-TeamName`

### Example

`SKILLLAB_PROR-2026-AuroWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---
# 1. Team Identity  

## 1.1 Studio / Group Name: Visionary Minds 
Project^2  

## 1.2 Team Members  

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|------|--------------|----------------|----------------------------------|
| Mehar Jha | Documentation | Coding & Testing | Material Handling, Hardware Setup, Troubleshooting |
| Arpita Yaligeti | Electronics / Hardware Testing | Coding | Hardware Setup, Sensor Integration, Debugging |
| Prashansa Vishe | Electronics / Coding | Documentation | Sensor Calibration, System Testing, Circuit Assembly |
| Ansh Upadhyay | Electronics / Documentation | Coding | Material Handling, Hardware Assembly |

---

## 1.3 Project Title  
**Smart Robo Car with Path Following and Obstacle Detection**

(because we wanted to learn robotics and understand how smart vehicles detect paths and obstacles.)

---

## 1.4 One-Line Pitch  

A smart robo car system that follows a path using IR sensors, detects obstacles using an ultrasonic sensor, and displays obstacle alerts on an LCD screen.

---

## 1.5 Expanded Project Idea  

Our project is a smart autonomous robo car designed to follow a predefined path and avoid obstacles using multiple sensors. The car uses **IR sensors** to detect and follow a path, an **ultrasonic sensor** to detect obstacles in front of the car, and a **touch sensor** to provide collision safety.  

When an obstacle is detected, the system stops the motors and displays **"Object Detected"** on the LCD screen. This demonstrates how intelligent vehicles sense their surroundings and respond automatically.

The system uses **Raspberry Pi**, **motor drivers**, **IR sensors**, **ultrasonic sensors**, and **LCD display modules** to perform detection, decision-making, and movement control.

---

# 2. Inspiration  

## 2.1 References  

We wanted to gain practical experience in robotics, sensors, and embedded systems by building a project that is both educational and useful. The idea of combining IR sensors and ultrasonic sensors helped us understand how multiple technologies work together.

---

## 2.2 Original Twist  

Our project combines **path following**, **obstacle detection**, and **LCD alert display** into a single system. The addition of an **LCD display to show obstacle detection messages** makes the project more interactive and user-friendly compared to basic line follower robots.

---

# 3. Project Intent  

## 3.1 User Journey  

1. The user switches ON the robo car.
2. The car starts moving automatically.
3. IR sensors detect the black path.
4. The car follows the path continuously.
5. If an obstacle appears, the ultrasonic sensor detects it.
6. The motors stop immediately.
7. The LCD displays **"Object Detected"**.
8. When the path is clear, the car continues moving.

---

# 4. Definition of Success  

## 4.1 Definition of Usable  

The system is usable when the robo car follows the path correctly and stops when an obstacle is detected.

---

## 4.2 Minimum Usable Version  

- Motors move correctly  
- IR sensors follow line  
- Ultrasonic detects obstacle  
- Car stops on obstacle  

---

## 4.3 Stretch Features  

- LCD display message  
- LED obstacle indication  
- Speed control  
- Mobile control (future)

---

# 5. System Overview  

## 5.1 Project Type  

- [x] Electronics-based  
- [x] Sensor-based  
- [x] Motorized  
- [x] Screen/UI-based  
- [x] Fabricated structure  

---

## 5.2 High-Level System Description  

The system works using sensors and motors controlled by Raspberry Pi.

**Input:**  
- IR Sensors → detect line  
- Ultrasonic Sensor → detect obstacle  
- Touch Sensor → detect collision  

**Processing:**  
- Raspberry Pi reads sensor data  
- Makes movement decision  

**Output:**  
- Motors rotate wheels  
- LCD displays messages  
- Car stops when obstacle detected  

---

## 5.3 Input / Output Map  

| System Part | Type | What It Does |
|-------------|------|---------------|
| IR Sensor | Input | Detects path |
| Ultrasonic Sensor | Input | Detects obstacles |
| Touch Sensor | Input | Detects collision |
| Raspberry Pi | Processing | Controls logic |
| Motor Driver | Output | Drives motors |
| LCD Display | Output | Shows obstacle message |

---

# 7. Electronics Planning  

## 7.1 Electronics Used  

| Component | Quantity | Purpose |
|----------|----------|--------|
| Raspberry Pi | 1 | Main controller |
| L298N Motor Driver | 1 | Motor control |
| BO Motors | 4 | Movement |
| IR Sensors | 2 | Path detection |
| Ultrasonic Sensor | 1 | Obstacle detection |
| Touch Sensor | 1 | Collision detection |
| LCD Display | 1 | Display message |


---

## 7.2 Wiring Plan  

The Raspberry Pi is connected to the **L298N motor driver** using GPIO pins to control motor direction.  

The **IR sensors** are connected to input GPIO pins to detect the line path.  

The **ultrasonic sensor** uses Trigger and Echo pins to measure distance from obstacles.  

The **touch sensor** is connected to detect physical collision.  

The **LCD display** is connected using I2C pins to show messages such as **"Object Detected"**.  

All components share a **common ground** for stable operation.

---

# 8. Software Planning  

## 8.2 Software Logic / Algorithm  

- **Startup:**  
  Initialize GPIO pins, sensors, motors, and LCD display.

- **Sensor Reading:**  
  Continuously read IR sensor values and ultrasonic distance.

- **Decision Logic:**  
  - If IR detects line → move forward  
  - If ultrasonic detects obstacle → stop motors  
  - Display "Object Detected" on LCD  
  - If touch sensor pressed → stop immediately  

- **Output Behavior:**  
  Motors rotate wheels based on commands.

- **Reset Behavior:**  
  Stop motors if error detected.

---

# 13. Biggest Unknown Right Now  

The biggest uncertainty is maintaining stable sensor readings and ensuring accurate obstacle detection without false triggers.

---

# 17. Final Outcome  

## 17.1 Final Description  

The final system is a smart robo car capable of following a line path using IR sensors and detecting obstacles using an ultrasonic sensor. When an obstacle is detected, the car stops immediately and displays **"Object Detected"** on the LCD screen. The system successfully demonstrates autonomous navigation and safety detection.

---

## 17.2 What Works Well  

- Accurate line following  
- Reliable obstacle detection  
- Clear LCD display alerts  
- Stable motor movement  

---

## 17.3 What Still Needs Improvement  

- Improve speed control  
- Reduce sensor noise  
- Improve battery life  

---

## 17.4 What Changed From Original Plan  

Initially, the project only included line following. Later, obstacle detection and LCD display features were added to improve functionality.

---

# 18. Reflection  

## 18.2 Technical Reflection  

We learned how to connect sensors to Raspberry Pi, control motors using drivers, read sensor data, and implement logic for autonomous movement. We also learned debugging techniques and hardware integration.

---

## 18.4 If You Had One More Hour  

We would add Bluetooth or WiFi control to manually control the robo car from a mobile device.


