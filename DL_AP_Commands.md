this is taken right from the DL_AP Commands tab:

# DroidLink_AP Commands

## Maestro Output and Holo Commands

| Command | Action |
|----------|----------|
| `:DS00–:DS59` | Run a saved output/servo sequence |
| `:DS60` | Run the saved random movement for all three holos |
| `:DS61` | Stop and center all holos and restore their saved lighting |
| `:DS0O / :DS0C` | Open or close output 0 |
| `:DS0T` | Toggle positional servo output 0 |
| `:DS0F / :DS0R / :DS0S` | Run 360° servo Forward, Reverse, or Stop |

## Built-In AstroPixels Sequences

| Command | Action |
|----------|----------|
| `:SE00` | Stop current sequence |
| `:SE01` | Scream |
| `:SE02` | Wave |
| `:SE03` | Smirk-wave |
| `:SE04` | Open/close-wave |
| `:SE05` | Beep Cantina |
| `:SE06` | Short-circuit |
| `:SE07` | Cantina |
| `:SE08` | Leia message |
| `:SE09` | Disco |
| ':SE50'| Scream effects without panel movement|
| ':SE51' |	Scream panel sequence|
| ':SE52' |	Wave panel sequence|
| ':SE53' |	Smirk-wave panel sequence|
| ':SE54' |	Open-wave panel sequence| 
| ':SE55' |	Marching-ants panel sequence|
| ':SE56' |	Faint panel sequence|
| ':SE57' |	Rhythmic panel sequence| 

## Saved Lighting Sequences

| Command | Action |
|----------|----------|
| `:AP00–:AP31` | Run a saved lighting or scrolling-text sequence |

## Prebuilt DroidLink Lighting Commands

| Command | Action |
|----------|----------|
| `:AP32` | Normal lighting |
| `:AP33` | Alarm lighting |
| `:AP34` | Failure lighting |
| `:AP35` | Leia lighting |
| `:AP36` | Imperial March lighting |
| `:AP37` | All holo LEDs on |
| `:AP38` | All holo LEDs off |
| `:AP39` | Normal lighting + holo LEDs on |
| `:AP40` | All displays and holo LEDs off |
| `:AP41` | Rainbow lighting |
| `:AP42` | Alarm + pulsing holo LEDs |
| `:AP43` | Failure + pulsing holo LEDs |
| `:AP44` | Leia + pulsing holo LEDs |
| `:AP45` | Imperial March |
| `:AP46` | Red Alert |
| `:AP47` | Fire effect |
| `:AP48` | Rainbow holo LEDs |

## Additional Commands

### Individual Holo Movement

- `*ST00` Stop and center all holos
- `*RD01-*RD03` Random movement
- `*HW01-*HW03` Wag holo
- `*HN01-*HN03` Nod holo
- `@APHRT0-3` Single twitch
- `@APHRS0-3` Continuous movement
- `@APHRX0-3` Stop and center

### Individual Holo Lighting

- `*ON01-*ON03` Turn holo LED on
- `*OF01-*OF03` Turn holo LED off
- `*HPS101-*HPS103` Restore automatic effect
- `*HPS301-*HPS303` Pulse effect
- `*HPS601-*HPS603` Rainbow effect

### Logic Display Effects

`@xT1` Normal  
`@xT2` Flash  
`@xT3` Alarm  
`@xT4` Failure  
`@xT5` Red Alert  
`@xT6` Leia  
`@xT11` Imperial March

### PSI Effects

`@xP1` Normal  
`@xP2` Flash  
`@xP3` Alarm  
`@xP4` Failure  
`@xP5` Red Alert  
`@xP6` Leia  
`@xP11` Imperial March

### Advanced Lighting Format

```text
@APLEEECSNN
```

- `EE` = Effect
- `C` = Color
- `S` = Speed (0-9)
- `NN` = Duration seconds
