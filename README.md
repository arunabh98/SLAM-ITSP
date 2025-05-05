# 2π-Mapper

*A Raspberry Pi-based robot that performs basic SLAM (Simultaneous Localisation and Mapping) with only low-cost ultrasonic sensors.*

This undergraduate summer project (IIT Bombay) demonstrates how a small mobile robot can **explore an unknown indoor area, build a 13 × 13 occupancy-grid map in real time, and stream that map to a laptop over Bluetooth**. Four HC-SR04 ultrasonic sensors provide distance data in the forward, rear, left and right directions; a digital compass keeps the wheels honest; Pygame renders the evolving map.

---

## Repository guide

| Purpose | File |
|---------|------|
| Main control loop, mapping & path-planning | [`ITSP.py`](ITSP.py) |
| Ultrasonic sensor driver | [`ultrasonic.py`](ultrasonic.py) |
| Stepper-motor control | [`Rpi_stepper.py`](Rpi_stepper.py) |
| Magnetometer (HMC5883L) interface | [`imu.py`](imu.py) |
| Bluetooth uplink Pi → PC | [`send_data.py`](send_data.py) |
| Bluetooth receiver on PC | [`recieve_data.py`](recieve_data.py) |
| Pygame visualiser | [`output.py`](output.py) |

---

## Quick facts

* **Hardware** Raspberry Pi 3 B, 2 × 28BYJ-48 steppers, 4 × HC-SR04, HMC5883L, Li-ion pack  
* **Grid size** 13 × 13 cells (20 cm × 20 cm each)  
* **Update rate** ≈ 2 Hz (sensor read → map update → drive)  
* **Communications** RFCOMM Bluetooth serial link  

---

## Demo

A 90-second video walk-through is available on YouTube:  
<https://youtu.be/W7FHppzeQhM>
