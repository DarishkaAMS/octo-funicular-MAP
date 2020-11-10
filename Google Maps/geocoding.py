from urllib.parse import urlencode

# https://console.cloud.google.com/apis/credentials?authuser=1&project=cfe-project-295104
api_key = "AIzaSyD31cVxW6IO9JOsvia_Eu96lRSKuFRzzxE"

data_type = "json"
endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
params = {'adress': "1600 Amphitheatre Parkway, Mountain+View, CA", "key": api_key}
# https://developers.google.com/maps/documentation/geocoding/start
url_params = urlencode(params)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?" \
#          "address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"
# print(url_params)

url = f"{endpoint}?{url_params}"
# print(url)


def extract_lat_len(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {'adress': address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    return url


extract_lat_len("1600 Amphitheatre Parkway, Mountain+View, CA")