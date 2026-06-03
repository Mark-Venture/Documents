# Making a PWM to SBUS-A translator for HotRC

DroidLink requires two HotRC SBUS-A receivers, one for Dome and one for Drive, but the required HotRC DS-650 Remote Controllers usually ship with F-06A receivers which only operate in PWM mode.   As such,  HotRC SBUS-A Receivers must be purchased separately, and they seem to only be available from AliExpress.  This poses the challenge of long shipping times, or challanges obtaining them.  Some credit cards will fail payment, etc.  

The parts and process on this page will allow you to create a "fake"  SBUS-A Reciver out of "left over" DroidLink Slave parts and the HotRC F-06A receivers, so that you can use your DS-650 Remotes while waiting to receive your REAL HotRC SBUS-A receivers.  

Purchase options from AliExpress for REAL SBUS-A Receivers,  before ordering any, please ensure SBUS-A is selected (maybe an option for "COLOR") !

Option 1:  https://tinyurl.com/5n8zxvvd
Option 2:  https://tinyurl.com/3zvnpr98
OPtion 3:  https://tinyurl.com/4ehh6hrm

If you are unable to get one, or shipping is delayed, you can proceed. 

##  WARING:   The steps on this page are ment to be a temporary work around if there is a delay in obtaining HotRC SBUS-A Receivers.   DO NOT USE THIS AS A PERMINANT SOLUTION!!!!
# THIS IS NOT AFFILATED nor SUPPORTED BY DROIDLINK!!  

## USE AT YOUR OWN RISK!!

This process requires parts, as well as using the Arduion IDE to send the code to your ESP32.  If you are not comfortable doing this, DO NOT DO IT.

This process assumes you have paired your DS650 Remote Controls with their F-06A receivers. 

Note: This is VERSION 2 of the documentation and code.   **Using these instructions a single ESP32 and Expansion Board will translate two F-06A into the SBUS-A for Dome and SBUS-A for Drive.  **
 
#  Parts Needed:

## ESP32 w/Breakout Board.  (Only 1 ESP323 and Expansion board is needed for this version, with its code below).  
_NOTE: For Version 1 you'll need **two** ESP32 and expansion boards.  (one ESP32 with expansion to translate Dome,  and one ESP32 w/expansion to translate Drive)_


