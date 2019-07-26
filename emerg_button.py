from gpiozero import LED, Button
from signal import pause

button_1 = Button(2)
button_2 = Button(3)
button_3 = Button(4)
"""
led = LED(17)

button_2.when_pressed = led.on
button_1.when_pressed = led.off
button_3.when_pressed = led.on
"""


button_1.when_pressed = fire_button
button_2.when_pressed = police_button
button_3.when_pressed = ambu_button


def fire_button():
	


def police_button():
	


def ambu_button():



pause()
