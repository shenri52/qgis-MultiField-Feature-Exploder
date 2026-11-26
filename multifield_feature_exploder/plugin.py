# -*- coding: utf-8 -*-
import os

from qgis.PyQt.QtGui import QAction, QIcon
from qgis.core import QgsApplication

from .i18n import tr
from .provider import MultiFieldFeatureExploderProvider


class MultiFieldFeatureExploderPlugin:
    ALGORITHM_ID = (
        "multifield_feature_exploder:"
        "explode_features_by_multiple_fields"
    )

    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.provider = None
        self.menu_name = tr("MultiField Feature Exploder")

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.svg")
        icon = QIcon(icon_path) if os.path.isfile(icon_path) else QIcon()
        self.action = QAction(
            icon,
            tr("Explode features by multiple fields"),
            self.iface.mainWindow(),
        )
        self.action.setObjectName("MultiFieldFeatureExploderAction")
        self.action.setToolTip(tr(
            "Open the MultiField Feature Exploder processing tool"
        ))
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(self.menu_name, self.action)
        self.iface.addToolBarIcon(self.action)

        self.provider = MultiFieldFeatureExploderProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def run(self):
        import processing
        processing.execAlgorithmDialog(self.ALGORITHM_ID, {})

    def unload(self):
        if self.action is not None:
            self.iface.removePluginMenu(self.menu_name, self.action)
            self.iface.removeToolBarIcon(self.action)
            self.action = None
        if self.provider is not None:
            QgsApplication.processingRegistry().removeProvider(self.provider)
            self.provider = None
