import os
import time
from gpiozero import LED, Button, Buzzer
import requests

red = LED(17)
green = LED(27)
button = Button(22)
bz = Buzzer(14)


def startgreen():
    print("Green light on")
    green.on()
    red.off()
    
def steadyred():
    print("Steady red")
    green.off()
    red.on()
    time.sleep(1)
    
    
def buzzer_beep():
    # Make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence
    print("Start walking")
    count = 1
    while count <= 4:
        print("Beep")
        bz.on()
        time.sleep(0.5)
        bz.off()
        time.sleep(0.5)
        count += 1
        print(count)
        
        
def flashingredgreen():
    print("Flashing amber and green")
    red.off()
    green.off()

    iCount = 1
    while iCount <= 6:
        red.on()
        time.sleep(0.5)
        red.off()
        time.sleep(0.5)
        iCount += 1
    #green.on()
    
    
def flashingsequence():
    print("Traffic Light sequence started")
    # Green will already be on
    steadyred()
    buzzer_beep()
    flashingredgreen()
    #startgreen()
        
def button_press():
     button.wait_for_press()
     flashingsequence()
     r = requests.get("https://maker.ifttt.com/trigger/globalcodeproject/with/key/wU04UjKRQ7uw40h78c8vH")
     print("Notification send successfully")
     if r:
         return startgreen()
    

    
        
