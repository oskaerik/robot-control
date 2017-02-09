import RPi.GPIO as GPIO
from socketIO_client import SocketIO

# Variables for pins and frequency
M1e = 36
M1a = 38
M1b = 40
M2e = 33
M2a = 35
M2b = 37
freq = 50

# Set up GPIO mode, pins and PWM
GPIO.setmode(GPIO.BOARD)
GPIO.setup(M1e, GPIO.OUT)
GPIO.setup(M1a, GPIO.OUT)
GPIO.setup(M1b, GPIO.OUT)
GPIO.setup(M2e, GPIO.OUT)
GPIO.setup(M2a, GPIO.OUT)
GPIO.setup(M2b, GPIO.OUT)
pwm1 = GPIO.PWM(M1e, freq)
pwm2 = GPIO.PWM(M2e, freq)

def connect():
    """Print a message when a connection to the output server is established"""
    print("Connected to server")

def movement(*args):
    """Gets a response from the output server and sets the PWM accordingly"""
    print(args[0])

    # Set direction of the motors
    if args[0][0] >= 0:
        # Motor1 forward
        GPIO.output(M1a, 1)
        GPIO.output(M1b, 0)
    else:
        # Motor1 backward
        GPIO.output(M1a, 0)
        GPIO.output(M1b, 1)
    if args[0][1] >= 0:
        # Motor2 forward
        GPIO.output(M2a, 1)
        GPIO.output(M2b, 0)
    else:
        # Motor2 backward
        GPIO.output(M2a, 0)
        GPIO.output(M2b, 1)

    # Set duty cycle of the motors
    pwm1.ChangeDutyCycle(abs(args[0][0]))
    pwm2.ChangeDutyCycle(abs(args[0][1]))

try:
    # Connect to Node.js server
    print("Connecting to output server")
    socketIO = SocketIO('127.0.0.1', 3000)
    socketIO.on('connect', connect)
    socketIO.on('reconnect', connect)
    socketIO.on('movement', movement)

    # Start motor PWM at 0
    pwm1.start(0)
    pwm2.start(0)

    # Wait for events
    socketIO.wait()

finally:
    # Stop motor PWM
    pwm1.stop()
    pwm2.stop()

    # Clean up GPIO
    GPIO.cleanup()
    print("Clean up successful")
