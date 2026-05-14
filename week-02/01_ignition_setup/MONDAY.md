# Monday — Week 2: Ignition Install & First Memory Tag

## Session Overview

Week 1 gave you the data pipeline in pure Python.
Week 2 moves that logic **inside Ignition** — the actual SCADA platform
you will use in every professional project.

Today is setup and exploration. No scripting yet — you need to understand
the environment before writing a single line of Jython.

By the end of this session you will be able to:
- Run Ignition Gateway locally and access it from a browser
- Open Ignition Designer and navigate its main panels
- Create a Memory Tag manually and read its value
- Explain the difference between Python 3 and Jython in Ignition

---

## Time Breakdown

| Time   | Activity                                          | Output                     |
|--------|---------------------------------------------------|----------------------------|
| 60 min | Technical — Install Ignition + first tag          | 1 Memory Tag created       |
| 20 min | English — Shadowing + vocabulary                  | `monday_notes.txt`         |

---

## Technical Activity — 60 min

### Step 1 — Install Ignition `(15 min)`

Go to the official download page:
```
https://inductiveautomation.com/downloads/ignition
```

Download the **Ignition 8.1** installer for your OS. Run it and follow
the setup wizard. When it asks for a license, choose **Start Trial** —
this gives you 2 hours of full functionality. The trial resets every time
you restart the Gateway, so you never actually run out of time for learning.

After installation, the Gateway starts automatically. Open your browser and go to:
```
http://localhost:8088
```

You should see the Ignition Gateway homepage. If you do, the install worked.

> **Note:** Ignition runs as a local web server on port 8088. This is
> the same Gateway that industrial plants run on their servers — you are
> running a full production-grade SCADA platform on your laptop.

---

### Step 2 — Explore the Gateway `(10 min)`

From `http://localhost:8088`, click **Config** in the top menu.
You are now in the Gateway Control Panel — the administrative backend
of your SCADA server.

Find and identify these sections without clicking anything yet:
- **Tags** — where tag providers are configured
- **Database Connections** — where you will connect MySQL in Week 3
- **OPC Connections** — where PLCs connect via OPC-UA
- **Modules** — what is currently installed

Write down what modules you see installed by default.

---

### Step 3 — Open Ignition Designer `(10 min)`

From the Gateway homepage (`http://localhost:8088`), click
**Launch Designer**. It will download a small launcher the first time.

Once Designer opens, create a **New Project** when prompted. Name it:
```
greenhouse_rc_project
```

Take 5 minutes to identify these panels in the Designer UI:
- **Tag Browser** (usually left panel) — shows all tags in the system
- **Project Browser** (left panel) — shows your views, scripts, and resources
- **Designer Canvas** (center) — where you build HMI screens
- **Property Editor** (right panel) — configures selected components

---

### Step 4 — Create your first Memory Tag `(15 min)`

In the Tag Browser panel, right-click on the root tag provider and
select **New Tag → New Standard Tag**.

Create a tag with these properties:

| Property | Value |
|---|---|
| Name | `TEMP_ZONE_A` |
| Data Type | `Float` |
| Tag Type | `Memory Tag` |
| Value | `23.5` |

A Memory Tag is a tag that lives only in Ignition's memory — it has no
physical device behind it. It is exactly what you will use this week to
simulate sensor data before connecting a real PLC.

After creating it, verify it appears in the Tag Browser with a green
status indicator and the value `23.5`.

---

### Step 5 — Understand Jython vs Python 3 `(10 min)`

Read this page for 10 minutes:
```
https://docs.inductiveautomation.com/docs/8.1/platform/scripting/python-scripting
```

Then answer these two questions in your head before writing them in your notes:

1. What Python version does Ignition use, and what does that mean for
   the `print` statement vs `print()` function?
2. What is one thing you can do in Python 3 that you **cannot** do
   in Jython 2.7?

---

## English Activity — 20 min

Search on YouTube:
```
"Ignition Designer overview" Inductive Automation
```

Watch for 15 minutes. While watching, write `monday_notes.txt` with:

```
1. Tag Browser    - ...your definition...
2. Designer       - ...your definition...
3. Gateway        - ...your definition...
4. Memory Tag     - ...your definition...
5. Tag Provider   - ...your definition...
```

Rules: write definitions in your own words, in English, without
Google Translate. Each definition must be at least one full sentence.

---

## Key Concepts for Today

| Concept | What it means |
|---|---|
| Gateway | The Ignition server — runs as a background process, accessible via browser |
| Designer | The IDE where you build HMI screens and write scripts |
| Tag Browser | The panel that shows all tags currently in the system |
| Memory Tag | A tag with no physical device — value lives only in Gateway memory |
| Tag Provider | A named container for tags — default is called `default` |
| Jython 2.7 | The Python interpreter built into Ignition — based on Python 2, not 3 |

---

## Important — Jython vs Python 3

You have been writing Python 3 all week. Ignition uses **Jython 2.7**.
The differences that will affect you most:

| Python 3 (what you know) | Jython 2.7 (Ignition) |
|---|---|
| `print("hello")` | `print "hello"` or `print("hello")` — both work |
| `json.dump(obj, file)` | `system.util.jsonEncode(obj)` |
| `json.load(file)` | `system.util.jsonDecode(string)` |
| `open("file.json")` | Not available — use Ignition's file functions |
| f-strings `f"{var}"` | Not supported — use `"text " + str(var)` |

> This is why Week 1 mattered. You learned the logic in Python 3 where
> you could run and test freely. Now you translate that logic into
> Jython inside Ignition — same concepts, slightly different syntax.

---

## Week 2 Milestone — Preview

> Due Saturday: a Jython script inside Ignition that simulates 3 tags
> (temperature, humidity, pH) updating automatically every 10 seconds,
> with an alarm tag that activates when pH drops below 5.5.

Today's Memory Tag is your first step toward that milestone.

---

## Git Commit

```bash
git add .
git commit -m "Week2/Mon: Ignition install + first Memory Tag + Jython overview"
git push
```
