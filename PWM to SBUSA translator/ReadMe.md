# Making a PWM to SBUS-A translator for HotRC

DroidLink requires two HotRC SBUS-A receivers, one for Dome and one for Drive, but the required HotRC DS-650 Remote Controllers usually ship with F-06A receivers which only operate in PWM mode.   As such,  HotRC SBUS-A Receivers must be purchased separately, and they seem to only be available from AliExpress.  This poses the challenge of long shipping times, or challanges obtaining them.  Some credit cards will fail payment.  

The parts and process on this page will allow you to create a "fake"  SBUS-A Reciver out of "left over" DroidLink Slave parts and the HotRC F-06A receiver, so that you can use your DS-650 Remote while waiting to receive your REAL HotRC SBUS-A receiver.  

Purchase options from AliExpress for REAL SBUS-A Receivers,  before ordering any, please ensure SBUS-A is selected (maybe an option for "COLOR") !

Option 1:  https://tinyurl.com/5n8zxvvd
Option 2:  https://tinyurl.com/3zvnpr98
OPtion 3:  https://tinyurl.com/4ehh6hrm

If you are unable to get one, or shipping is delayed, you can proceed. 

##  WARING:   The steps on this page are ment to be a temporary work around if there is a delay in obtaining HotRC SBUS-A Receivers.   DO NOT USE THIS AS A PERMINANT SOLUTION!!!!
# THIS IS NOT SUPPORTED BY DROIDLINK!!  
## USE AT YOUR OWN RISK!!

This process requires parts, as well as using the Arduion IDE to send the code to your ESP32.  If you are not comfortable doing this, DO NOT DO IT.

This process assumes you have paired your DS650 Remote Controls with their F-06A receivers. 

Note: This is VERSION 1 of the documentation and code.   You need to make TWO of these.   One for each receiver.    Verison 2 of this process will hope to perform the translation for both Dome and Drive on one ESP32 board.  Verison 2 might require different ESP32 hardware.
 
#  Parts Needed:

## ESP32 w/Breakout Board. (Quantity 2 of each).  
_NOTE: For Version 1 you'll need **two** ESP32 and expansion boards.  (one ESP32 with expansion to translate Dome,  and one ESP32 w/expansion to translate Drive)_


