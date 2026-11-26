# Changelog

All notable changes to **MultiField Feature Exploder** are documented in this file.

## [0.1.0] - 2026-11-26

### Added
- Initial QGIS plugin release, based on the personal processing script created by **shenri52**.
- Processing algorithm that creates one output feature for each populated value across the selected membership fields.
- Preservation of the complete source geometry for every generated feature; this operation duplicates features and does not split geometries spatially.
- Retention of non-selected attributes, with selected membership fields replaced by one output field.
- Handling of features for which all selected fields are empty by retaining one output feature with the text value `NULL`.
- Plugin menu entry, toolbar action, and Processing provider integration.
- Compatibility handling for Qt5 and Qt6 field type definitions.
- Automated Python compilation, unit tests, Bandit security scan, and GitHub Actions release-archive workflow.
- French and English documentation with fictional example data.

### Notes
- The plugin requires QGIS 3.28 or later.
- Automated checks do not replace testing inside a running QGIS installation.
