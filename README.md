#Tuesday — Week 1: Python Sensors

##Create a file named sensors.py in VS Code. The goal is to model 5 temperature sensors from your greenhouse using Python's two most important data structures: lists and dictionaries.
Complete this in 4 progressive steps:
Step 1 — Simple List (10 min)
Create a list with 5 numerical temperature values. Print the entire list, then print only the third element. Research how to access an element by its index.
Expected Output:
[23.5, 24.1, 22.8, 25.0, 31.2]
22.8
Step 2 — Your First Dictionary (10 min)
Model ONE sensor using these keys: tag, value, and timestamp. Print the entire dictionary, then access only the "tag" value.
Expected Output:
{'tag': 'TEMP_ZONE_A', 'value': 23.5, 'timestamp': '2026-04-19 18:00:00'}
TEMP_ZONE_A
Step 3 — List of Dictionaries (20 min)
Now, create a list containing 5 sensors, each represented as a dictionary. One of them must be the RC car motor sensor with a temperature of 38.0. Use a "for loop" to iterate through the list and print each sensor's data on a single line.
Expected Output:
TEMP_ZONE_A: 23.5°C — 2026-04-19 18:00:00
TEMP_ZONE_B: 24.1°C — 2026-04-19 18:00:01
TEMP_ZONE_C: 22.8°C — 2026-04-19 18:00:02
TEMP_ZONE_D: 25.0°C — 2026-04-19 18:00:03
TEMP_RC_MOTOR: 38.0°C — 2026-04-19 18:00:04
Step 4 — Alert Filtering (20 min)
Without modifying the previous list, iterate through it again and display only the sensors whose value exceeds 30. Finally, print the total count of sensors in "alert" status vs. "normal" status.
Expected Output:
--- Out of Range Sensors ---
ALERT: TEMP_RC_MOTOR = 38.0°C
Summary: 1 in alert / 4 normal
English Activity (20 min)
Write a short email in a file named tuesday_email.txt. The recipient is your fictional team. Explain what you learned today and what technical issue you encountered while programming.
Minimum structure: greeting → what you did → what went well → what was difficult → what you will do tomorrow → sign-off.