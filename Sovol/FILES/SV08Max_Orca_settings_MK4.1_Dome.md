# OrcaSlicer settings for the MK4.1 single-print dome (SV08 Max, SUNLU Silk PLA+)

Project: `MK4.1_Dome_SinglePrint_NoFins_v2_SV08Max_Tuned_AlignedSeam.3mf` (OrcaSlicer 2.4.2).

**Starting point:** Orca's stock presets
- Printer: **Sovol SV08 MAX 0.4 nozzle**
- Process: **0.20mm Standard @Sovol SV08 MAX 0.4 nozzle**
- Filament: **SUNLU Silk PLA+** (system preset)

Every setting below differs from those stock presets. Anything not listed stays stock.
★ = changed during the Nov 2026 tuning; the rest were already in Mike's own profile before that.
Tip: if a setting isn't where this list says (Orca moves things between versions), type its name into the
search box at the top of the settings panel.

> Easiest route: open the 3mf itself. It carries all of these, plus the painted seam. This list is for building
> the profile by hand or checking an existing one.

---

## PROCESS

### Quality tab

**Layer height**
| Setting | Stock | Final | Note |
|---|---|---|---|
| Layer height | 0.20 | **0.12** | First layer height stays 0.25 |

**Line width**
| Setting | Stock | Final |
|---|---|---|
| Default | 0.4 | **0.45** |
| First layer | 0.5 | **0.48** |
| Inner wall | 0.45 | **0.42** |
| Top surface | 0.38 | **0.42** |
| Sparse infill | 0.45 | **0.42** |
| Internal solid infill | 0.45 | **0.42** |
| Support | 0.45 | **0.42** |

Outer wall stays 0.42.

**Seam**
| Setting | Stock | Final | Note |
|---|---|---|---|
| Seam position | Aligned | **Aligned** ★ | Tried Back first; Aligned puts the window-band seams in the panel-seat corners, under the blue panels |
| Staggered inner seams | off | **on** ★ | |
| Seam gap | 5% | **7%** | |
| Scarf joint seam (seam slope type) | None | **None** ★ | Scarf was tested and dropped; the plain seam looks cleaner on silk |

Plus a **painted seam** on the model (see "Seam painting" at the end).

**Precision**
| Setting | Stock | Final | Note |
|---|---|---|---|
| Elephant foot compensation | 0 | **0.15** | |
| Arc fitting | off | **off** ★ | Make sure it's off; arcs gave rougher curves on Klipper |

**Walls and surfaces**
| Setting | Stock | Final |
|---|---|---|
| Wall loop direction | Auto | **Counter clockwise** |
| Avoid crossing walls | off | **on** |

### Strength tab

**Walls**
| Setting | Stock | Final | Note |
|---|---|---|---|
| Wall loops | 2 | **4** ★ | Stiffer skin, no infill showing through. More walls don't fix the crosshatch and cost ~120 g each |

**Top/bottom shells**
| Setting | Stock | Final |
|---|---|---|
| Top surface pattern | Monotonic | **Monotonic line** |
| Bottom shell layers | 3 | **4** |

Top shell layers stays 4.

**Infill**
| Setting | Stock | Final |
|---|---|---|
| Sparse infill pattern | Grid | **Gyroid** |
| Infill/wall overlap | 25% | **5%** |
| Top/bottom solid infill/wall overlap | 25% | **10%** |

Sparse infill density stays 10%.

**Advanced**
| Setting | Stock | Final | Note |
|---|---|---|---|
| Ensure vertical shell thickness | All | **Moderate** ★ | |

### Speed tab

**First layer speed**
| Setting | Stock | Final |
|---|---|---|
| First layer | 40 | **20** |
| First layer infill | 65 | **30** |

**Other layers speed** (mm/s)
| Setting | Stock | Final | Note |
|---|---|---|---|
| Outer wall | 200 | **40** | Slow for silk shine. 80 was tested: worse (more layer banding) |
| Inner wall | 300 | **40** | |
| Small perimeters | 50% | **15** (mm/s) | |
| Sparse infill | 400 | **100** ★ | Less vibration right behind the skin |
| Internal solid infill | 230 | **45** | |
| Top surface | 180 | **40** | |
| Gap infill | 180 | **40** | |
| Support interface | 100% | **80** | |
| Bridge | 50 | **40** | |
| Internal bridge | 200 | **40** | |
| Overhang 50–75% (overhang_2_4) | 50 | **40** | |

**Travel speed**
| Setting | Stock | Final |
|---|---|---|
| Travel | 600 | **400** |

