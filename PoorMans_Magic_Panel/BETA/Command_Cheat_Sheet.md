# BETA Magic Panel Unified Command Cheat Sheet (v2.6)

This document provides a single reference sheet for controlling both **4x8** and **8x15** matrices. 

This cheat sheet summarizes all serial commands, settings options, and pattern lists supported by the Magic Panel ESP32-C3 firmware. Commands can be sent via USB Serial (PC Monitor) or Hardware UART (GPIO 6 RX ) at **9600 baud**. ** Connect your LED Panel to GPIO 6.**  

Inside Droidlink Slave, configure the serial port for Marcduino,  9600.  Connect GPIO 25 (Serial1) or GPIO 17 (Serial2) from the DroidLink Slave to **GPIO 20 on the ESP32 Mini.**

> [!NOTE]
> For DroidLink, commands are case-sensitive and must be upper case. A leading colon (`:`) is required (e.g. `T01` needs to be sent as `:T01` ).  Equal sign ('=') should be used as a separator instead of a colon (':').  Example....    :T23=15=C1   Runs the Eye Scan pattern for 15 seconds in the color Green.
   
---

## 1. Parameters & System Commands

| Command | Action | Example | Notes |
| :--- | :--- | :--- | :--- |
| **`B<0-255>`** | Set brightness | `B120` | Default is `60` |
| **`V<1-100>`** / **`SP`** | Set animation speed | `V50` | Default is `50` |
| **`C<0-8>`** | Preset Color | `C1` | Colors: `0`=Red, `1`=Green, `2`=Blue, `3`=Yellow, `4`=Cyan, `5`=Magenta, `6`=White, `7`=Orange, `8`=Pink |
| **`C9`** | Rainbow Color Mode | `C9` | Dynamically cycles color hue |
| **`C<r>,<g>,<b>`** | Custom RGB Color | `C0,255,255` | Aqua/Light Blue |
| **`P<0/1>`** | Run Mode | `P1` | `0` = Timed (8 seconds), `1` = Always On |
| **`ON`** / **`A`** | Turn all LEDs on | `ON` | Fills display with active color |
| **`OFF`** / **`D`** | Standby mode | `OFF` | Clears display and halts active pattern |
| **`FONT<0/1>`** | Set font family | `FONT1` | `0` = Standard Font, `1` = Aurebesh Font |
| **`SAVE`** | Save configuration | `SAVE` | Commits current parameters to EEPROM |
| **`LOAD`** | Load configuration | `LOAD` | Loads parameters from EEPROM |
| **`STATUS`** | Display status | `STATUS` | Prints active speed, color, brightness, etc. to Serial |
| **`LIST`** | List patterns | `LIST` | Prints all pattern names and IDs to Serial |
| **`HELP`** / **`HELP FULL`**| Show Help info | `HELP` | Prints quick-start or detailed documentation |
| **`START<id>`** | Set startup pattern | `START62` | Configures pattern to load on bootup |
| **`TRANSITION<0/1>`** | Toggle fade effect | `TRANSITION1` | `0` = Instant change, `1` = Fade-out previous pattern |
| **`PLAYLIST_RUN:<list>`**| Run playlist | `PLAYLIST_RUN:57,62` | Plays comma-separated list of pattern IDs |

---

## 2. Text Commands

| Command | Action | Example | Notes |
| :--- | :--- | :--- | :--- |
| **`TEXT:<string>`** / **`TEXT=<str>`** | Scroll custom text | `TEXT:Hello!` | Dynamically centered vertically |
| **`TEXT_BOUNCE:<string>`** | Bouncing text letters | `TEXT_BOUNCE:C3` | Dynamically centered horizontally & vertically |
| **`TEXTSAVE<0-9>:<string>`** | Save text to slot | `TEXTSAVE0:HELLO` | Saves to slot `0` through `9` in EEPROM |
| **`TEXTLOAD<0-9>`** | Load & scroll text slot | `TEXTLOAD0` | Scrolls the text stored in the slot |

---

## 3. Pattern Execution Syntax

Trigger animations using either `:` or `=` as delimiters. Chained arguments are fully supported.

