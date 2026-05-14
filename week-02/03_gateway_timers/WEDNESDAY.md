# Wednesday — Week 2: Gateway Timer Scripts

## Session Overview

On Tuesday you wrote functions that read and write tags on demand —
you called them manually from the Script Console.

Today those functions run **automatically**, on a schedule, without
anyone triggering them. That is a Gateway Timer Script — the foundation
of every automated process in Ignition.

By the end of this session you will be able to:
- Create a Gateway Timer Script that runs every N seconds
- Update tag values automatically on a timer
- Understand the difference between Gateway, Designer, and Client script scopes
- Simulate a live sensor feed using only Ignition Memory Tags

---

## Time Breakdown

| Time   | Activity                                              | Output               |
|--------|-------------------------------------------------------|----------------------|
| 60 min | Technical — Gateway Timer Script + tag simulation     | timer running live   |
| 20 min | English — IU: Tag Groups + Gateway Events             | `wednesday_notes.txt`|

---

## Technical Activity — 60 min

### Step 1 — Understand script scopes `(10 min)`

Before writing any code, read this table carefully. Scope is the most
common source of confusion in Ignition scripting:

| Scope | Where it runs | When it runs | Has access to |
|---|---|---|---|
| **Gateway** | Gateway server | Always, even with no clients | Tags, DB, files |
| **Designer** | Designer app | Only when Designer is open | Tags, UI components |
| **Client** | Vision client | Only when a client is connected | Tags, UI components |
| **Perspective Session** | Browser session | Only when session is active | Tags, session props |

Gateway Timer Scripts run in **Gateway scope** — they keep running
24/7 regardless of whether anyone has the Designer or a client open.
This is why they are used for data simulation, polling, and automation.

---

### Step 2 — Create your first Gateway Timer Script `(20 min)`

In Ignition Designer, go to:
```
Project Browser → Scripting → Gateway → Gateway Timer Scripts
```

Right-click **Gateway Timer Scripts** and select **New Script**.
Name it:
```
simulate_greenhouse
```

Set the execution rate to **5000 milliseconds** (5 seconds).

In the script editor, write a script that:
1. Reads the current value of `TEMP_ZONE_A`
2. Adds a small random variation (between -0.5 and +0.5)
3. Writes the new value back to the tag
4. Logs the update using `system.util.getLogger()`

**Structure to implement — do not copy, build it yourself:**
```
import random

logger = system.util.getLogger("greenhouse_timer")

current = # read TEMP_ZONE_A using your read pattern from Tuesday
variation = # random float between -0.5 and 0.5
new_value = # current + variation

# write new_value to TEMP_ZONE_A

logger.info("TEMP_ZONE_A updated to: " + str(round(new_value, 2)))
```

Save the project (`Ctrl+S`) and watch the Tag Browser — `TEMP_ZONE_A`
should change value every 5 seconds automatically.

> **Important:** after writing the script, go to
> **Tools → Diagnostics → Gateway Script Console** to see the log output.
> You should see the logger messages appearing every 5 seconds.

---

### Step 3 — Expand to all 3 tags `(20 min)`

Update `simulate_greenhouse` to simulate all three tags with realistic
variation ranges for a hydroponic greenhouse:

| Tag | Base value | Variation range | Unit |
|---|---|---|---|
| `TEMP_ZONE_A` | current value | ±0.5 | °C |
| `HUMIDITY_ZONE_A` | current value | ±1.0 | % |
| `PH_ZONE_A` | current value | ±0.05 | pH |

Requirements:
- Keep all 3 values within realistic bounds using `min()` and `max()`:
  - Temperature: 15.0 – 40.0 °C
  - Humidity: 40.0 – 95.0 %
  - pH: 4.0 – 8.5
- Log each update on a single line, for example:
  ```
  TEMP: 23.7 | HUM: 64.2 | PH: 6.75
  ```

---

### Step 4 — Verify it is running `(10 min)`

Open the Tag Browser and watch all 3 tags for 30 seconds. Values should
fluctuate within their ranges automatically.

Then open:
```
Tools → Diagnostics → Gateway Script Console
```

Verify the log line appears every 5 seconds. If you see errors instead,
read the error message carefully — it will tell you exactly which line
failed and why.

**Common errors at this step:**

| Error | Cause | Fix |
|---|---|---|
| `AttributeError: 'NoneType'` | `read_tag` returned `None` | Tag path is wrong — check spelling |
| `TypeError: unsupported operand` | Value is not a float | Wrap read result in `float()` |
| `KeyError` | Tag does not exist | Verify tag name in Tag Browser |

---

## English Activity — 20 min

Go to Inductive University and watch these two videos:

```
Tags in Ignition → Tag Groups → Tag Group Overview  (3:23)
Tags in Ignition → Tag Groups → Driven Tag Group    (3:41)
```

Then write `wednesday_notes.txt` with answers to these 3 questions
in your own English words:

```
1. What is a Tag Group and how does it control scan rate?
2. What is the difference between a Default Tag Group and a Driven Tag Group?
3. How does a Gateway Timer Script differ from a Tag Group in terms
   of when and how it executes?
```

Minimum 2 sentences per answer. No Google Translate.

---

## Key Concepts for Today

| Concept | What it means |
|---|---|
| Gateway Timer Script | A Jython script that runs automatically on a fixed interval in the Gateway |
| Execution rate | How often the script runs — set in milliseconds |
| `system.util.getLogger("name")` | Creates a named logger — use `.info()`, `.warn()`, `.error()` |
| `logger.info("msg")` | Writes a message to the Gateway log at INFO level |
| `random.uniform(a, b)` | Returns a random float between a and b |
| `min(value, max_limit)` | Clamps a value so it never exceeds max_limit |
| `max(value, min_limit)` | Clamps a value so it never goes below min_limit |
| Gateway scope | Scripts run on the server — no UI access, always running |

---

## Why This Matters in Production

In a real plant, the Gateway Timer Script is replaced by actual PLC data
coming through OPC-UA or Modbus. But the script structure is identical —
read a value, process it, write it somewhere, log it.

What you build today is a **software simulator** of a PLC. In Week 7
when you connect a real Modbus device, you will replace the `random`
variation with an actual hardware read — and everything else stays the same.

---

## IU Progress Target

| Course | Target by Sunday |
|---|---|
| Tags in Ignition | 100% |
| Ignition Gateway Setup | 100% |
| Launching Ignition | 100% |

---

## Week 2 Milestone — Reminder

> Due Saturday: a Jython script inside Ignition that simulates 3 tags
> (temperature, humidity, pH) updating automatically every 10 seconds,
> with an alarm tag that activates when pH drops below 5.5.

Today's `simulate_greenhouse` timer is the milestone — Saturday you
add the alarm logic on top of what you built today.

---

## Git Commit

```bash
git add .
git commit -m "Week2/Wed: Gateway Timer Script simulating 3 greenhouse tags"
git push
```

> **What to commit:** `wednesday_notes.txt` and a file called
> `gateway_timer.py` with the script you wrote in the Designer.
> Copy it from the Designer script editor to VS Code before closing.
