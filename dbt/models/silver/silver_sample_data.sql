{{ config(materialized='table') }}

SELECT
    id,
    {{ standardize_column_names('name') }} AS name,
    value * 10 AS adjusted_value
FROM {{ source('public', 'sample_data') }}
