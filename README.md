# OrbitPulse: Apple Satellite Connectivity Telemetry & Anomaly Engine

---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---

![GCP BigQuery](https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4?style=flat\&logo=google-cloud\&logoColor=white)
![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat\&logo=python\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ML-Isolation_Forest-F7931E?style=flat\&logo=scikit-learn\&logoColor=white)
![Looker Studio](https://img.shields.io/badge/BI-Looker_Studio-4285F4?style=flat\&logo=google\&logoColor=white)

## Executive Overview

**OrbitPulse** is an enterprise-grade telemetry analytics pipeline and machine learning engine designed to monitor, evaluate, and optimize non-terrestrial satellite connectivity across Apple hardware devices (iPhone 15 Pro, iPhone 16 Pro, iPhone 17 Pro, and Apple Watch Ultra 2).

By synthesizing 100,000 real-time handshake events across August 2026, this system isolates critical operational bottlenecks:

1. **Software Build Regression:** Candidate firmware `v18.2.0-b2` introduced a statistically significant latency spike (+70.2% increase over baseline).
2. **Infrastructure Failure:** Ground station `GS-CA-B` experienced severe packet loss (14.12% drop rate vs. 6.98% fleet baseline).
3. **Automated Defect Flagging:** An Unsupervised Isolation Forest model isolated 3,000 extreme multi-variate anomalies (3.00% anomaly rate).

---

## System Architecture

```text
┌─────────────────────────┐       ┌─────────────────────────┐       ┌─────────────────────────┐
│ Synthetic Telemetry Gen │ ────> │ Google BigQuery (GCP)   │ ────> │ Python Analytics / ML   │
│ Python (Pandas/NumPy)   │       │ ETL & SQL Views         │       │ SciPy / Scikit-Learn    │
└─────────────────────────┘       └─────────────────────────┘       └─────────────────────────┘
│                                 │
▼                                 ▼
┌──────────────────────────────────────────────────────────┐
│ Looker Studio Executive QoE & Anomaly Dashboard          │
└──────────────────────────────────────────────────────────┘
```

---

## Key Performance Indicators (KPIs)

| Metric Name                             | Baseline Standard     | Pipeline Measured Value    | SLA Status                   |
| :-------------------------------------- | :-------------------- | :------------------------- | :--------------------------- |
| **Total Evaluated Sessions**            | 100,000 Handshakes    | 100,000 Sessions           | Complete                     |
| **Mean Handshake Latency**              | $\le 1,000\text{ ms}$ | **1,074.54 ms**            | Breach (Software Regression) |
| **Average Signal-to-Noise Ratio (SNR)** | $\ge 12.00\text{ dB}$ | **12.50 dB**               | Compliant                    |
| **Average Packet Drop Rate**            | $\le 5.00%$           | **8.75%**                  | Breach (Gateway Failure)     |
| **SLA Degraded Session Rate**           | $< 5.00%$             | **11.28%**                 | Action Required              |
| **ML Flagged Anomaly Rate**             | $3.00%$ Target        | **3.00% (3,000 Sessions)** | Isolated                     |

---

## Statistical Diagnostics & Hypothesis Testing

Welch’s Two-Sample t-Test was performed to compare candidate firmware `v18.2.0-b2` against stable production release `v18.2.1`:

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{N_1} + \frac{s_2^2}{N_2}}}
$$

* **Null Hypothesis ($H_0$):** Mean handshake latency for `v18.2.0-b2` equals stable release `v18.2.1`.
* **Alternative Hypothesis ($H_1$):** Mean handshake latency for `v18.2.0-b2` is significantly higher than `v18.2.1`.
* **Results:**

  * Candidate Build (`v18.2.0-b2`): $\mu = 1,510.06\text{ ms}$, $\sigma = 1,123.17\text{ ms}$ ($n = 30,075$)
  * Stable Build (`v18.2.1`): $\mu = 887.22\text{ ms}$, $\sigma = 111.72\text{ ms}$ ($n = 40,169$)
  * **Test Statistic ($t$):** $95.68$ | **p-value:** $0.0000$ ($p < 0.001$)
* **Conclusion:** Reject $H_0$. Candidate firmware build `v18.2.0-b2` demonstrates a statistically significant performance degradation and must be blocked from production deployment.

---

## Repository Contents

* `/sql/`: Production BigQuery DDL/DML scripts for tables, cleaning transformations, median imputation, and executive aggregation views.
* `/python/`: Source code for synthetic data simulation, SNR median imputation, statistical hypothesis testing, and Scikit-Learn Isolation Forest execution.
