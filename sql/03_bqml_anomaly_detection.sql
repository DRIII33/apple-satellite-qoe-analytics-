-- =============================================================================
-- Project: OrbitPulse Satellite Connectivity Telemetry Engine
-- Author: Daniel Rodriguez III
-- Target Engine: Google BigQuery ML (BQML)
-- Description: Materialized Anomaly Detection Table Generation via ML.DETECT_ANOMALIES
-- =============================================================================

CREATE OR REPLACE TABLE `driiiportfolio.satellite_analytics.fact_satellite_qoe_ml` AS
SELECT
  * EXCEPT(mean_squared_error),

  -- Standardize the BigQuery ML boolean anomaly flag into an integer
  -- for compatibility with the reporting schema and easier aggregation
  -- in downstream dashboards.
  CASE
    WHEN is_anomaly THEN 1
    ELSE 0
  END AS ml_anomaly_flag

FROM
  -- Apply the pre-trained PCA-based anomaly detection model to each
  -- session in the source fact table.
  -- The model evaluates multiple network-quality dimensions simultaneously,
  -- including SNR, handshake latency, and packet drop rate, to identify
  -- sessions that deviate from learned normal network behavior.
  ML.DETECT_ANOMALIES(

    -- Reference the pre-trained QoE anomaly detection model.
    MODEL `driiiportfolio.satellite_analytics.qoe_anomaly_model`,

    -- Set contamination to 0.01, indicating that approximately 1% of
    -- sessions are expected to represent statistical anomalies.
    STRUCT(0.01 AS contamination),

    -- Use the existing fact_satellite_qoe table as the input dataset.
    -- This table contains cleaned telemetry data and initial qoe_tier
    -- classifications for each session.
    TABLE `driiiportfolio.satellite_analytics.fact_satellite_qoe`

  );
