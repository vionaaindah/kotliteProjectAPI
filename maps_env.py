import googlemaps

def gmaps_init():
    API_KEY = '[YOUR API KEY]'
    client = googlemaps.Client(key=API_KEY)

    return client