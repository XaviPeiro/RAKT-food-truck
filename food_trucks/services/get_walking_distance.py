import googlemaps


# NOT TESTED DUE OF ISSUES CREATING A GOGGLE BILLING ACCOUNT
def get_walking_duration(request, origin_lat, origin_lng, destination_lat, destination_lng):

    api_key = 'YOUR_API_KEY'
    gmaps = googlemaps.Client(key=api_key)

    origin = f"{origin_lat},{origin_lng}"
    destination = f"{destination_lat},{destination_lng}"

    directions_result = gmaps.directions(origin, destination, mode="walking")

    walking_duration = directions_result[0]['legs'][0]['duration']['text']

    return walking_duration
