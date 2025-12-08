from geopy.distance import distance

# ai generated helper function
def bounding_rectangle(lat, lon, radius_m):
    # Move north, south, east, and west
    north = distance(meters=radius_m).destination((lat, lon), 0)
    south = distance(meters=radius_m).destination((lat, lon), 180)
    east  = distance(meters=radius_m).destination((lat, lon), 90)
    west  = distance(meters=radius_m).destination((lat, lon), 270)

    top_left = (north.latitude, west.longitude)
    bottom_right = (south.latitude, east.longitude)

    return top_left, bottom_right