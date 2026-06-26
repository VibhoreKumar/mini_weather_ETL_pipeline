def classify_temp(t):
    if t >= 35: return "Hot"
    if t <= 10: return "Cold"
    return "Normal"

def build_record(city_name, raw_json):
    current = raw_json["current"]
    return {
        "city": city_name,
        "temperature_c": current["temperature_2m"],
        "wind_speed_kmh": current["wind_speed_10m"],
        "temp_category": classify_temp(current["temperature_2m"])
    }