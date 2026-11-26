# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QCoreApplication, QMetaType, QVariant
from qgis.core import (
    NULL,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterField,
    QgsProcessingParameterString,
    QgsProcessingParameterFeatureSink,
    QgsFields,
    QgsField,
    QgsFeature,
)

from .. import core


class MultiFieldFeatureExploderAlgorithm(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    FIELDS = "FIELDS"
    OUTPUT_FIELD = "OUTPUT_FIELD"
    OUTPUT = "OUTPUT"

    def tr(self, text):
        return QCoreApplication.translate("MultiFieldFeatureExploder", text)

    def createInstance(self):
        return MultiFieldFeatureExploderAlgorithm()

    def name(self):
        return "explode_features_by_multiple_fields"

    def displayName(self):
        return self.tr("Explode features by multiple fields")

    def group(self):
        return "MultiField Feature Exploder"

    def groupId(self):
        return "multifield_feature_exploder"

    def shortHelpString(self):
        return self.tr(
            "Creates one output feature for each non-empty value found in the "
            "selected fields. The source geometry and all non-selected attributes "
            "are copied unchanged. The selected fields are replaced by one text "
            "field. If every selected field is empty, one feature is kept with "
            "the value 'NULL'. This duplicates whole geometries; it does not "
            "split polygons or other geometries spatially."
        )

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT,
            self.tr("Input layer"),
            [QgsProcessing.TypeVectorAnyGeometry],
        ))
        self.addParameter(QgsProcessingParameterField(
            self.FIELDS,
            self.tr("Fields containing the memberships to explode"),
            parentLayerParameterName=self.INPUT,
            allowMultiple=True,
        ))
        self.addParameter(QgsProcessingParameterString(
            self.OUTPUT_FIELD,
            self.tr("Name of the output field"),
            defaultValue="membership",
        ))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT,
            self.tr("Exploded features"),
        ))

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsSource(parameters, self.INPUT, context)
        if source is None:
            raise QgsProcessingException(self.tr("Please select a valid input layer."))

        selected_fields = self.parameterAsFields(parameters, self.FIELDS, context)
        if not selected_fields:
            raise QgsProcessingException(self.tr("Select at least one field to explode."))

        output_field = self.parameterAsString(
            parameters, self.OUTPUT_FIELD, context
        ).strip()
        if not output_field:
            raise QgsProcessingException(self.tr("Enter a name for the output field."))

        source_fields = source.fields()
        source_names = {source_fields.at(i).name()
                        for i in range(source_fields.count())}
        if any(name not in source_names for name in selected_fields):
            raise QgsProcessingException(self.tr("One or more selected fields do not exist."))

        retained_indexes = core.retained_field_indexes(source_fields, selected_fields)
        retained_names = {source_fields.at(index).name()
                          for index in retained_indexes}
        if output_field in retained_names:
            raise QgsProcessingException(self.tr(
                "The output field already exists among the fields that will be kept. "
                "Choose another name."
            ))

        output_fields = QgsFields()
        for index in retained_indexes:
            output_fields.append(source_fields.at(index))

        # QMetaType.Type.QString is the Qt6 form; QVariant.String is retained
        # as a fallback for QGIS builds using Qt5.
        qstring_type = getattr(getattr(QMetaType, "Type", QMetaType), "QString", None)
        if qstring_type is None:
            qstring_type = QVariant.String
        output_fields.append(QgsField(output_field, qstring_type))

        sink, destination_id = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            output_fields,
            source.wkbType(),
            source.sourceCrs(),
        )
        if sink is None:
            raise QgsProcessingException(self.tr("Could not create the output layer."))

        total = source.featureCount()
        for feature_index, source_feature in enumerate(source.getFeatures()):
            if feedback.isCanceled():
                break

            values = core.values_for_feature(source_feature, selected_fields, NULL)
            retained_attributes = source_feature.attributes()
            output_attributes = [retained_attributes[index]
                                 for index in retained_indexes]

            for value in values:
                output_feature = QgsFeature(output_fields)
                output_feature.setGeometry(source_feature.geometry())
                output_feature.setAttributes(output_attributes + [value])
                if not sink.addFeature(output_feature):
                    raise QgsProcessingException(
                        self.tr("Could not write an exploded feature to the output layer.")
                    )

            if total:
                feedback.setProgress(int((feature_index + 1) * 100 / total))

        feedback.pushInfo(self.tr(
            "Exploded {0} selected field(s) into the output field '{1}'."
        ).format(len(selected_fields), output_field))
        return {self.OUTPUT: destination_id}
