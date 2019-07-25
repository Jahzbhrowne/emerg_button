import requests
import json
import geolocate

def ambulance():
    ambukey = "hMa7HtNAnbnNYmIaqMXhbNKNT3bTAYyemD6uHZveyEw"
    ambuevent = "nancy"
    ambu1 = geolocate.location
    ambu2 = "val 1"
    ambu3 = "val 2"
    
    url = "https://maker.ifttt.com/trigger/nancy/with/key/hMa7HtNAnbnNYmIaqMXhbNKNT3bTAYyemD6uHZveyEw"
    ambu = {"value1" : ambu1, "value2" :ambu2 , "value3" : ambu3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(ambu), headers=headers)
    
def fire():
    firekey = "bO2KQdy-gXJhlkQLfYyP3P"
    fireevent = "button_pressed"
    fire1 = geolocate.location
    fire2 = "val 1"
    fire3 = "val 2"
    
    url = "https://maker.ifttt.com/trigger/button_pressed/with/key/bO2KQdy-gXJhlkQLfYyP3P"
    firemap = {"value1" : fire1, "value2" :fire2 , "value3" : fire3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(firemap), headers=headers)
    
    
def police():
    
    key = "wU04UjKRQ7uw40h78c8vH"
    event = 'globalcodeproject'
    payload1 = geolocate.location
    payload2 = 'val 1'
    payload3 = 'val 2'

    url = 'https://maker.ifttt.com/trigger/globalcodeproject/with/key/wU04UjKRQ7uw40h78c8vH' 
    payload = {"value1" : payload1, "value2" : payload2, "value3" : payload3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(payload), headers=headers)
