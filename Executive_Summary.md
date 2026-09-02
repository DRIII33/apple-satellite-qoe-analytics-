# Executive Summary: OrbitPulse Satellite Telemetry Engine

---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---

## Objective & Scope
The **OrbitPulse** platform evaluates non-terrestrial satellite handshakes for consumer satellite services (Emergency SOS, Find My Ping, Satellite Messaging, and Voice Telemetry). This study analyzes 100,000 session events generated during August 2026 across major U.S. ground stations (`GS-CA-B`, `GS-TX-A`, `GS-FL-C`, `GS-OR-D`).

---

## Root Cause Analysis & Core Insights

### 1. Firmware Latency Regression (`v18.2.0-b2`)
Analysis of handshake latency by software version revealed a severe performance regression in candidate build `v18.2.0-b2`.
* Stable releases `v18.1.0` ($\mu = 887.24\text{ ms}$) and `v18.2.1` ($\mu = 887.22\text{ ms}$) consistently maintain low latency baselines.
* Candidate build `v18.2.0-b2` recorded a mean latency of **1,510.06 ms**, with degraded sessions reaching peaks up to **4,719 ms**.
* **Impact:** 69.8% of all SLA-degraded sessions originated from devices running build `v18.2.0-b2`.

### 2. Infrastructure Failure at Ground Station `GS-CA-B`
Evaluation of packet loss metrics across ground gateway infrastructure isolated a localized hardware failure:
* Regional stations `GS-TX-A` (7.00%), `GS-OR-D` (6.98%), and `GS-FL-C` (6.97%) operated within expected packet loss bounds.
* Station **`GS-CA-B`** registered an average packet drop rate of **14.12%**—more than double the fleet average.
* **Impact:** `GS-CA-B` accounts for 40.3% of total packet drop volume across the entire satellite footprint.

### 3. Machine Learning Anomaly Detection
An Unsupervised Isolation Forest model evaluated 4 dimensional features (`handshake_latency_ms`, `packet_drop_rate`, `snr_db`, `elevation_degrees`):
* Isolated **3,000 anomalous sessions** (3.00% anomaly rate).
* 2,964 anomalies coincided with SLA-degraded states, while 36 anomalies surfaced high-drop edge cases occurring under high signal-to-noise ratios.

---

## Actionable Recommendations
1. **Immediate Release Hold:** Block software build `v18.2.0-b2` from over-the-air (OTA) deployment. Roll back affected test devices to `v18.2.1`.
2. **Gateway Infrastructure Remediation:** Issue an automated alert to Network Operations Center (NOC) teams to inspect RF hardware, feedlines, and antenna alignment at ground station `GS-CA-B`.
3. **Automated SLA Monitoring:** Embed the Isolation Forest inference engine into BigQuery scheduled queries to automatically flag real-time anomaly clusters.
