""" Python program to calculate the distance between Cairo and Nairobi City. """

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def distance_apart(location1, location2):
    geolocation = Nominatim(user_agent="Nimah")
    location1 = geolocation.geocode(location1)
    location2 = geolocation.geocode(location2)
    distance = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km
    return distance

print(distance_apart("Nairobi","Cairo"))