* **Format**: `T<id>` or `T<id>:<seconds>` or `T<id>:C<color>` or `T<id>:<seconds>:C<color>`
* **Examples**:
  - `T57` (Runs pattern 57 indefinitely or for default timed duration)
  - `T57:30` or `T57=30` (Runs pattern 57 for 30 seconds)
  - `T62:C1` or `T62=C1` (Runs pattern 62 in Green)
  - `T65:C0,255,255` (Runs pattern 65 in Aqua/Cyan)
  - `T62:30:C1` or `T62=30=C1` (Runs pattern 62 in Green for 30 seconds)

---

## 4. Complete Pattern Registry (0 - 200)

The table below lists all patterns. **If a pattern is disabled on the 4x8 panel, it is noted in red.** All patterns are fully enabled on the 8x15 matrix.

| Pattern ID | Pattern Name | 4x8 Panel Status |
| :---: | :--- | :--- |
| **0** | Off | ✅ Supported |
| **1** | On Indefinite | ✅ Supported |
| **2** | On 2s | ✅ Supported |
| **3** | On 5s | ✅ Supported |
| **4** | On 10s | ✅ Supported |
| **5** | Toggle | ✅ Supported |
| **6** | Alert 4s | ✅ Supported |
| **7** | Alert 10s | ✅ Supported |
| **8** | Trace Up Fill | ✅ Supported |
| **9** | Trace Up Line | ✅ Supported |
| **10** | Trace Down Fill | ✅ Supported |
| **11** | Trace Down Line | ✅ Supported |
| **12** | Trace Right Fill | ✅ Supported |
| **13** | Trace Right Line | ✅ Supported |
| **14** | Trace Left Fill | ✅ Supported |
| **15** | Trace Left Line | ✅ Supported |
| **16** | Expand Fill | ✅ Supported *(Center expands dynamically)* |
| **17** | Expand Ring | ✅ Supported |
| **18** | Compress Fill | ✅ Supported *(Center compresses dynamically)* |
| **19** | Compress Ring | ✅ Supported |
| **20** | Cross | ❌ **Disabled** *(Needs 8 columns)* |
| **21** | Cylon Column | ✅ Supported |
| **22** | Cylon Row | ✅ Supported |
| **23** | Eye Scan | ✅ Supported *(Bidirectional back-and-forth)* |
| **24** | Fade Out/In | ✅ Supported |
| **25** | Fade Out | ✅ Supported |
| **26** | Flash All | ✅ Supported |
| **27** | Flash Vertical | ✅ Supported *(Scales col divisions)* |
| **28** | Flash Quadrants | ✅ Supported *(Scales quadrant divisions)* |
| **29** | Two Loop | ✅ Supported *(Scales to perimeter)* |
| **30** | One Loop | ✅ Supported *(Scales to perimeter)* |
| **31** | Test Fill | ✅ Supported |
| **32** | Test Pixel | ✅ Supported |
| **33** | AI Logo | ❌ **Disabled** *(Hardcoded 8x8 bitmap)* |
| **34** | 2GWD Logo | ❌ **Disabled** *(Hardcoded 8x8 bitmap)* |
| **35** | Quadrant TL->TR->BR->BL | ✅ Supported *(Scales quadrant boundaries)* |
| **36** | Quadrant TR->TL->BL->BR | ✅ Supported *(Scales quadrant boundaries)* |
| **37** | Quadrant TR->BR->BL->TL | ✅ Supported *(Scales quadrant boundaries)* |
| **38** | Quadrant TL->BL->BR->TR | ✅ Supported *(Scales quadrant boundaries)* |
| **39** | Random Pixel | ✅ Supported |
| **40** | Countdown 9-0 | ✅ Supported *(Centered)* |
| **41** | Countdown 3-0 | ✅ Supported *(Centered)* |
| **42** | Alert Random 4s | ✅ Supported |
| **43** | Alert Random 8s | ✅ Supported |
| **44** | Smiley Face | ❌ **Disabled** *(Hardcoded 8x8 bitmap)* |
| **45** | Sad Face | ❌ **Disabled** *(Hardcoded 8x8 bitmap)* |
| **46** | Heart | ❌ **Disabled** *(Hardcoded 8x8 bitmap)* |
| **47** | Checkerboard | ✅ Supported *(Uses 2D coordinates)* |
| **48** | Compress In Fill | ✅ Supported |
| **49** | Compress In Clear | ✅ Supported |
| **50** | Explode Out Fill | ✅ Supported |
| **51** | Explode Out Clear | ✅ Supported |
| **52** | VU Meter Columns Up | ✅ Supported *(Starts bottom, grows up)* |
| **53** | VU Meter Rows Left | ✅ Supported *(Starts right, grows left)* |
| **54** | VU Meter Columns Down | ✅ Supported *(Starts top, grows down)* |
| **55** | VU Meter Rows Right | ✅ Supported *(Starts left, grows right)* |
| **56** | Animated Heart | ❌ **Disabled** *(Hardcoded 8x8 bitmaps)* |
| **57** | Rainbow Cycle | ✅ Supported |
| **58** | Fire Effect | ✅ Supported |
| **59** | Twinkle | ✅ Supported |
| **60** | Plasma | ✅ Supported |
| **61** | Game of Life | ❌ **Disabled** *(Needs minimum 8x8 grid)* |
| **62** | Matrix Rain | ✅ Supported *(Default color: Green)* |
| **63** | 3D Cube | ❌ **Disabled** *(Needs minimum 8x8 grid)* |
| **64** | Kaleidoscope | ✅ Supported *(Mirrors coordinates dynamically)* |
| **65** | Raindrops | ✅ Supported *(Default color: Aqua)* |
| **66** | Drip Effect | ✅ Supported *(Default color: Aqua)* |
| **67** | Pac-Man | ❌ **Disabled** *(Hardcoded 8x8 bitmaps)* |
| **68** | Space Invaders | ❌ **Disabled** *(Hardcoded 8x8 bitmaps)* |
| *69 - 79* | *Unassigned* | — |
| **80** | Bouncing Text | ✅ Supported *(Centered)* |
| *81 - 96* | *Unassigned* | — |
| **97** | Scroll Text (EN) | ✅ Supported *(Centered)* |
| **98** | Scroll Text (AU) | ✅ Supported *(Centered)* |
| **99** | Test All Patterns | ✅ Supported |
| **100** | PSI Solid Red | ✅ Supported *(Astromech)* |
| **101** | PSI Solid Blue | ✅ Supported *(Astromech)* |
| **102** | PSI Solid Green | ✅ Supported *(Astromech)* |
| **103** | PSI Solid Yellow | ✅ Supported *(Astromech)* |
| **104** | PSI Solid Cyan | ✅ Supported *(Astromech)* |
| **105** | PSI Solid Magenta | ✅ Supported *(Astromech)* |
| **106** | PSI Solid White | ✅ Supported *(Astromech)* |
| **107** | PSI Color Wipe Down | ✅ Supported *(Astromech)* |
| **108** | PSI Color Wipe Up | ✅ Supported *(Astromech)* |
| **109** | PSI Random Flicker | ✅ Supported *(Astromech)* |
| **110** | PSI Pulse | ✅ Supported *(Astromech)* |
| **111** | PSI Rainbow | ✅ Supported *(Astromech)* |
| **112** | PSI March Horizontal | ✅ Supported *(Astromech)* |
| **113** | PSI March Vertical | ✅ Supported *(Astromech)* |
| **114** | PSI March Diagonal | ✅ Supported *(Astromech)* |
| **115** | PSI March Checkerboard | ✅ Supported *(Astromech)* |
| **116** | PSI March Spiral | ✅ Supported *(Astromech)* |
| **117** | R2-D2 Communication | ✅ Supported *(Astromech)* |
| **118** | R2-D2 Thinking | ✅ Supported *(Astromech - Swirl centers dynamically)* |
| **119** | R2-D2 Alert | ✅ Supported *(Astromech - Flashes quadrants dynamically)* |
| *120 - 199* | *Unassigned* | — |
| **200** | Smart Demo | ✅ Supported |
