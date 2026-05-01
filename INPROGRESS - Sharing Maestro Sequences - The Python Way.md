# Sharing your Maestro Sequences and Settings

Working with setting up my R2D2, I didn't have any of the cool sequences for opening and closing panels like I see in the MrBaddeley FB group.  I was investigating how to share some of those fancy sequences with others to make it easier to those just getting started with Droid building.  This is based on one of the several options I tested.   

When it comes to controlling Servos connected to a Maestro, or any servo controller,  each servo has its own end and neutral points.  No matter what way you get someone else's sequences, you'll need to compensate for this. 

There are several methods to backup/restore Maestro Scripts which can be used to share, but each has their pros and cons.  NONE of them are perfect. This is just one way, and in my opinion its the best because it allows you to bring in sequences created by someone else, keeps them in order, and allows you to add your own Sequences by "save frame" process in Maestro Control Center in the future.   

When you update then run the Python script,  it will take your supplied Settings_OLD.TXT  with the servo min/max/home/neutral for your servos, and make sure the channels section and all sequences are updated for your servo limits, wirting it to an output file called Settings_NEW.TXT that you can load into your Maestro. It can also compensate for any servos which the original author might physcially reversed in their setup (open/close are opposit from your configuration)

**This process is "destructive" it will overwrite any settings or sequences you have on your Maestro**, including servo end points, sequences, scripts, etc. Because we need the Min/Max/Neutral/Home settings of your servos,  we will perform a settings back up as one of the first steps.  You will be able to restore this backup later should you desire to return to the state your Maestro was in before starting this process. 

## Requirements
1. Windows PC, as the Maestro Control Center doesn't run on a Mac.
2. Donor Maestro Settings file with the scrips you want to save on your Maestro
3. Your Servo Settings (min/max) configured Maestro Control Center.
4.  Python installed and configured on your computer:
  - To get Python ready for your automation script, follow these simple steps:
  - 1. Download and Install
    - Go to [python.org/downloads](https://www.python.org/downloads/windows/) and download the latest version for Windows. 
    - Important: When the installer opens, check the box at the bottom that says "**Add Python to PATH**" before clicking Install.
  - 2. Verify Installation
    - Open your Start Menu, type cmd, and press **Enter** to open the Command Prompt.
    - Type `python --version` and press Enter. I
    - If it shows "Python 3.x.x," you are ready to go.
5. The [MaestroUpdateV2.py](https://github.com/Mark-Venture/Documents/blob/main/Downloads/MaestroUpdateV2.py) Python Script file

## Short Overview: 
1.  Rename the Donor Settings file (exported via  Maestro Control Center file -> Save Settings..)  to Settings_OLD.txt
2.  Update the PY with the servos that are mirrored (see line 8),
3.  Update the PY to set the new limits for your servos on lines 13-24.
4.  Run the PY
5.  Import the Settings_NEW.txt it created into the maestro  (File -> Open Settings)

## Here are the detailed steps:

1.  On the Channel Settings tab in Maestro Control Center,  ensure each of your servos are configured for Min and Max. This is crucial for future steps. 
2.  Backup your current settings: In Maestro Control Center, select File -> Save Settings File... When prompted, select the folder you want to save to,  and set the name to something like *My Original Settings.txt* or the like.   You will need this file in future steps!!
3.  Take the Donor Settings file with the sequences you want to use, and rename it to  Settings_OLD.txt
4.  Open the PY file in an editor like Notepad or NotePad++
5.  Open your *My Original Settings.TXT*  , near the top will be the Channels section.  It will contain the Min, Max, Home and Neutral settings for each of your servos.
6.  Update the Servo Limits in the PY file (lines 13-24) with the values you'll see in the Channels section of your *My Original Settings.TXT*  and save the PY file
7.  Run the PY file:   From a CMD prompt, change to the folder holding your  Settings_OLD.txt, and updated Python script, and type  `PY Maestroupdate.py` then press **Enter**
8.  In the Maestro Control Center app,  import the new settings file  by going File -> Open Settings File ->  select the  Settings_New.txt that was just created
9.  If you receive a prompt that the settings file was from a different Maestro,  select OK.  It will import.
10.  Confirm the Sequence order:  In Maestro Control Center,  
11.  Once its imported, you should be able to run the sequences. 
