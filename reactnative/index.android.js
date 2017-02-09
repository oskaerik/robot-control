/**
 * A Robot Control app built in React Native
 */
import React, { Component } from 'react';
import { AppRegistry, View, DeviceEventEmitter } from 'react-native';

import Connection from './components/connection/Connection'
import Camera from './components/camera/Camera';

import { SensorManager } from 'NativeModules';

class RobotControlReact extends Component {
    constructor(props) {
        super(props);
        this.connection = new Connection();
        var connection = this.connection;

        SensorManager.startOrientation(100);
        DeviceEventEmitter.addListener('Orientation', function (data) {
            var throttle = 0;
            if (data.roll >= 0 && data.roll <= 90) {
                // Convert to a number between 0 and 1
                throttle = data.roll / 90;
            } else if (data.roll >= 270 && data.roll <= 360) {
                // Convert to a number between -1 and 0
                throttle = (data.roll - 360) / 90;
            }

            var turn = 0;
            if (data.pitch >= 0 && data.pitch <= 90) {
                // Convert to a number between -1 and 0
                turn = -data.pitch / 90;
            } else if (data.pitch >= 270 && data.pitch <= 360) {
                // Convert to a number between 0 and 1
                turn = (360 - data.pitch) / 90;
            }


            // Get motor PWMs
            var motors = [0, 0];

            // Check for spinning in place
            if (turn >= 0.2 && Math.abs(throttle) < 0.2) {
                console.log("spin right");
                motors = [-28*turn*turn + 97*turn + 31, -(-28*turn*turn + 97*turn + 31)];
            } else if (turn <= -0.2 && Math.abs(throttle) < 0.2) {
                console.log("spin left");
                motors = [-(-28*turn*turn - 97*turn + 31), -28*turn*turn - 97*turn + 31];
            } else {
                // Convert throttle to PWM
                if (throttle >= 0) {
                    motors = [-53 * throttle * throttle + 135 * throttle + 19, -53 * throttle * throttle + 135 * throttle + 19];
                } else {
                    motors = [53 * throttle * throttle + 135 * throttle - 19, 53 * throttle * throttle + 135 * throttle - 19];
                }
            }

            // Trim down PWM to "safe" values
            if (motors[0] > 100) {
                motors[0] = 100;
            } else if (motors[0] >= 0 && motors[0] < 50) {
                motors[0] = 0;
            } else if (motors[0] < -100) {
                motors[0] = -100;
            } else if (motors[0] < 0 && motors[0] > -50) {
                motors[0] = 0;
            }
            if (motors[1] > 100) {
                motors[1] = 100;
            } else if (motors[1] >= 0 && motors[1] < 50) {
                motors[1] = 0;
            } else if (motors[1] < -100) {
                motors[1] = -100;
            } else if (motors[1] < 0 && motors[1] > -50) {
                motors[1] = 0;
            }
            motors[0] = Math.round(motors[0]);
            motors[1] = Math.round(motors[1]);

            // Send the motor values
            connection.input(motors);
        });
    }

    render() {
        return (
            <View style={{ flex: 1 }}>
                <Camera />
            </View>
        );
    }
}

AppRegistry.registerComponent('RobotControlReact', () => RobotControlReact);
