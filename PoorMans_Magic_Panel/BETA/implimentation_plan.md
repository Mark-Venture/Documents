# Implementation Plan - PoorMansMagicPanel Matrix Expansion (Updated)

We will update the PoorMansMagicPanel codebase to support both 4x8 and 8x15 matrices. We'll set up GPIO5 as the input (Serial1) at 9600 baud, connect the LED panel to GPIO4, add serpentine support for the 4x8 layout, support both `:` and `=` as separators, disable patterns that the 4x8 matrix cannot display, ensure text/shapes are centered on the panel, and update the default colors for Matrix Rain (Green), RainDrops (Aqua), and Drip Effect (Aqua).

## Proposed Changes

We will compile for either the 4x8 or 8x15 matrix using compilation directives in `config.h`.

---

### [Component: Configuration]

#### [MODIFY] [config.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/config.h)
- Introduce compile-time options `MATRIX_TYPE_4X8` and `MATRIX_TYPE_8X15` to dynamically adjust `MATRIX_WIDTH`, `MATRIX_HEIGHT`, and `NUM_LEDS`.
- Enable `MATRIX_SERPENTINE` for `MATRIX_TYPE_4X8`.
- Change `LED_PIN` to `6`.
- Set `SERIAL1_BAUD` to `9600` and specify pin configurations for Serial1: `RX1_PIN 20` and `TX1_PIN -1`.
- Declare `isPatternSupported` check for the 4x8 matrix.

---

### [Component: LED Control]

#### [MODIFY] [led_control.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/led_control.h)
- Update `xyToIndex` and `indexToXY` to handle serpentine layout when `MATRIX_SERPENTINE` is defined.
- Modify `setColumn` and `safeSetColumn` parameters to accept `uint16_t pattern` instead of `uint8_t pattern`, allowing the 15-high matrix to light all rows when drawing columns.

---

### [Component: Command Parsing]

#### [MODIFY] [command_processor.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/command_processor.h)
- Update `parseCommand()` to accept **both** `:` and `=` as separators:
  - Check for both separators when parsing text command prefixes (e.g. `TEXT:`, `TEXT=`, `TEXT_BOUNCE:`, `TEXT_BOUNCE=`, `PLAYLIST_RUN:`, `PLAYLIST_RUN=`).
  - Search for both `:` and `=` for `TEXTSAVE` slots.
  - Normalize separators in JawaLite pattern argument strings (e.g. `T57=30=C4` or `T57:30:C4` by replacing `=` with `:` on the parameter substring, preserving any `=` characters inside user-supplied scrolling text).

---

### [Component: Patterns & Animations]

#### [MODIFY] [patterns_text.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_text.h)
- Add a helper `getCharacterWidth` to retrieve font character widths.
- Center the text vertically in `displayBuffer()` and `scrollRainbowText()` by computing `yOffset = (MATRIX_HEIGHT - 7) / 2`.
- Center `bouncingText()` horizontally using character width and vertically using `yOffset`.

#### [MODIFY] [patterns_shapes.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_shapes.h)
- Update `drawShape()` to center shapes horizontally and vertically using:
  - `xOffset = (int8_t(MATRIX_WIDTH) - 8) / 2`
  - `yOffset = (int8_t(MATRIX_HEIGHT) - 8) / 2`
- Clear the panel first in `drawShape()` so out-of-bounds rows/columns are black.

#### [MODIFY] [patterns_basic.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_basic.h)
- Update `toggle()` half-screen divisions to dynamically use `MATRIX_HEIGHT / 2` instead of hardcoded `4` and `8` values.

#### [MODIFY] [patterns_effects.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_effects.h)
- Dynamically center `expand()` and `compress()` vertically using `yOffset = (MATRIX_HEIGHT - 8) / 2`.
- Make `flashV()` dynamic based on `MATRIX_WIDTH`.
- Update `raindrops()` to use `MATRIX_WIDTH` and `MATRIX_HEIGHT` instead of hardcoded `8`.
- Change default color of `raindrops()` and `dripEffect()` to `CRGB::Aqua` (if the active color is the default Red).

#### [MODIFY] [patterns_animations.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_animations.h)
- Make `vuMeter()` fully dynamic: adjust max level, number of bars, and bit alignment of patterns to adapt to the active matrix width and height.
- Change default color of `matrixRain()` to `CRGB::Green` (if the active color is the default Red).

#### [MODIFY] [patterns_astromech.h](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/patterns_astromech.h)
- Make `r2Thinking()` center dynamically based on `MATRIX_WIDTH` and `MATRIX_HEIGHT` (replacing hardcoded `3.5`).
- Make `r2Alert()` partition quadrant checks dynamically using `MATRIX_WIDTH / 2` and `MATRIX_HEIGHT / 2`.

---

### [Component: Main Sketch]

#### [MODIFY] [Magic_Panel_ESP32_C3_Mini_v2.6.ino](file:///D:/MIKEM/Arduino/PoorMansMagicPanel/Magic_Panel_ESP32_C3_Mini_v2.6.ino)
- Configure `Serial1` initialization to use `SERIAL1_BAUD` (9600) and `RX1_PIN` (20).
- Remove USB serial blocking `while (!Serial)` to avoid hanging in standalone mode when USB is disconnected.
- Block execution of unsupported patterns at the beginning of `runPattern()` when `MATRIX_TYPE_4X8` is defined.
- Update serial terminal helper messages to output both `=` and `:` options in documentation.

## Verification Plan

### Automated/Compilation Tests
- We will verify that the project compiles cleanly under both `#define MATRIX_TYPE_4X8` and `#define MATRIX_TYPE_8X15` configurations.

### Manual Verification
- Verify that standard serial communication on `Serial1` accepts commands like `TEXT=Hello` and `TEXT:Hello`.
- Verify 4x8 serpentine coordinates.
- Verify 8x15 vertical centering.
