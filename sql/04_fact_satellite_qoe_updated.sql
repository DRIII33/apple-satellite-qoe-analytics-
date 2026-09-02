-- =============================================================================
-- Project: OrbitPulse Satellite Connectivity Telemetry Engine
-- Author: Daniel Rodriguez III
-- Target Engine: Google BigQuery (GCP)
-- Description: Updated Primary Fact View Sourced from BQML Table
-- =============================================================================

CREATE OR REPLACE VIEW `driiiportfolio.satellite_analytics.fact_satellite_qoe` AS
SELECT
    session_id,
    timestamp,
    session_date,
    device_model,
    firmware_version,
    satellite_id,
    ground_station_id,
    service_type,
    snr_db,
    elevation_degrees,
    handshake_latency_ms,
    packet_drop_rate,
    qoe_tier,
    ml_anomaly_flag,
    is_anomaly
FROM `driiiportfolio.satellite_analytics.fact_satellite_qoe_ml`;
