from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing 'city' parameter."}), 400

    # Dummy data — replace with actual weather API if needed
    weather_data = {
        "Seattle": {"temp": "15°C", "status": "Cloudy"},
        "Tokyo": {"temp": "19°C", "status": "Partly Cloudy"},
        "New York": {"temp": "16°C", "status": "Sunny"}
    }

    data = weather_data.get(city, {"temp": "N/A", "status": "Unknown city"})
    data["city"] = city
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5001)
