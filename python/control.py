#import RPi.GPIO as GPIO
from urllib.request import urlopen

# Set up GPIO mode
#GPIO.setmode(GPIO.BOARD)
print("Setting GPIO mode")

# Set up pin variables
M1e = 36
M1a = 38
M1b = 40
M2e = 33
M2a = 35
M2b = 37

# Set up pins
#GPIO.setup(M1e, GPIO.OUT)
#GPIO.setup(M1a, GPIO.OUT)
#GPIO.setup(M1b, GPIO.OUT)
#GPIO.setup(M2e, GPIO.OUT)
#GPIO.setup(M2a, GPIO.OUT)
#GPIO.setup(M2b, GPIO.OUT)
print("Setting up output pins")


# Movement function
def move(direction):
    """Moves the robot"""
    if direction == "up":
        print("UP")
        #GPIO.output(M1e, GPIO.HIGH)
        #GPIO.output(M1a, GPIO.HIGH)
        #GPIO.output(M1b, GPIO.LOW)
        #GPIO.output(M2e, GPIO.HIGH)
        #GPIO.output(M2a, GPIO.HIGH)
        #GPIO.output(M2b, GPIO.LOW)
    elif direction == "down":
        print("DOWN")
        #GPIO.output(M1e, GPIO.HIGH)
        #GPIO.output(M1a, GPIO.LOW)
        #GPIO.output(M1b, GPIO.HIGH)
        #GPIO.output(M2e, GPIO.HIGH)
        #GPIO.output(M2a, GPIO.LOW)
        #GPIO.output(M2b, GPIO.HIGH)
    elif direction == "right":
        print("RIGHT")
        #GPIO.output(M1e, GPIO.HIGH)
        #GPIO.output(M1a, GPIO.HIGH)
        #GPIO.output(M1b, GPIO.LOW)
        #GPIO.output(M2e, GPIO.HIGH)
        #GPIO.output(M2a, GPIO.LOW)
        #GPIO.output(M2b, GPIO.HIGH)
    elif direction == "left":
        print("LEFT")
        #GPIO.output(M1e, GPIO.HIGH)
        #GPIO.output(M1a, GPIO.LOW)
        #GPIO.output(M1b, GPIO.HIGH)
        #GPIO.output(M2e, GPIO.HIGH)
        #GPIO.output(M2a, GPIO.HIGH)
        #GPIO.output(M2b, GPIO.LOW)
    elif direction == "stop":
        print("STOP")
        #GPIO.output(M1e, GPIO.LOW)
        #GPIO.output(M2e, GPIO.LOW)

try:
    print("Set up done")
    running = True

    while running:
        print(urlopen('http://localhost:3001').read().decode('utf-8'))

finally:
    #GPIO.cleanup()
    print("Clean up successful")
