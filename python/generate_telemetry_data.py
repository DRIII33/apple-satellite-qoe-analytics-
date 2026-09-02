"""
OrbitPulse: Synthetic Telemetry Data Generator
Author: Daniel Rodriguez III
Description: Generates 100,000 realistic satellite connectivity telemetry records 
             with injected firmware latency regressions and ground station failures.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_satellite_telemetry(num_records=100000, seed=42):
    np.random.seed(seed)
    
    start_date = datetime(2026, 8, 1)
    timestamps = [start_date + timedelta(seconds=int(x)) for x in np.random.randint(0, 31*86400, num_records)]
    timestamps.sort()
    
    devices = ['iPhone 15 Pro', 'iPhone 16 Pro', 'iPhone 17 Pro', 'Watch Ultra 2']
    device_probs = [0.25, 0.30, 0.30, 0.15]
    
    firmware_versions = ['v18.1.0', 'v18.2.0-b2', 'v18.2.1']
    firmware_probs = [0.30, 0.30, 0.40]
    
    satellites = [f'GS-LEO-{i:02d}' for i in range(1, 31)]
    ground_stations = ['GS-CA-B', 'GS-TX-A', 'GS-FL-C', 'GS-OR-D']
    service_types = ['Emergency_SOS', 'FindMy_Ping', 'Messages_Satellite', 'Voice_Telemetry']
    
    device_choice = np.random.choice(devices, p=device_probs, size=num_records)
    firmware_choice = np.random.choice(firmware_versions, p=firmware_probs, size=num_records)
    satellite_choice = np.random.choice(satellites, size=num_records)
    station_choice = np.random.choice(ground_stations, size=num_records)
    service_choice = np.random.choice(service_types, size=num_records)
    
    elevation = np.random.uniform(15.0, 85.0, size=num_records)
    snr = np.random.normal(loc=13.0, scale=3.5, size=num_records)
    
    # SNR Null injection (2.5%)
    null_mask = np.random.rand(num_records) < 0.025
    snr[null_mask] = np.nan
    
    # Latency modeling (Injected v18.2.0-b2 regression)
    base_latency = np.random.normal(loc=885.0, scale=110.0, size=num_records)
    regression_mask = (firmware_choice == 'v18.2.0-b2')
    base_latency[regression_mask] += np.random.exponential(scale=625.0, size=regression_mask.sum())
    base_latency = np.clip(base_latency, 350.0, 4800.0)
    
    # Packet drop rate modeling (Injected GS-CA-B failure)
    base_drop = np.random.beta(a=2, b=25, size=num_records)
    station_mask = (station_choice == 'GS-CA-B')
    base_drop[station_mask] += np.random.beta(a=2, b=10, size=station_mask.sum())
    base_drop = np.clip(base_drop, 0.0, 0.95)
    
    df = pd.DataFrame({
        'session_id': [f'SES-{i:06d}' for i in range(100000, 100000 + num_records)],
        'timestamp': [t.strftime('%Y-%m-%d %H:%M:%S+00:00') for t in timestamps],
        'device_model': device_choice,
        'firmware_version': firmware_choice,
        'satellite_id': satellite_choice,
        'ground_station_id': station_choice,
        'service_type': service_choice,
        'snr_db': np.round(snr, 2),
        'elevation_degrees': np.round(elevation, 1),
        'handshake_latency_ms': np.round(base_latency, 0),
        'packet_drop_rate': np.round(base_drop, 4)
    })
    
    return df

if __name__ == '__main__':
    df = generate_satellite_telemetry()
    df.to_csv('raw_satellite_telemetry.csv', index=False)
    print(f"Generated raw_satellite_telemetry.csv with {len(df)} records.")
