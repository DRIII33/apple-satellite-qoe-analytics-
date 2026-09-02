# Dashboard Guide & Storytelling Brief: OrbitPulse Looker Studio

---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---

## Dashboard Canvas Architecture
The **OrbitPulse Looker Studio Executive Dashboard** translates complex satellite telemetry into interactive visual indicators designed for network operation directors and engineering leads.

---

## Visual Component Reference & Data Story

### 1. Header Banner & Global Control Bar
* **Controls:** Filter by `Device Model`, `Service Type`, and `Session Date`.
* **Story:** Enables cross-functional teams to isolate performance across specific hardware (e.g., iPhone 17 Pro vs. Apple Watch Ultra 2) or messaging types.

### 2. Executive KPI Scorecards
* **Total Connection Sessions (`100,000`):** Confirms complete data capture over the 31-day monitoring window.
* **Avg Handshake Latency (`1,074.54 ms`):** Volume-weighted average latency across all global handshakes.
* **SLA Degraded Session Rate (`11.28%`):** Tracks overall business SLA compliance ($>1,200\text{ ms}$ latency or $>5\%$ packet loss).
* **ML Flagged Anomalies (`3.00%`):** Quantifies multi-variate statistical anomalies detected by machine learning.

### 3. Time-Series Line Chart: `Daily Latency Trend by Firmware`
* **X-Axis:** `session_date` | **Y-Axis:** `avg_latency_ms` | **Breakdown:** `firmware_version`
* **Data Story:** Visually isolates `v18.2.0-b2` as a sustained top-line orange curve ($\sim 1,510\text{ ms}$) hovering far above stable builds `v18.1.0` and `v18.2.1` ($\sim 887\text{ ms}$), proving the regression was constant throughout August.

### 4. Heatmap Table: `Packet Drop Rate by Ground Station`
* **Dimension:** `ground_station_id` | **Metric:** `packet_drop_rate` (Formatted as %)
* **Data Story:** Displays metric conditional heat-shading, instantly highlighting `GS-CA-B` in dark blue at **14.12%**, compared to 6.97%–7.00% across remaining stations.

### 5. Detail Table: `Flagged Session Anomalies`
* **Dimensions:** `session_date`, `device_model`, `timestamp`, `handshake_latency_ms`, `packet_drop_rate`
* **Filter:** `is_anomaly = 1`
* **Data Story:** Provides granular session level verification (`1-100 / 3000` records), showing extreme failure instances (e.g., drop rates reaching 93.01%).
