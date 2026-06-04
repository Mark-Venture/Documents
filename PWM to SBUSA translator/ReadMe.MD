# PWM to SUBS-A Translator

DroidLink requires two SBUS-A receivers, one for Drive and one for Dome. 

The HotRC DS-650 comes with the F-06A PWM receiver which only works in PWM mode.   The instructions in this folder give you two options to get up and running temporarily.

Warning: Because this is a translator, and it converts signals, there may be the intermittan "ghost button presses" when sitting idle.  For example, you might hear a sound play, or your utility arms may open, etc. therefore its not recomended for regular use.  You really need to buy real SBUS-A receivers.

[Option 1:](https://github.com/Mark-Venture/Documents/blob/main/PWM%20to%20SBUSA%20translator/Individual_Translators.md)   Create One translator that takes input from One F-06A PWM Receiver and outputs it in an SBUS-A format. This is suitable for a single remote.  If you have two remotes, you'll need to make two translators (two ESP32's with two expansion boards).  

[Option 2:](https://github.com/Mark-Venture/Documents/blob/main/PWM%20to%20SBUSA%20translator/Combined_Translator.md) Create One Translator that will take input from Two F-06A receivers and output as Two SBUS-A.    This option requires only a single ESP32 w/breakout board. 
