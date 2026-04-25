# Tuesday — Week 1: Python Sensors Practice

## Project Overview
The objective of this module is to model a real-world scenario: monitoring a greenhouse with 5 temperature sensors. This practice focuses on mastering Python's core data structures—**Lists** and **Dictionaries**—which are essential for handling industrial data in SCADA systems.

## Progressive Challenges

### Step 1: Simple Lists
*   **Goal:** Store 5 numerical temperature values.
*   **Concept:** Understanding zero-based indexing and list access.
*   **Expected Output:** `[23.5, 24.1, 22.8, 25.0, 31.2]`

### Step 2: The First Dictionary
*   **Goal:** Model a single sensor with metadata.
*   **Concept:** Using **Key-Value pairs** (`tag`, `value`, `timestamp`) to represent industrial tags.
*   **Expected Output:** `TEMP_ZONE_A`

### Step 3: List of Dictionaries
*   **Goal:** Scale the system to 5 sensors, including an RC car motor sensor.
*   **Concept:** Implementing **For Loops** to iterate through complex datasets and print formatted strings.
*   **Expected Output:** 
    `TEMP_ZONE_A: 23.5°C — 2026-04-19 18:00:00`
    `TEMP_RC_MOTOR: 38.0°C — 2026-04-19 18:00:04`

### Step 4: Alert Filtering
*   **Goal:** Identify sensors exceeding safety thresholds (>30°C).
*   **Concept:** Applying **Conditional Logic** (`if` statements) to filter industrial data.
*   **Expected Result:** A summary count of "Alert" vs "Normal" sensors.

---

## English Immersion Activity
Inside this folder, you will find `tuesday_email.txt`. This file contains a short technical report written in English explaining:
1. What was accomplished today.
2. Technical roadblocks encountered during programming.
3. Plans for the next development cycle.

---
**Focus:** Industrial Automation & Python Programming.