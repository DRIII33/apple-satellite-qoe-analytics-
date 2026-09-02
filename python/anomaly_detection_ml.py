"""
OrbitPulse: Machine Learning & Statistical Analysis Engine
Author: Daniel Rodriguez III
Description: Executes median SNR imputation, Welch's t-Test for firmware regression,
             and Unsupervised Isolation Forest anomaly detection.
"""

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.ensemble import IsolationForest

def process_telemetry_analytics(file_path='raw_satellite_telemetry.csv'):
    df = pd.read_csv(file_path)
    
    # 1. Median SNR Imputation
    median_snr = df['snr_db'].median()
    df['snr_db'] = df['snr_db'].fillna(median_snr)
    
    # 2. SLA QoE Classification
    def assign_qoe(row):
        if row['handshake_latency_ms'] > 1200 or row['packet_drop_rate'] > 0.05:
            return 'Degraded'
        elif row['handshake_latency_ms'] <= 900 and row['packet_drop_rate'] <= 0.02:
            return 'Optimal'
        return 'Acceptable'
    
    df['qoe_tier'] = df.apply(assign_qoe, axis=1)
    
    # 3. Welch's t-Test (v18.2.0-b2 vs v18.2.1)
    b2_latency = df[df['firmware_version'] == 'v18.2.0-b2']['handshake_latency_ms']
    v1821_latency = df[df['firmware_version'] == 'v18.2.1']['handshake_latency_ms']
    
    t_stat, p_val = stats.ttest_ind(b2_latency, v1821_latency, equal_var=False)
    print("=== WELCH'S T-TEST RESULTS ===")
    print(f"t-statistic: {t_stat:.4f} | p-value: {p_val:.4e}")
    
    # 4. Isolation Forest Anomaly Detection (Target: 3.0% contamination)
    features = ['handshake_latency_ms', 'packet_drop_rate', 'snr_db', 'elevation_degrees']
    X = df[features]
    
    model = IsolationForest(contamination=0.03, random_state=42, n_jobs=-1)
    df['ml_anomaly_flag'] = model.fit_predict(X)
    df['is_anomaly'] = (df['ml_anomaly_flag'] == -1).astype(int)
    
    # Save outputs
    df.to_csv('fact_satellite_qoe.csv', index=False)
    anomalies = df[df['is_anomaly'] == 1]
    anomalies.to_csv('telemetry_anomalies.csv', index=False)
    
    print("=== ML PIPELINE COMPLETE ===")
    print(f"Total Processed: {len(df)} | Total Anomalies Flagged: {len(anomalies)} ({len(anomalies)/len(df)*100:.2f}%)")

if __name__ == '__main__':
    process_telemetry_analytics()
