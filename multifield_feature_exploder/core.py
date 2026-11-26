# -*- coding: utf-8 -*-
"""Small processing helpers kept independent from QGIS and Qt."""

MISSING_LABEL = "NULL"


def is_empty(value, qgis_null=None):
    """Return True for Python None, QGIS NULL, or whitespace-only values."""
    if value is None:
        return True
    if qgis_null is not None and value == qgis_null:
        return True
    return str(value).strip() == ""


def values_for_feature(feature, field_names, qgis_null=None):
    """Return one text value per populated field, or the NULL sentinel."""
    values = []
    for field_name in field_names:
        value = feature[field_name]
        if not is_empty(value, qgis_null):
            values.append(str(value).strip())
    return values if values else [MISSING_LABEL]


def retained_field_indexes(fields, selected_names):
    """Return source field indexes excluding the selected exploder fields."""
    selected = set(selected_names)
    return [index for index in range(fields.count())
            if fields.at(index).name() not in selected]
