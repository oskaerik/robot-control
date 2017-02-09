/**
 * The camera display
 */

import React, { Component } from 'react';
import { AppRegistry, View, WebView } from 'react-native';

export default class Camera extends Component {
    render() {
        return (
            <View style={{
                flex: 1.5,
                justifyContent: 'center',
                alignItems: 'center',
                backgroundColor: 'powderblue',
            }}>
                <View style={{ width: 240, height: 320 }}>
                    <WebView
                        automaticallyAdjustContentInsets={true}
                        scalesPageToFit={true}
                        startInLoadingState={false}
                        scrollEnabled={false}
                        source={{uri: 'http://192.168.0.106:8080/stream/video.mjpeg'}}
                    />
                </View>
            </View>
        );
    }
}