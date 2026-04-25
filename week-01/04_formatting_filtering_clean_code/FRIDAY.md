# Friday — Week 1: Formatting, Filtering & Clean Code
 
## Session Overview

This week you built the core tools: lists, dicts, JSON, functions, and
error handling. Today you put them together into **clean, readable,
production-style code** — the kind that a senior engineer can read and
understand without asking you questions.

By the end of this session you will be able to:
- Format terminal output so it is readable by an operator
- Filter and sort sensor data using functions you already wrote
- Write code that follows Python naming and structure conventions

---

## Time Breakdown

| Time   | Activity                                        | Output file          |
|--------|-------------------------------------------------|----------------------|
| 60 min | Technical — Formatting & filtering (Steps 1–3) | `friday_practice.py` |
| 20 min | English — Write a technical summary             | `friday_notes.txt`   |

---

## Technical Activity — 60 min

### Step 1 — Format output like an operator panel `(20 min)`

Take your `temperature_sensors` list and print a formatted status report.
No raw dicts, no `{'tag': ...}` output. It must look like something an
operator would read on a screen.

Requirements:
- Each line must be exactly the same width
- Tag name left-aligned, status right-aligned
- A header and a footer separator line
- Summary at the bottom

**Expected output:**
```
========================================
       GREENHOUSE STATUS REPORT
========================================
TEMP_ZONE_A          |   23.5 °C  NORMAL
TEMP_ZONE_B          |   19.5 °C  NORMAL
TEMP_ZONE_C          |   32.1 °C   ALERT
TEMP_ZONE_D          |   22.8 °C  NORMAL
TEMP_RC_MOTOR        |   38.0 °C   ALERT
========================================
Summary: 2 ALERT / 3 NORMAL
========================================
```

> **Hint:** research Python's string `.ljust(n)` and `.rjust(n)` methods.
> They pad a string to a fixed width — exactly what formatted reports need.

---

### Step 2 — Filter and sort without modifying the original list `(20 min)`

Write two functions:

- `get_alerts(sensor_list, threshold)` — returns a **new list** containing
  only the sensors whose value exceeds the threshold. The original list
  must remain unchanged.
- `sort_by_value(sensor_list)` — returns a **new list** sorted from highest
  to lowest value. The original list must remain unchanged.

Call both functions on your `temperature_sensors` list and print the results.

**Expected output:**
```
--- Alerts only (threshold: 30) ---
TEMP_ZONE_C          |   32.1 °C
TEMP_RC_MOTOR        |   38.0 °C

--- All sensors sorted by value (high to low) ---
TEMP_RC_MOTOR        |   38.0 °C
TEMP_ZONE_C          |   32.1 °C
TEMP_ZONE_A          |   23.5 °C
TEMP_ZONE_D          |   22.8 °C
TEMP_ZONE_B          |   19.5 °C
```

> **Hint:** research Python's built-in `sorted()` function and its
> `key` and `reverse` parameters. You do not need a loop to sort.

---

### Step 3 — Load from JSON and run the full pipeline `(20 min)`

Open `plc_payload.json`. Run the full pipeline on its readings:

1. Load the file
2. Run `get_alerts()` with threshold `30`
3. Run `sort_by_value()` on the full list
4. Print the formatted report from Step 1 using the sorted list
5. Print the alerts section below it

**Expected output:**
```
========================================
  RC_GREENHOUSE_01 — STATUS REPORT
========================================
TEMP_ZONE_B          |   19.5 °C  NORMAL
TEMP_ZONE_D          |   22.8 °C  NORMAL
TEMP_ZONE_A          |   23.5 °C  NORMAL
TEMP_ZONE_C          |   32.1 °C   ALERT
TEMP_RC_MOTOR        |   38.0 °C   ALERT
========================================
Summary: 2 ALERT / 3 NORMAL

--- Active alerts ---
TEMP_ZONE_C          |   32.1 °C
TEMP_RC_MOTOR        |   38.0 °C
```

> **Note:** the report is sorted low to high this time — that is intentional.
> Operators scan from normal to critical. Adjust `reverse` accordingly.

---

## English Activity — 20 min

Write a short technical summary in `friday_notes.txt` as if you were
reporting to your team at the end of the week.

Cover these four points in English, one paragraph each:

```
1. What you built this week (list the 3 scripts and what each one does)
2. What was the hardest concept and how you solved it
3. One thing you would do differently if you started again
4. What you plan to build next week
```

Minimum 100 words total. Write it yourself first — do not use a translator.
Paste it here when done for feedback.

> **Tip:** use past tense for what you did (`I built`, `I wrote`, `I learned`)
> and future tense for next week (`I will`, `I plan to`, `I expect to`).

---

## Key Concepts for Today

| Concept | What it does |
|---|---|
| `"text".ljust(20)` | Pads the string on the right to reach width 20 |
| `"text".rjust(10)` | Pads the string on the left to reach width 10 |
| `sorted(list, key=..., reverse=True)` | Returns a new sorted list without modifying the original |
| `[x for x in list if condition]` | List comprehension — filters into a new list in one line |

---

## Week 1 Milestone — Reminder

> Due Sunday: a Python script that reads a CSV file of 20 sensor records,
> filters anomalies, and saves the result as a JSON file.

Today's `get_alerts()` and formatting functions are ready to be reused
directly in the milestone script. Keep them clean.

---

## Git Commit

```bash
git add .
git commit -m "Week1/Fri: output formatting, filtering, and sort functions"
git push
```
