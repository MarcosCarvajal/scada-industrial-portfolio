# Tuesday — Week 2: system.tag.write() and system.tag.read()

## Session Overview

Yesterday you created a Memory Tag manually in the Designer UI.
Today you control tags **programmatically** using Jython — the same
way Ignition controls them in production.

This is the moment where your Week 1 Python logic moves inside Ignition.

By the end of this session you will be able to:
- Read and write tag values from the Script Console
- Understand the `[default]` tag path syntax
- Run a Jython script that reads a tag, modifies the value, and writes it back
- Handle the differences between Python 3 and Jython 2.7 in practice

---

## Time Breakdown

| Time   | Activity                                         | Output                  |
|--------|--------------------------------------------------|-------------------------|
| 60 min | Technical — Tag read/write in Script Console     | screenshots + notes     |
| 20 min | English — IU course: Tags in Ignition            | `tuesday_notes.txt`     |

---

## Technical Activity — 60 min

### Step 1 — Open the Script Console `(5 min)`

In Ignition Designer, go to:
```
Tools → Script Console
```

This is your interactive Jython interpreter — equivalent to the Python
terminal you used all of Week 1. Every line you run here executes
**inside the Gateway**, not on your local Python installation.

Verify Jython is working by running:
```python
print "Script Console is working"
print system.util.getVersion()
```

You should see the Ignition version printed. If you see a syntax error
on `print`, you are accidentally in a Python 3 context — check that
you are in the Script Console, not a Python file in VS Code.

> **Important:** in Jython 2.7, `print` without parentheses works.
> But `print("text")` also works. Use parentheses from now on —
> it keeps your code compatible if you ever migrate to newer versions.

---

### Step 2 — Read your first tag `(10 min)`

Your `TEMP_ZONE_A` tag exists in the `default` tag provider.
In Ignition, every tag path follows this format:
```
[provider_name]folder/tag_name
```

For your tag, the full path is:
```
[default]TEMP_ZONE_A
```

Run this in the Script Console:
```python
tag_path = "[default]TEMP_ZONE_A"
tag_value = system.tag.readBlocking([tag_path])
print(tag_value)
```

You will see a `QualifiedValue` object, not a plain number. To get
the actual value:
```python
print(tag_value[0].value)
```

**Expected output:**
```
23.5
```

> **Note:** `system.tag.readBlocking()` takes a **list** of paths and
> returns a **list** of QualifiedValue objects. Always use index `[0]`
> to get the first result. This is different from what you might expect.

---

### Step 3 — Write a new value to the tag `(10 min)`

Now write a new value to `TEMP_ZONE_A`:

```python
tag_path = "[default]TEMP_ZONE_A"
system.tag.writeBlocking([tag_path], [29.8])
```

After running this, look at the Tag Browser. The value should update
to `29.8` immediately.

Then read it back to confirm:
```python
result = system.tag.readBlocking([tag_path])
print("Current value: " + str(result[0].value))
```

**Expected output:**
```
Current value: 29.8
```

> **Note:** just like `readBlocking`, `writeBlocking` takes a **list**
> of paths and a **list** of values. The two lists must have the same
> length — one value per path.

---

### Step 4 — Build a reusable read/write function `(20 min)`

Now apply what you learned in Week 1. Write two functions in the
Script Console that wrap the system calls:

- `read_tag(tag_name)` — receives a tag name (without provider prefix),
  builds the full path, reads the value, and returns it as a plain number.
- `write_tag(tag_name, value)` — receives a tag name and a value,
  builds the full path, writes it, and prints a confirmation message.

Both functions must handle errors with `try/except` — if the tag does
not exist or the write fails, print an error message instead of crashing.

Test with:
```python
current = read_tag("TEMP_ZONE_A")
print("Read: " + str(current))

write_tag("TEMP_ZONE_A", 31.5)

updated = read_tag("TEMP_ZONE_A")
print("After write: " + str(updated))
```

**Expected output:**
```
Read: 29.8
Tag TEMP_ZONE_A updated to 31.5
After write: 31.5
```

---

### Step 5 — Create 2 more tags and test the functions `(15 min)`

Go back to the Tag Browser and create two more Memory Tags:

| Name | Data Type | Initial value |
|---|---|---|
| `HUMIDITY_ZONE_A` | Float | `65.0` |
| `PH_ZONE_A` | Float | `6.8` |

Then run your functions on all three tags in a loop:

```python
tags = ["TEMP_ZONE_A", "HUMIDITY_ZONE_A", "PH_ZONE_A"]
for tag in tags:
    value = read_tag(tag)
    print(tag + ": " + str(value))
```

**Expected output:**
```
TEMP_ZONE_A: 31.5
HUMIDITY_ZONE_A: 65.0
PH_ZONE_A: 6.8
```

---

## English Activity — 20 min

Go to Inductive University and watch the full **Tags in Ignition** course:
```
https://inductiveuniversity.com/courses/ignition/tags-in-ignition/8.3
```

While watching, write `tuesday_notes.txt` with 5 terms you did not
know before, using this format:

```
1. QualifiedValue  - The object returned by system.tag.readBlocking().
                     It contains the value, quality, and timestamp of a tag read.
2. Tag quality     - ...
3. ...
```

> **Focus on:** what is a QualifiedValue, what does tag quality mean,
> and what is the difference between `readBlocking` and the older
> `system.tag.read` (deprecated). These will appear in the certification exam.

---

## Key Concepts for Today

| Concept | What it means |
|---|---|
| `[default]TAG_NAME` | Full tag path — provider in brackets, then tag name |
| `system.tag.readBlocking([path])` | Reads one or more tags — always pass a list, get a list back |
| `system.tag.writeBlocking([path], [value])` | Writes one or more tags — lists must match in length |
| `QualifiedValue` | Object returned by read — use `.value` to get the raw number |
| `.value` | The actual data inside a QualifiedValue |
| `.quality` | Whether the read was successful — `Good`, `Bad`, `Uncertain` |
| `.timestamp` | When the value was last updated |

---

## Why readBlocking and writeBlocking?

Ignition has older functions (`system.tag.read`, `system.tag.write`) that
are now deprecated. The `Blocking` versions are the current standard because
they wait for the operation to complete before returning — safer in
production scripts where timing matters.

Always use `readBlocking` and `writeBlocking` in new code.

---

## IU Progress Target for This Week

| Course | Target by Sunday |
|---|---|
| Tags in Ignition | ✅ 100% |
| Ignition Gateway | ✅ 100% |
| Clients and Sessions | 50%+ |

---

## Week 2 Milestone — Reminder

> Due Saturday: a Jython script inside Ignition that simulates 3 tags
> (temperature, humidity, pH) updating automatically every 10 seconds,
> with an alarm tag that activates when pH drops below 5.5.

Today's `read_tag` and `write_tag` functions are the core of that milestone.

---

## Git Commit

```bash
git add .
git commit -m "Week2/Tue: system.tag.readBlocking writeBlocking + reusable functions"
git push
```

> **What to commit today:** your `tuesday_notes.txt` and a file called
> `tag_functions.py` where you paste the two functions you wrote in the
> Script Console. Even though the Script Console code runs inside Ignition,
> keeping a `.py` copy in your repo documents what you built.
