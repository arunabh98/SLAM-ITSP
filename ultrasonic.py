# Import required Python libraries
import time
import RPi.GPIO as GPIO
GPIO.cleanup()
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
ultrasonic1_pins = [7, 8]
ultrasonic2_pins = [21, 20]
ultrasonic3_pins = [5, 6]
ultrasonic4_pins = [15, 14]


def get_ultrasonic(ultrasonic_number):
    try:
        # Define GPIO to use on Pi
        if ultrasonic_number == 1:
            GPIO_TRIGGER = ultrasonic1_pins[0]
            GPIO_ECHO = ultrasonic1_pins[1]
        if ultrasonic_number == 2:
            GPIO_TRIGGER = ultrasonic2_pins[0]
            GPIO_ECHO = ultrasonic2_pins[1]
        if ultrasonic_number == 3:
            GPIO_TRIGGER = ultrasonic3_pins[0]
            GPIO_ECHO = ultrasonic3_pins[1]
        if ultrasonic_number == 4:
            GPIO_TRIGGER = ultrasonic4_pins[0]
            GPIO_ECHO = ultrasonic4_pins[1]

        print "Ultrasonic Measurement"

        # Set pins as output and input
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
        GPIO.setup(GPIO_ECHO, GPIO.IN)      # Echo

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER, False)

        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop - start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2

        print "Distance : %.1f" % distance
        return distance
    except KeyboardInterrupt:
        GPIO.cleanup()

    # Reset GPIO settings
    GPIO.cleanup()
