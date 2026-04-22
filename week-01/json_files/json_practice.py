import json #For create a Json file we need a import library

# Step 1 Copy list from sensor.py file (temperature_sensors)
temperature_sensors = [{"tag": "TEMP_ZONE_A", "value": 23.5, "degree":"°C", "timestamp": "2026-04-18 13:05:22"},
                 {"tag": "TEMP_ZONE_B", "value": 19.5, "degree":"°C", "timestamp": "2026-04-18 14:10:32"},
                 {"tag": "TEMP_ZONE_C", "value": 32.1, "degree":"°C", "timestamp": "2026-04-18 14:18:02"},
                 {"tag": "TEMP_ZONE_D", "value": 22.8, "degree":"°C", "timestamp": "2026-04-18 13:10:00"},
                 {"tag": "TEMP_RC_MOTOR", "value": 38.0, "degree": "°C", "timestamp": "2026-04-18 13:42:55"}
                 ]

# Step 2 Write a json file using a temperature_sensors list
data_parse = json.dumps(temperature_sensors, indent=4, ensure_ascii=False)

# Step 3 Create or Write file with JSON data
file_name = "sensor_data.json"
with open(file_name, "w", encoding= "utf-8") as f:
    f.write(data_parse)
    print("the file "+file_name+" was wroten successfully")

# Step 4 Read JSON file and show in terminal
plc_01 = {
            "device": "RC_GREENHOUSE_01",
            "location": "Pereira",
            "readings": [
            ]
        }
with open(file_name, "r", encoding= "utf-8") as f:
    data_loads = json.loads(f.read())
    for i in data_loads:
        data_plc_values = {"tag": i["tag"], "value": i["value"]}
        plc_01["readings"].append(data_plc_values)

# Step 5 Write the new file plc_playload.json
plc_01_file_name = "plc_payload.json"
with open(plc_01_file_name, "w", encoding="utf-8") as f:
    json.dump(plc_01, f, indent=4, ensure_ascii=False)

# Step 6 Open and read new file with PLC Data
with open(plc_01_file_name) as f:
    loads_plc_file =json.loads(f.read())
    
print("device: "+loads_plc_file["device"])
print("location: "+loads_plc_file["location"])
print("--- readings above threshold ---")
for i in loads_plc_file["readings"]:
    if i["value"] >= 30:
        print(i["tag"]+": "+str(i["value"]))
        
