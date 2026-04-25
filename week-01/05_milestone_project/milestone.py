import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
from tools import utils
import json
import datetime

# Setp 2 Read CSV data
reader = []
threshold = 30
with open('sensor_records.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file,delimiter=';')
    processed_data = utils.get_sensor_status(reader, threshold)

# Step 3 Process every record
all_records = len(list(processed_data))
print("Processing "+str(all_records)+" records...")
for i in processed_data:
    print(utils.centered_text('→',i))

anomalies_status = list(filter(lambda x: x["code_status"] == 1 or x["code_status"] == 3, processed_data))
clean_records = list(filter(lambda x: x["code_status"] == 2, processed_data))
print("... \n")
print("Processing complete: "+str(len(anomalies_status))+ " anomalies / "+str(len(clean_records))+" clean")

json_data = {"generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "threshold": threshold,
             "total_records": all_records,
             "summary": {"anomalies": len(anomalies_status), "clean": len(clean_records)},
             "anomalies": anomalies_status,
             "clean": clean_records}
# Step 4 Save results to JSON
text_anomalies = "Anomalies"
text_clean = "Clean"
text_generated = "Generated"
x_anomalies = text_anomalies.ljust(11).rjust(13)
x_clean = text_clean.ljust(11).rjust(13)
x_generated = text_generated.ljust(11).rjust(13)
simbol = ':'
try:
    with open('milestone_results.json','w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
        
    print("\nResults saved to milestone_results.json \n"+x_anomalies+simbol.ljust(3)+str(len(anomalies_status))+"\n"+x_clean+simbol.ljust(3)
          +str(len(clean_records))+"\n"+x_generated+simbol.ljust(3)+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
# Step 5 Print the final operator report
    data_centered = utils.centered_text_2('|','ANOMALY REPORT — WEEK 1',anomalies_status)
    for i in data_centered:
        print(i)
    print("Total anomalies: "+str(len(anomalies_status))+ " anomalies / "+str(all_records)+" records")
    print(data_centered[len(data_centered)-1])
except IOError as e:
    print(f"Error: Could not write to file. {e}")
except TypeError as e:
    print(f"Error: Data contains non-JSON serializable objects. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
