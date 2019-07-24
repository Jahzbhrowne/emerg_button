import geocoder
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
print(g.latlng)


geolocator = Nominatim(user_agent = "emerg_button")
loc = geolocator.reverse("6.6833,  -1.6167")
print(loc.address)

