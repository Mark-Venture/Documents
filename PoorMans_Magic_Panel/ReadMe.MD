# Poor Man's Magic Panel

The original Magic Panel can be purchased from Printed-Droid.com.  It is an 8x8 LED Panel controlled by an ESP32 Mini to do shapes, patterns, text and such.

Marc Frank has also devised a simple Magic Panel by joining two W2812 4x4 LED panels,  to make a 4x8 matrix, and created a mounting system available on Maker World https://makerworld.com/en/models/2799417-r2d2-magic-panel-mk3-4#profileId-3114056

While Marc's panel can be enabled as an LED strand on a DroidLink Slave, specifying 32 as the LED count, you could only send the regular LED commands

This project takes the ESP32 Mini code from the original Magic Panel, and adopts it to a 4x8 Panel. While some of the Pattern Shapes or Advanced Animation Patters can not be properly sized for 4x8 matrix and still look presentable,  most of the commands still work.   

The Command Cheat Sheet shows what commands are available.  

Parts Required:

ESP32-C3 Mini  w/Breakout board   https://a.co/d/0cywsGyt
Two W2812 4x4 LED Panels