* [AITRIP 2 Sets ESP-WROOM-32 \*WITH\* Expansion Board](https://a.co/d/0aBikVDW)  
  * Alternate board: [AITRIP ESP-WROOM-32 \*WITHOUT\*  Expansion Board](https://a.co/d/03f9A5iy)  
  * Alternate expansion board:  [AITRIP  ESP-WROOM-32 Expansion Board only](https://a.co/d/0dhr2P1q)
  
  NOTE: These are available as multi packs which is the preferred way to order,  So you may have extras from your DroidLink Parts order.  

## Wires:  
* [3Pin servo wires](https://a.co/d/0e7YYnSx) You need at least 14 wires, so this 20 pack will be sufficent. 

## Power: 
There are two options. Either barrel connector supplying  12V or USB-C connector supplying 5v.   You only need one of these, not both.

* Barrel for 12v [DC Power Pigtail Cable, 2-Pack 5.5mm x 2.1mm 90 Degree Right Angle DC Barrel Male](https://a.co/d/0cBU9CgQ) 
* USB-C for 5v [Type C Male Plug Bare Wire Pigtail](https://a.co/d/02wyy1HZ)

## Process: 

## Assembling the parts:

1. Properly insert the ESP32 into the Breakout board.
2. Connect the 3wire leads between your F-06A and your "Translator" ESP32 breakout boards as follows:

|HotRC PWM Rx Pin|ESP32 Pin|Notes|
|:---:|:---:|:---:| 
| CH1 (e.g., Roll) | GPIO 13 | PWM Input 1 |
|CH2 (e.g., Pitch) | GPIO 12| PWM Input 2 |
| CH3 (e.g., Throttle)  |GPIO 14| PWM Input 3|
|CH4 (e.g., Yaw)|GPIO 27|PWM Input 4|
|CH5 (Aux 1) | GPIO 26 | PWM Input 5 |
|CH6 (Aux 2) |GPIO 25| PWM Input 6 |

3.  Cut the VCC/Power (red) wire on TWO of the 3 pin servo wires which will be used to connect the translators to the DroidLink Master.   You will only want to connect Signal and GND pins in the next step!
4.  Connect the 3 Wire Lead with the cut VCC/Power between the "Translator" ESP32 breakout board and your DroidLink Master.  Again, you are only connecting Signal and Ground pins. 

Drive Translator: 
|Translator ESP32 GPIO|DroidLink Master GPIO|Notes|
|:---:|:---:|:---:| 
|GPIO 17 | GPIO 16 |  SBUS input from the drive RC receiver|

Dome Translator:
|Translator ESP32 GPIO|DroidLink Master GPIO|Notes|
|:---:|:---:|:---:| 
|GPIO 17 | GPIO 17 |  SBUS input from the drive RC receiver|

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

With the Arduino IDE open, create a new sketch,   replace anything which is in the editor by default with the following code:  

```

#include <Arduino.h>

// ==========================================
// CONFIGURATION & PIN ASSIGNMENTS
// ==========================================
const int PWM_PINS[6] = {13, 12, 14, 27, 26, 25}; 

// Volatile variables for ISR timing capture
volatile unsigned long pulse_start[6] = {0, 0, 0, 0, 0, 0};
volatile int raw_pwm_values[6] = {1500, 1500, 1500, 1500, 1500, 1500}; 

// SBUS structural definitions
uint16_t sbus_channels[16];
uint8_t sbus_packet[25];

// ==========================================
// INTERRUPT SERVICE ROUTINES (ISR)
// ==========================================
void IRAM_ATTR ch1_isr() { if(digitalRead(PWM_PINS[0])) pulse_start[0] = micros(); else raw_pwm_values[0] = micros() - pulse_start[0]; }
void IRAM_ATTR ch2_isr() { if(digitalRead(PWM_PINS[1])) pulse_start[1] = micros(); else raw_pwm_values[1] = micros() - pulse_start[1]; }
void IRAM_ATTR ch3_isr() { if(digitalRead(PWM_PINS[2])) pulse_start[2] = micros(); else raw_pwm_values[2] = micros() - pulse_start[2]; }
void IRAM_ATTR ch4_isr() { if(digitalRead(PWM_PINS[3])) pulse_start[3] = micros(); else raw_pwm_values[3] = micros() - pulse_start[3]; }
void IRAM_ATTR ch5_isr() { if(digitalRead(PWM_PINS[4])) pulse_start[4] = micros(); else raw_pwm_values[4] = micros() - pulse_start[4]; }
void IRAM_ATTR ch6_isr() { if(digitalRead(PWM_PINS[5])) pulse_start[5] = micros(); else raw_pwm_values[5] = micros() - pulse_start[5]; }

// Map standard PWM (1000us-2000us) to strict Futaba SBUS scales (172-1811)
uint16_t pwm_to_sbus(int pwm) {
  pwm = constrain(pwm, 1000, 2000);
  return map(pwm, 1000, 2000, 172, 1811);
}

// ==========================================
// MATHEMATICALLY EXACT SBUS PACKER
// ==========================================
void build_sbus_packet() {
  sbus_packet[0]  = 0x0F; // Standard SBUS Header Byte

  // Explicit bit-packing mechanics (Splits 16 x 11-bit fields across 22 bytes)
  sbus_packet[1]  = (uint8_t) ((sbus_channels[0] & 0x07FF));
  sbus_packet[2]  = (uint8_t) ((sbus_channels[0] & 0x07FF) >> 8  | (sbus_channels[1] & 0x07FF) << 3);
  sbus_packet[3]  = (uint8_t) ((sbus_channels[1] & 0x07FF) >> 5  | (sbus_channels[2] & 0x07FF) << 6);
  sbus_packet[4]  = (uint8_t) ((sbus_channels[2] & 0x07FF) >> 2);
  sbus_packet[5]  = (uint8_t) ((sbus_channels[2] & 0x07FF) >> 10 | (sbus_channels[3] & 0x07FF) << 1);
  sbus_packet[6]  = (uint8_t) ((sbus_channels[3] & 0x07FF) >> 7  | (sbus_channels[4] & 0x07FF) << 4);
  sbus_packet[7]  = (uint8_t) ((sbus_channels[4] & 0x07FF) >> 4  | (sbus_channels[5] & 0x07FF) << 7);
  sbus_packet[8]  = (uint8_t) ((sbus_channels[5] & 0x07FF) >> 1);
  sbus_packet[9]  = (uint8_t) ((sbus_channels[5] & 0x07FF) >> 9  | (sbus_channels[6] & 0x07FF) << 2);
  sbus_packet[10] = (uint8_t) ((sbus_channels[6] & 0x07FF) >> 6  | (sbus_channels[7] & 0x07FF) << 5);
  sbus_packet[11] = (uint8_t) ((sbus_channels[7] & 0x07FF) >> 3);
  sbus_packet[12] = (uint8_t) ((sbus_channels[8] & 0x07FF));
  sbus_packet[13] = (uint8_t) ((sbus_channels[8] & 0x07FF) >> 8  | (sbus_channels[9] & 0x07FF) << 3);
  sbus_packet[14] = (uint8_t) ((sbus_channels[9] & 0x07FF) >> 5  | (sbus_channels[10] & 0x07FF) << 6);
  sbus_packet[15] = (uint8_t) ((sbus_channels[10] & 0x07FF) >> 2);
  sbus_packet[16] = (uint8_t) ((sbus_channels[10] & 0x07FF) >> 10 | (sbus_channels[11] & 0x07FF) << 1);
  sbus_packet[17] = (uint8_t) ((sbus_channels[11] & 0x07FF) >> 7  | (sbus_channels[12] & 0x07FF) << 4);
  sbus_packet[18] = (uint8_t) ((sbus_channels[12] & 0x07FF) >> 4  | (sbus_channels[13] & 0x07FF) << 7);
  sbus_packet[19] = (uint8_t) ((sbus_channels[13] & 0x07FF) >> 1);
  sbus_packet[20] = (uint8_t) ((sbus_channels[13] & 0x07FF) >> 9  | (sbus_channels[14] & 0x07FF) << 2);
  sbus_packet[21] = (uint8_t) ((sbus_channels[14] & 0x07FF) >> 6  | (sbus_channels[15] & 0x07FF) << 5);
  sbus_packet[22] = (uint8_t) ((sbus_channels[15] & 0x07FF) >> 3);

  sbus_packet[23] = 0x00; // Flags byte (Digital channels 17/18 off, Failsafe off)
  sbus_packet[24] = 0x00; // Standard SBUS Footer End Byte
}

// ==========================================
// INITIALIZATION
// ==========================================
void setup() {
  // Setup PC Debug Monitor
  Serial.begin(115200);

  // Initialize Native SBUS Hardware Serial Profile on UART2
  // Configuration settings: 100000 bps, Even Parity, 2 Stop bits, RX=16, TX=17, Inverted=true
  Serial2.begin(100000, SERIAL_8E2, 16, 17, true);

  // Configure input pins
  for (int i = 0; i < 6; i++) {
    pinMode(PWM_PINS[i], INPUT_PULLUP);
  }

  // Bind precise interrupt change routines
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[0]), ch1_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[1]), ch2_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[2]), ch3_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[3]), ch4_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[4]), ch5_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[5]), ch6_isr, CHANGE);

  // Set unused SBUS channels (7 through 16) to structural defaults (midpoint)
  for (int i = 6; i < 16; i++) {
    sbus_channels[i] = 992; 
  }
}

// ==========================================
// RUNTIME EXECUTION
// ==========================================
void loop() {
  int local_raw[6];

  // Atomic block protection: capture copies safely without mid-execution ISR changes
  noInterrupts();
  for(int i = 0; i < 6; i++) { 
    local_raw[i] = raw_pwm_values[i]; 
  }
  interrupts();

  // Convert raw inputs to standard SBUS ranges
  for (int i = 0; i < 6; i++) {
    sbus_channels[i] = pwm_to_sbus(local_raw[i]);
  }

  // Compile full structural frame array and send across Serial2
  build_sbus_packet();
  Serial2.write(sbus_packet, 25);

  // PRINT CURRENT CAPTURED VALUES TO ARDUINO SERIAL MONITOR
  Serial.print("CH1:"); Serial.print(local_raw[0]);
  Serial.print(" | CH2:"); Serial.print(local_raw[1]);
  Serial.print(" | CH3:"); Serial.print(local_raw[2]);
  Serial.print(" | CH4:"); Serial.print(local_raw[3]);
  Serial.print(" | CH5:"); Serial.print(local_raw[4]);
  Serial.print(" | CH6:"); Serial.println(local_raw[5]);

  // Frame delay (14 milliseconds is strict RC SBUS frame timing)
  delay(14); 
}
|



`#include <Arduino.h>

// ==========================================
// CONFIGURATION & PIN ASSIGNMENTS
// ==========================================
const int PWM_PINS[6] = {13, 12, 14, 27, 26, 25}; 

// Volatile variables for ISR timing capture
volatile unsigned long pulse_start[6] = {0, 0, 0, 0, 0, 0};
volatile int raw_pwm_values[6] = {1500, 1500, 1500, 1500, 1500, 1500}; 

// SBUS structural definitions
uint16_t sbus_channels[16];
uint8_t sbus_packet[25];

// ==========================================
// INTERRUPT SERVICE ROUTINES (ISR)
// ==========================================
void IRAM_ATTR ch1_isr() { if(digitalRead(PWM_PINS[0])) pulse_start[0] = micros(); else raw_pwm_values[0] = micros() - pulse_start[0]; }
void IRAM_ATTR ch2_isr() { if(digitalRead(PWM_PINS[1])) pulse_start[1] = micros(); else raw_pwm_values[1] = micros() - pulse_start[1]; }
void IRAM_ATTR ch3_isr() { if(digitalRead(PWM_PINS[2])) pulse_start[2] = micros(); else raw_pwm_values[2] = micros() - pulse_start[2]; }
void IRAM_ATTR ch4_isr() { if(digitalRead(PWM_PINS[3])) pulse_start[3] = micros(); else raw_pwm_values[3] = micros() - pulse_start[3]; }
void IRAM_ATTR ch5_isr() { if(digitalRead(PWM_PINS[4])) pulse_start[4] = micros(); else raw_pwm_values[4] = micros() - pulse_start[4]; }
void IRAM_ATTR ch6_isr() { if(digitalRead(PWM_PINS[5])) pulse_start[5] = micros(); else raw_pwm_values[5] = micros() - pulse_start[5]; }

// Map standard PWM (1000us-2000us) to strict Futaba SBUS scales (172-1811)
uint16_t pwm_to_sbus(int pwm) {
  pwm = constrain(pwm, 1000, 2000);
  return map(pwm, 1000, 2000, 172, 1811);
}

// ==========================================
// MATHEMATICALLY EXACT SBUS PACKER
// ==========================================
void build_sbus_packet() {
  sbus_packet[0]  = 0x0F; // Standard SBUS Header Byte

  // Explicit bit-packing mechanics (Splits 16 x 11-bit fields across 22 bytes)
  sbus_packet[1]  = (uint8_t) ((sbus_channels[0] & 0x07FF));
  sbus_packet[2]  = (uint8_t) ((sbus_channels[0] & 0x07FF) >> 8  | (sbus_channels[1] & 0x07FF) << 3);
  sbus_packet[3]  = (uint8_t) ((sbus_channels[1] & 0x07FF) >> 5  | (sbus_channels[2] & 0x07FF) << 6);
  sbus_packet[4]  = (uint8_t) ((sbus_channels[2] & 0x07FF) >> 2);
  sbus_packet[5]  = (uint8_t) ((sbus_channels[2] & 0x07FF) >> 10 | (sbus_channels[3] & 0x07FF) << 1);
  sbus_packet[6]  = (uint8_t) ((sbus_channels[3] & 0x07FF) >> 7  | (sbus_channels[4] & 0x07FF) << 4);
  sbus_packet[7]  = (uint8_t) ((sbus_channels[4] & 0x07FF) >> 4  | (sbus_channels[5] & 0x07FF) << 7);
  sbus_packet[8]  = (uint8_t) ((sbus_channels[5] & 0x07FF) >> 1);
  sbus_packet[9]  = (uint8_t) ((sbus_channels[5] & 0x07FF) >> 9  | (sbus_channels[6] & 0x07FF) << 2);
  sbus_packet[10] = (uint8_t) ((sbus_channels[6] & 0x07FF) >> 6  | (sbus_channels[7] & 0x07FF) << 5);
  sbus_packet[11] = (uint8_t) ((sbus_channels[7] & 0x07FF) >> 3);
  sbus_packet[12] = (uint8_t) ((sbus_channels[8] & 0x07FF));
  sbus_packet[13] = (uint8_t) ((sbus_channels[8] & 0x07FF) >> 8  | (sbus_channels[9] & 0x07FF) << 3);
  sbus_packet[14] = (uint8_t) ((sbus_channels[9] & 0x07FF) >> 5  | (sbus_channels[10] & 0x07FF) << 6);
  sbus_packet[15] = (uint8_t) ((sbus_channels[10] & 0x07FF) >> 2);
  sbus_packet[16] = (uint8_t) ((sbus_channels[10] & 0x07FF) >> 10 | (sbus_channels[11] & 0x07FF) << 1);
  sbus_packet[17] = (uint8_t) ((sbus_channels[11] & 0x07FF) >> 7  | (sbus_channels[12] & 0x07FF) << 4);
  sbus_packet[18] = (uint8_t) ((sbus_channels[12] & 0x07FF) >> 4  | (sbus_channels[13] & 0x07FF) << 7);
  sbus_packet[19] = (uint8_t) ((sbus_channels[13] & 0x07FF) >> 1);
  sbus_packet[20] = (uint8_t) ((sbus_channels[13] & 0x07FF) >> 9  | (sbus_channels[14] & 0x07FF) << 2);
  sbus_packet[21] = (uint8_t) ((sbus_channels[14] & 0x07FF) >> 6  | (sbus_channels[15] & 0x07FF) << 5);
  sbus_packet[22] = (uint8_t) ((sbus_channels[15] & 0x07FF) >> 3);

  sbus_packet[23] = 0x00; // Flags byte (Digital channels 17/18 off, Failsafe off)
  sbus_packet[24] = 0x00; // Standard SBUS Footer End Byte
}

// ==========================================
// INITIALIZATION
// ==========================================
void setup() {
  // Setup PC Debug Monitor
  Serial.begin(115200);

  // Initialize Native SBUS Hardware Serial Profile on UART2
  // Configuration settings: 100000 bps, Even Parity, 2 Stop bits, RX=16, TX=17, Inverted=true
  Serial2.begin(100000, SERIAL_8E2, 16, 17, true);

  // Configure input pins
  for (int i = 0; i < 6; i++) {
    pinMode(PWM_PINS[i], INPUT_PULLUP);
  }

  // Bind precise interrupt change routines
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[0]), ch1_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[1]), ch2_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[2]), ch3_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[3]), ch4_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[4]), ch5_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PWM_PINS[5]), ch6_isr, CHANGE);

  // Set unused SBUS channels (7 through 16) to structural defaults (midpoint)
  for (int i = 6; i < 16; i++) {
    sbus_channels[i] = 992; 
  }
}

