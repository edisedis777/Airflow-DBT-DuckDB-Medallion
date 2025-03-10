{% macro cast_to_integer(column_name) %}
    CAST({{ column_name }} AS INTEGER)
{% endmacro %}
