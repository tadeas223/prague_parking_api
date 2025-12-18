from flask import Flask, request, jsonify
import external_apis.prague_api as prague_api
import external_apis.geograpify as geoapify

app = Flask(__name__)

@app.route("/parking", methods=["GET"])
def post_parking():
    data = request.get_json()

    if ("position"     not in data \
        and "address"  not in data)\
        or "radius"    not in data:
        return jsonify({"error": "missing arguments"}), 400

    if "position" in data and "address" in data:
        return jsonify({"error": "position and address cannot be used together"}), 400


    position = None

    if "position" in data:
        required_position_keys = ["lat", "lon"]
        req_position = data["position"]

        if not all(key in req_position for key in required_position_keys):
            return jsonify({"error": "missing arguments in position"}), 400

        position = (data["position"]["lat"], data["position"]["lon"])

    if "address" in data:
        required_position_keys = ["postal_code", "street", "house_number"]
        req_address = data["address"]

        if not all(key in req_address for key in required_address_keys):
            return jsonify({"error": "missing arguments in address"}), 400

        address = Address(req_address["street"], req_address["postal_code"], req_address["house_number"])
        position = geoapify.request_position_of_address(address)

    response_data = prague_api.request_parking_by_position(position[0], position[1], data["radius"])

    return jsonify([data.to_dict() for data in response_data]), 200

        


if __name__ == "__main__":
    app.run(debug=True, port=8080)