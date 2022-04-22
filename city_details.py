""" Python function to get the city, state and country name of a specified
latitude and longitude using Nominatim API and Geopy package """


from geopy.geocoders import Nominatim

def city_details(latitude, longitude):
    geolocation = Nominatim(user_agent="Nimah")
    locale = geolocation.reverse(latitude,longitude)
    location = locale.raw["address"]
    city = location.get('city', '')
    state = location.get('state', '')
    country = location.get('country', '')
    return city, state, country

print(city_details(47.470706, -99.704723))
