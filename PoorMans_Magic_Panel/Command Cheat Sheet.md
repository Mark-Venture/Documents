# Magic Panel Command Cheat Sheet (v2.6)

This cheat sheet summarizes all serial commands, settings options, and pattern lists supported by the Magic Panel ESP32-C3 firmware. Commands can be sent via USB Serial (PC Monitor) or Hardware UART (GPIO 5 RX / GPIO 6 TX) at **9600 baud**.

> [!NOTE]
> Commands are case-insensitive. A leading colon (`:`) or star (`*`) is optional and will be automatically stripped (e.g. `:T01` is identical to `T01`).

---

## 1. Pattern Control

| Command | Action | Example |
| :--- | :--- | :--- |
| **`T<id>`** or **`S<id>`** | Runs the specified pattern by ID (0-200) | `T23` (Run Eye Scan) |
| **`T<id>:<seconds>`** | Runs a pattern for a temporary duration in seconds | `T23:30` (Runs Eye Scan for 30s) |
| **`T<id>:<seconds>:C<color>`** | Runs a pattern with custom duration and preset color index | `T57:30:C1` (Rainbow Cycle for 30s using Green) |
| **`DEMO`** or **`T200`** | Runs the curated Smart Demo animation loop | `DEMO` |

---

## 2. Display Control

| Command | Action | Example |
| :--- | :--- | :--- |
| **`A`** or **`ON`** | Turn all LEDs ON (with current active color) | `ON` |
| **`D`** or **`OFF`** | Turn all LEDs OFF | `OFF` |
| **`B<value>`** | Set brightness level (0 - 255) | `B128` (50% brightness) |
| **`V<value>`** or **`SP<value>`** | Set animation speed (1 - 100) | `V80` (Fast animation speed) |
| **`P<mode>`** | Playback mode: `P0` = Timed loops, `P1` = Run Indefinitely | `P1` |

### Preset Colors (`C<index>`)
* **`C0`** = Red
* **`C1`** = Green
* **`C2`** = Blue
* **`C3`** = White
* **`C4`** = Yellow
* **`C5`** = Cyan
* **`C6`** = Magenta
* **`C7`** = Orange
* **`C8`** = Purple
* **`C9`** = Rainbow Mode (Auto color cycle)

### Custom RGB Colors
Set a direct RGB value using the format **`C<r>,<g>,<b>`** (values 0-255):
* `C0,255,0` (Green)
* `C255,100,0` (Warm Orange)
* `C0,180,255` (Ice Blue)

---

## 3. Scrolling Text Commands

> [!IMPORTANT]
> If your host controller (such as a MarcDuino board) splits commands on colons, **do not use colons in your text strings**. Use space (` `) or equals (`=`) as separators instead.

| Delimiter | Standard Scroll | Bouncing Scroll | Saved Text Load |
| :--- | :--- | :--- | :--- |
| **Space (` `)** | `:TEXT HELLO` | `:TEXT_BOUNCE ALERT` | `:TEXTLOAD 3` |
| **Equals (`=`)** | `:TEXT=HELLO` | `:TEXT_BOUNCE=ALERT` | `:TEXTLOAD=3` |
| **Colon (`:`)** | `:TEXT:HELLO` | `:TEXT_BOUNCE:ALERT` | `:TEXTLOAD:3` |

### Saving Messages in Memory (10 Slots: 0 - 9)
* **Using Equals**: `:TEXTSAVE3=SYSTEM ACTIVE`
* **Using Space**: `:TEXTSAVE3 SYSTEM ACTIVE`
* **Using Colon**: `:TEXTSAVE3:SYSTEM ACTIVE`

---

## 4. System Commands

| Command | Action | Description |
| :--- | :--- | :--- |
| **`SAVE`** | Save settings | Persists current brightness, color, speed, font, mode, and start pattern to EEPROM. |
| **`LOAD`** | Load settings | Force loads stored settings from EEPROM. |
| **`STATUS`** | Print status | Prints configuration parameters and stored texts to Serial. |
| **`LIST`** | Print pattern list | Prints all pattern names and IDs (marks 8x8 only patterns as `[DISABLED]`). |
| **`HELP`** | Quick help | Displays quick guide on Serial monitor. |
| **`HELP FULL`** | Full guide | Displays detailed usage FAQ. |
| **`START<id>`** | Set startup pattern | Configures which pattern runs automatically on boot. Example: `START109`. |
| **`TRANSITION<value>`** | Smooth fade | `TRANSITION1` enables smooth fading between patterns; `TRANSITION0` disables. |

---

## 5. Complete Pattern List

The following list shows all pattern IDs, their categories, and whether they are active on your **4x8** panel.

> [!WARNING]
> Pattern IDs marked **[DISABLED]** require an 8x8 panel matrix size for static sprites/digits and will print a "disabled" warning if called.

### Basic Patterns
* **`0`**: Off (Clear display)
* **`1`**: On Indefinite (Solid color fill)
* **`2`**: On 2 seconds
* **`3`**: On 5 seconds
* **`4`**: On 10 seconds
* **`5`**: Toggle (Toggle panel state on/off)
* **`6`**: Alert 4 seconds (Red alert flash sequence)
* **`7`**: Alert 10 seconds

