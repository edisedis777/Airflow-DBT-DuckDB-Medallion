{% macro get_source(source_name, table_name) %}
    {{ source(source_name, table_name) }}
{% endmacro %}
