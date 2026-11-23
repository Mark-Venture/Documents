# SV08 Max printer.cfg: final changes (R2 MK4.1 dome project, Nov 2026)

These are the only printer.cfg changes we kept. Everything else is stock Sovol.
Back up printer.cfg in Mainsail before editing. After all edits: Save & Restart.

---

## 1. Install the klipper_tmc_autotune plugin (needed for section 4)

SSH into the printer (user `sovol`) and run:

```
wget -O - https://raw.githubusercontent.com/andrewmcgr/klipper_tmc_autotune/main/install.sh | bash
```

Optional, so Mainsail can update it: add to `moonraker.conf`

```
[update_manager klipper_tmc_autotune]
type: git_repo
channel: dev
path: ~/klipper_tmc_autotune
origin: https://github.com/andrewmcgr/klipper_tmc_autotune.git
managed_services: klipper
primary_branch: main
install_script: install.sh
```

---

## 2. `[stepper_x]` and `[stepper_y]`

| Line | Stock | Final |
|---|---|---|
| `microsteps:` | 16 | **64** |

Don't change `rotation_distance: 40` (Klipper scales the steps itself). X/Y home on physical endstops, so homing needs no retune.

---

## 3. `[tmc5160 stepper_x]` and `[tmc5160 stepper_y]`

| Line | Stock | Final |
|---|---|---|
| `interpolate:` | false | **true** |
| all 14 `driver_...` lines | active | **commented out** (put `#` in front) |

The 14 lines are: `driver_MULTISTEP_FILT`, `driver_IHOLDDELAY`, `driver_TPOWERDOWN`, `driver_TBL`, `driver_TOFF`,
`driver_HEND`, `driver_HSTRT`, `driver_PWM_FREQ`, `driver_PWM_AUTOSCALE`, `driver_PWM_AUTOGRAD`, `driver_PWM_OFS`,
`driver_PWM_REG`, `driver_VHIGHFS`, `driver_VHIGHCHM`. Autotune sets these instead.

Unchanged and still active: `cs_pin` (X: PE0, Y: PD4), the `spi_software_*` pins, `run_current: 3.0`,
`sense_resistor: 0.05`, `stealthchop_threshold: 0`. Watch the `cs_pin` when copy-pasting between X and Y.

Result (X shown, Y is the same apart from cs_pin PD4):

```
[tmc5160 stepper_x]
cs_pin: PE0
spi_software_mosi_pin: PB6
spi_software_miso_pin: PB5
spi_software_sclk_pin: PB4
interpolate: true
run_current: 3.0
sense_resistor: 0.05
stealthchop_threshold: 0
#driver_MULTISTEP_FILT: True
#driver_IHOLDDELAY: 15
#driver_TPOWERDOWN: 1
#driver_TBL: 3
#driver_TOFF: 5
#driver_HEND: 0
#driver_HSTRT: 7
#driver_PWM_FREQ: 2
#driver_PWM_AUTOSCALE: True
#driver_PWM_AUTOGRAD: True
#driver_PWM_OFS: 28
#driver_PWM_REG: 8
#driver_VHIGHFS: 0
#driver_VHIGHCHM: 1
```

---

## 4. New sections: `[autotune_tmc stepper_x]` and `[autotune_tmc stepper_y]`

Add after the tmc5160 sections:

```
[autotune_tmc stepper_x]
motor: shengyang-42bygh3025-4m-25d
voltage: 24
tuning_goal: auto
tbl: 3

[autotune_tmc stepper_y]
motor: shengyang-42bygh3025-4m-25d
voltage: 24
tuning_goal: auto
tbl: 3
```

- Motor: the SV08 Max X/Y motors are Shengyang 42BYGH3025-4M-25D (4.0 A), already in the autotune database.
  (The 42BYGH2904-A on Sovol's wiki is the plain SV08's motor; don't use it.)
- `tbl: 3` is needed: without it (and with `tbl: 2`) the motors whine at standstill.
- Check after restart: `DUMP_TMC STEPPER=stepper_x` should show new TOFF/HSTRT/HEND values, then home and jog.
- Motor case temperature after a ~11 h print: 48–49 °C. Fine.

---

## 5. `[extruder]`

| Line | Stock | Final |
|---|---|---|
| `microsteps:` | 16 | **64** |

Don't change `rotation_distance` (keep your own calibrated value; Klipper scales the steps).
Check afterwards: mark the filament 120 mm above the extruder, heat, run `M83` then `G1 E100 F60`;
about 20 mm should remain to the mark.

---

## 6. `[tmc2209 extruder]`: no change

We tried `stealthchop_threshold: 999999` (stealthChop on the extruder). It didn't help, and Klipper cautions
against stealthChop with pressure advance, so it was removed. Leave this section stock.

---

## Not changed (for reference)

- `max_accel`, `square_corner_velocity`, `minimum_cruise_ratio`, input shaper, `pressure_advance` in printer.cfg.
  The Orca project sets acceleration and pressure advance itself (`SET_PRESSURE_ADVANCE` from the filament
  settings overrides printer.cfg's `pressure_advance`).

## How much it helped

The fine diagonal "salmon skin" crosshatch on silk got smoother and more even with sections 2–4, but didn't go away
completely. The extruder change (section 5) made no visible difference but does no harm. None of these are needed to
print the dome; they only affect that fine texture.

## To undo

Remove the two `[autotune_tmc]` blocks, un-comment the `driver_` lines, set `interpolate: false` and microsteps back to
16, Save & Restart.