### Trace Patterns (Progressive filling)
* **`8`**: Trace Up Fill
* **`9`**: Trace Up Line
* **`10`**: Trace Down Fill
* **`11`**: Trace Down Line
* **`12`**: Trace Right Fill
* **`13`**: Trace Right Line
* **`14`**: Trace Left Fill
* **`15`**: Trace Left Line

### Expand/Compress Effects
* **`16`**: Expand Fill (Fills outward from center)
* **`17`**: Expand Ring (Rectangular ring grows outward)
* **`18`**: Compress Fill (Shrinks inward to center)
* **`19`**: Compress Ring (Rectangular ring shrinks inward)

### Shapes & Loops
* **`20`**: **[DISABLED]** Cross
* **`21`**: Cylon Column (Slowed vertical bar sweeping side-to-side)
* **`22`**: Cylon Row (Horizontal bar sweeping top-to-bottom)
* **`23`**: Eye Scan (Simultaneous horizontal and vertical sweeping lines)
* **`24`**: Fade Out/In
* **`25`**: Fade Out
* **`26`**: Flash All
* **`27`**: Flash Vertical (Flashes left vs right sides)
* **`28`**: Flash Quadrants (Flashes TL, TR, BR, BL)
* **`29`**: Two Loop (Traces outer perimeter twice)
* **`30`**: One Loop (Traces outer perimeter once)
* **`31`**: Test Fill
* **`32`**: Test Pixel (Illuminates individual pixels sequentially)
* **`33`**: **[DISABLED]** AI Logo
* **`34`**: **[DISABLED]** 2GWD Logo
* **`35`**: Quadrant clockwise sweep (TL $\rightarrow$ TR $\rightarrow$ BR $\rightarrow$ BL)
* **`36`**: Quadrant counter-clockwise sweep (TR $\rightarrow$ TL $\rightarrow$ BL $\rightarrow$ BR)
* **`37`**: Quadrant sweep (TR $\rightarrow$ BR $\rightarrow$ BL $\rightarrow$ TL)
* **`38`**: Quadrant sweep (TL $\rightarrow$ BL $\rightarrow$ BR $\rightarrow$ TR)
* **`39`**: Random Pixel
* **`40`**: **[DISABLED]** Countdown 9-0
* **`41`**: **[DISABLED]** Countdown 3-0
* **`42`**: Alert Random 4 seconds
* **`43`**: Alert Random 8 seconds
* **`44`**: **[DISABLED]** Smiley Face
* **`45`**: **[DISABLED]** Sad Face
* **`46`**: **[DISABLED]** Heart
* **`47`**: Checkerboard (Serpentine aligned chess pattern)

### Central Compression/Explosion
* **`48`**: Compress In Fill
* **`49`**: Compress In Clear
* **`50`**: Explode Out Fill
* **`51`**: Explode Out Clear

### VU Meters
* **`52`**: VU Meter Columns Up (4 track column meters)
* **`53`**: VU Meter Rows Left (8 track row meters)
* **`54`**: VU Meter Columns Down
* **`55`**: VU Meter Rows Right

### Advanced Animation Patterns
* **`56`**: **[DISABLED]** Animated Heart
* **`57`**: Rainbow Cycle
* **`58`**: Fire Effect
* **`59`**: Twinkle
* **`60`**: Plasma
* **`61`**: Game of Life (Cellular automation)
* **`62`**: Matrix Rain (Digital rain effect - defaults to green)
* **`63`**: **[DISABLED]** 3D Cube
* **`64`**: Kaleidoscope
* **`65`**: Raindrops
* **`66`**: Drip Effect
* **`67`**: **[DISABLED]** Pac-Man
* **`68`**: **[DISABLED]** Space Invaders

### Text Scrolling
* **`80`**: **[DISABLED]** Bouncing Text
* **`97`**: Scroll English Text (Uses stored or custom string)
* **`98`**: Scroll Aurebesh Text (Uses stored or custom string)
* **`99`**: Test All Patterns (Sequentially cycles all enabled patterns)

---

## 6. Curated Astromech/PSI Patterns (100 - 119)
These are custom-designed specifically for R2-D2 style dome indicator displays:
* **`100` - `106`**: Solid colors (Red, Blue, Green, Yellow, Cyan, Magenta, White)
* **`107`**: Color Wipe Down
* **`108`**: Color Wipe Up
* **`109`**: PSI Random Flicker (Classic dome blinking sequence)
* **`110`**: PSI Pulse (Glow breathing)
* **`111`**: PSI Rainbow cycle
* **`112`**: March Horizontal
* **`113`**: March Vertical
* **`114`**: March Diagonal
* **`115`**: March Checkerboard
* **`116`**: March Spiral
* **`117`**: Droid Communication (Fast flickering data stream)
* **`118`**: Droid Thinking (Calm scan)
* **`119`**: Droid Alert (Rapid flashing red alarm)

---

## 7. Smart Demo Show (200)
* **`200`**: Smart Demo. Runs a complete sequence showing scrolling text, basic animations, and droid modes. Ideal for display stands and testing.
