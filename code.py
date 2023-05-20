import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

Button1 = board.GP15
Button2 = board.GP14
Button3 = board.GP13
Button4 = board.GP12
Button5 = board.GP11
Button6 = board.GP10
Button7 = board.GP9

keyboard = Keyboard(usb_hid.devices)

key1 = digitalio.DigitalInOut(Button1)
key1.direction = digitalio.Direction.INPUT
key1.pull = digitalio.Pull.DOWN

key2 = digitalio.DigitalInOut(Button2)
key2.direction = digitalio.Direction.INPUT
key2.pull = digitalio.Pull.DOWN

key3 = digitalio.DigitalInOut(Button3)
key3.direction = digitalio.Direction.INPUT
key3.pull = digitalio.Pull.DOWN

key4 = digitalio.DigitalInOut(Button4)
key4.direction = digitalio.Direction.INPUT
key4.pull = digitalio.Pull.DOWN

key5 = digitalio.DigitalInOut(Button5)
key5.direction = digitalio.Direction.INPUT
key5.pull = digitalio.Pull.DOWN

key6 = digitalio.DigitalInOut(Button6)
key6.direction = digitalio.Direction.INPUT
key6.pull = digitalio.Pull.DOWN

key7 = digitalio.DigitalInOut(Button7)
key7.direction = digitalio.Direction.INPUT
key7.pull = digitalio.Pull.DOWN

while True:
    if	key1.value: // enter key
        keyboard.press(Keycode.ENTER)
        time.sleep(0.5)
        keyboard.release(Keycode.ALT, Keycode.TAB)
    if	key2.value: //new tab in browser
        keyboard.press(Keycode.CONTROL, Keycode.T)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.T)
    if	key3.value: //change window
        keyboard.press(Keycode.ALT, Keycode.F4)
        time.sleep(0.1)
        keyboard.release(Keycode.ALT, Keycode.F4)
    if	key4.value: //paste
        keyboard.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.V)
    if	key5.value: //cut
        keyboard.press(Keycode.CONTROL, Keycode.X)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.X)
    if	key6.value: //copy
        keyboard.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        keyboard.release(Keycode.CONTROL, Keycode.C)
    if	key7.value: //lock the windows
        keyboard.press(Keycode.WINDOWS, Keycode.L)
        time.sleep(0.1)
        keyboard.release(Keycode.WINDOWS, Keycode.L) 
    time.sleep(0.1)   
