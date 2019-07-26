import geocoder
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
print(g.latlng)