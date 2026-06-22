# sc-control-box

A custom USB HID game controller built on a Raspberry Pi Pico, designed for use with Star Citizen. Features 23 inputs including momentary buttons, toggle switches, and two analogue axes — all registered as a single game controller in Windows.

Built as a collaboration — hardware design and 3D printed enclosure by my dad, software by me.

---

## Features

- 23 total inputs registered as a single USB HID joystick
- Mix of momentary buttons, toggle switches, and analogue axes
- Toggle switches send a button pulse on state change, compatible with games that expect press events rather than held states
- Two analogue axes for fine-grained control (speed limiter and acceleration limiter)
- Plug and play — no drivers required, recognised natively by Windows as a game controller

---

## Hardware

| Component | Details |
|---|---|
| Microcontroller | Raspberry Pi Pico |
| Inputs | 15x momentary buttons, 6x toggle switches, 2x analogue axes |
| Enclosure | Custom 3D printed case |
| Connection | USB (native HID) |

---

## Input Layout

| Input Type | Count | GPIO Pins |
|---|---|---|
| Momentary buttons | 15 | GP0–GP14, GP19, GP26 |
| Toggle switches | 6 | GP16, GP17, GP18, GP20, GP21, GP22 |
| Analogue axes | 2 | GP27, GP28 |

---

## Dependencies

This project uses [joystick_xl](https://github.com/fasteddy516/CircuitPython_JoystickXL) — a CircuitPython library for building custom HID joystick devices.

Install CircuitPython on your Pico and copy the `joystick_xl` library folder to the `lib` directory on your device.

---

## Setup

1. Flash your Pico with the latest [CircuitPython UF2](https://circuitpython.org/board/raspberry_pi_pico/)
2. Copy the `joystick_xl` library to the `lib` folder on your Pico
3. Copy `code.py` to the root of your Pico
4. Wire up your buttons, switches, and axes according to the input layout above
5. Plug in via USB — Windows will recognise it as a game controller automatically
6. Open your game's keybinding settings and bind inputs as needed

---

## Toggle Switch Behaviour

Physical toggle switches maintain a persistent on/off state, but most games expect button press events rather than held states. To handle this, the code detects when a toggle switch changes state and sends a brief pulse (off → short delay → on) to simulate a button press. This ensures compatibility with Star Citizen's keybinding system.

---

## Analogue Axes

The two analogue axes in my set-up are mapped to:
- **Axis 1 (GP27)** — Speed limiter
- **Axis 2 (GP28)** — Acceleration limiter

but can mapped to anything in game.

These provide fine-grained analogue control over flight parameters that would otherwise require keyboard inputs or menu navigation mid-flight.

---

## Photos

*Coming soon*

---

## Notes

- Tested with Star Citizen but should work with any game that supports custom HID controllers
- Pin assignments can be modified in `code.py` to suit different wiring layouts
- Additional toggle switches or buttons can be added by extending the switch list in the main loop

---

## License

MIT License — free to use, modify, and build on.
