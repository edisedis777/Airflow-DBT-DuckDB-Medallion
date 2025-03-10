{{ config(materialized='table') }}

SELECT
    id,
    name,
    value * 10 AS adjusted_value
FROM {{ source('public', 'sample_data') }}
