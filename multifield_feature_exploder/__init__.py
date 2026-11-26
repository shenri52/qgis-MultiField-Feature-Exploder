# -*- coding: utf-8 -*-
"""MultiField Feature Exploder QGIS plugin."""


def classFactory(iface):
    from .plugin import MultiFieldFeatureExploderPlugin
    return MultiFieldFeatureExploderPlugin(iface)
