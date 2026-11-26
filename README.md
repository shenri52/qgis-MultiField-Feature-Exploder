# MultiField Feature Exploder

[![QGIS](https://img.shields.io/badge/QGIS-3.28%2B-green)](https://qgis.org/)
[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/shenri52/qgis-MultiField-Feature-Exploder/releases)

## Français

**MultiField Feature Exploder** transforme plusieurs champs d'appartenance en plusieurs entités géographiques. Chaque valeur non vide trouvée dans les champs sélectionnés produit une entité distincte qui reprend exactement la géométrie de l'entité source.

Il s'agit d'une **duplication de géométrie complète**, et non d'un découpage spatial : un polygone communal est reproduit pour chaque organisme auquel la commune appartient.

### Exemple avec des données fictives

**Source**

| COMMUNE | SYNDICAT_AEP1 | SYNDICAT_AEP2 | SYNDICAT_AEP3 |
|---|---|---|---|
| Commune Alpha | Syndicat Bleu | Syndicat Vert | Syndicat Orange |
| Commune Bêta | Syndicat Bleu | *(vide)* | *(vide)* |
| Commune Gamma | *(vide)* | Syndicat Vert | Syndicat Orange |

**Résultat**

| COMMUNE | SYNDICAT |
|---|---|
| Commune Alpha | Syndicat Bleu |
| Commune Alpha | Syndicat Vert |
| Commune Alpha | Syndicat Orange |
| Commune Bêta | Syndicat Bleu |
| Commune Gamma | Syndicat Vert |
| Commune Gamma | Syndicat Orange |

La géométrie de chaque commune est conservée à l'identique pour chacune de ses lignes de résultat. Les champs sélectionnés sont remplacés par un champ de sortie unique ; les autres attributs sont conservés.

### Fonctionnement

- Sélectionner une couche vectorielle (points, lignes ou polygones).
- Sélectionner un ou plusieurs champs indépendants contenant les appartenances.
- Indiquer le nom du champ qui recevra les valeurs extraites.
- Chaque valeur non vide génère une entité de sortie avec la géométrie source.
- Les champs utilisés sont retirés de la sortie et remplacés par le champ de sortie.
- Les autres champs sont conservés.
- Si tous les champs sélectionnés sont vides, une seule entité est conservée avec la valeur `NULL`.
- Les valeurs sont converties en texte dans le champ de sortie.

### Utilisation

L'outil est accessible depuis **Extensions → MultiField Feature Exploder**, depuis son icône dans la barre d'outils et depuis la boîte à outils **Traitements**.

L'action du menu ouvre la boîte de dialogue native de l'algorithme de traitement. L'algorithme est également utilisable dans le modeleur graphique et dans les traitements par lots.

### Installation

1. Téléchargez `multifield_feature_exploder.zip` depuis la page [Releases](https://github.com/shenri52/qgis-MultiField-Feature-Exploder/releases).
2. Dans QGIS, ouvrez **Extensions → Installer/Gérer les extensions → Installer depuis un ZIP**.
3. Sélectionnez l'archive téléchargée.

Le workflow GitHub Actions construit et joint automatiquement l'archive à chaque Release publiée. Il ne publie pas directement le plugin sur le dépôt officiel QGIS : cette publication reste une étape distincte.

### Historique des versions

- **0.1.0** – Première version. Création de l'algorithme de traitement qui génère une entité par valeur renseignée dans les champs sélectionnés, en conservant la géométrie complète de l'entité source. Ajout de l'accès depuis le menu Extensions, la barre d'outils et la boîte à outils Traitements. Prise en charge du modeleur graphique et des traitements par lots.

## English

**MultiField Feature Exploder** transforms several membership columns into separate geographic features. Each non-empty value found in the selected fields creates one output feature with exactly the same geometry as its source feature.

This is **whole-geometry duplication**, not a spatial split: a municipality polygon is copied once for every organization it belongs to.

### Example with fictional data

**Input**

| MUNICIPALITY | WATER_SYNDICATE_1 | WATER_SYNDICATE_2 | WATER_SYNDICATE_3 |
|---|---|---|---|
| Municipality Alpha | Blue Syndicate | Green Syndicate | Orange Syndicate |
| Municipality Beta | Blue Syndicate | *(empty)* | *(empty)* |
| Municipality Gamma | *(empty)* | Green Syndicate | Orange Syndicate |

**Output**

| MUNICIPALITY | SYNDICATE |
|---|---|
| Municipality Alpha | Blue Syndicate |
| Municipality Alpha | Green Syndicate |
| Municipality Alpha | Orange Syndicate |
| Municipality Beta | Blue Syndicate |
| Municipality Gamma | Green Syndicate |
| Municipality Gamma | Orange Syndicate |

Each output row keeps the original municipality geometry unchanged. Selected source fields are replaced by one output field; all other attributes are retained.

### Usage

The tool is available from the **Plugins** menu, its toolbar icon, and the **Processing** toolbox. The menu action opens the native Processing algorithm dialog. The algorithm supports the graphical modeler and batch processing.

### Installation

1. Download `multifield_feature_exploder.zip` from the [Releases page](https://github.com/shenri52/qgis-MultiField-Feature-Exploder/releases).
2. In QGIS, open **Plugins → Manage and Install Plugins → Install from ZIP**.
3. Select the downloaded archive.

The GitHub Actions workflow builds and attaches the archive to every published Release. It does not publish the plugin directly to the official QGIS plugin repository; that upload remains a separate step.

### Version history

- **0.1.0** – Initial release. Added the Processing algorithm that creates one feature for each populated value in the selected fields while preserving the complete source geometry. Added access from the Plugins menu, toolbar and Processing toolbox. Supports the graphical modeler and batch processing.

## License

GPL-2.0-or-later. See [LICENSE](LICENSE).
