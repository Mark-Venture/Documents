The following is a list of the electronics you’ll need when making an R2 D2 from the Mr. Baddeley files. The Optional components listed are suggestions, feel free to purchase from your preferred retailer.  

# **Parts for DroidLink**:

Note: due to some supply issues, alternatives are listed here, of the preferred parts are not available.   When it comes to DroidLink Slave and DFPlayer it doesn’t hurt to order extra.  For the master, it’s nice to have a backup.

***Important: Because not all ESP32’s are the same, these exact models/parts are required for DroidLink to work.***  

## DroidLink Master:
It is an ESP32-S3 N16R8 Development board and Breakout Board.  The parts are as follows:   

* [Meshnology ESP32-S3](https://a.co/d/0iwS0lk4)    
  * If out of stock an alternative is:  [https://a.co/d/0f3qa6Uq](https://a.co/d/0f3qa6Uq)  
* [Meshnology N40 \- ESP32 Expansion Board](https://a.co/d/0heCsPTG)  
  * If out of stock an alternate source is: [Direct form manufacturer](https://meshnology.com/products/n40-esp32-expansion-board-for-esp32-esp32-s3-core-modules)   
  * If the N40 is out of stock, alternate Option is [Freenove Breakout Board for ESP32 / ESP32-S3 WROVER WROOM](https://a.co/d/0g1QBTRy)  Please note, The ESP-S3 N16R8 will “hang over” the socket on this breakout board.  You should have one set of exposed pins at the top, and one set at the bottom.  

NOTE: if you have to purchase a different variant of the ESP32-S3 N16R8, please ensure it includes an Antenna for the Wi-Fi.  We have seen some 3rd party ESP32-S3 N16R8 have just an “Antenna base” connector on board for an external antenna, but do not include the external antenna\!


## **DroidLink Display**:  
It is a [Waveshare ESP32-S3 2.06inch AMOLED w/400mAh Battery](https://a.co/d/01TigaiF)   Please check the listing you order from, as this is also available without battery from some sellers\!  You must have a battery.  

* Alternate higher capacity Battery [DC 3.7V 900mAh 803035 Battery with JST 1.25mm connector](https://a.co/d/0bbDGhk2)  
* [Waveshare ESP32-S3 Amoled 2.06inch 900mAh case back](https://makerworld.com/en/models/2763002-waveshare-esp32-s3-amoled-2-06-900mah-case#profileId-3067793) REQUIRED only if you wish to use the 900mAh battery. 

## **DroidLink Slave**:  
It is an ESP32-DevKitC-32 w/Expansion board

* [AITRIP 2 Sets ESP-WROOM-32 \*WITH\* Expansion Board](https://a.co/d/0aBikVDW)  
  * Alternate board: [AITRIP ESP-WROOM-32 \*WITHOUT\*  Expansion Board](https://a.co/d/03f9A5iy)  
  * Alternate expansion board:  [AITRIP  ESP-WROOM-32 Expansion Board only](https://a.co/d/0dhr2P1q)

  NOTE: These are available as multi packs which is the preferred way to order, as for a full DroidLink Implementation you’ll need more than 1 slave.  Example: Dome Slave (connect lights like AstroPixel, and servo controller like Maestro), Body Slave (connect a servo controller like Maestro), if you plan on doing a Lifter assembly in the dome, you’ll need a Slave for that (it also needs a servo controller).

## **RC Remote**:  
HotRC DS-650 is currently the only one supported.   These are needed if you want to drive or pilot your droid around.  **You’ll need two**, one to control the Drive motors and the other to control the Dome and give you more buttons to trigger actions. 

NOTE: Pay attention when you order.  Some packages include the F-06A PWM receivers, the receivers cannot be used with DroidLink. SBUSA receivers which are required must be purchased separately.

* [HotRC DS-650 Remote Controller](https://a.co/d/082LogKp) (order 2):   This does come with the F-06A and is the only way to order from Amazon.  
* [HotRC S-BUS-A Receivers](https://tinyurl.com/5n8zxvvd) (order 2): Note, this is not available from Amazon.  AliExpress is the only source, and you might find on Ebay.   NOTE: there are various listings on AliExpress at different prices, please make sure you order HotRC **SBUS-A** receivers. 

## **DFPlayer Mini MP3 Player**:   
The DFPlayer board is used to play back the droid sounds. 

* [DFPlayer Mini MP3 Player for Arduino/ESP32](https://a.co/d/03fNwlU8)  (Single)  
  * If out of stock, alternate source is [5PC Mini MP3 Module](https://a.co/d/0akwmUBJ)  This often is the same price as a single, but includes 5\.     
* MicroSD card.   Up to 32gig card can be used, but must be formatted as FAT32  
    
NOTE: For speakers, see “Optional Parts” section below for info. 

## **DFPlayer Mini Carrier**:   
Optional but highly suggested as it makes connecting the DFPlayer easier and neater with the DroidLink Master. 

* Contact  [Droidlink77@gmail.com](mailto:Droidlink77@gmail.com) for availability and price.

# **Optional Parts**:  

## **Amplifier**:  
* [ZK-1002T 100W+100W Bluetooth Amplifier Board](https://a.co/d/04iiWMWC)  \- Recommended to enjoy louder and cleaner sound, with easy adjustability form your droid.  You’ll also need a cable to connect to the DFPlayer.   NOTE: if you are attending Con’s or using your droid in loud places, the amplifier is highly recommended.   If you are just “at home” then an amplifier may not be necessary.

## **Speakers**:
(depending on the size of your speaker, you may require custom mounts)

* If not using an amplifier:  [Visaton FRS8-4 3.3" Full-Range Speaker](https://a.co/d/02sfUU9x)  A single speaker can be directly connected to the DFPlayer board.  While sold as a pair, a single speaker from  [Pyle PL32BL (Pair)](https://a.co/d/0fPfsmun)  can be used, just connect/mount 1 speaker to DFPlayer.   
* If using the ZK-1002T amplifier:  [Pyle PL32BL (Pair)](https://a.co/d/0fPfsmun)  These connect to the Amp and handle the power nicely. 

## **Servos**:  
If you want the blue panels in your dome to open/close, or you printed the Complex body and want the doors to open/close, or the holo projectors and utility arms to move, you’ll need servos.    The PDFs in the EarlyBird \-\> MK4 AstroMech folders will call out what servos to use in these positions. 

**Servo Controller**:  If you plan to have opening panels, or other accessories that are driven by servos, the Pololu Mini Maestro is recommended due to its ease of programming and configuration. 

* [Mini Maestro 24](https://www.pololu.com/product/1356)  Can control up to 24 servos.   
* [Mini Maestro 18](https://www.pololu.com/product/1354)  Can control up to 18 servos  
* [Mini Maestro 12](https://www.pololu.com/product/1352)  Can control up to 12 servos

NOTE: it is recommended to use at least two Mini Maestro 24 as your servo controllers. One for the Dome, and One for the Body.  This allows for the best future expansion, and pricing usually is reasonably close to the Mini Maestro 18\. 

NOTE: it is NOT recommended to get a Micro Maestro (6) due to its limited internal memory/script size, and ability to control only 6 servos.   The low script size will prevent you from doing more servo sequences, as well as complex sequences. 

**Servo Savers**:   When it comes to opening and closing the panels, there is a solid bar or linkage between the end of the arm of the servo (also known as the horn) and the hinge for the panel.  If the panel gets stuck while the servo is trying to turn, the servo keeps trying to turn and could get burned out, or break teeth inside.  Instead of that fixed length bar, servo savers use springs and tension to allow some extra play and movement. The servo can continue to turn a little bit, while the panel is stuck, thus preventing the servo from burning out.

Typically, you make them by ordering the individual parts and assembling them.  For example, I purchased ball joints, push rods, springs and linkage stoppers off Amazon, and put mine together.  And I got a cutter to cut the push rods shorter. There are many posts on the Mr Baddeley Facebook page on what to order and how to make them.

**Servo Extension wires**:  If your servo wires, or PWM wires are not long enough,  these are a great way to extend them.
* [30 Pcs 3-Pin Extension Cable Cord Male to Female Lead Wire](https://a.co/d/0f83B7xD)  Multiple lengths of wires that can extend the 3pin wires to the ESP32 breakout boards. 

## **Power**: 

When it comes to powering your system there are many options and configurations which are all outside of DroidLink. This section doesn’t provide links to parts, only highlights some options. 

**Power Source**: Many use tool batteries of various voltages and Ah ratings.  Please ensure it has onboard Battery Management System for optimum performance. 

* [Ryobi 18V Lithium HighPerformance](https://www.homedepot.com/p/RYOBI-ONE-18V-Lithium-Ion-4-0-Ah-Battery-2-Pack-PBP2005/316767033)  are a popular option. They are available as 4AH (minimum for an R2 unit),  6Ah, 8Ah or 12Ah. Higher Ah rating provides longer run time.  Often two-packs go on sale.  
* Clones [are available on Amazon](https://a.co/d/02RyX91n)     
    
  NOTE: There are various battery boxes and mountings available on Makerworld and the MrBaddeley Facekbook page. 

**Voltage Converters (aka Buck Converters)**:   Here too there are many options. These are needed to step down voltage from 18, 20 or 24volt batteries to 12v and 5V the electronics use.  Some choose to go with adjustable or variable output BUCKs, others with fixed output BUCKs. Do Not connect anything to the Output of an adjustable converter until AFTER you have configured it for the proper output voltage.  Failure to do so could harm your components\!

When shopping for a converter Pay attention to the Voltage(V) and Current (Amp or A) output to ensure you have a BUCK that can handle what it will be feeding power to.   For example, there are some smaller adjustable Buck’s that only can output 2Amps.  While this might be enough if you are running just Astropixels or such, it will not be enough if you want to run a large number of servos, your dome motor, or such. 

* Some Examples:   
  [DROK DC Buck Converter, 5.3V-32V to 1.2V-32V 12A Adjustable Power Supply](https://a.co/d/02iev547)  this takes up to 32V in, and steps it down as low as 1V.  Without added cooling it’s rated to support up to 8Amps (12v if you add a fan to cool it), so it’s good all-around one. It can be used in both the Body and Dome.  
* [DROK DC Buck Converter Adjustable Voltage Regulator 12V 6V-32V to 1.5-32V 5A](https://a.co/d/0dVWCDhi)  this is very similar to the other, except it only does a maximum of 5Amps so it can’t power as much simultaneously.   
* [DC HOUSE 20A 240W 12V Golf Cart 48V 36V to 12V](https://a.co/d/0gNxa7J9)  It takes voltage in, and outputs a non-adjustable 12V up to 20A output. I deal if you have many options installed in your Droid.     
  [DC-DC 36V 48V to 12V 20A 240W Golf cart, Buck Converter](https://a.co/d/0jbcqF9p)  another that outputs a non-adjustable 12V up to 20A output.    
* [HOMELYLIFE Voltage Converter DC 12V 24V Step Down to 5V 20A 100W](https://a.co/d/0gjXog5l)  It take the input voltage and steps it down to a constant 5V up to 20A.  

**Fuses**: Fuses add protection for your circuits and subsystems.  The intent is, if there is something wrong in your system, the fuse blows before your other components.  Some run with a single fuse off their main battery into a bus bar to distribute power, others run power from the battery into a Fuse Block which distributes power and provides fuse protection for each subsystem (drive motor, dome motor, DroidLink Master, Power to Dome, etc).  The advantage to a fuse block and individual fuses per subsystem is that if you experience an issue with one subsystem, it won’t take out your other subsystems. 

* [6 Way Fuse Block Box 12V/24V DC, ATC/ATO Fuse Panel with LED Display](https://a.co/d/0h1Q94VS) suitable for 6 circuits, of 12v up to 32v with real time voltage display.  It should also work with 5V.   
* [Nilight \- 50029R 120 Pcs Standard Blade Fuse Assorted Set with 10 Pack 14 AWG Inline Fuse holders](https://a.co/d/0b8S5fsr).   Comes with an assortment of 5A/7.5A/10A/15A/20A/25A/30A AMP blade fuses wth 10 Inline Fuse Holders.  Splice the inline fuse holder into the positive side of your circuit’s power lead, insert a fuse, and that circuit is protected. 

**Lever Wire Connectors or Wago Connectors**: for those who can’t or don’t like to solder, these connectors allow relatively secure connections to various wire sizes.  I make use of these extensively in my R2. 

* [Wago Lever Nuts 90pc assortment with case](https://a.co/d/09LqwN3n)  
* [65 Pcs Lever Wire Connector assortment with storage box](https://a.co/d/0fl65G21)   nice assortment to connect and split wires  
*  [60 pcs XHF Colourful Conductor Compact Connectors](https://a.co/d/08A3VhUc)  great to color code your wires as you connect/extend them.   
* [DIN Rail Terminal Blocks](https://a.co/d/01A853dZ)  these are a great alternative to bus bars for power distribution.  Multiple options like 2 in 10 out (make 1 \+/- combo into 5), 2 in 8 out, etc.  

  NOTE: some 12gauge wires may not properly fit into these connectors. 

**Wires**:   Typically, your wire gauge (or AWG) should be sized for the current you expect to run across it \+ 25% as  a margin for error.  Many use the following as a general guide: 

* 12 AWG to carry up to 36 volts.    
* 14 AWG to carry up to 24 volts.   
* 16 AWG to carry up to 18 volts.   
* 18 or 20 AWG to carry 12 volts.  
* 20 or 22 AWG to carry up to 5 volts  
* 18, 20 or 22 AWG for PWM signals, USB signals, etc. 




