# OrbitPulse: Apple Satellite Connectivity Telemetry & Anomaly Engine
---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---


![GCP BigQuery](https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4?style=flat&logo=google-cloud&logoColor=white)
![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ML-Isolation_Forest-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Looker Studio](https://img.shields.io/badge/BI-Looker_Studio-4285F4?style=flat&logo=google&logoColor=white)

## Executive Overview
**OrbitPulse** is an enterprise-grade telemetry analytics pipeline and machine learning engine designed to monitor, evaluate, and optimize non-terrestrial satellite connectivity across Apple hardware devices (iPhone 15 Pro, iPhone 16 Pro, iPhone 17 Pro, and Apple Watch Ultra 2).

By synthesizing 100,000 real-time handshake events across August 2026, this system isolates critical operational bottlenecks:
1. **Software Build Regression:** Candidate firmware `v18.2.0-b2` introduced a statistically significant latency spike (+70.2% increase over baseline).
2. **Infrastructure Failure:** Ground station `GS-CA-B` experienced severe packet loss (14.12% drop rate vs. 6.98% fleet baseline).
3. **Automated Defect Flagging:** An Unsupervised Isolation Forest model isolated 3,000 extreme multi-variate anomalies (3.00% anomaly rate).

---

## System Architecture
