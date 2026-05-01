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
ROBOCAR  

## 1.2 Team Members  

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|------|--------------|----------------|----------------------------------|
| Mehar Jha | Documentation, PPT | Coding & Testing | Material Handling, Hardware Setup, Troubleshooting |
| Arpita Yaligeti | Electronics / Hardware Testing | Coding | Hardware Setup, Sensor Integration, Debugging, Circuit Assembly |
| Prashansa Vishe | Electronics / Coding | Documentation | Sensor Calibration, System Testing |
| Ansh Upadhyay | Electronics / Documentation | Material Handling | Material Handling, Hardware Assembly |

---

## 1.3 Project Title  
**Smart Robo Car with Path Following and Obstacle Detection**

(because we wanted to learn robotics and understand how smart vehicles detect paths and obstacles.)

---

## 1.4 One-Line Pitch  

An autonomous security assistant using computer vision and IR sensors to monitor restricted areas and provide real-time age-detection analytics.

---

## 1.5 Expanded Project Idea  

Our project is a 4WD robotic vehicle designed for surveillance in environments where human presence is restricted or physically demanding, such as high-altitude school corridors, industrial sites, or areas requiring 24/7 monitoring. The project creates a bridge between physical mobility and intelligent data recording by deploying a car on specific floors to act as a mobile sentry. It utilizes a Raspberry Pi for high-level logic and an Arduino for motor control, ensuring a stable and responsive drive system.

The experience centers on automated human detection. Equipped with a camera and OpenCV-powered face recognition, the car identifies individuals and currently estimates their age—a feature designed to log demographic data of visitors in schools or colleges. By replacing the need for elderly security personnel to climb stairs or navigate difficult terrain, GuardianBot provides a safe, efficient, and recordable method of site security.

---

# 2. Inspiration  

## 2.1 References  

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
|`[Project]`|`https://github.com/MichielBontenbal/RoboCar/tree/master`|`Create a robot car with a camera.`|
| `[Project]`| `[https://www.instagram.com/reel/DW4CT7WCDry/?igsh=cXg3dzAxYmdncDBo](https://github.com/GilLevi/AgeGenderDeepLearning/tree/master)` | `Implementing real-time age and gender detection using deep learning models on edge devices.` |
|`[Project]`|`[https://github.com/ArminJo/Arduino-RobotCar](https://youtu.be/RPDQvuAIhus?si=N5lOAUN0sSBaQyfA)`|`Making a Raspberry Pi Pico Bluetooth Control Car`|          

---

## 2.2 Original Twist  

Unlike standard remote-controlled cars, GuardianBot focuses on "floor-specific" intelligence. It is specifically designed for multi-story institutions where it can be left to patrol a single level independently. The original twist lies in its demographic-logging feature (age detection), turning a simple surveillance camera into a data-gathering tool for institutional security.

---

# 3. Project Intent  

## 3.1 User Journey  

A security officer at a large university needs to monitor the 4th-floor labs after hours but cannot easily access the stairs due to physical constraints and the elevators is out of service or electricity is switched off after working hours. They deploy RoboCar on the 4th floor. As the car patrolys, it uses IR sensors to navigate around hallway obstacles. When a student enters the frame, the car's camera triggers a face-detection algorithm, estimates the student's age, and records the event. The officer receives this data remotely, allowing them to verify who is on-site without ever leaving the ground floor.

---

# 4. Definition of Success  

## 4.1 Definition of Usable  

The project is considered "usable" if the car can navigate a flat surface without colliding with obstacles (via IR sensors) while maintaining a stable camera feed that correctly identifies a human face and displays an age estimate on the local monitoring screen.

---

## 4.2 Minimum Usable Version  

- Motors move correctly  
- IR sensors follow line and to avoid crashes   
- Car stops recognizes the age of the human
- Stalls and then starts the movement again  

---

## 4.3 Stretch Features  

- Human-following mode (controlling the car via body position/gestures).
- Full database logging of recognized faces with time-stamps.
- Automated stair-climbing or elevator-calling integration. 
- Mobile control

---

# 5. System Overview  

## 5.1 Project Type  

- [x] Electronics-based
- [ ] Mechanical
- [x] Sensor-based
- [ ] App-connected
- [x] Motorized
- [ ] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [x] Fabricated structure
- [ ] Game logic based
- [ ] Installation (Surveillance) 

---

## 5.2 High-Level System Description  

The system works using sensors and motors controlled by Raspberry Pi.

**Input:**  
- Visual Data: A USB camera captures live frames, focusing on human presence.
- Proximity Data: Dual IR sensors provide real-time distance measurements to detect obstacles  
- Control Input: The system accepts serial commands for Start/Stop.  

**Processing:**  
- Primary Logic (Raspberry Pi): Acts as the high-level controller, running Python-based scripts to process video and perform subtle age detection via OpenCV.
- Motor Control (Arduino): Acts as the hardware interface, translating serial commands from the Pi into motor pulses while monitoring IR sensor interrupts for safety.  

**Output:**  
- Physical Motion: Four BO motors execute movement (Forward, Reverse, Right and Left).
- Safety Response: The motors are automatically disabled if the IR sensors detect an immediate collision risk.
- Information: The system outputs detects the estimated age data.  
**Physical Structure:**
- Chassis: A 4WD mobile platform with a dual-tier arrangement.
- Component Placement: The motors are all placed at the bottom and the Hw-130 aurdino sheild at he top centre for stability, while the Pi "brain" at the top back and camera sit on the top front for a clear field of view.
---

## 5.3 Input / Output Map  

| System Part | Type | What It Does |
|-------------|------|---------------|
| IR Sensor | Input | Detects path |
| Raspberry Pi | Processing | Controls logic |
| HW-130 Motor Shield | Output | Drives motors |
| LCD Display | Output | Shows obstacle message |
| USB Camera | Input | Captures live video feed |
| Serial Connection (USB) | Input/Output | Communication bridge|

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

The primary uncertainty is the accuracy and processing lag of the age-detection model when running on the Raspberry Pi hardware in real-time, especially in variable lighting conditions typical of school hallways. And running raspi wirelessly with power supply if less or finished might stop the working of raspi

---

# 17. Final Outcome  

## 17.1 Final Description  

The final project is a compact, 4WD autonomous vehicle housed in a custom-fabricated chassis. It successfully integrates a Raspberry Pi and Arduino to perform  the robo car to move as needed with the help of ir sensors and real-time age estimation and surveillance. 

---

## 17.2 What Works Well  

- Accurate line following  
- Reliable obstacle detection
- Stable motor environment

---

## 17.3 What Still Needs Improvement  
  
- Sensor accuracy  
- Improve battery life
- Make wireless 

---

## 17.4 What Changed From Original Plan  

Originally, we intended to implement a gesture-based control system where the car would move based on a human's physical position. However, due to time constraints and the complexity of mapping spatial coordinates to motor logic, we pivoted to perfecting the face recognition and age detection features.

---

# 18. Reflection  

## 18.2 Technical Reflection  

We gained significant experience in inter-board communication (Serial between Pi and Arduino) and the nuances of power management—specifically how high-current motor draws can cause logic brownouts if not properly regulated.

---

## 18.4 If You Had One More Hour  

We would add WiFi control to manually control the robo car from a laptop, and add face recognition accurately.


