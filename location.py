""" Python program to find the details of a given zip code using the
Nominatim API and GeoPy package. """
from geopy.geocoders import Nominatim
def zip_code():
    geolocator = Nominatim(user_agent = "Nimah")
    location = geolocator.geocode(zipcode)
    return location.address, location.longitude,location.latitude, location.raw

zipcode = '20102'
print(zip_code())


