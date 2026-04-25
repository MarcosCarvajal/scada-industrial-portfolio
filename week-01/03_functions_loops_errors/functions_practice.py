import json
# Step 1 Reusable function
def get_sensor_status(tag, value, threshold):
    data = {"tag": tag, "status": None, "code_status": 0}
    if value > threshold:
        data["status"] = "ALERT!"
        data["code_status"] = 1
    else:
        data["status"] = "NORMAL"
    return data

# List of Values
temperature_sensors = [{"tag": "TEMP_ZONE_A", "value": 23.5, "degree":"°C", "timestamp": "2026-04-18 13:05:22"},
                 {"tag": "TEMP_ZONE_B", "value": 19.5, "degree":"°C", "timestamp": "2026-04-18 14:10:32"},
                 {"tag": "TEMP_ZONE_C", "value": 32.1, "degree":"°C", "timestamp": "2026-04-18 14:18:02"},
                 {"tag": "TEMP_ZONE_D", "value": 22.8, "degree":"°C", "timestamp": "2026-04-18 13:10:00"},
                 {"tag": "TEMP_RC_MOTOR", "value": 38.0, "degree": "°C", "timestamp": "2026-04-18 13:42:55"}
                 ]

for i in temperature_sensors:
    print(get_sensor_status(i["tag"], i["value"], 18))
    
# Step 2 Apply the function to a loop
normal = 0
alert = 0
for i in temperature_sensors:
    data_sensors = get_sensor_status(i['tag'],i['value'], 22.9)
    if  data_sensors["code_status"]== 1:
        alert = alert + 1
        print(data_sensors["tag"]+"   → "+data_sensors["status"])
    else:
        normal = normal + 1
        print(data_sensors["tag"]+"   → "+data_sensors["status"])
       
print("Sumary: " + str(alert) + " ALERT / "+ str(normal) + " NORMAL")

# Step 3 Make the function safe with try/except
def get_sensor_status_try_except(tag, value, threshold):
    data = {"tag": tag, "status": None, "code_status": 0}
    try:
        if value > threshold:
            data["status"] = "ALERT!"
            data["code_status"] = 1
        else:
            data["status"] = "NORMAL"
            data["code_status"] = 2
        return data
    except:
        data["status"] = "ERROR"
        data["code_status"] = 3
        return data

# List of Values
temperature_sensors_try_except = [{"tag": "TEMP_ZONE_A", "value": 23.5, "degree":"°C", "timestamp": "2026-04-18 13:05:22"},
                 {"tag": "TEMP_ZONE_B", "value": 19.5, "degree":"°C", "timestamp": "2026-04-18 14:10:32"},
                 {"tag": "TEMP_ZONE_C", "value": "N/A", "degree":"°C", "timestamp": "2026-04-18 14:18:02"},
                 {"tag": "TEMP_ZONE_D", "value": None, "degree":"°C", "timestamp": "2026-04-18 13:10:00"},
                 {"tag": "TEMP_RC_MOTOR", "value": 38.0, "degree": "°C", "timestamp": "2026-04-18 13:42:55"}
                 ]

# Loop
normal = 0
alert = 0
errors = 0
for i in temperature_sensors_try_except:
    data_sensors = get_sensor_status_try_except(i['tag'],i['value'], 22.9)
    if  data_sensors["code_status"]== 1:
        alert = alert + 1
        print(data_sensors["tag"]+"   → "+data_sensors["status"])
    elif data_sensors["code_status"]== 2:
        normal = normal + 1
        print(data_sensors["tag"]+"   → "+data_sensors["status"])
    elif data_sensors["code_status"]== 3:
        errors = errors + 1
        print(data_sensors["tag"]+"   → "+data_sensors["status"])
        

print("Sumary: " + str(alert) + " ALERT / "+ str(normal) + " NORMAL /" + " ERRORS "+ str(errors))

# Step 4 Load from JSON and apply function
f = open("../json_files/sensor_data.json", "r", encoding="utf-8")
data_json = json.loads(f.read())
data= {}
alert_2 = 0
normal_2 = 0
errors_2 = 0
print("Device: RC_GREENHOUSE_01  |  Location: Pereira")
print("----------------------------------------------")
for i in data_json:
    data = get_sensor_status(i["tag"], i["value"], 30)
    try:
        if data["code_status"] == 1:
            alert_2 += 1
            print(data["tag"]+"   → "+data["status"])
        else:
            normal_2 += 1
            print(data["tag"]+"   → "+data["status"])
    except:
        errors_2 += 1
        print(data["tag"]+"   → "+"ERROR")

print("Sumary: " + str(alert_2) + " ALERT / "+ str(normal_2) + " NORMAL /" + " ERRORS "+ str(errors_2))