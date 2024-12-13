from flask import Flask, request, jsonify

app = Flask(__name__)


data_store = {
    "illumination": None,
    "humidity": None
}


@app.route('/illumination', methods=['POST'])
def set_illumination():
    value = request.json.get("illumination")
    if 0 <= value <= 1:  
        data_store["illumination"] = value
        return {"message": "Освещенность сохранена"}, 200
    return {"error": "Значение освещенности должно быть от 0 до 1"}, 400


@app.route('/humidity', methods=['POST'])
def set_humidity():
    value = request.json.get("humidity")
    if 0 <= value <= 1: 
        data_store["humidity"] = value
        return {"message": "Влажность сохранена"}, 200
    return {"error": "Значение влажности должно быть от 0 до 1"}, 400


@app.route('/humidity', methods=['GET'])
def get_humidity():
    humidity = data_store["humidity"]
    if humidity is None:
        return {"error": "Данные о влажности отсутствуют"}, 404

    level = "low" if humidity <= 0.3 else "normal" if humidity <= 0.7 else "high"
    return jsonify({"humidity": humidity, "level": level})


@app.route('/illumination', methods=['GET'])
def get_illumination():
    illumination = data_store["illumination"]
    if illumination is None:
        return {"error": "Данные об освещенности отсутствуют"}, 404

    level = "low" if illumination <= 0.3 else "normal" if illumination <= 0.7 else "high"
    return jsonify({"illumination": illumination, "level": level})


@app.route('/status', methods=['GET'])
def get_status():
    illumination = data_store["illumination"]
    humidity = data_store["humidity"]

    if illumination is None or humidity is None:
        return {"error": "Недостаточно данных для генерации описания"}, 404

    illum_level = "темно" if illumination <= 0.3 else "нормально" if illumination <= 0.7 else "светло"
    humid_level = "влажно" if humidity > 0.7 else "сухо" if humidity <= 0.3 else "нормально"

    return {"status": f"В комнате {humid_level} и {illum_level}."}

if __name__ == '__main__':
    app.run(debug=True)
