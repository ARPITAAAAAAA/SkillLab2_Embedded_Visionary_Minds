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
|Li-ion Battery Pack| Power | Voltage and current to drive both the processing boards and the high-draw motors |

---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `25.5 cm` |
| Width            | `15 cm` |
| Height           | `12 cm`  |
| Estimated weight | `350-450 g` |

---


# 7. Electronics Planning  

## 7.1 Electronics Used  

| Component | Quantity | Purpose |
|----------|----------|--------|
| Raspberry Pi | 1 | High-level logic & Face Recognition |
| Arduino Uno | 1 | Low-level motor control |
|HW-130 Motor Shield| 1 | Interface for 4 BO Motors |
| BO Motors + wheels | 4 | 4WD Movement |
| IR Sensors | 2 | Path detection |
| USB | 1 | Visual data for age detection |

---

## 7.2 Wiring Plan  

The Raspberry Pi is connected to the **L298N motor driver** using GPIO pins to control motor direction.  

The **IR sensors** are connected to input GPIO pins to detect the line path.  

The **ultrasonic sensor** uses Trigger and Echo pins to measure distance from obstacles.  

The **touch sensor** is connected to detect physical collision.  

The **LCD display** is connected using I2C pins to show messages such as **"Object Detected"**.  

All components share a **common ground** for stable operation.

---

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `DC Power Supply` |
| Voltage required | `~9-12V for motors (via HW-130 driver)`|
| Current concerns | `Motors can draw high current under load, which may cause Raspi to shut down if not enough voltage power supplied wirelessly`|
| Safety concerns  | `Excess power me damage the raspi and extra load on it due to drivers and usb` |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `Python 3`                | `Main programming language for logic and AI integration.`|
| `OpenCV (cv2)`       | `Used for real-time video capture, face detection (Haar Cascades), and DNN inference.` |
| `Caffe Models` | `Pre-trained Deep Neural Networks used for Gender and Age classification.`                      |
| `RPi.GPIO`|`Python library to interface with the hardware IR sensors on the Raspberry Pi pins.`|
|`PySerial`|`Enables communication between the Raspberry Pi and the Arduino/Motor Controller.`|
|`Threading`|`Allows the AI vision, keyboard input, and motor logic to run simultaneously without lagging.`|

## 8.2 Software Logic/Algorithm

The software is built on a multi-threaded architecture to ensure that heavy AI processing does not interfere with real-time motor safety.

- **Startup:**  
 - The system initializes Serial communication (/dev/ttyACM0 or ttyUSB0).
 - GPIO pins are configured for the IR sensors.
 - The pre-trained Caffe models (Age and Gender nets) and Haar Cascade classifiers are loaded into memory.

- **Input Handling:**  
  - Keyboard Thread: Listens for 'W' (Start), 'S' (Stop), or 'Q' (Quit) using termios for raw input.
  - Vision Thread: Captures 320x240 resolution frames (optimized for Pi performance).
  - Sensor Polling: The main loop constantly checks IR sensor states (high/low).

- **Decision Logic:**  
  - Keyboard Thread: Listens for 'W' (Start), 'S' (Stop), or 'Q' (Quit) using termios for raw input.
  - Vision Thread: Captures frames (optimized for Pi performance).
  - Sensor Polling: The main loop constantly checks IR sensor states (high/low).  

- **Navigation Logic (IR Path Following):**
  - Forward ('F'): Both IR sensors detect the path.
  - Left/Right ('L'/'R'): One sensor detects an edge, triggering a corrective turn.
  - Stop ('S'): Both sensors lose the path or the AI triggers a stall.

- **Output Behavior:**  
  - Single-byte characters are sent via Serial to the Arduino to drive the motors.
  - A visual "Car Vision" window displays green bounding boxes around faces with age/gender text overlays.
    
- **Reset Behavior:**  
  Pressing 'Q' or a KeyboardInterrupt triggers a safety stop command and cleans up the GPIO pins before exiting.
  
---
## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `[RASPI]`                        | `1`      | `Yes`   | `No`         | `0`            | `38 Pin ESP32`                | `[To control components]` |
| `[HW-130 Sheild]`                 | `[1]`    | `[Yes]` | `[No]`       | `0`            | `[L298N]`                     | `[To drive both motors]`  |
| `[Arduino Uno]`                 | `[1]`    | `[Yes]` | `[No]`       | `0`            | `[Microcontroller	ATmega328P, 14 GPIO pins (6 provide PWM output for motor speed control)]`                     | `[To generate PWM for motorss]`  |
| `[IR sensors]`                 | `[2]`    | `[Yes]` | `[No]`       | `0`            | `[Digital (High/Low) — compatible with Pi GPIO and Arduino]`                     | `[Fast response detection]`  |
| `[DC Motors and wheel]`          | `[4]`    | `[Yes]`  | `[No]`      | `[0]`        | `[BO Motors and 7 cm wheels]` | `[high torque motors]`    |
| `[Female and male headers]`               | `[1 pack]`    | `[No]`  | `[Yes]`      | `[80]`         |                              |        `For soldering`                   |
| `[Batteries with holder]` | `[1]`    | `[Yes]`  | `[No]`      | `[0]`        |  |          |

## 9.2 Material Justification

Explain why you selected your main materials and components.

**Response:**  
`DC motors (BO motors) were chosen instead of servos or steppers because the system requires continuous rotation for movement rather than precise angular control (Previously, we were considering using steppers as we were planning on tracking movement on the ESP using its relative position from an origin, but since we're using a camera now, this is not required). A motor driver (L298N) was used to allow bidirectional control and speed variation using PWM.`


## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| `BO Motors + Wheels` | `Drive system for car`   | `robu.in`     | `15th April`                | `[Received]` |
| `Buck Converter`     | `Stable power for ESP32` | `local store` | `before testing`            | `[Received]` |
| `Li-ion Batteries`   | `Portable power`         | `local store` | `before testing`            | `Recieved`   |

## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[400]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Available on campus)]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[900]`                     |

## 9.5 Budget Reflection

If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  

---

# 10. Planning the Work

## 10.1 Team Working Agreement

Write how your team will work together.

Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  


## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Concept              | `[Mrugendra]`  | `[Jyoti]`     |
| Electronics          | `[]`           | `[]`          |
| Coding               | `[]`           | `[]`          |
| Mechanical build     | `[]`           | `[]`          |
| Testing              | `[]`           | `[]`          |
| Documentation        | `[]`           | `[]`          |

---

# 6 hour Milestones

## 11.1 6-hour Plan

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Hour   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Day 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Gopal]`           |


## 13.2 Biggest Unknown Right Now

The primary uncertainty is the accuracy and processing lag of the age-detection model when running on the Raspberry Pi hardware in real-time, especially in variable lighting conditions typical of school hallways. And running raspi wirelessly with power supply if less or finished might stop the working of raspi 

---
# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
                       |
## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting (NA),
- 3D printing (NA),
- assembly,
- fastening(NA),
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />


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


