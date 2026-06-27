
# Flysky in PWM mode.  Output as SBUS-A #1 and SUBS-A #2

This allows me to use the Left Stick, SWA, SWB, VRR  as one "DS650", and Right Stick, SWC, SWD, VRB as the "other DS650" 

Because this emulates a Stick and 3 Buttons, and the DS650 has a Stick and 4 buttons you lose 1 button "per remote".   

Note: SWC is 3 position (on/mid/off),  in translator software I have it limited to two positions(on/off) because the buttons on DS650 are only two positions(on/off).

The stick/button associations are based on the mappings of your FlySky FS-i6X.    

## FlySky settings:  

|Input Channel|Value|Notes|
|:--:|:--:|:--:|
|Sticks Mode| Mode 2| Left stick up=ch3, Left Stick left= Ch4, right stick up=ch2, right stick left=ch1|
|Aux Switches| SwA, SwB, SwC, SwD, VrA, VrB = On| enable all extra switches/knobs|
|Aux Switches| Ch = 10|This aloows for 10 channels rather than the default of 6|
|Aux Channels Ch5| Source SwA | sets SWA=ch5|
|Aux Channels Ch6| Source SwB | sets SWB=ch6|
|Aux Channels Ch7| Source SwC | sets SWC=ch7|
|Aux Channels Ch8| Source SwD | sets SWD=ch8|
|Aux Channels Ch9| Source VrA | sets VrA=ch9|
|Aux Channels Ch10| Source VrB | sets VrB=ch10|

* Note: Rx1 Ch7 is 3 position. I want high to be on, neutral and negative to be off.
* Note: by default,  swtich A/B/C/D in the UP position = OFF, down = On.  You can reverse this in the remote menus if you wish. 
* Note: by default VRA and VRB Fully Counter Clockwise is OFF,  fully clockwise is ON.  to simulate "button press" for VrA/VrB, just rotate fully clickwise, then back counter clockwise.




## Hardware Wiring (10-Channel Input, Dual Split Output)

|FS-ia10b|ESP32 Input Pin| Output Channel|Notes|
|:---:|:---:|:--:|:--:|
|RX1 CH1 (right stick)|GPIO 13|TX1 ch 1| Remote 1 Stick Left/right|
|RX1 CH2 (right stick)|GPIO 12|TX1 Ch 2| Remote 1 Stick Up/Down|
|RX1 CH3 (left stick)|GPIO 14|TX2 Ch 2| Remote 2 Stick Up/Down|
|RX1 CH4 (left stick)|GPIO 27|TX2 Ch 1| Remote 2 Stick Left/right|
|RX1 CH5 (SwA)|GPIO 26|TX1 Ch 3| Remote 1 Button 3/A|
|RX1 CH6 (SwB)|GPIO 25|TX1 Ch 4| Remote 1 Button 4/B|
|RX1 CH7 (SwC)(3-Pos Switch)|GPIO 23|TX2 Ch 3| Remote 2 Button 3/A|
|RX1 CH8 (SwD)|GPIO 19|Tx2 Ch 4| Remote 2 Button 4/B|
|RX1 CH9 (VrA)|GPIO 18|TX1 ch 5| Remote 1 Button 5/C|
|RX1 CH10(VrB)|GPIO 5|TX2 Ch 5| Remote 2 Button 5/C|


|ESP32 Output Pins|Destination Device| Notes|
|:---:|:---:|:--:|
|TX2 (GPIO 17)|Remote 1 SBUS RX|Natively Inverted Split Stream 1|
|TX1 (GPIO 4)|Remote 2 SBUS RX|Natively Inverted Split Stream 2|





## Code:

