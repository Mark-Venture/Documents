# Creating a DroidLink sequence

Creating a Sequence for Droidlink can seem intimidating for new uers.  This article walks you through the process I recently undertook when I created a "bad motivator" sequence for my R2. See ->  https://photos.app.goo.gl/ienNywkaaeWPuZmq8

The template of this process can be followed for any new sequence you want to make.

The audience for this document is someone who needs extra help and explaination of the process and commands for having DroidLink make your droid do fancy things, beyond what is contained in the initial DroidLink setup documentation. 

While it looks like a long process, that is because this is a complex sequences with a lot of instructions, and there is an explaniation for each step, as well as testing each part individually, to help you understand in order to provide you with the foundation for creating your own sequences.  

As you get started, its helpful to think of DroidLink as a "director" or "manager" so you'll need your servo controllers (Mini Maestro 12/18/24 preferred), dome motor controller (Syren 10 is extremely popular), lights (AstroPixels is very popular),  all installed and ready to go before you install DroidLink, so that DroidLink can send instructions or commands to them.  And this does require you to know how to program your Mini Maestro to move the servos and make Maestro Sequences.  There are plenty of videos online showing how to do this, for Example: https://youtu.be/zkbtoDOW7bI?si=--T-4Xh9ye_oaH8l&t=159  

