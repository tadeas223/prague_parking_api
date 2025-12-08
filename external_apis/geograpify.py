import requests
import utils
import data

geoapify_url = 'https://api.geoapify.com'

def request_position_of_address(address):
    api_key = load_env("GEOAPIFY_KEY")
    
    params = {
        "housenumber": address.house_number,
        "street": address.street,
        "postcode": address.postal_code,
        "city": "Prague",
        "country": "Czechia",
        "format": "json",
        "apiKey": api_key
    }

    response = requests.get(f"{geoapify_url}/v1/geocode/search", params=params)
    
    if(response.status_code != 200):
        raise Exception(f"something went wronk, womp womp :( \n{response.status_code}\n{response.text}")
    
    return parse_geoapify_data(response.json())

def parse_geoapify_data(json):
    lat = json["results"][0]["lat"]
    lon = json["results"][0]["lon"]

    return (lat, lon)