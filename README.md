# Autonomous Driving Decision System

This project demonstrates a simplified autonomous driving decision system built using Python.

## Overview
Autonomous vehicles rely on multiple sensors to understand their environment and make driving decisions. This project simulates a decision-making module that processes sensor data and determines appropriate vehicle actions.

The system analyzes inputs such as:
- Distance to nearby vehicles
- Road conditions
- Relative speed of surrounding vehicles

Based on this data, the system decides whether the vehicle should:
- Accelerate
- Maintain speed
- Slow down
- Stop

## Features
- Sensor data processing
- Decision-making logic for vehicle control
- Simulation of autonomous driving behavior
- Modular design for future expansion

## Technologies Used
- Python
- NumPy (optional for data processing)

## Decision Algorithm

The system follows a simple decision process:

1. Collect sensor inputs (distance, speed, obstacles).
2. Compare with predefined safety thresholds.
3. Determine the appropriate driving action.
4. Execute the decision logic.

Example decision flow:

If distance < safe_distance:
slow_down()
Else if road_clear:
accelerate()
Else:
maintain_speed()


## Future Improvements
- Integration with real sensor datasets
- Machine learning for decision prediction
- Advanced obstacle detection algorithms
- Real-time vehicle simulation

## Author
Joshua Karan Bibeiro
