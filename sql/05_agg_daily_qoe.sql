-- =============================================================================
-- Project: OrbitPulse Satellite Connectivity Telemetry Engine
-- Author: Daniel Rodriguez III
-- Target Engine: Google BigQuery (GCP)
-- Description: Executive Aggregation View with SLA & Machine Learning Metrics
-- =============================================================================

CREATE OR REPLACE VIEW `driiiportfolio.satellite_analytics.agg_daily_qoe` AS
SELECT
  session_date,
  device_model,
  firmware_version,
  ground_station_id,
  service_type,
  COUNT(session_id) AS total_sessions,
  AVG(handshake_latency_ms) AS avg_latency_ms,
  AVG(snr_db) AS avg_snr_db,
  AVG(packet_drop_rate) AS avg_packet_drop_rate,
  COUNTIF(qoe_tier = 'Degraded') AS degraded_session_count,
  SAFE_DIVIDE(COUNTIF(qoe_tier = 'Degraded'), COUNT(session_id)) * 100 AS degraded_session_pct,
  -- Add ML anomaly aggregations:
  COUNTIF(is_anomaly = 1) AS anomaly_session_count,
  SAFE_DIVIDE(COUNTIF(is_anomaly = 1), COUNT(session_id)) * 100 AS anomaly_session_pct
FROM `driiiportfolio.satellite_analytics.fact_satellite_qoe`
GROUP BY 1, 2, 3, 4, 5;
