from microbit import *
import radio

radio.on()
radio.config(channel = 6)
while True:
    if button_a.was_pressed():
        radio.send("YOUR_MESSAGE_HERE")
        display.scroll(".")
    incoming = radio.receive()
    if incoming is not None:
        display.scroll(str(incoming))
