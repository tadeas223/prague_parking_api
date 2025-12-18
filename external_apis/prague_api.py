import requests

from data.address import Address
from data.parking import Parking
import utils.position_utils as pos_utils
from utils.load_env import load_env

prague_api_url = 'https://api.golemio.cz'

def request_parking_by_position_with_box(topLeft, bottomRight):
    api_key = load_env("PRAGUE_API_KEY")

    topLeftLat = topLeft[0]
    topLeftLon = topLeft[1]
    bottomRightLat = bottomRight[0]
    bottomRightLon = bottomRight[1]

    headers = {
        "X-Access-Token": api_key
    }

    params = {
        "boundingBox": f"{topLeftLat},{topLeftLon},{bottomRightLat},{bottomRightLon}"
    }

    response = requests.get(f"{prague_api_url}/v3/parking", headers=headers, params=params)

    if(response.status_code != 200):
        raise Exception(f"something went wronk, womp womp :( \n{response.status_code}\n{response.text}")

    return parse_parking_data(response.json())

def request_parking_by_position(lat, lon, radius):
    (topLeft, bottomRight) = pos_utils.bounding_rectangle(lat, lon, radius)    
    return request_parking_by_position_with_box(topLeft, bottomRight)

def parse_parking_data(json):
    parkings = []

    features = json["features"]
    for feature in features:
        space_propertions = feature["properties"]["space"]["features"][0]["properties"]
        capacity = space_propertions["capacity"]
        position = (space_propertions["centroid"]["coordinates"][0],space_propertions["centroid"]["coordinates"][1])

        address_data = space_propertions.get("address") or None
        if(address_data == None):
            continue

        postal_code = address_data.get("postal_code")
        street = address_data.get("street_address")
        house_number = address_data.get("house_number")

        address = Address(postal_code, street, house_number)
        parkings.append(Parking(capacity, position, address))
    return parkings 