In my R2, I have a Mini Maestro 12 in the Body connected to DroidLink Slave 2 (commands sent to it by DroidLink start with :BS) with the upper and lower utility arm servos connected. I have a Mini Maestro 24 in the Dome connected to DroidLink Slave 3 (DroidLink commands sent to it start with :DS) that has the pie panel servos connected.  Also connected to DroidLink Slave 3 is an AstroPixels in my dome, with the AstroPixelPlus firmware installed ( https://reeltwo.github.io/AstroPixels-Installer/ ). 

I am usnig the newer AMOLED 2.06" Display with DroidLink, so while I expect the process is similar using the 1.28" Round display, I can not confirm.  

This process creates the sequence as a button under the DOME section on the watch.  If you want to call it, you use the watch.   If you want to trigger it from a DS650 Remote Control's button, you'd need to enter the final sequence as a MS or Master Sequence on the DroidLink Master, and on the DL Master you can then assign it to a RC Button. 

Here are the steps I took. 

1.  Write down what you want your sequence to do. Some will skip this and struggle with "what do I add next"  I came up with a list of the following:
    - Play bad motivator sound
    - Open Pie Panels in crazy sequence
    - Open utility arms
    - Can dome motor move in a "crazy" pattern?
    - play some time of short circuit sound
    - send AstroPixels the "failure" command @APLE20000
    - do I need to reset astropixels?
    - play "we're back" type of sound
    - close pie panels
    - close utility arms

2. Decide what is needed for each of those steps.
   - I need to Program two sequences in Maestro 12,  one to open arms, one to close.  And keep track of their numbers.  (For my Example,  Sequence 3 will OPEN, Sequence 4 will CLOSE)
   - I need Program two sequences in Maestro 24,  one to open the panels in steps,  the other to close.  Keep track of their numbers.  (For my Example,  Sequence 5 will OPEN, Sequence 6 will CLOSE)
   - Find each sound file I want to and make notes of the numbers in their file names.
   - test any commands I'm sending for AstroPixel
   - test sending the Failure Logic Displays command to AstroPixels:   @APLE20000
   - look up an test the commands i need to send
   - put it all together and test it
  
Lets get to work...  

3. Program your Maestro, keeping track of your Sequence Numbers and what action they perform.
   - Connect your computer to the Maestro 12, and use the Maestro Control program the first sequence to open the Utility Arms, and then program the second sequence to close the Utlity Arm, saving them to your Maestro, and keeping note of their Sequence Number. In my case, Sequence 3 Opens and Sequence 4 Closed.
   -  Then do the same with the Maestro 24 and the sequences for the Pie Pieces, again, saving to the Maestro 24 and keeping track of their sequence numbers. In my case Sequence 5 Opens and Sequence 6 Closes. 

4. Test sending the Failure command @APLE20000 to the AstroPixles.  Make note of what happens (are all lights affected, how long does it run? Do AstroPixels restart on their own or do you have to reset them?)
   - Connect to the DroidLink display's Configuration using a web browser.  (connect to DroidLink Display hot spot, then in your browser visit  192.168.4.1 )
   - Go to the DOME button section
   - Take a button you haven't programmed yet, like 15
   - enter the command @APLE20000
   - Press Send and watch what happens on your R2.   (You should see the logic display lights change from their usual, to an all red, and slowly dim. The Logic Displays should turn off)
   
   How did I know that was the command for Failure Mode?  I looked at the commands here -> https://github.com/reeltwo/AstroPixelsPlus/tree/main
5. Test calling your Maestro sequences
     - Again in the DroidLink display configuration
     - Find another Dome buton you haven't programmed, like 16
     - Enter the command   :BS03
     - Press Send, you should see the Utility Arms open.
     - On another button, like 17 assign the command  :BS04 and press send.  You should see the Utiltiy Arms close.
       Why :BS03 and :BS04 ?    :BS denotes a "Body Slave" action, which in my case has my Maestro 12 connected.  03 is the sequence I programmed on the Maestro 12 to Open the arms, and 04 is the sequence I programmed on the Maestro 12 to close the arms
     - On another button, like 18, and assign the command  :DS05 and press Send.  You should see your Pie Panels open.
     - On another button, like 19, assign the command  :DS06 and press Send.  You should see your Pie Panels closed.
     
   Why :DS05 and :DS06 ?   :DS denotes a "Dome Slave" action,  which in my case has my Maestro 24 connected.   05 is the sequence I programmed on the Maestro 24 to open the pie panels, and 06 is the sequence I programmed on the Maestro 24 to close the panels.  
     
     - If those tests work, you're ready to move on.
       
6. Test Playing an audio file
     - Find the audio files you want to play.  In my case, I selected 0131_screa-3.mp3 for the "bad motivator" sound step,  and 0010_gen-10.mp3 for the "we're back" sound.
     - On another button, either under Dome or Audio,  assign the command :AS0131 and hit send.   R2 should play the sound.
     - On another button,  assign the command :AS010 and hit send.  R2 should play that sound.
     
   Why :AS010 and :AS131 ?   :ASnnn (where nnn is 001 to 255) denotes play this audio file whose file name start with that number.
      
      - If those tests work, you're ready to move on.

  7.  Test moving the dome
     - The DroidLink instructions mention using :DC,LEFT  :DC,RIGHT and :DC,STOP  as Dome Movement commands, so lets try those
      - Find a button under Dome, and set the command to  :DC,LEFT
      - Find another button and set the command to   :DC,RIGHT
      - Find a third button and set it to :DC,STOP
      - Press send for :DC,Left
      - if it doesn't stop on its own, press send for :DC,STOP
      - Press Send for  :DC,RIGHT
      - if it doesn't stop on its own, press send for :DC,STOP
      - IF those tests work, your ready to move on.
    
  8.  The last command you need to know is the Wait command, or   :Wnnnn   where nnnn is time in milliseconds.   So :W500 would be wait for 1/2 second.  :W1000 would be wait 1 Second.
  9.  Lets put it all together
      - find a button you want to use,  I used Dome 20.  and my command is:
      :DS05:BS03@APLE20000:W500:AS0131:DC,LEFT:W1000:DC,RIGHT:W1000:DC,STOP:DC,LEFT:W500:DC,RIGHT:W500:DC,STOP:W13000:BS04:DS06:AS011

Lets break that command string down:


| Command |  Meaning |
|:---:|:---:|
| :DS05 | Tell the Dome DroidLink Slave's attached Maestro to execute Sequence 5 (Open the pie panels) |
| :BS03 | Tell the Body DroidLink Slave's attached Maestro to execute Sequence 3 (Open the Utility Arms) |
| @APLE20000 | As discusssed, this sends the "failure mode" command to the AstroPixels. |
| :W500 |     Wait for 500 milliseconds (1/2 second)  |
| :AS0131 |   Play the audio file starting with the number 131 or 0131  |
| :DC,LEFT |   Turn the Dome motor to the left|
|:W1000 |   Wait for 1000 milliseconds (1 second) |
| :DC,RIGHT | Turn the Dome motor to the right |
|:W1000 |  Wait for 1000 milliseconds (1 second) |
| :DC,STOP | Stop the Dome Motor|
|:DC,LEFT  |  Turn the Dome motor to the left|
|:W500 |     Wait for 500 milliseconds (1/2 second)|
|:DC,RIGHT  |  Turn the Dome motor to the right|
|:W500 |   Wait for 500 milliseconds (1/2 second) |
|:DC,STOP |   Stop the Dome Motor |
| :W13000  |  Wait for 13000 milliseconds (13 seconds) |
|:BS04 | Tell the Body DroidLink Slave's attached Maestro to execute Sequence 4 (Close the Utility Arms) |
| :DS06 |  Tell the Dome DroidLink Slave's attached Maestro to execute Sequence 6 (Close the pie panels) |
| :AS011 |   Play sound file 011 or 0011 |

Did I need all those waits in there? It helps space things out to the timing of the lights and sounds.    Its also possible I could re-arrange things a little and not need the waits. It would take experimentation.  

Well, that is it.  

       
