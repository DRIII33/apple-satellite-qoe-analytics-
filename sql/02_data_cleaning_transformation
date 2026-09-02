-- =============================================================================
-- Project: OrbitPulse Satellite Connectivity Telemetry Engine
-- Author: Daniel Rodriguez III
-- Target Engine: Google BigQuery (GCP)
-- Description: Base Data Cleaning, Partitioned Median Imputation, & QoE Tiering
-- =============================================================================

CREATE OR REPLACE VIEW `driiiportfolio.satellite_analytics.fact_satellite_qoe` AS
WITH ImputedData AS (
    SELECT
        session_id,
        timestamp,
        DATE(timestamp) AS session_date,
        device_model,
        firmware_version,
        satellite_id,
        ground_station_id,
        service_type,
        -- Impute missing SNR using device model median
        COALESCE(snr_db, PERCENTILE_CONT(snr_db, 0.5) OVER(PARTITION BY device_model)) AS snr_db,
        elevation_degrees,
        handshake_latency_ms,
        packet_drop_rate,
        -- Calculate Quality of Experience (QoE) Score Flag
        CASE 
            WHEN handshake_latency_ms > 2500 OR packet_drop_rate > 0.25 THEN 'Degraded'
            WHEN handshake_latency_ms > 1500 OR packet_drop_rate > 0.10 THEN 'Acceptable'
            ELSE 'Optimal'
        END AS qoe_tier
    FROM `driiiportfolio.satellite_analytics.raw_telemetry`
)
SELECT * FROM ImputedData;
