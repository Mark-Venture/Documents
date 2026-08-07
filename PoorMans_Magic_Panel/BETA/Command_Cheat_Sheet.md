# BETA Magic Panel Unified Command Cheat Sheet (v2.6)

This document provides a single reference sheet for controlling both **4x8** and **8x15** matrices. 

This cheat sheet summarizes all serial commands, settings options, and pattern lists supported by the Magic Panel ESP32-C3 firmware. Commands can be sent via USB Serial (PC Monitor) or Hardware UART (GPIO 6 RX ) at **9600 baud**. ** Connect your LED Panel to GPIO 6.**  

Inside Droidlink Slave, configure the serial port for Marcduino,  9600.  Connect GPIO 25 (Serial1) or GPIO 17 (Serial2) from the DroidLink Slave to **GPIO 20 on the ESP32 Mini.**

> [!NOTE]
> Some systems to not accept a colon (':') as a separator in sequences like T23:15:C1,  in those cases you can use an equal sign ('=') instead.  
> 
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


4. Complete Pattern Registry (0 - 200)
8x8 and 8x15 Configurations: All patterns below are 100% supported.
4x8 Configuration: Patterns marked with ❌ Disabled are excluded to prevent distorted or broken rendering.
Pattern ID	Pattern Name	8x8 & 8x15 Status	4x8 Panel Status	Notes / Reasons for 4x8 Exclusions
0	Off	✅ Supported	✅ Supported	
1	On Indefinite	✅ Supported	✅ Supported	
2	On 2s	✅ Supported	✅ Supported	
3	On 5s	✅ Supported	✅ Supported	
4	On 10s	✅ Supported	✅ Supported	
5	Toggle	✅ Supported	✅ Supported	
6	Alert 4s	✅ Supported	✅ Supported	
7	Alert 10s	✅ Supported	✅ Supported	
8	Trace Up Fill	✅ Supported	✅ Supported	
9	Trace Up Line	✅ Supported	✅ Supported	
10	Trace Down Fill	✅ Supported	✅ Supported	
11	Trace Down Line	✅ Supported	✅ Supported	
12	Trace Right Fill	✅ Supported	✅ Supported	
13	Trace Right Line	✅ Supported	✅ Supported	
14	Trace Left Fill	✅ Supported	✅ Supported	
15	Trace Left Line	✅ Supported	✅ Supported	
16	Expand Fill	✅ Supported	✅ Supported	Center expands dynamically on 4x8
17	Expand Ring	✅ Supported	✅ Supported	
18	Compress Fill	✅ Supported	✅ Supported	Center compresses dynamically on 4x8
19	Compress Ring	✅ Supported	✅ Supported	
20	Cross	✅ Supported	❌ Disabled	Graphics require a minimum of 8 columns to draw
21	Cylon Column	✅ Supported	✅ Supported	Loops scaled to custom duration
22	Cylon Row	✅ Supported	✅ Supported	Loops scaled to custom duration
23	Eye Scan	✅ Supported	✅ Supported	Simultaneous bidirectional sweep
24	Fade Out/In	✅ Supported	✅ Supported	
25	Fade Out	✅ Supported	✅ Supported	
26	Flash All	✅ Supported	✅ Supported	
27	Flash Vertical	✅ Supported	✅ Supported	Scales column divisions dynamically
28	Flash Quadrants	✅ Supported	✅ Supported	Scales quadrant divisions dynamically
29	Two Loop	✅ Supported	✅ Supported	Scales perimeter path dynamically
30	One Loop	✅ Supported	✅ Supported	Scales perimeter path dynamically
31	Test Fill	✅ Supported	✅ Supported	
32	Test Pixel	✅ Supported	✅ Supported	
33	AI Logo	✅ Supported	❌ Disabled	Hardcoded 8x8 bitmap; cannot render on 4-wide screen
34	2GWD Logo	✅ Supported	❌ Disabled	Hardcoded 8x8 bitmap; cannot render on 4-wide screen
35	Quadrant TL->TR->BR->BL	✅ Supported	✅ Supported	Scales quadrant boundaries dynamically
36	Quadrant TR->TL->BL->BR	✅ Supported	✅ Supported	Scales quadrant boundaries dynamically
37	Quadrant TR->BR->BL->TL	✅ Supported	✅ Supported	Scales quadrant boundaries dynamically
38	Quadrant TL->BL->BR->TR	✅ Supported	✅ Supported	Scales quadrant boundaries dynamically
39	Random Pixel	✅ Supported	✅ Supported	
40	Countdown 9-0	✅ Supported	✅ Supported	Vertically and horizontally centered
41	Countdown 3-0	✅ Supported	✅ Supported	Vertically and horizontally centered
42	Alert Random 4s	✅ Supported	✅ Supported	
43	Alert Random 8s	✅ Supported	✅ Supported	
44	Smiley Face	✅ Supported	❌ Disabled	Hardcoded 8x8 graphic
45	Sad Face	✅ Supported	❌ Disabled	Hardcoded 8x8 graphic
46	Heart	✅ Supported	❌ Disabled	Hardcoded 8x8 graphic
47	Checkerboard	✅ Supported	✅ Supported	Scales tiles dynamically using 2D coordinates
48	Compress In Fill	✅ Supported	✅ Supported	
49	Compress In Clear	✅ Supported	✅ Supported	
50	Explode Out Fill	✅ Supported	✅ Supported	
51	Explode Out Clear	✅ Supported	✅ Supported	
52	VU Meter Columns Up	✅ Supported	✅ Supported	Grows from bottom to top
53	VU Meter Rows Left	✅ Supported	✅ Supported	Grows from right to left
54	VU Meter Columns Down	✅ Supported	✅ Supported	Grows from top to bottom
55	VU Meter Rows Right	✅ Supported	✅ Supported	Grows from left to right
56	Animated Heart	✅ Supported	❌ Disabled	Hardcoded 8x8 animated graphics sequence
57	Rainbow Cycle	✅ Supported	✅ Supported	
58	Fire Effect	✅ Supported	✅ Supported	
59	Twinkle	✅ Supported	✅ Supported	
60	Plasma	✅ Supported	✅ Supported	
61	Game of Life	✅ Supported	❌ Disabled	Conway's rules require a minimum 8x8 simulation grid
62	Matrix Rain	✅ Supported	✅ Supported	Default color: Green
63	3D Cube	✅ Supported	❌ Disabled	3D projection algorithms require minimum 8x8 resolution
64	Kaleidoscope	✅ Supported	✅ Supported	Mirrors coordinates dynamically based on panel bounds
65	Raindrops	✅ Supported	✅ Supported	Default color: Aqua
66	Drip Effect	✅ Supported	✅ Supported	Default color: Aqua
67	Pac-Man	✅ Supported	❌ Disabled	Hardcoded 8x8 animated graphics sequence
68	Space Invaders	✅ Supported	❌ Disabled	Hardcoded 8x8 animated graphics sequence
69 - 79	Unassigned	—	—	
80	Bouncing Text	✅ Supported	✅ Supported	Centered dynamically
81 - 96	Unassigned	—	—	
97	Scroll Text (EN)	✅ Supported	✅ Supported	Centered dynamically
98	Scroll Text (AU)	✅ Supported	✅ Supported	Centered dynamically
99	Test All Patterns	✅ Supported	✅ Supported	Loops through enabled patterns
100	PSI Solid Red	✅ Supported	✅ Supported	Astromech
101	PSI Solid Blue	✅ Supported	✅ Supported	Astromech
102	PSI Solid Green	✅ Supported	✅ Supported	Astromech
103	PSI Solid Yellow	✅ Supported	✅ Supported	Astromech
104	PSI Solid Cyan	✅ Supported	✅ Supported	Astromech
105	PSI Solid Magenta	✅ Supported	✅ Supported	Astromech
106	PSI Solid White	✅ Supported	✅ Supported	Astromech
107	PSI Color Wipe Down	✅ Supported	✅ Supported	Astromech
108	PSI Color Wipe Up	✅ Supported	✅ Supported	Astromech
109	PSI Random Flicker	✅ Supported	✅ Supported	Astromech
110	PSI Pulse	✅ Supported	✅ Supported	Astromech
111	PSI Rainbow	✅ Supported	✅ Supported	Astromech
112	PSI March Horizontal	✅ Supported	✅ Supported	Astromech
113	PSI March Vertical	✅ Supported	✅ Supported	Astromech
114	PSI March Diagonal	✅ Supported	✅ Supported	Astromech
115	PSI March Checkerboard	✅ Supported	✅ Supported	Astromech
116	PSI March Spiral	✅ Supported	✅ Supported	Astromech
117	R2-D2 Communication	✅ Supported	✅ Supported	Astromech
118	R2-D2 Thinking	✅ Supported	✅ Supported	Astromech (swirls scale dynamically)
119	R2-D2 Alert	✅ Supported	✅ Supported	Astromech (flashes scale dynamically)
120 - 199	Unassigned	—	—	
200	Smart Demo	✅ Supported	✅ Supported	Curated demo show
