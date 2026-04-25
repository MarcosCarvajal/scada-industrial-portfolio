def sortFunc(e):
    try:
        return float(e["value"])
    except (ValueError, TypeError):
        return -999.0
    
def get_sensor_status(list, threshold):
    new_list = []
    for i in list:
        new_codes = {"code_status": None, "status":None}
        try:
            float_value = float(i["value"])
            if float_value > threshold:
                new_codes["status"] = "ALERT"
                new_codes["code_status"] = 1
            else:
                new_codes["status"] = "NORMAL"
                new_codes["code_status"] = 2
        except (TypeError, ValueError):
            new_codes["status"] = "ERROR"
            new_codes["code_status"] = 3
        i.update({"code_status":new_codes["code_status"], "status":new_codes["status"]})
        new_list.append(i)
    return new_list

def centered_text(simbol,dict):
    x_data_body = dict["tag"][:20].ljust(20)+simbol.ljust(3)+str(dict["value"]).ljust(5)+str(dict["unit"]).ljust(5)+dict["status"].rjust(7)
    return x_data_body

def centered_text_2(simbol,title,list):
    list.sort(key=sortFunc, reverse=True)
    format_data = []
    equals = ""
    x = equals.ljust(45, "=")
    format_data.append("\n"+x)
    width_title = 45
    x_title = title.ljust(len(title)+((width_title - len(title))//2)).rjust(width_title)
    format_data.append(x_title)
    format_data.append(x)
    for ldict in list:
        x_data_body = ldict["tag"][:25].ljust(25)+simbol.ljust(3)+str(ldict["value"]).ljust(5)+str(ldict["unit"]).ljust(5)+ldict["status"].rjust(7)
        format_data.append(x_data_body)
    format_data.append(x)
    return format_data