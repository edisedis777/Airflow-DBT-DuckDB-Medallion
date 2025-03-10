select * from {{ ref('example_bronze_model') }} where id is null
