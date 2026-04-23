# Thursday — Week 1: Functions, Loops & Error Handling

## Session Overview

This week you have worked with lists, dictionaries, and JSON files.
Today you will write your **first reusable function** and make your scripts
**production-safe** using error handling — two skills that separate hobby
scripts from real industrial code.

By the end of this session you will be able to:
- Write a reusable function with parameters and a return value
- Use `try/except` to handle errors gracefully
- Apply both skills to your greenhouse and RC car sensor data

---

## Time Breakdown

| Time   | Activity                                          | Output file             |
|--------|---------------------------------------------------|-------------------------|
| 60 min | Technical — Functions & error handling (Steps 1–4) | `functions_practice.py` |
| 20 min | English — Read + annotate Ignition docs           | `thursday_notes.txt`    |

---

## Technical Activity — 60 min

### Step 1 — Your first reusable function `(15 min)`

Write a function called `get_sensor_status` that receives three parameters:
`tag`, `value`, and `threshold`. It must **return** (not print) a dictionary
with two keys: `"tag"` and `"status"`. The status must be `"ALERT"` if the
value exceeds the threshold, and `"NORMAL"` otherwise.

Call the function once for each sensor in your `temperature_sensors` list and
print the result of each call.

**Expected output:**
```
{'tag': 'TEMP_ZONE_A', 'status': 'NORMAL'}
{'tag': 'TEMP_ZONE_B', 'status': 'NORMAL'}
{'tag': 'TEMP_ZONE_C', 'status': 'ALERT'}
{'tag': 'TEMP_ZONE_D', 'status': 'NORMAL'}
{'tag': 'TEMP_RC_MOTOR', 'status': 'ALERT'}
```

> **Hint:** a function uses the `def` keyword and `return` to send a value
> back to the caller. The caller receives whatever you `return`.

---

### Step 2 — Apply the function to a loop `(10 min)`

Now call `get_sensor_status` inside a `for` loop over the full sensor list.
At the end, print a summary line showing how many sensors are in each status.

**Expected output:**
```
TEMP_ZONE_A     → NORMAL
TEMP_ZONE_B     → NORMAL
TEMP_ZONE_C     → ALERT
TEMP_ZONE_D     → NORMAL
TEMP_RC_MOTOR   → ALERT

Summary: 2 ALERT / 3 NORMAL
```

---

### Step 3 — Make the function safe with `try/except` `(20 min)`

In real systems, sensor data can arrive corrupted — a string instead of a
number, a missing key, or a `None` value. Your function must not crash the
entire script when one sensor has bad data.

Add a `try/except` block **inside** `get_sensor_status`. If anything goes
wrong while comparing the value, the function must return `"ERROR"` as the
status instead of crashing.

Test your function with this corrupted sensor list — do **not** modify it,
your function must handle it as-is:

```python
corrupted_sensors = [
    {"tag": "TEMP_ZONE_A", "value": 23.5},
    {"tag": "TEMP_ZONE_B", "value": "N/A"},      # string instead of number
    {"tag": "TEMP_ZONE_C", "value": None},        # missing reading
    {"tag": "TEMP_RC_MOTOR", "value": 38.0},
]
```

**Expected output:**
```
TEMP_ZONE_A     → NORMAL
TEMP_ZONE_B     → ERROR
TEMP_ZONE_C     → ERROR
TEMP_RC_MOTOR   → ALERT
```

> **Hint:** wrap only the comparison line inside `try`, not the entire
> function. Catching too broadly hides real bugs.

---

### Step 4 — Load from JSON and apply the function `(15 min)`

Open the `plc_payload.json` file you created on Wednesday. Load it, then run
every reading through `get_sensor_status` with a threshold of `30`.

This simulates what Ignition does every time it receives a payload from a
field device: parse → validate → classify.

**Expected output:**
```
Device: RC_GREENHOUSE_01  |  Location: Pereira
----------------------------------------
TEMP_ZONE_A     → NORMAL
TEMP_ZONE_B     → NORMAL
TEMP_ZONE_C     → ALERT
TEMP_ZONE_D     → NORMAL
TEMP_RC_MOTOR   → ALERT

Summary: 2 ALERT / 3 NORMAL
```

---

## English Activity — 20 min

Open this page in your browser — no login required:

```
https://docs.inductiveautomation.com/docs/8.1/platform/scripting/python-scripting
```

Read it for **15 minutes** straight in English without translating. Then
write 5 sentences in `thursday_notes.txt` that summarize what you read.

Use this structure for each sentence:

```
1. Ignition uses Jython 2.7, which means you should check Python 2.7 docs
   instead of Python 3 docs when looking up built-in functions.
2. ...
```

> **Rule:** each sentence must contain at least one technical term from the
> page. Do not copy sentences directly — rewrite them in your own words.

---

## Key Concepts for Today

| Concept | What it means in industrial code |
|---|---|
| `def func(a, b)` | Defines a reusable block of logic with inputs |
| `return value` | Sends a result back to the caller — always prefer this over `print` inside functions |
| `try / except` | Catches a runtime error so the script keeps running |
| `except TypeError` | Catches only type errors — more precise than bare `except` |
| `except (TypeError, ValueError)` | Catches multiple specific error types |

---

## Why this matters in SCADA

In Ignition, your scripts run **automatically** on a gateway server — there
is no one watching the terminal. If one bad sensor reading crashes your
script, the entire data pipeline stops silently.

A function that returns `"ERROR"` instead of crashing lets the rest of the
system keep running and gives operators a visible signal that one sensor
needs attention.

---

## Week 1 Milestone — Reminder

> Due Sunday: a Python script that reads a CSV file of 20 sensor records,
> filters anomalies, and saves the result as a JSON file.

Today's `get_sensor_status` function is the core logic of that milestone.
You will reuse it directly on Sunday.

---

## Git Commit

```bash
git add .
git commit -m "Week1/Thu: reusable function + try/except error handling"
git push
```
