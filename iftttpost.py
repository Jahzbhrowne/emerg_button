import requests
import json
import geolocate

def ambulance():
    ambukey = "hMa7HtNAnbnNYmIaqMXhbNKNT3bTAYyemD6uHZveyEw"
    ambuevent = "nancy"
    ambu1 = geolocate.location
    ambu2 = "val1"
    ambu3 = "val2"
    
    url = "https://maker.ifttt.com/trigger/nancy/with/key/hMa7HtNAnbnNYmIaqMXhbNKNT3bTAYyemD6uHZveyEw"
    ambu = {"value1" : ambu1, "value2" :ambu2 , "value3" : ambu3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(ambu), headers=headers)
    
def fire():
    firekey = "bO2KQdy-gXJhlkQLfYyP3P"
    fireevent = "button_pressed"
    fire1 = geolocate.location
    fire2 = "val1"
    fire3 = "val2"
    
    url = "https://maker.ifttt.com/trigger/button_pressed/with/key/bO2KQdy-gXJhlkQLfYyP3P"
    ambu = {"value1" : fire1, "value2" :fire2 , "value3" : fire3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(fire), headers=headers)
    
    
def police():
    
    policekey = "gSr14mo0qQ2n46Zt1nDCNfLCoupKoB8mmO1j_HauDTG"
    policeevent = 'globalcodeproject'
    police1 = geolocate.location
    police2 = 'Police Service'
    police3 = 'Please iI need help ohhh!!!'
    
    url = 'https://maker.ifttt.com/trigger/globalcodeproject/with/key/wU04UjKRQ7uw40h78c8vH' 
    police = {"value1" : police1, "value2" :police2 , "value3" : police3}
    headers = {'content-type': 'application/json'}
    fowardEvent = requests.post(url, data=json.dumps(police), headers=headers)