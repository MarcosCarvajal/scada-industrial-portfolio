# Saturday — Week 1: Milestone Project

## What today is

This is not a learning day. Today you **assemble** everything you built
this week into one complete, clean script. No new concepts — only
execution.

Every function you need already exists in your previous files.
Your job is to connect them.

---

## The Milestone

> Read a CSV file of 20 sensor records, run each record through
> `get_sensor_status`, and save the filtered results to a JSON file.

This is the exact pipeline that Ignition runs internally every time
it receives data from a field device and stores it in a historian.

---

## Step 1 — Create the CSV file `(10 min)`

Create a file called `sensor_records.csv` manually. It must have exactly
20 rows of sensor data with this structure:

```
tag,value,unit,timestamp
TEMP_ZONE_A,23.5,°C,2026-04-19 06:00:00
TEMP_ZONE_B,19.5,°C,2026-04-19 06:00:01
...
```

Rules for your data:
- At least **5 different tag names** (mix greenhouse and RC car sensors)
- At least **4 readings above 30** (these are your anomalies)
- At least **2 corrupted values** — use `NULL` or `N/A` as the value
- Timestamps must be realistic and sequential

> This simulates a data export from a real historian. In production you
> would receive this file automatically — today you create it by hand
> so you understand the structure.

---

## Step 2 — Read the CSV `(15 min)`

In a new file called `milestone.py`, read `sensor_records.csv` using
Python's built-in `csv` module. No pandas — use only the standard library.

Print the first 3 rows to verify the data loaded correctly before
continuing.

**Expected output:**
```
CSV loaded: 20 records
Preview:
  TEMP_ZONE_A | 23.5 | °C | 2026-04-19 06:00:00
  TEMP_ZONE_B | 19.5 | °C | 2026-04-19 06:00:01
  TEMP_ZONE_C | 31.2 | °C | 2026-04-19 06:00:02
```

> **Hint:** research `csv.DictReader` — it reads each row as a dictionary
> where the keys are the column headers. That matches exactly the
> structure you have been using all week.

---

## Step 3 — Process every record `(15 min)`

Loop through all 20 records. For each one, call `get_sensor_status`
with a threshold of `30`. Collect the results into two separate lists:
`anomalies` and `clean`.

A record is an **anomaly** if its status is `ALERT` or `ERROR`.
A record is **clean** if its status is `NORMAL`.

Print a processing summary after the loop.

**Expected output:**
```
Processing 20 records...
  [OK]    TEMP_ZONE_A        23.5°C  →  NORMAL
  [OK]    TEMP_ZONE_B        19.5°C  →  NORMAL
  [ALERT] TEMP_ZONE_C        31.2°C  →  ALERT
  [ERROR] TEMP_ZONE_D        NULL    →  ERROR
  ...

Processing complete: 6 anomalies / 14 clean
```

---

## Step 4 — Save results to JSON `(15 min)`

Save both lists to a single JSON file called `milestone_results.json`
with this structure:

```json
{
    "generated_at": "2026-04-25 08:00:00",
    "threshold": 30,
    "total_records": 20,
    "summary": {
        "anomalies": 6,
        "clean": 14
    },
    "anomalies": [ ... ],
    "clean_records": [ ... ]
}
```

For `generated_at` use Python's `datetime` module:
```python
from datetime import datetime
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

**Expected terminal output after saving:**
```
Results saved to milestone_results.json
  Anomalies : 6
  Clean     : 14
  Generated : 2026-04-25 08:00:00
```

---

## Step 5 — Print the final operator report `(5 min)`

Reuse your `centered_text` and formatting functions from `friday_practice.py`.
Print the anomalies as a formatted report after saving the file.

**Expected output:**
```
========================================
        ANOMALY REPORT — WEEK 1
========================================
TEMP_ZONE_C          |   31.2 °C   ALERT
TEMP_ZONE_D          |   NULL  °C   ERROR
TEMP_RC_MOTOR        |   38.0 °C   ALERT
...
========================================
Total anomalies: 6 / 20 records
========================================
```

---

## English Activity — 20 min

Write `saturday_notes.txt`. This week you identified a real problem in
Point 4 of your Friday notes — no clear plan for next week.

Fix that today. Write a short plan in English for **Week 2** covering:

```
1. What technical topic you will start (Jython in Ignition)
2. One thing you want to understand better from this week
3. One English skill you want to improve next week
4. How you will measure if Week 2 was successful
```

Minimum 80 words. Paste it here when done.

---

## Definition of Done

Your milestone is complete when all of these are true:

- [ ] `sensor_records.csv` exists with 20 rows, 4+ anomalies, 2+ errors
- [ ] `milestone.py` runs without errors from start to finish
- [ ] `milestone_results.json` is saved with the correct structure
- [ ] The anomaly report prints to terminal in formatted output
- [ ] All files committed and pushed to GitHub

---

## Git Commit

```bash
git add .
git commit -m "Week1/Milestone: CSV pipeline - read, process, filter, export JSON"
git push
```

---

## Folder structure after today

```
week-01/
├── sensors.py
├── json_practice.py
├── functions_practice.py
├── friday_practice.py
├── milestone.py              ← new today
├── sensor_records.csv        ← new today
├── milestone_results.json    ← generated by milestone.py
├── sensor_data.json
├── plc_payload.json
├── TUESDAY.md
├── WEDNESDAY.md
├── THURSDAY.md
├── FRIDAY.md
├── SATURDAY.md               ← this file
├── tuesday_email.txt
├── wednesday_notes.txt
├── thursday_notes.txt
├── friday_notes.txt
└── saturday_notes.txt        ← new today
```
