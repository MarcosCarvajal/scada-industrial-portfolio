import json
# Step 1 Format output like an operator panel
def get_sensor_status(tag, value, threshold):
    data = {"tag": tag, "status": None, "code_status": 0}
    try:
        if value > threshold:
            data["status"] = "ALERT!"
            data["code_status"] = 1
        else:
            data["status"] = "NORMAL"
            data["code_status"] = 2
        return data
    except (TypeError, ValueError):
        data["status"] = "ERROR"
        data["code_status"] = 3
        return data

def centered_text(simbol,dict):
    x_data_body = dict["tag"][:20].ljust(20)+simbol.ljust(3)+str(dict["value"]).ljust(5)+str(dict["degree"]).ljust(5)+dict["status"].rjust(7)
    return x_data_body

def sortFunc(e):
    try:
        return float(e["value"])
    except (ValueError, TypeError):
        return -999.0

f = open("../json_files/sensor_data.json", "r", encoding="utf-8")
data_json = json.loads(f.read())

data= {}
alert_2 = 0
normal_2 = 0
errors_2 = 0
equals = ""
x = equals.ljust(40, "=")
title = "GREENHOUSE STATUS REPORT"
width_title = 40
x_title = title.ljust(len(title)+((width_title - len(title))//2)).rjust(width_title)
print(x)
print(x_title)
print(x)
new_data_json = []
for i in data_json:
    data = get_sensor_status(i["tag"], i["value"], 30)
    if data["code_status"] == 1:
        alert_2 += 1
    elif data["code_status"] == 2:
        normal_2 += 1
    elif data["code_status"] == 3:
        errors_2 += 1
    i.update({"code_status":data["code_status"], "status":data["status"]})
    new_data_json.append(i)
    #print(centered_text(data["tag"],"|",i["value"],i["degree"],data["status"]))

new_data_json.sort(key=sortFunc, reverse=True)

for i in new_data_json:
    print(centered_text('|',i))

print(x)
print("Sumary: " + str(alert_2) + " ALERT / "+ str(normal_2) + " NORMAL /" + " ERRORS "+ str(errors_2))
print(x+"\n")

active_alerts_title = "Active alerts"
x_active_alerts_title= active_alerts_title.ljust(len(active_alerts_title)+((width_title - len(active_alerts_title))//2),"-").rjust(width_title,"-")
print(x_active_alerts_title)
for i in new_data_json:
    if i["code_status"] == 1:
        print(centered_text('|',i))
