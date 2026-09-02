# Looker Studio Dashboard Guide: OrbitPulse Telemetry Command Center
---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---

## Dashboard Overview
The **OrbitPulse Telemetry Command Center** is a high-impact Looker Studio visual interface designed for hardware engineers, telemetry analysts, and executive leadership within Apple's Satellite Connectivity Group. It translates raw underlying BigQuery views (`agg_daily_qoe` and `fact_satellite_qoe`) into real-time visual metrics, performance trends, and statistical alerts.

---

## Core Visual Modules & KPIs

### 1. Primary Header KPIs (Top Scorecards)
* **Total Session Volume (`SUM(total_sessions)`)**: Ingested handshake events over the target operational period.
* **Average Handshake Latency (`avg_latency_ms`)**: Average latency (in ms) across all satellite connection requests.
* **SLA Degraded Session Rate (%)**: Percentage of total sessions failing baseline QoE thresholds ($\text{Handshake Latency} > 2500\text{ ms}$ or $\text{Packet Drop Rate} > 0.25$).
* **ML Anomaly Rate (%)**: Percentage of sessions flagged as statistical outliers by the BigQuery ML PCA model (`ml_anomaly_flag = 1`).

### 2. SLA Performance & Degradation Trends
* **Degraded Session Distribution by Device Model**: Bar chart comparing degradation rates between iPhone generations and Apple Watch Ultra hardware.
* **Daily QoE Tier Breakdown**: Stacked area chart showing relative daily proportions of Optimal vs. Acceptable vs. Degraded connection sessions.

### 3. Machine Learning Anomaly Detection Suite
* **Anomalous vs. Standard Latency Profile**: Dual-axis scatter/line chart overlaying standard operational latency against ML-detected anomaly clusters.
* **Ground Station & Firmware Anomaly Heatmap**: Visual matrix isolating specific ground station IDs or firmware builds driving localized network instability.

---

## User Interaction & Dynamic Filtering
* **Global Date & Time Range Picker**: Allows drill-down analysis into specific orbital events, software release dates, or outage windows.
* **Hardware & Firmware Selectors**: Interactive dropdowns enabling hardware teams to isolate specific device models (`device_model`) or software builds (`firmware_version`) for rapid patch validation.
* **Service Type Filter**: Segregates voice, messaging, and background location payload telemetry.
