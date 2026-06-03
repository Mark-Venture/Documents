# PWM to SUBS-A Translator

DroidLink requires two SBUS-A receivers, one for Drive and one for Dome. 

The HotRC DS-650 comes with the F-06A PWM receiver which only works in PWM mode.   The instructions in this folder give you two options to get up and running temporarily.

[Option 1:\(https://github.com/Mark-Venture/Documents/blob/main/PWM%20to%20SBUSA%20translator/Individual_Translators.md)   Create two translators,  one for drive and one for dome, which wil take the signals from a F-06A PWM Receiver and output it in an SBUS-A format.  Following these instructions you'll make two identical setups, utilizing two ESP32s and Expansion boards,  one set for Dome and one set for Drive. 

[Option 2:](https://github.com/Mark-Venture/Documents/blob/main/PWM%20to%20SBUSA%20translator/Combined_Translator.md)   You'll create on combined translator. It will accept two F-06A receivers as input, translate each separately, and output each as their own SBUS-A formats.   In this setup you'll need only one ESP32 and expansion board.  
