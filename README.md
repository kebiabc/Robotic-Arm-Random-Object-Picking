# Robotic Arm Random Object Picking Project

This project implements a system for random object picking using a robotic arm, combining computer vision, object detection, and robot control. The solution is designed for applications in industrial automation, warehousing, and production lines.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Overview](#system-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Future Work](#future-work)
- [License](#license)

---

## Introduction

This project focuses on enabling a robotic arm to perform random object picking tasks. Using computer vision and object detection algorithms, the system identifies objects in a cluttered environment and calculates their positions and orientations for precise picking.

### Applications

- Industrial automation  
- Logistic systems  
- Warehousing and sorting  

---

## Features

- **Object Detection**: YOLO-based object detection for identifying objects in cluttered environments.
- **3D Pose Estimation**: Accurate pose estimation using depth cameras.  
- **Robot Control**: Seamless control of robotic arms (UR/ABB supported).  
- **Grasp Planning**: Efficient grasp planning for unstructured scenarios.  
- **Visualization**: Real-time visualization of object detection and arm movements.  

---

## System Overview

The system consists of the following components:

1. **Vision System**:  
   - A depth camera mounted on the robotic arm's end-effector.  
   - Object detection and pose estimation algorithms.  

2. **Control System**:  
   - Robotic arm (AUBO i10H).  
   - Gripper with RS485 communication.  

3. **Processing Pipeline**:  
   - Capturing object information from the vision system.  
   - Sending grasp commands to the robotic arm.  

---

## Installation

### Prerequisites

- **Operating System**: Ubuntu
- **Languages**: Python 3.8+  
- **Dependencies**: 
  - OpenCV
  - PyTorch
  - NumPy
  - ROS 1

### Setup

### Configuration


### Future Work
Improved Grasp Planning: Add support for soft-body and irregular object handling.
Optimized Detection: Improve detection accuracy in low-light conditions.
Scalability: Expand support for additional robotic arm models.
### License
This project is licensed under the MIT License. See the LICENSE file for details.
