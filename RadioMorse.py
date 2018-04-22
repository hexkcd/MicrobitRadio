from microbit import *
import radio

radio.on()
radio.config(channel = 10)
while True:
    if button_a.was_pressed():
        radio.send(".")
    elif button_b.was_pressed():
        radio.send("-")
    incoming = radio.receive()
    
    if incoming is not None:
        display.scroll(str(incoming))

