# -*- coding: utf-8 -*-
import unittest

from multifield_feature_exploder import core


class FakeFeature:
    def __init__(self, attributes):
        self.attributes = attributes

    def __getitem__(self, field_name):
        return self.attributes[field_name]


class FakeField:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class FakeFields:
    def __init__(self, names):
        self._fields = [FakeField(name) for name in names]

    def count(self):
        return len(self._fields)

    def at(self, index):
        return self._fields[index]


class CoreTests(unittest.TestCase):
    def test_empty_values(self):
        qgis_null = object()
        self.assertTrue(core.is_empty(None, qgis_null))
        self.assertTrue(core.is_empty(qgis_null, qgis_null))
        self.assertTrue(core.is_empty("   ", qgis_null))
        self.assertFalse(core.is_empty("Syndicate Blue", qgis_null))

    def test_values_are_exploded_independently(self):
        feature = FakeFeature({
            "COMMUNE": "Commune Alpha",
            "SYNDICAT_AEP1": "Syndicat Bleu",
            "SYNDICAT_AEP2": "Syndicat Vert",
            "SYNDICAT_AEP3": "",
        })
        self.assertEqual(
            core.values_for_feature(
                feature,
                ["SYNDICAT_AEP1", "SYNDICAT_AEP2", "SYNDICAT_AEP3"],
            ),
            ["Syndicat Bleu", "Syndicat Vert"],
        )

    def test_all_empty_fields_keep_one_null_value(self):
        feature = FakeFeature({"A": None, "B": "  "})
        self.assertEqual(core.values_for_feature(feature, ["A", "B"]), ["NULL"])

    def test_retained_fields_exclude_selected_fields(self):
        fields = FakeFields(["COMMUNE", "SYNDICAT_AEP1", "CODE", "SYNDICAT_AEP2"])
        self.assertEqual(
            core.retained_field_indexes(fields, ["SYNDICAT_AEP1", "SYNDICAT_AEP2"]),
            [0, 2],
        )


if __name__ == "__main__":
    unittest.main()
