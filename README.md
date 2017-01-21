# robot-movement
This is a basic application for controlling a Raspberry Pi robot using a smartphone. Watch the video `video.mp4` to see it in action!

The GPIO output is handled by a Python program and the input is handled by a Node.js server.

## Hardware
The standard settings are for a robot with a L293D motor driver and the GPIO pins of the Raspberry Pi connected as follows:
```
Enable 1 -> Pin 36
Input 1  -> Pin 38
Input 2  -> Pin 34
Enable 2 -> Pin 33
Input 3  -> Pin 35
Input 4  -> Pin 37
```
If you prefer to use other GPIO pins, edit the `control.py` file in the `python` directory.

## Software
First install Node.js, Socket.IO and socketIO-client for Python on your Raspberry Pi. Then clone the repository to your Raspberry Pi, open a terminal and `cd` into the `nodejs` directory and run `nodejs server.js`. Finally use `cd` to get into the `python` directory run the Python program using `sudo python3 control.py`.

Use your smartphone to connect to `your-local-ip-address:3000`, which is the input server. The Python program automatically connects to `localhost:3001`, which is the output server.
