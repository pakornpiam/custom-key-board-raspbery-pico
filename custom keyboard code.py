import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)


mute_pin = board.GP19       # pin to connect button to



# Initializing Button
mute = digitalio.DigitalInOut(mute_pin)
mute.direction = digitalio.Direction.INPUT
mute.pull = digitalio.Pull.DOWN

while True:
	# Check if button is pressed and if it is, to press the Macros and toggle LED
    if mute.value:  
        print(" mute button Pressed")
        keyboard.press(Keycode.F14)
        time.sleep(0.15)
        keyboard.release(Keycode.F14)
    time.sleep(0.1)