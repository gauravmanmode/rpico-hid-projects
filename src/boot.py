import usb_cdc
import storage
import board, digitalio


usb_cdc.enable(console=False, data=True)
button = digitalio.DigitalInOut(board.GP22)
button.pull = digitalio.Pull.UP

