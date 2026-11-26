# -*- coding: utf-8 -*-
from qgis.core import QgsProcessingProvider

from .i18n import tr
from .algorithms.exploder import MultiFieldFeatureExploderAlgorithm


class MultiFieldFeatureExploderProvider(QgsProcessingProvider):
    def loadAlgorithms(self):
        self.addAlgorithm(MultiFieldFeatureExploderAlgorithm())

    def id(self):
        return "multifield_feature_exploder"

    def name(self):
        return tr("MultiField Feature Exploder")

    def longName(self):
        return self.name()
