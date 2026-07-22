# Poor Man's Magic Panel

The original Magic Panel can be purchased from Printed-Droid.com.  It is an 8x8 LED Panel controlled by an ESP32 Mini to do shapes, patterns, text and such. https://www.printed-droid.com/kb/magic-panel-32-wireless/

Marc Frank has also devised a simple Magic Panel by joining two W2812 4x4 LED panels,  to make a 4x8 matrix, and created a mounting system available on Maker World https://makerworld.com/en/models/2799417-r2d2-magic-panel-mk3-4#profileId-3114056

While Marc's panel can be enabled as an LED strand on a DroidLink Slave, specifying 32 as the LED count, you could only send the regular LED commands

This project takes the ESP32 Mini code from the original Magic Panel, and adopts it to a 4x8 Panel. While some of the Pattern Shapes or Advanced Animation Patters can not be properly sized for 4x8 matrix and still look presentable (they are marked DISABLED on the command cheat sheet),  most of the commands still work.   

The Command Cheat Sheet shows what commands are available.  

## Parts Required:

[ESP32-C3 Mini  w/Breakout board](https://a.co/d/0cywsGyt)

[W2812 4x4 LED Panels](https://www.aliexpress.us/item/3256807317418742.html?spm=a2g0o.order_list.order_list_main.35.45d71802ouVGM3&gatewayAdapt=glo2usa) QTY 2.

NOTE: BE SURE TO SELECT THE 4x4 16Bit panel before adding to cart!  You need 2.  

## CODE

In the Files sub folder, you will find a ZIP of the files needed.   Open the included  .INO and load into your Arduino IDE,  then write to your ESP32 C3 Mini.  

If you have a different model ESP32,  it might work, but you may or may not need additional modifications to the code. 
