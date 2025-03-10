{% macro standardize_column_names(column_name) %}
    {%- set clean_name = column_name | replace(' ', '_') | lower -%}
    {{ clean_name }}
{% endmacro %}