**Acceleration** (mm/s²) — the most important group
| Setting | Stock | Final | Note |
|---|---|---|---|
| Normal printing | 20000 | **4000** ★ | **Never leave this at 0.** At 0 Orca sends no accel commands and the printer runs everything at printer.cfg max_accel (30000) |
| Outer wall | 6000 | **3000** ★ | Less ringing |
| Inner wall | 8000 | **4000** ★ | |
| Top surface | 5000 | **3000** ★ | |
| Travel | 20000 | **6000** ★ | |
| Initial layer | 1000 | 1000 | (check it isn't 0) |

Bridge 50% and internal solid infill 50% stay stock.

**Advanced (speed)**
| Setting | Stock | Final |
|---|---|---|
| Enable accel_to_decel | on | **off** |

(accel_to_decel factor shows 1% in the file; irrelevant while off.)

### Support tab
The dome needs no support; these only matter if someone turns support on.

| Setting | Stock | Final |
|---|---|---|
| Type | Normal (auto) | **Tree (manual)** |
| Style | Default | **Organic** |
| Threshold angle | 20 | **50** |
| Top Z distance | 0.235 | **0.25** |
| Bottom Z distance | 0.235 | **0.25** |
| Bottom interface layers | Same as top | **2** |
| Interface pattern | Default | **Grid** |
| Tree support wall loops | 0 | **1** |
| Raft: first layer density | 100% | **60%** |

### Multimaterial tab
| Setting | Stock | Final |
|---|---|---|
| Enable prime tower | on | **off** |

### Others tab
| Setting | Stock | Final |
|---|---|---|
| Skirt loops | 1 | **2** |
| Brim type | Auto | **Outer brim only** |
| Brim width | 5 | **10** |
| Reduce infill retraction | on | **off** |

---

## FILAMENT (SUNLU Silk PLA+)

### Filament tab
| Setting | Stock | Final | Note |
|---|---|---|---|
| Nozzle temperature | 230 / 230 | 230 / 230 | unchanged |
| Nozzle temp range (low) | 190 | **200** | |
| Bed: Textured PEI plate (first layer / other) | 60 / 60 | **55 / 55** | |
| Max volumetric speed | 16 | **12** | |
| Pressure advance: Enable | off | **on** ★ | |
| Pressure advance | — | **0.04** ★ | From a PA line test with this filament on Mike's printer. Re-test for another printer/filament |

Orca's pressure advance overrides `pressure_advance` in printer.cfg.

### Cooling tab
| Setting | Stock | Final | Note |
|---|---|---|---|
| Min fan speed threshold: Fan speed | 100% | **50%** ★ | Gentler cooling; full fan every layer helped curl the tall thin posts |
| Min fan speed threshold: Layer time | 100 s | **30 s** ★ | |
| Max fan speed threshold | 100% / 4 s | unchanged | |
| Slow printing down for better layer cooling | on | on | |
| Min print speed | 20 | **10** | |
| Don't slow down outer walls | off | **on** | |

Max fan 100%, overhang fan 100% above 50%, aux fan 70% all stay stock.

### Advanced tab
| Setting | Stock | Final | Note |
|---|---|---|---|
| Filament start G-code | turns on the chamber/exhaust fan (`M106 P3`) based on bed temp | **just a comment** | Mike's choice; optional |
| Filament end G-code | `;M106 P3 S0` (commented out anyway) | just a comment | no effect |

---

## PRINTER (Sovol SV08 MAX 0.4 nozzle)

| Where | Setting | Stock | Final | Note |
|---|---|---|---|---|
| Basic information → Accessory | Auxiliary part cooling fan | off | **on** ★ | Lets Orca drive the aux fan |
| Machine G-code | Layer change G-code | `;AFTER_LAYER_CHANGE` comment | empty | no effect |
| Machine G-code | Start / End G-code | stock | stock | `START_PRINT` / `END_PRINT` macros |

Machine limits (accel/speed/jerk) are unchanged.

## PLATE
- **Bed type: Textured PEI Plate** ★ (plate settings on the Prepare tab).

---

## Seam painting (on the model, not a setting)

The 3mf has a **painted seam strip** on the outside back of the dome: a full-height strip at +Y (rear of the bed),
about 89° at the bottom rim leaning to about 84° at the top. With Seam position = Aligned, every full ring layer
puts its seam on that strip; in the window band, seams go into the panel-seat corners under the blue panels.

To recreate by hand: select the dome → Seam painting tool → paint a narrow vertical strip on the outer surface at the
back, from the bottom rim to the top. **Don't rotate the dome after painting**: the dome's front must face the
front of the bed.

---

## Result with these settings
About 970 g, about 5 days 10 hours on the SV08 Max (3 plates in the project: plate 1 is the dome; plates 2–3 are
test wedges).
