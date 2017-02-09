# robot-movement
This is a basic application for controlling a Raspberry Pi robot using a smartphone. Watch the video `video.mp4` to see it in action!

The GPIO output is handled by a Python program and the input is handled by a Node.js server.

Credits goes to https://github.com/kprimice/react-native-sensor-manager which is used to get input from the phone's gyroscope.

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
If you prefer to use other GPIO pins, edit the `control.py` file in the `python` directory. Also connect your Raspberry Pi camera.

## Software
Install http://www.linux-projects.org/uv4l/ so you can stream video from your Raspberry Pi camera. Then go to `reactnative/components/` and tweak `connection/Connection.js` so it connects to your Raspberry Pi's local IP address and `camera/Camera.js` so it connects to your UV4L streaming server.

Install Node.js and socketIO-client-2 for Python on your Raspberry Pi, then clone the repository to your Raspberry Pi. Run the React Native app on your Android phone. Run `nodejs server.js` in the terminal in the `nodejs` folder to start the server. Finally run `sudo python3 control.py` in the `python` directory. Start the app on your Android phone and start driving!
