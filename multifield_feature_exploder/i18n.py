# -*- coding: utf-8 -*-
"""Small system-locale based translations for the plugin interface."""

from qgis.PyQt.QtCore import QLocale


_FR = {
    "MultiField Feature Exploder": "Décomposition multi-champs",
    "Explode features by multiple fields": "Décomposer les entités selon plusieurs champs",
    "Open the MultiField Feature Exploder processing tool":
        "Ouvrir l'outil de décomposition multi-champs",
    "Input layer": "Couche source",
    "Fields containing the memberships to explode":
        "Champs contenant les appartenances à décomposer",
    "Name of the output field": "Nom du champ de sortie",
    "Exploded features": "Entités décomposées",
    "Creates one output feature for each non-empty value found in the selected fields. "
    "The source geometry and all non-selected attributes are copied unchanged. "
    "The selected fields are replaced by one text field. If every selected field is "
    "empty, one feature is kept with the value 'NULL'. This duplicates whole "
    "geometries; it does not split polygons or other geometries spatially.":
        "Crée une entité de sortie pour chaque valeur non vide trouvée dans les champs "
        "sélectionnés. La géométrie source et tous les attributs des autres champs sont "
        "copiés à l'identique. Les champs sélectionnés sont remplacés par un seul champ "
        "texte. Si tous les champs sélectionnés sont vides, une entité est conservée "
        "avec la valeur « NULL ». Cette opération duplique les géométries complètes ; "
        "elle ne découpe pas spatialement les polygones ni les autres géométries.",
    "Please select a valid input layer.": "Veuillez sélectionner une couche source valide.",
    "Select at least one field to explode.":
        "Sélectionnez au moins un champ à décomposer.",
    "Enter a name for the output field.": "Saisissez un nom pour le champ de sortie.",
    "One or more selected fields do not exist.":
        "Un ou plusieurs champs sélectionnés n'existent pas.",
    "The output field already exists among the fields that will be kept. "
    "Choose another name.":
        "Le champ de sortie existe déjà parmi les champs conservés. "
        "Choisissez un autre nom.",
    "Could not create the output layer.": "Impossible de créer la couche de sortie.",
    "Could not write an exploded feature to the output layer.":
        "Impossible d'écrire une entité décomposée dans la couche de sortie.",
    "Exploded {0} selected field(s) into the output field '{1}'.":
        "{0} champ(s) sélectionné(s) traité(s) dans le champ de sortie « {1} ».",
}


def tr(text):
    """Translate a source string when the computer's system locale is French."""
    if QLocale.system().name().lower().startswith("fr"):
        return _FR.get(text, text)
    return text
