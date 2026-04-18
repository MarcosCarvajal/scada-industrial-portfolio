# Step 1 Simple lists
temperatures = [23.5, 24.1, 22.8, 25.0, 31.2]
print(temperatures)

# Step 2 The First Dictionary
temp = {"tag": "TEMP_ZONE_A", "value": 23.5, "timestamp": "2026-04-18 13:05:22"}
print(temp["tag"])

# Step 3 List of Dictionaries
temperature_sensors = [{"tag": "TEMP_ZONE_A", "value": 23.5, "degree":"°C", "timestamp": "2026-04-18 13:05:22"},
                 {"tag": "TEMP_ZONE_B", "value": 19.5, "degree":"°C", "timestamp": "2026-04-18 14:10:32"},
                 {"tag": "TEMP_ZONE_C", "value": 32.1, "degree":"°C", "timestamp": "2026-04-18 14:18:02"},
                 {"tag": "TEMP_ZONE_D", "value": 22.8, "degree":"°C", "timestamp": "2026-04-18 13:10:00"},
                 {"tag": "TEMP_RC_MOTOR", "value": 38.0, "degree": "°C", "timestamp": "2026-04-18 13:42:55"}
                 ]
for i in temperature_sensors:
    print(str(i["tag"])+" - "+str(i["value"])+" "+str(i["degree"])+" - "+str(i["timestamp"]))
    
# Step 4 Alert Filtering
normal = 0
alert = 0
for i in temperature_sensors:
    if float(i["value"]) >= 30:
        print("ALERT !! "+ str(i["tag"])+" - "+str(i["value"])+" "+str(i["degree"])+" - "+str(i["timestamp"]))
        alert = alert + 1
    elif float(i["value"]) < 30:
        normal = normal + 1
print("Resume: " + str(alert) + " in ALERT - " + str(normal) + " in NORMAL")
        
# Setp 5 Tuesday_email.txt
with open("tuesday_email.txt", "r", encoding='utf-8') as file:
    content = file.read()
    print(content)        
