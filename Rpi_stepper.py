import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
motor1_pins = [4, 17, 23, 24]
motor2_pins = [9, 10, 13, 19]
delay = 20
steps_forward = 47
steps_turn = 38

try:

    def forward(delay, steps):
        for i in range(0, steps):
            setStep(1, [1, 0, 0, 0])
            setStep(2, [0, 0, 0, 1])
            time.sleep(delay)
            setStep(1, [0, 0, 1, 0])
            setStep(2, [0, 1, 0, 0])
            time.sleep(delay)
            setStep(1, [0, 1, 0, 0])
            setStep(2, [0, 0, 1, 0])
            time.sleep(delay)
            setStep(1, [0, 0, 0, 1])
            setStep(2, [1, 0, 0, 0])
            time.sleep(delay)

    def backwards(delay, steps):
        for i in range(0, steps):
            setStep(1, [1, 0, 0, 0])
            setStep(2, [0, 0, 0, 1])
            time.sleep(delay)
            setStep(1, [0, 0, 1, 0])
            setStep(2, [0, 1, 0, 0])
            time.sleep(delay)
            setStep(1, [0, 1, 0, 0])
            setStep(2, [0, 0, 1, 0])
            time.sleep(delay)
            setStep(1, [0, 0, 0, 1])
            setStep(2, [1, 0, 0, 0])
            time.sleep(delay)

    def turn(delay, steps):
        if steps > 0:
            motor1 = 1
            motor2 = 2
        elif steps < 0:
            motor1 = 2
            motor2 = 1
            steps = -steps
        for i in range(0, steps):
            setStep(motor1, [1, 0, 0, 0])
            setStep(motor2, [1, 0, 0, 0])
            time.sleep(delay)
            setStep(motor1, [0, 0, 1, 0])
            setStep(motor2, [0, 0, 1, 0])
            time.sleep(delay)
            setStep(motor1, [0, 1, 0, 0])
            setStep(motor2, [0, 1, 0, 0])
            time.sleep(delay)
            setStep(motor1, [0, 0, 0, 1])
            setStep(motor2, [0, 0, 0, 1])
            time.sleep(delay)


    def setStep(motor, output):
        if motor == 1:
            for pin in range(4):
                GPIO.output(motor1_pins[pin], output[pin])
        if motor == 2:
            for pin in range(4):
                GPIO.output(motor2_pins[pin], output[pin])

    def move_forward():
        for pin in range(4):
            GPIO.setup(motor1_pins[pin], GPIO.OUT)
            GPIO.setup(motor2_pins[pin], GPIO.OUT)
        forward(int(delay) / 1000.0, int(steps_forward))

    def move_left():
        for pin in range(4):
            GPIO.setup(motor1_pins[pin], GPIO.OUT)
            GPIO.setup(motor2_pins[pin], GPIO.OUT)
        turn(int(delay) / 1000.0, int(steps_turn))

    def move_right():
        for pin in range(4):
            GPIO.setup(motor1_pins[pin], GPIO.OUT)
            GPIO.setup(motor2_pins[pin], GPIO.OUT)
        turn(int(delay) / 1000.0, -int(steps_turn))
    move_left()
except KeyboardInterrupt:
    GPIO.cleanup()
