""" Python program to search the country name from a given state name
using the Nominatim API and GeoPy package. """

from geopy.geocoders import Nominatim

def country_name(state):
    geolocator = Nominatim(user_agent="Nimah")
    state = geolocator.geocode(state)
    state_details= state.raw
    name = state_details["display_name"].split()
    country_name = name[-1]
    return country_name

print(country_name("Nairobi"))

    
