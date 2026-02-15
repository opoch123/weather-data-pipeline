import json

# 1. Create the dictionary
weather_data = {
    "city": "Toronto",
    "temperature": 15,
    "humidity": 65,
    "status": "Partly Cloudy"
}

# 2. Save to a file (The "Load" part of a local ETL)
with open("daily_report.json", "w") as f:
    json.dump(weather_data, f, indent=4)

# 3. Read it back (The "Extract" part)
with open("daily_report.json", "r") as f:
    loaded_data = json.load(f)
    print(f"Ingestion successful! Humidity is: {loaded_data['humidity']}%")