# 2π-Mapper

This is the code repository for my Summer Project in IIT Bombay.

This project involved developing a robot that maps an unknown environment through feedback using ultrasonic distance sensors 
located in all four directions, and the live map along with the movements of the robot, is updated and displayed on the laptop 
screen in real time.

The main algorithm used in mapping the environment can be found in [ITSP.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/ITSP.py). <br/>
The code for interfacing the various components is listed below:
- Ultrasonic sensors-[ultrasonic.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/ultrasonic.py)
- stepper motors-[Rpi_stepper.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/Rpi_stepper.py)
- magnetometer-[imu.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/imu.py)

For sending data from [Raspberry Pi](https://www.raspberrypi.org/) we used Bluetooth and the 
code for sending and receiving data can be found in [send_data.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/send_data.py) 
and [recieve_data.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/recieve_data.py).
 
 For the graphical output of the map we used [Pygame](http://www.pygame.org/hifi.html) and code can be found in 
 [output.py](https://github.com/Arunabh98/SLAM-ITSP/blob/master/output.py).
 
 We have made a vedio of the project which you can view over [here](https://youtu.be/W7FHppzeQhM).