// ==========================================
// RUNTIME EXECUTION
// ==========================================
void loop() {
  int local_raw[6];

  // Atomic block protection: capture copies safely without mid-execution ISR changes
  noInterrupts();
  for(int i = 0; i < 6; i++) { 
    local_raw[i] = raw_pwm_values[i]; 
  }
  interrupts();

  // Convert raw inputs to standard SBUS ranges
  for (int i = 0; i < 6; i++) {
    sbus_channels[i] = pwm_to_sbus(local_raw[i]);
  }

  // Compile full structural frame array and send across Serial2
  build_sbus_packet();
  Serial2.write(sbus_packet, 25);

  // PRINT CURRENT CAPTURED VALUES TO ARDUINO SERIAL MONITOR
  Serial.print("CH1:"); Serial.print(local_raw[0]);
  Serial.print(" | CH2:"); Serial.print(local_raw[1]);
  Serial.print(" | CH3:"); Serial.print(local_raw[2]);
  Serial.print(" | CH4:"); Serial.print(local_raw[3]);
  Serial.print(" | CH5:"); Serial.print(local_raw[4]);
  Serial.print(" | CH6:"); Serial.println(local_raw[5]);

  // Frame delay (14 milliseconds is strict RC SBUS frame timing)
  delay(14); 
}
```

You are now read to send to your ESP32.

1. In the IDE,  just below the File, Edit, Sketch, etc.  menu,   click the right facing arrow.   The IDE should compile and send the code to your translator ESP32.
2. When complete,  repleat the process for your second Translator ESP32 and program it.

Power down R2,  and power it back up.   You should be good.  

