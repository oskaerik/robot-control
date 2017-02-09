/**
 * Handles connection with the Node.js server
 */

import React, { Component } from 'react';
import { AppRegistry, View, WebView } from 'react-native';

import socket from 'socket.io-client';

export default class Connection extends Component {
    constructor(props) {
        super(props);

        // Connect to server
        this.socket = socket('192.168.0.106:3000', { transports: ['websocket'] });
        this.socket.on('connect', (socket) => {
            console.log("Connected to server");
        });

        this.lastMotors = [0, 0];
    }

    input(motors) {
        if (JSON.stringify(motors) != JSON.stringify(this.lastMotors)) {
            this.lastMotors = motors;
            console.log(motors);
            this.socket.emit('movement', {motors: motors});
        }
    }
}
