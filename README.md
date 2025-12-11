# PRAGUE PARKING API

Find a free nearby parking spot in Prague.

## HOW TO USE

### ENDPOINT

**/parking**

**Method:** GET  
**Input type:** JSON
**Input:** position, address, and radius

You can choose either position or address.

Position must include *lat* (latitude) and *lon* (longitude).

Address must include *postal_code*, *street*, and *house_number*.

Radius is the radius of the circle within which the API finds a free parking spot.

**Returns:**

List of parking spots with their position and address

**Request:**

```
address: server-address/parking
# header
Content-type: application/json
# body
{
    "position": {
        "lat": <latitude>
        "lon": <longitude>
    } 
    (or)
    "address": {
        "postal_code": <postal code>
        "street": <street name>
        "house_number": <house number>
    }
    "radius": <radius of a circle>
}
 ```

**Response:**

```
[
    # parking spot
    {
        "position": {
            "lat": <latitude>
            "lon": <longitude>
        },
        "address": {
            "postal_code": <postal code>
            "street": <street name>
            "house_number": <house number>
        }
        "capacity": <free parking spots>
        "date": <last update of data>
    }
    ... (other parking spots)
]
```
