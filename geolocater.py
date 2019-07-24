import geocoder
from geopy.geocoders import Nominatim

def geolocatormap():
    g = geocoder.ip('me')
    lat = g.lat
    #print(lat)
    lng = g.lng
    #print(lng)

    geolocator = Nominatim(user_agent = "emerg_button")
    loc = geolocator.reverse(lat,  lng)
    print(loc.address)

