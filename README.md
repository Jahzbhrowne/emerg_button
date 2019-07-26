# emerg_button
Emerg_button 
The emerg_button is a system created to enable just in time response to emergency situations, by sending a message containing the location of the emergency to the appropriate agency be it the police or fire service.  

Requirements; 
This project has some hardware requirements. You need a raspberry pi, a buzzer, two LED lights, three buttons, a breadboard and connecting wires for connection.
For software requirements, python 3 and above would be suitable for this project and the ifttt api must be installed to aid in the sending of messages.
You will also need to install the packages geopy and geocoder
pip install geopy
pip install geocoder

This is how it works; 
When the button is pressed, the buzzer sounds an alarm, the red LED  light turns and the message is sent.  As soon as the message is sent, the red LED light goes off and the green LED turns on.
