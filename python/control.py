import RPi.GPIO as GPIO
from socketIO_client import SocketIO

# Output pin variables
M1e = 36
M1a = 38
M1b = 40
M2e = 33
M2a = 35
M2b = 37

# Movement list, which pins to be turned on to go in a specific direction
movement = [
    [
        # Drive forwards
        (M1e, GPIO.HIGH),
        (M1a, GPIO.HIGH),
        (M1b, GPIO.LOW),
        (M2e, GPIO.HIGH),
        (M2a, GPIO.HIGH),
        (M2b, GPIO.LOW)
    ],
    [
        # Drive backwards
        (M1e, GPIO.HIGH),
        (M1a, GPIO.LOW),
        (M1b, GPIO.HIGH),
        (M2e, GPIO.HIGH),
        (M2a, GPIO.LOW),
        (M2b, GPIO.HIGH)
    ],
    [
        # Spin right
        (M1e, GPIO.HIGH),
        (M1a, GPIO.HIGH),
        (M1b, GPIO.LOW),
        (M2e, GPIO.HIGH),
        (M2a, GPIO.LOW),
        (M2b, GPIO.HIGH)
    ],
    [
        # Spin left
        (M1e, GPIO.HIGH),
        (M1a, GPIO.LOW),
        (M1b, GPIO.HIGH),
        (M2e, GPIO.HIGH),
        (M2a, GPIO.HIGH),
        (M2b, GPIO.LOW)
    ],
    [
        # Full stop
        (M1e, GPIO.LOW),
        (M1a, GPIO.LOW),
        (M1b, GPIO.LOW),
        (M2e, GPIO.LOW),
        (M2a, GPIO.LOW),
        (M2b, GPIO.LOW)
    ]
]

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(M1e, GPIO.OUT)
GPIO.setup(M1a, GPIO.OUT)
GPIO.setup(M1b, GPIO.OUT)
GPIO.setup(M2e, GPIO.OUT)
GPIO.setup(M2a, GPIO.OUT)
GPIO.setup(M2b, GPIO.OUT)
print("GPIO set up successful")


# Movement function
def move(index):
    """Turns on the correct GPIO pins to move the robot"""
    print(index)
    for t in movement[index]:
        GPIO.output(t[0], t[1])


def connect():
    """Print a message when a connection to the output server is established"""
    print("Connected")


def event(*args):
    """Gets a response from the output server and calls the move function"""
    for index, on in enumerate(args[0]):
        # Find the first direction
        if on:
            move(index)
            break
        # If no movement was detected, full stop
        if index == len(args[0])-1:
            move(4)

try:
    # Connect to Node.js server
    print("Connecting to output server")
    socketIO = SocketIO('localhost', 3001, )
    socketIO.on('connect', connect)
    socketIO.on('reconnect', connect)
    socketIO.on('event', event)

    # Wait for events
    socketIO.wait()

finally:
    # Clean up GPIO
    GPIO.cleanup()
    print("Clean up successful")
