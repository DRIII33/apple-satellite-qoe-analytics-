-- =============================================================================
-- Project: OrbitPulse Satellite Connectivity Telemetry Engine
-- Author: Daniel Rodriguez III
-- Target Engine: Google BigQuery (GCP)
-- Description: Raw Table DDL Definition for Ingested Telemetry Data
-- =============================================================================

CREATE TABLE IF NOT EXISTS `driiiportfolio.satellite_analytics.raw_telemetry` (
    session_id STRING OPTIONS(description="Unique handshake session identifier"),
    timestamp TIMESTAMP OPTIONS(description="UTC timestamp of connection attempt"),
    device_model STRING OPTIONS(description="Hardware hardware generation"),
    firmware_version STRING OPTIONS(description="Installed software release build"),
    satellite_id STRING OPTIONS(description="LEO Satellite vehicle ID"),
    ground_station_id STRING OPTIONS(description="Receiving ground gateway station"),
    service_type STRING OPTIONS(description="Satellite application service type"),
    snr_db FLOAT64 OPTIONS(description="Signal-to-Noise ratio in dB (contains nulls)"),
    elevation_degrees FLOAT64 OPTIONS(description="Satellite elevation angle in degrees"),
    handshake_latency_ms FLOAT64 OPTIONS(description="Connection latency in milliseconds"),
    packet_drop_rate FLOAT64 OPTIONS(description="Ratio of lost telemetry packets (0.0 to 1.0)")
);
