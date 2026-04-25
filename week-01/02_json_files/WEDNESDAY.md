# Wednesday — Week 1: JSON Files & PLC Payloads

## Session Overview

Yesterday you modeled sensors using Python dictionaries.
Today you will learn to **persist and exchange that data using JSON** — the standard format for moving data between PLCs, APIs, databases, and Ignition.

By the end of this session you will be able to:
- Write sensor data to a `.json` file
- Load a JSON file back into Python
- Parse a realistic PLC payload and extract only the values you need

---

## Time Breakdown

| Time   | Activity                                      | Output file            |
|--------|-----------------------------------------------|------------------------|
| 60 min | Technical — JSON in Python (Steps 1–3)        | `json_practice.py`     |
| 20 min | English — Watch tutorial + vocabulary notes   | `wednesday_notes.txt`  |

---

## Technical Activity — 60 min

### Step 1 — Write sensor data to a JSON file `(15 min)`

Take the `temperature_sensors` list from Tuesday's `sensors.py` and save it to a new file called `sensor_data.json`.

Research the `json` module and the function that writes a Python object **directly to a file**. Use **4-space indentation** so the file is human-readable.

**Expected result in `sensor_data.json`:**
```json
[
    {
        "tag": "TEMP_ZONE_A",
        "value": 23.5,
        "degree": "°C",
        "timestamp": "2026-04-18 13:05:22"
    },
    ...
]
```

> **Hint:** the `json` module has two similar functions — one writes to a string, the other writes directly to a file object. You want the one that accepts a file object as its second argument.

---

### Step 2 — Load the JSON file back into Python `(15 min)`

In the same script (`json_practice.py`), after writing the file, open `sensor_data.json` and load its contents back into a new variable. Then loop through the list and print only the `tag` of each sensor.

**Expected terminal output:**
```
Sensors loaded from file:
TEMP_ZONE_A
TEMP_ZONE_B
TEMP_ZONE_C
TEMP_ZONE_D
TEMP_RC_MOTOR
```

> **Hint:** the counterpart to the write function is the load function. It also has a version for strings and a version for file objects. Use the file version.

---

### Step 3 — Parse a realistic PLC payload `(30 min)`

In real automation projects, a PLC or MQTT gateway sends data like this — a single JSON object with device metadata and a **nested list** of readings:

```json
{
    "device": "RC_GREENHOUSE_01",
    "location": "Pereira",
    "readings": [
        { "tag": "TEMP_ZONE_A",    "value": 23.5 },
        { "tag": "HUMIDITY_ZONE_A","value": 65.0 },
        { "tag": "TEMP_RC_MOTOR",  "value": 38.0 }
    ]
}
```

**Your task:**
1. Create this structure as a Python dictionary in your script.
2. Save it to a new file called `plc_payload.json`.
3. Load `plc_payload.json` back into Python.
4. Print the device name and location.
5. Loop through the `readings` list and print only the tags whose value exceeds `30`.

**Expected terminal output:**
```
Device: RC_GREENHOUSE_01
Location: Pereira
--- Readings above threshold ---
TEMP_RC_MOTOR: 38.0
```

---

## English Activity — 20 min

Search on YouTube for:

```
"Ignition SCADA Python Scripting basics"
```

Watch the first **15 minutes** with full attention. While you listen, write down exactly **5 technical terms** you did not know before, using this format in `wednesday_notes.txt`:

```
1. Tag Provider    - A configured source of tags in the Ignition Gateway
2. Script Console  - An interactive Jython interpreter inside Ignition Designer
3. ...
```

> **Shadowing tip:** pause the video each time the speaker says a term you do not recognize. Say it aloud **twice** before writing it down. Do not use Google Translate — write the definition in your own words based on what you heard.

---

## Key Concepts for Today

| Function | What it does |
|---|---|
| `json.dump(obj, file)` | Writes a Python object to an open file as JSON |
| `json.load(file)` | Reads a JSON file and returns a Python object |
| `json.dumps(obj)` | Converts a Python object to a JSON string (no file) |
| `json.loads(string)` | Parses a JSON string into a Python object |

---

## Week 1 Milestone — Reminder

> Due Sunday: a Python script that reads a CSV file of 20 sensor records, filters anomalies, and saves the result as a JSON file.

Today's Steps 1–3 are direct building blocks for that milestone. Keep `json_practice.py` clean and well-commented — you will reuse parts of it.

---

## Git Commit

When you finish, run:

```bash
git add .
git commit -m "Week1/Wed: JSON read-write and PLC payload parsing"
git push
```

> Good commit messages follow this pattern: `Scope/Day: short description of what was built.`
