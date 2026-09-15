# My Sovol SV08 Max Printer Settings #


I started with a Bambu Lab A1 Mini,  then several months later I got a Bambu A1 Combo (the A1 Printer with AMS Lite).  Bambu really makes their printers for the casual user.  Someone who wants to spend more time printing than tinkering.  Their Printer and Filament profiles are dialed in real well that a user can just load a model, select the filament they are using and hit print, and they'll get a very good looking print. 

Mr. Baddeley has the R2 parts sliced for 250mm cubed print volume printers, so I was able to print R2 and glue and screw it together using the A1 Combo (256mm cubed volume), and the A1 Mini (185mm cubed volume) for smaller parts.    He also has the parts for 500 cubed print volume printers, so there is less gluing, screwing and seams.  

I picked up a Sovol SV08 Max which is 500mm cubed print volume.  Unfortunately its more for those who like to tinker and tweak.  Who like to work on their 3D printer as much as they like to print.  This posed a challenge for me trying to get it to print nice. The printer and filament profiles for Sovol printers is not nearly dialed in. I had to test, calibrate, test print, make adjustments, and so on until I finally got it looking pretty good. I still have some tweaks that I need to make, but its about 90 to 95% there, and I'm happy with the R2 parts I've printed so far.  

## What is here... ##

The files and folders under this section contain the profile settings I use in Orca 2.4.2 Slicer to 3d Print my R2 D2.   You can do a File -> Import -> Import Configs, and load them up.   You'll see process for the body and dome, as well as my modified Sunlu PETG filament profile.  

Please note these Orca settings were only part of the process getting my Sovol SV08 Max dialed in.  

If you are using PETG or advanced filaments, make sure you try them before printing.  I use the Polydryer and boxes.  I have an XL Box for my 3KG rolls.   For PETG 3KG spools, I dried them for 15 hours before printing.  1KG spools I dried for 10 hours. this really helped the print quality.

I also included my Printer.cfg which has various changes.  Each change is commented, so you can open in your favorite editor and search for the comments to see what has changed.  

## Recreating, rather than just loading...#

If you'd rather not load someone else's settings,  Here are the steps I took:

1. Follow this post -> [https://www.facebook.com/share/p/1DREUM6zfc/]   There are tweaks for the Printer.CFG among others.  I've uploaded mine here, with comments added inline for on what I changed. 

2.  Calibrate the filaments, and save as updated Filament Profiles.   I used this tool -> [https://github.com/tayloraaro.../Filament_Calibration_Wizard](https://github.com/tayloraaron078-tech/Filament_Calibration_Wizard?fbclid=IwY2xjawUOgGVwZG9mBWV4dG4DYWVtAjEwAGJyaWQRMTlFc2FMOG9pZE9ZSXQ3V3FzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEeyIA4kRBEyxxZmNqTAXwOfxhHU3AV-ErHRewNPmW4zjsoThynI7bS-0_ybPw_aem_VRB_H0xyQ9vzxn7O419eng)  While my settings could be used as a base, there may be variations between the printers, so you'll really want to run through this with yours. Remember, you'll need to calibrate for each size nozzle. So if you plan to print with .4mm and .6mm  you'll need to make sure you calibrate your filament with each.  

3. After that, I made the adjustments to the process settings in Orca.  I can't remember all the tweaks. If you don't import my files/settings, you can open the Orca files with WinRar or the like to see the .JSON files inside. 

4.  (STILL TO COME)  I have not yet attempted to check the belt tension in my printer. That is something I will try in the future. 
