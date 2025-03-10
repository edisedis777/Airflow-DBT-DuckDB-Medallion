{{ config(materialized='table') }}

SELECT
    name,
    SUM(adjusted_value) AS total_adjusted_value
FROM {{ ref('silver_sample_data') }}
GROUP BY name