```

#include <Arduino.h>

// ==========================================
// CONFIGURATION & PIN ASSIGNMENTS (10 CHANNELS)
// ==========================================
const int rx1_pins[] = {13, 12, 14, 27, 26, 25, 23, 19, 18, 5};

// Volatile arrays for 10-channel ISR tracking
volatile unsigned long rx1_start[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
volatile int rx1_raw[] = {1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500};

// Local storage array for cross-mapping
uint16_t rx1_mapped_sbus[10];

// Destination SBUS channel blocks (16 channels each)
uint16_t tx1_channels[16];
uint16_t tx2_channels[16];

uint8_t packet1[25];
uint8_t packet2[25];

// ==========================================
// INTERRUPT SERVICE ROUTINES (10-CHANNEL INTERRUPTS)
// ==========================================
void IRAM_ATTR ch1_isr()  { if(digitalRead(rx1_pins[0])) rx1_start[0] = micros(); else rx1_raw[0] = micros() - rx1_start[0]; }
void IRAM_ATTR ch2_isr()  { if(digitalRead(rx1_pins[1])) rx1_start[1] = micros(); else rx1_raw[1] = micros() - rx1_start[1]; }
void IRAM_ATTR ch3_isr()  { if(digitalRead(rx1_pins[2])) rx1_start[2] = micros(); else rx1_raw[2] = micros() - rx1_start[2]; }
void IRAM_ATTR ch4_isr()  { if(digitalRead(rx1_pins[3])) rx1_start[3] = micros(); else rx1_raw[3] = micros() - rx1_start[3]; }
void IRAM_ATTR ch5_isr()  { if(digitalRead(rx1_pins[4])) rx1_start[4] = micros(); else rx1_raw[4] = micros() - rx1_start[4]; }
void IRAM_ATTR ch6_isr()  { if(digitalRead(rx1_pins[5])) rx1_start[5] = micros(); else rx1_raw[5] = micros() - rx1_start[5]; }
void IRAM_ATTR ch7_isr()  { if(digitalRead(rx1_pins[6])) rx1_start[6] = micros(); else rx1_raw[6] = micros() - rx1_start[6]; }
void IRAM_ATTR ch8_isr()  { if(digitalRead(rx1_pins[7])) rx1_start[7] = micros(); else rx1_raw[7] = micros() - rx1_start[7]; }
void IRAM_ATTR ch9_isr()  { if(digitalRead(rx1_pins[8])) rx1_start[8] = micros(); else rx1_raw[8] = micros() - rx1_start[8]; }
void IRAM_ATTR ch10_isr() { if(digitalRead(rx1_pins[9])) rx1_start[9] = micros(); else rx1_raw[9] = micros() - rx1_start[9]; }

uint16_t pwm_to_sbus(int pwm) {
  pwm = constrain(pwm, 1000, 2000);
  return map(pwm, 1000, 2000, 172, 1811);
}

// Universal Bit Packer
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
  delay(500);

  // Setup dual serial tracking with inverted logics
  Serial2.begin(100000, SERIAL_8E2, 16, 17, true); // TX2 out Pin 17
  Serial1.begin(100000, SERIAL_8E2, 2, 4, true);   // TX1 out Pin 4

  // Declare 10 pins as inputs
  for (int i = 0; i < 10; i++) {
    pinMode(rx1_pins[i], INPUT_PULLUP);
  }

  // Attach all 10 distinct interrupt triggers
  attachInterrupt(digitalPinToInterrupt(rx1_pins[0]), ch1_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[1]), ch2_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[2]), ch3_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[3]), ch4_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[4]), ch5_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[5]), ch6_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[6]), ch7_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[7]), ch8_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[8]), ch9_isr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(rx1_pins[9]), ch10_isr, CHANGE);

  // Default baseline unassigned lanes to central safe configurations (992)
  for (int i = 0; i < 16; i++) {
    tx1_channels[i] = 992;
    tx2_channels[i] = 992;
  }
}

// ==========================================
// RUNTIME EXECUTION
// ==========================================
void loop() {
  int local_rx1[10];

  // Capture current PWM intervals safely
  noInterrupts();
  for(int i = 0; i < 10; i++) { 
    local_rx1[i] = rx1_raw[i]; 
  }
  interrupts();

  // Convert inputs to SBUS scale configurations
  for (int i = 0; i < 10; i++) {
    // Structural implementation for Channel 7 (3-position logic)
    if (i == 6) { 
      if (local_rx1[6] > 1750) {
        rx1_mapped_sbus[6] = 1811; // High => ON
      } else {
        rx1_mapped_sbus[6] = 172;  // Neutral or Low => OFF
      }
    } else {
      rx1_mapped_sbus[i] = pwm_to_sbus(local_rx1[i]);
    }
  }

  // ==========================================
  // DIRECT CUSTOM MATRIX MAPPING BLOCK
  // ==========================================
  // TX1 Stream Mapping Assignments (Note: Array Indices start at 0, so Ch1 = index 0)
  tx1_channels[0] = rx1_mapped_sbus[0]; // RX1 Ch1 => TX1 Ch1
  tx1_channels[1] = rx1_mapped_sbus[1]; // RX1 Ch2 => TX1 Ch2
  tx1_channels[2] = rx1_mapped_sbus[4]; // RX1 Ch5 => TX1 Ch3
  tx1_channels[3] = rx1_mapped_sbus[5]; // RX1 Ch6 => TX1 Ch4
  tx1_channels[4] = rx1_mapped_sbus[8]; // RX1 Ch9 => TX1 Ch5

  // TX2 Stream Mapping Assignments
  tx2_channels[0] = rx1_mapped_sbus[3]; // RX1 Ch4 => TX2 Ch1
  tx2_channels[1] = rx1_mapped_sbus[2]; // RX1 Ch3 => TX2 Ch2
  tx2_channels[2] = rx1_mapped_sbus[6]; // RX1 Ch7 => TX2 Ch3 (Special Toggle)
  tx2_channels[3] = rx1_mapped_sbus[7]; // RX1 Ch8 => TX2 Ch4
  tx2_channels[4] = rx1_mapped_sbus[9]; // RX1 Ch10 => TX2 Ch5

  // Assemble split packets
  serialize_sbus(tx1_channels, packet1);
  serialize_sbus(tx2_channels, packet2);

  // Broadcast data sets
  Serial2.write(packet1, 25); // Pushes target assignments to TX2 (GPIO 17)
  Serial1.write(packet2, 25); // Pushes target assignments to TX1 (GPIO 4)

  // Verify inputs on the computer serial window
  Serial.print("Rx1-Ch7 Raw: "); Serial.print(local_rx1[6]);
  Serial.print(" | Tx2-Ch3 Out: "); Serial.println(tx2_channels[2]);

  delay(14); 
}


```