* [AITRIP 2 Sets ESP-WROOM-32 \*WITH\* Expansion Board](https://a.co/d/0aBikVDW)  
  * Alternate board: [AITRIP ESP-WROOM-32 \*WITHOUT\*  Expansion Board](https://a.co/d/03f9A5iy)  
  * Alternate expansion board:  [AITRIP  ESP-WROOM-32 Expansion Board only](https://a.co/d/0dhr2P1q)
  
  NOTE: These are available as multi packs which is the preferred way to order,  So you may have extras from your DroidLink Parts order and not need to order this!!  

## Wires:  
* [3Pin servo wires](https://a.co/d/0e7YYnSx) You need at least 14 wires, so this 20 pack will be sufficent if you don't have enough already. 

## Power: 
There are two options. Either barrel connector supplying  12V or USB-C connector supplying 5v to the Expansion Boards's USB-C port.   You only need one of these, not both.

12v barrel is preferred!

* Barrel for 12v [DC Power Pigtail Cable, 2-Pack 5.5mm x 2.1mm 90 Degree Right Angle DC Barrel Male](https://a.co/d/0cBU9CgQ) 
* USB-C for 5v [Type C Male Plug Bare Wire Pigtail](https://a.co/d/02wyy1HZ)

## Process: 

## Assembling the parts:

1. Properly insert the ESP32 into the Breakout board.
2. Connect the 3wire leads between your F-06A and your "Translator" ESP32 breakout boards as follows:

|F-06A Receiver 1 PWM|ESP32 Pin|Notes|
|:---:|:---:|:---:| 
|CH1 (e.g., Left/Right) | GPIO 13 | PWM Input 1 |
|CH2 (e.g., Forward/Reverse) | GPIO 12| PWM Input 2 |
|CH3 (e.g., Button A or 3)  |GPIO 14| PWM Input 3|
|CH4 (e.g., Button B or 4)|GPIO 27|PWM Input 4|
|CH5 (Button C or 5) | GPIO 26 | PWM Input 5 |
|CH6 (Button D or 6) |GPIO 25| PWM Input 6 |

|F-06A Receiver 2 PWM|ESP32 Pin|Notes|
|:---:|:---:|:---:| 
|CH1 (e.g., Left/Right) | GPIO 13 | PWM Input 1 |
|CH2 (e.g., Up/Down) | GPIO 12| PWM Input 2 |
|CH3 (e.g., Button A or 3)  |GPIO 14| PWM Input 3|
|CH4 (e.g., Button B or 4)|GPIO 27|PWM Input 4|
|CH5 (Button C or 5) | GPIO 26 | PWM Input 5 |
|CH6 (Button D or 6) |GPIO 25| PWM Input 6 |



3.  Cut the VCC/Power (red) wire on TWO of the 3 pin servo wires which will be used to connect the translators to the DroidLink Master.   You will only want to connect Signal and GND pins in the next step!
4.  Connect the 3 Wire Lead with the cut VCC/Power between the "Translator" ESP32 breakout board and your DroidLink Master.  Again, you are only connecting Signal and Ground pins. 

Drive Translator: 
|Translator ESP32 GPIO|DroidLink Master GPIO|Notes|
|:---:|:---:|:---:| 
|GPIO 17 | GPIO 16 |  SBUS input from the drive RC receiver|

Dome Translator:
|Translator ESP32 GPIO|DroidLink Master GPIO|Notes|
|:---:|:---:|:---:| 
|GPIO 4 | GPIO 17 |  SBUS input from the drive RC receiver|

5. Connect Power to the Translator ESP32:
   There are two options.  If you wish to supply 12v, select option 1.  If you wish to use 5v,  select option 2.

  Option 1:   
  * Connect the red and black leads from the barrel connector pigtail to your 12V source.
  * Plug the barrel into your Translator ESP32's expansion board.

  Option 2: 
  * Connect the red and black from the USB-C Pigtail to your 5v source.
  * Plug the USB-C connector into the USB-C port on EITHER the USB-C port on your Translator ESP chip, or the USB-C port on the Translator expansion board.


## Programming the Translator ESP32 with the code.  (the following steps were written by Google Gemini


## Installing and configuring Arduino IDE
Follow these steps to configure your Arduino IDE environment to support ESP32 development hardware, SBUS protocol decoding, and standard Arduino header structures.

---

## Step 1: Install the Arduino IDE
1. Navigate to the [Arduino Official Software Page](https://arduino.cc).
2. Download the latest stable version of the **Arduino IDE 2.x** installer for your operating system.
3. Run the installer executable.
4. Keep all default checkboxes marked to ensure standard USB/serial drivers install correctly.
5. Launch the application.

## Step 2: Add the ESP32 Board Core
1. Open the Arduino IDE.
2. Go to **File > Preferences** (Windows/Linux) or **Arduino IDE > Settings** (macOS).
3. Locate the **Additional boards manager URLs** text field.
4. Paste the following official Espressif URL into the field:
     https://espressif.github.io/arduino-esp32/package_esp32_index.json
5. Click **OK** to save your preferences.
6. Open the Boards Manager by clicking the board icon on the left sidebar (or navigate to **Tools > Board > Boards Manager**).
7. Type `ESP32` into the search bar.
8. Locate the bundle titled **esp32** by **Espressif Systems**.
9. Click **Install** and wait for the compiler toolchain installation to complete.

## Step 3: Install an SBUS Library
"SBUSA" refers to the Futaba S.BUS serial data protocol. You must install a dedicated library to decode these serial data frames.
1. Open the Library Manager by clicking the library icon on the left panel (or navigate to **Tools > Manage Libraries...**).
2. Type `SBUS` into the search field.
3. Choose a robust, well-maintained library from the list, such as:
   * **Bolder Flight Systems SBUS by Brian Taylor**
4. Click **Install** to add the packages to your local registry.

## Step 4: Configure Hardware 

1. Connect your physical ESP32 development board (your Translator ESP32) to your computer using a data-capable USB cable.
2. Navigate to **Tools > Board > esp32** and select your exact board variant (`ESP32 Dev Module`).
3. Navigate to **Tools > Port** and select the virtual COM port assigned to your USB-UART chip.
4. Create a new sketch and paste the template code structure below into your file.


## Code to use

With the Arduino IDE open, create a new sketch,   replace anything which is in the editor by default with the following code (generated by Google Gemnini):  

```

#include <Arduino.h>

// ==========================================
// CONFIGURATION & PIN ASSIGNMENTS 
// ==========================================
const int rx1_pins[] = {13, 12, 14, 27, 26, 25};
const int rx2_pins[] = {23, 19, 18, 5, 22, 21}; 

// Volatile arrays for ISR timing capture (Receiver 1)
volatile unsigned long rx1_start[] = {0, 0, 0, 0, 0, 0};
volatile int rx1_raw[] = {1500, 1500, 1500, 1500, 1500, 1500};

// Volatile arrays for ISR timing capture (Receiver 2)
volatile unsigned long rx2_start[] = {0, 0, 0, 0, 0, 0};
volatile int rx2_raw[] = {1500, 1500, 1500, 1500, 1500, 1500};

// SBUS structural arrays (16 channels each)
uint16_t rx1_channels[16];
uint16_t rx2_channels[16];
uint8_t packet1[25];
uint8_t packet2[25];

// ==========================================
// INTERRUPT SERVICE ROUTINES (ISR)
// ==========================================
void IRAM_ATTR rx1_ch1() { if(digitalRead(rx1_pins[0])) rx1_start[0] = micros(); else rx1_raw[0] = micros() - rx1_start[0]; }
void IRAM_ATTR rx1_ch2() { if(digitalRead(rx1_pins[1])) rx1_start[1] = micros(); else rx1_raw[1] = micros() - rx1_start[1]; }
void IRAM_ATTR rx1_ch3() { if(digitalRead(rx1_pins[2])) rx1_start[2] = micros(); else rx1_raw[2] = micros() - rx1_start[2]; }
void IRAM_ATTR rx1_ch4() { if(digitalRead(rx1_pins[3])) rx1_start[3] = micros(); else rx1_raw[3] = micros() - rx1_start[3]; }
void IRAM_ATTR rx1_ch5() { if(digitalRead(rx1_pins[4])) rx1_start[4] = micros(); else rx1_raw[4] = micros() - rx1_start[4]; }
void IRAM_ATTR rx1_ch6() { if(digitalRead(rx1_pins[5])) rx1_start[5] = micros(); else rx1_raw[5] = micros() - rx1_start[5]; }

void IRAM_ATTR rx2_ch1() { if(digitalRead(rx2_pins[0])) rx2_start[0] = micros(); else rx2_raw[0] = micros() - rx2_start[0]; }
void IRAM_ATTR rx2_ch2() { if(digitalRead(rx2_pins[1])) rx2_start[1] = micros(); else rx2_raw[1] = micros() - rx2_start[1]; }
void IRAM_ATTR rx2_ch3() { if(digitalRead(rx2_pins[2])) rx2_start[2] = micros(); else rx2_raw[2] = micros() - rx2_start[2]; }
void IRAM_ATTR rx2_ch4() { if(digitalRead(rx2_pins[3])) rx2_start[3] = micros(); else rx2_raw[3] = micros() - rx2_start[3]; }
void IRAM_ATTR rx2_ch5() { if(digitalRead(rx2_pins[4])) rx2_start[4] = micros(); else rx2_raw[4] = micros() - rx2_start[4]; }
void IRAM_ATTR rx2_ch6() { if(digitalRead(rx2_pins[5])) rx2_start[5] = micros(); else rx2_raw[5] = micros() - rx2_start[5]; }

uint16_t pwm_to_sbus(int pwm) {
  pwm = constrain(pwm, 1000, 2000);
  return map(pwm, 1000, 2000, 172, 1811);
}

// ==========================================
// UNIVERSAL BIT PACKER FUNCTION
// ==========================================
void serialize_sbus(uint16_t* channels, uint8_t* output_packet) {
  output_packet[0] = 0x0F; // Header

  output_packet[1]  = (uint8_t) ((channels[0] & 0x07FF));
  output_packet[2]  = (uint8_t) ((channels[0] & 0x07FF) >> 8  | (channels[1] & 0x07FF) << 3);
  output_packet[3]  = (uint8_t) ((channels[1] & 0x07FF) >> 5  | (channels[2] & 0x07FF) << 6);
  output_packet[4]  = (uint8_t) ((channels[2] & 0x07FF) >> 2);
  output_packet[5]  = (uint8_t) ((channels[2] & 0x07FF) >> 10 | (channels[3] & 0x07FF) << 1);
  output_packet[6]  = (uint8_t) ((channels[3] & 0x07FF) >> 7  | (channels[4] & 0x07FF) << 4);
  output_packet[7]  = (uint8_t) ((channels[4] & 0x07FF) >> 4  | (channels[5] & 0x07FF) << 7);
  output_packet[8]  = (uint8_t) ((channels[5] & 0x07FF) >> 1);
  output_packet[9]  = (uint8_t) ((channels[5] & 0x07FF) >> 9  | (channels[6] & 0x07FF) << 2);
  output_packet[10] = (uint8_t) ((channels[6] & 0x07FF) >> 6  | (channels[7] & 0x07FF) << 5);
  output_packet[11] = (uint8_t) ((channels[7] & 0x07FF) >> 3);
  output_packet[12] = (uint8_t) ((channels[8] & 0x07FF));
  output_packet[13] = (uint8_t) ((channels[8] & 0x07FF) >> 8  | (channels[9] & 0x07FF) << 3);
  output_packet[14] = (uint8_t) ((channels[9] & 0x07FF) >> 5  | (channels[10] & 0x07FF) << 6);
  output_packet[15] = (uint8_t) ((channels[10] & 0x07FF) >> 2);
  output_packet[16] = (uint8_t) ((channels[10] & 0x07FF) >> 10 | (channels[11] & 0x07FF) << 1);
  output_packet[17] = (uint8_t) ((channels[11] & 0x07FF) >> 7  | (channels[12] & 0x07FF) << 4);
  output_packet[18] = (uint8_t) ((channels[12] & 0x07FF) >> 4  | (channels[13] & 0x07FF) << 7);
  output_packet[19] = (uint8_t) ((channels[13] & 0x07FF) >> 1);
  output_packet[20] = (uint8_t) ((channels[13] & 0x07FF) >> 9  | (channels[14] & 0x07FF) << 2);
  output_packet[21] = (uint8_t) ((channels[14] & 0x07FF) >> 6  | (channels[15] & 0x07FF) << 5);
  output_packet[22] = (uint8_t) ((channels[15] & 0x07FF) >> 3);

  output_packet[23] = 0x00; // Flags byte
  output_packet[24] = 0x00; // Footer End Byte
}

// ==========================================
// INITIALIZATION
// ==========================================
void setup() {
  Serial.begin(115200); 
  delay(500); // Small breathing window for serial hardware stabilization

  // Hardware Serial outputs with register inversion enabled
  Serial2.begin(100000, SERIAL_8E2, 16, 17, true);
  
  // FIXED: Changed dummy RX pin from dangerous 9 to completely safe GPIO 2
  Serial1.begin(100000, SERIAL_8E2, 2, 4, true); 

  for (int i = 0; i < 6; i++) {
    pinMode(rx1_pins[i], INPUT_PULLUP);
    pinMode(rx2_pins[i], INPUT_PULLUP);
  }

  // Bind Interrupts for Rx1
  attachInterrupt(digitalPinToInterrupt(rx1_pins[0]), rx1_ch1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[1]), rx1_ch2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[2]), rx1_ch3, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[3]), rx1_ch4, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[4]), rx1_ch5, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[5]), rx1_ch6, CHANGE);

  // Bind Interrupts for Rx2
  attachInterrupt(digitalPinToInterrupt(rx2_pins[0]), rx2_ch1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx2_pins[1]), rx2_ch2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx2_pins[2]), rx2_ch3, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx2_pins[3]), rx2_ch4, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx2_pins[4]), rx2_ch5, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx2_pins[5]), rx2_ch6, CHANGE);

  for (int i = 6; i < 16; i++) {
    rx1_channels[i] = 992;
    rx2_channels[i] = 992;
  }
  
  Serial.println("System Initialized! No crash loop.");
}

// ==========================================
// RUNTIME EXECUTION
// ==========================================
void loop() {
  int local_rx1[6];
  int local_rx2[6];

  noInterrupts();
  for(int i = 0; i < 6; i++) { 
    local_rx1[i] = rx1_raw[i]; 
    local_rx2[i] = rx2_raw[i];
  }
  interrupts();

  for (int i = 0; i < 6; i++) {
    rx1_channels[i] = pwm_to_sbus(local_rx1[i]);
    rx2_channels[i] = pwm_to_sbus(local_rx2[i]);
  }

  serialize_sbus(rx1_channels, packet1);
  serialize_sbus(rx2_channels, packet2);

  Serial2.write(packet1, 25); // Output out GPIO 17 (Rx1)
  Serial1.write(packet2, 25); // Output out GPIO 4  (Rx2)

  // Multi-receiver debugging monitor output
  Serial.print("Rx1-Ch1: "); Serial.print(local_rx1[0]);
  Serial.print(" | Rx2-Ch1: "); Serial.println(local_rx2[0]);

  delay(14); 
}

```

You are now read to send to your ESP32.

1. In the IDE,  just below the File, Edit, Sketch, etc.  menu,   click the right facing arrow.   The IDE should compile and send the code to your translator ESP32.
2. When complete,  repleat the process for your second Translator ESP32 and program it.

Power down R2,  and power it back up.   You should be good.  

