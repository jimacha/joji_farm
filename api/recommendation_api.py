from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your actual crop recommendation logic
def recommend_crop(temperature, humidity, soil_type):
    # Implement your crop recommendation algorithm here
    # You can use external data sources or APIs for recommendations
    # Return a list of recommended crops

    recommended_crops = ["Wheat", "Rice", "Maize"]
    return recommended_crops

@app.route('/crop-recommendations', methods=['POST'])
def get_crop_recommendations():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    soil_type = data.get('soil_type')

    if not all([temperature, humidity, soil_type]):
        return jsonify({"error": "Missing data"}), 400

    recommended_crops = recommend_crop(temperature, humidity, soil_type)

    return jsonify({"recommended_crops": recommended_crops})

if __name__ == '__main__':
    app.run(debug=True)
