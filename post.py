import requests
import json
key = "wU04UjKRQ7uw40h78c8vH"
event = 'globalcodeproject'
payload1 = 'val 1'
payload2 = 'val 2'
payload3 = 'val 3'

url = 'https://maker.ifttt.com/trigger/globalcodeproject/with/key/wU04UjKRQ7uw40h78c8vH' 
payload = {"value1" : payload1, "value2" : payload2, "value3" : payload3}
headers = {'content-type': 'application/json'}
fowardEvent = requests.post(url, data=json.dumps(payload), headers=headers)