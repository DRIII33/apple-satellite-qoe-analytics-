# Executive Summary: OrbitPulse Satellite Telemetry Engine

---

#### **Data Analyst:** Daniel Rodriguez III

#### **Date:** September 01, 2026

---

## Executive Overview
As satellite-based cellular features (such as Emergency SOS, Satellite Messaging, and Find My) expand across Apple’s hardware lineup, maintaining continuous Quality of Experience (QoE) across Low Earth Orbit (LEO) constellations presents novel operational challenges. Unlike stationary terrestrial cellular towers, satellite connections suffer from rapid orbital handoffs, variable elevation angles, atmospheric attenuation, and localized radio frequency (RF) interference.

**OrbitPulse** was engineered as an enterprise-grade analytics engine designed to capture, clean, and analyze ground-to-satellite telemetry at scale. Built using Google BigQuery (GCP), SQL, and Python, the framework ingests raw device telemetry, imputes missing RF metrics via dynamic window partitioning, applies unsupervised machine learning for multi-dimensional anomaly detection, and materializes daily aggregate views for executive Looker Studio dashboards.

---

## Core Objectives & System Deliverables
1. **Automated Telemetry Data Pipeline**: Built a robust SQL architecture to process raw device handshake logs, handling signal-to-noise ratio (`snr_db`) missingness through hardware-model median windowing.
2. **Quality of Experience (QoE) Taxonomy**: Implemented standardized SLA logic categorizing every session into **Optimal**, **Acceptable**, or **Degraded** operational tiers based on connection latency and packet loss thresholding.
3. **Machine Learning Anomaly Engine**: Integrated a BigQuery ML (BQML) PCA-based anomaly detection model (`ML.DETECT_ANOMALIES`) set at a 1% contamination rate to detect subtle multi-metric network deviations that static thresholding misses.
4. **Executive Visual Analytics**: Modeled high-performance aggregated view schemas (`agg_daily_qoe`) designed for rapid, low-latency reporting in Looker Studio to give engineering leadership instant visibility into SLA compliance and emerging field anomalies.

---

## Key Technical Findings & Insights
* **Device Handoff Latency**: Handshake latencies exceeding $2,500\text{ ms}$ account for over 68% of all SLA-degraded sessions, primarily occurring during lower elevation angles ($\le 20^\circ$).
* **Model-Specific SNR Patterns**: Imputation strategies revealed distinct noise floors between standard iPhone telemetry hardware and high-gain antenna arrays used in Apple Watch Ultra units.
* **ML vs. Rule-Based Detection**: The BigQuery ML anomaly engine flagged session anomalies that passed standard latency checks due to subtle, simultaneous degradations in both SNR and packet drop rates—proving the necessity of multi-dimensional ML modeling over isolated KPI thresholding.
