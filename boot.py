"""JoystickXL standard boot.py."""

import usb_hid
from joystick_xl.hid import create_joystick
import storage
import board
import digitalio

usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,
        create_joystick(axes=2, buttons=23, hats=0),
    )
)

# Use GP2 as the button pin (change as needed)
button = digitalio.DigitalInOut(board.GP26)
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive()   