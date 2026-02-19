---
title: "Catalogue des Datasets — IA pour Thermostats Intelligents"
description: "Inventaire exhaustif des datasets publics pour le contrôle HVAC, la prédiction de température, le confort thermique, la détection d'occupation et le Edge AI embarqué"
date_created: 2026-02-19
total_datasets: 85
tags:
  - datasets
  - hvac
  - thermal-comfort
  - occupancy
  - building-energy
  - tinyml
  - edge-ai
sources_searched:
  - Kaggle
  - UCI ML Repository
  - Zenodo
  - IEEE DataPort
  - OpenEI / NREL
  - Harvard Dataverse
  - Pecan Street
  - Nature Scientific Data
  - GitHub Research
  - Data.gov / data.gov.uk
  - EIA
  - IEA
---

# 💾 Catalogue des Datasets — IA pour Thermostats Intelligents

> **Mise à jour :** 2026-02-19 · **Total :** 85+ datasets · **Sources :** Kaggle, UCI, Zenodo, IEEE, OpenEI, NREL, Nature, GitHub…

---

## ⭐ Incontournables — À retenir en priorité

- **[ASHRAE Global Thermal Comfort Database II](https://datadryad.org/dataset/doi:10.6078/D1F671)** (Kaggle + Dryad) — 109 000+ mesures terrain mondiales. Probablement le dataset le plus précieux pour entraîner un modèle de confort thermique personnalisé.
- **[Building Data Genome Project 2](https://github.com/buds-lab/building-data-genome-project-2)** — 3 053 compteurs, 1 636 bâtiments, 2 ans de données horaires. La référence absolue pour la prédiction de charge énergétique.
- **[Sinergym](https://github.com/ugr-sail/sinergym)** — Wrapper OpenAI Gym pour EnergyPlus. L'outil standard de facto pour entraîner des agents DRL HVAC. Absent des papiers les plus anciens mais incontournable aujourd'hui.
- **[MLPerf Tiny Benchmarks](https://github.com/mlcommons/tiny)** — Benchmarks officiels TinyML sur microcontrôleurs. Donnent des baselines officielles pour comparer des modèles embarqués (Visual Wake Words, Anomaly Detection, Keyword Spotting).

---

## 🗺️ Navigation rapide

| Catégorie | Nb | Aller à |
|-----------|-----|---------|
| 🔧 Plateformes de simulation | 6 | [→](#-plateformes-de-simulation--outils) |
| 🏢 Énergie bâtiment & HVAC | 22 | [→](#-énergie-bâtiment--hvac) |
| 👤 Détection d'occupation | 16 | [→](#-détection-doccupation) |
| 🌡️ Confort thermique | 10 | [→](#️-confort-thermique) |
| 🏠 Smart home & IoT | 12 | [→](#-smart-home--iot) |
| ⚡ Désagrégation de charge (NILM) | 10 | [→](#-désagrégation-de-charge-nilm) |
| 🏛️ Benchmarks & gouvernement | 9 | [→](#️-benchmarks--données-gouvernementales) |
| 🔌 Edge AI / TinyML spécifique | 4 | [→](#-edge-ai--tinyml-spécifique) |

---

## 🔧 Plateformes de simulation & outils

> Outils de simulation utilisés comme environnement d'entraînement dans les papiers RL pour HVAC.

| Nom | Lien | Description | Cité dans | Licence |
|-----|------|-------------|-----------|---------|
| **EnergyPlus** | [energyplus.net](https://energyplus.net) | Simulateur de bâtiment de référence (DOE). Utilisé dans presque tous les papiers RL HVAC pour entraîner et valider les agents. Couplable à Python via Gym-Eplus. | wei-2017, du-ddpg-2024, dqn-d3qn-2024, ed-dqn-2023, rl-pid-2025, expert-rl-2025, survey-rl-hvac-2024 *(15 papiers)* | Open Source (BSD) |
| **BCVTB** *(Building Controls Virtual Test Bed)* | [github.com/lbl-srg/bcvtb](https://github.com/lbl-srg/bcvtb) | Plateforme de co-simulation couplant EnergyPlus avec des contrôleurs externes (Python, Modelica, Matlab). | du-ddpg-2024, survey-rl-hvac-2024, octopus-2024, ed-dqn-2023 | BSD |
| **Sinergym** | [github.com/ugr-sail/sinergym](https://github.com/ugr-sail/sinergym) | Environnement OpenAI Gym wrappant EnergyPlus. Standard de facto pour le DRL HVAC. | — *(non cité mais fondamental)* | MIT |
| **Gym-Eplus** | [github.com/jajimer/Gym-Eplus](https://github.com/jajimer/Gym-Eplus) | Alternative Gym pour EnergyPlus, utilisée dans ED-DQN. | ed-dqn-2023 | Open |
| **TRNSYS** | [trnsys.com](https://www.trnsys.com) | Logiciel commercial de simulation thermique dynamique (bâtiments résidentiels & commerciaux). | survey-rl-hvac-2024 | Commercial |
| **BESOS** *(Building Energy Simulation, Optimization & Surrogate Modeling)* | [gitlab.com/energyincities/besos](https://gitlab.com/energyincities/besos) | Python + JupyterHub pour simulation EnergyPlus, analyse paramétrique et modèles surrogates ML. | — | Apache 2.0 |

---

## 🏢 Énergie bâtiment & HVAC

### Datasets majeurs multi-bâtiments

| Nom | Lien | Source | Description | Échelle | Résolution | Cité dans | Licence |
|-----|------|--------|-------------|---------|-----------|-----------|---------|
| **Building Data Genome Project 2 (BDG2)** | [Kaggle](https://www.kaggle.com/datasets/claytonmiller/buildingdatagenomeproject2) · [GitHub](https://github.com/buds-lab/building-data-genome-project-2) | Kaggle / GitHub | **3 053 compteurs d'énergie** (électricité, eau, vapeur, chauffage/refroidissement) provenant de **1 636 bâtiments** non-résidentiels. 2 ans de données horaires (2016-2017). Base du concours ASHRAE Great Energy Predictor III. | 3053 compteurs, 1636 bâtiments | Horaire | — | CC BY 4.0 |
| **ASHRAE Great Energy Predictor III** | [Kaggle](https://www.kaggle.com/c/ashrae-energy-prediction/data) | Kaggle Competition | 1 449 bâtiments, prédiction de consommation d'énergie (électricité, eau chaude, vapeur, eau glacée). Référence pour les modèles de prédiction énergétique. | 1449 bâtiments | Horaire | — | ASHRAE |
| **End-Use Load Profiles (NREL)** | [data.openei.org](https://data.openei.org/s3_viewer) | OpenEI / NREL | **~900 000 modèles de bâtiments** (550K résidentiels ResStock + 350K commerciaux ComStock). Profils de charge par usage final à intervalles de 15 min. | 900K bâtiments | 15 min | — | Domaine public |
| **ResStock 2024** | [resstock.nrel.gov](https://resstock.nrel.gov/datasets) | NREL | 550K+ modèles résidentiels US avec profils de charge, 16 packages de mesures, Hawaï & Alaska inclus. | 550K bâtiments | 15 min | ml-indoor-temp-2025 | Domaine public |
| **ComStock** | [comstock.nrel.gov](https://comstock.nrel.gov) | NREL | 350K+ modèles commerciaux US avec détail HVAC et usages finaux. | 350K bâtiments | 15 min | — | Domaine public |
| **Building Performance Database (BPD)** | [bpd.lbl.gov](https://bpd.lbl.gov) | LBNL | **Plus de 1M d'enregistrements** de bâtiments fédéraux, étatiques, privés, utilitaires. Données de performance énergétique. | 1M+ enreg. | Annuel | survey-rl-hvac-2024 | Open |
| **CBECS 2018** *(Commercial Buildings Energy Consumption Survey)* | [eia.gov/consumption/commercial](https://www.eia.gov/consumption/commercial/data/2018/) | EIA | Données de 5,9M de bâtiments commerciaux US : caractéristiques énergétiques, consommation, dépenses. Référence nationale. | 5.9M bâtiments | Annuel | — | Domaine public |

### Datasets bâtiment unique / expérimental

| Nom | Lien | Source | Description | Durée | Cité dans | Licence |
|-----|------|--------|-------------|-------|-----------|---------|
| **Three-Year Building Operational Performance Dataset** | [Zenodo 5951008](https://zenodo.org/records/5951008) | Zenodo | 3 ans d'un bâtiment de bureau Berkeley : énergie totale et par usage, conditions HVAC, paramètres environnementaux, comptage d'occupants (300+ capteurs). | 3 ans | — | CC BY 4.0 |
| **HVAC Fault Detection Dataset** | [Nature Sci. Data](https://www.nature.com/articles/s41597-023-02197-w) | Nature Sci. Data | **Plus grand dataset public** d'équipements HVAC en états défaillants et normaux. 7 types de systèmes, plusieurs climats. | Variable | — | CC BY 4.0 |
| **Multizone Office Building HVAC Dataset** | [Nature Sci. Data](https://www.nature.com/articles/s41597-022-01858-6) | Nature Sci. Data | Données multi-zones sous différents scénarios opérationnels HVAC avec météo et conditions thermiques. | Variable | — | CC BY 4.0 |
| **RICO** *(Multivariate HVAC Indoor/Outdoor Time-Series)* | [ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S2352340925004081) | ScienceDirect | Séries temporelles multivariées HVAC intérieur/extérieur depuis un bâtiment de test contrôlé dédié. | Variable | — | Open |
| **Honda R&D Smart Building** *(Offenbach, Allemagne)* | [Nature Sci. Data 2025](https://www.nature.com/articles/s41597-025-05186-3) | Nature Sci. Data | **6 ans** (2018-2023) : 72 compteurs d'énergie, 9 compteurs thermiques, station météo, données PV/CHP. | 6 ans | Variable | CC BY 4.0 |
| **Two-Year Ultra-Low Energy Office** | [Nature Sci. Data 2024](https://www.nature.com/articles/s41597-024-03770-7) | Nature Sci. Data | 2 ans énergie, environnement et opérations système pour un bâtiment bureau net-zéro. | 2 ans | Variable | CC BY 4.0 |
| **Pre-Retrofit IEQ & Energy Dataset** *(Syracuse, NY)* | [Nature Sci. Data 2025](https://www.nature.com/articles/s41597-025-05355-4) | Nature Sci. Data | 12 mois haute fréquence, 14 appartements (2 bâtiments), pré-rénovation : énergie, QAI, comportement occupants, météo. | 12 mois | Haute fréquence | — | CC BY 4.0 |
| **I-BLEND** *(Campus-Scale Building Energy)* | [Nature Sci. Data](https://www.nature.com/articles/sdata201915) | Nature Sci. Data | 52 mois, 7 bâtiments campus IIIT-Delhi, résolution 1 min : tension, courant, puissance, fréquence, facteur de puissance, occupation, météo. | 52 mois | 1 min | — | Open |
| **CU-BEMS** *(Smart Building Energy & IAQ)* | [Kaggle](https://www.kaggle.com/datasets/claytonmiller/cubems-smart-building-energy-and-iaq-data) | Kaggle | Consommation d'énergie et qualité de l'air intérieur d'un bâtiment de l'Université du Colorado. | Variable | Variable | — | Open |
| **Multi-Year Campus-Level Smart Meter** | [Nature Sci. Data 2024](https://www.nature.com/articles/s41597-024-04106-1) | Nature Sci. Data | Données long-terme de compteurs intelligents d'un campus académique. | Multi-ans | Variable | — | CC BY 4.0 |
| **Three-Year Building Energy Mgmt & Occupancy Analytics** | [Nature Sci. Data 2022](https://www.nature.com/articles/s41597-022-01257-x) | Nature Sci. Data | 3 ans bâtiment académique avec analytique énergie + occupation. | 3 ans | Variable | — | CC BY 4.0 |
| **UCI Energy Efficiency Dataset** | [UCI](https://archive.ics.uci.edu/dataset/242/energy+efficiency) | UCI | 768 configurations synthétiques prédisant charge chauffage/refroidissement (8 paramètres bâtiment). Référence ML. | — | — | ml-indoor-temp-2025 | CC BY 4.0 |
| **OpenEI Building Data** | [openei.org](https://openei.org) | OpenEI | Données de bâtiments avec profils d'occupation réels et profils énergétiques. | Variable | Variable | dqn-d3qn-2024, du-ddpg-2024 | Open |
| **NREL RSF Measured Data 2011** | [data.openei.org/submissions/358](https://data.openei.org/submissions/358) | OpenEI | Données de performance mesurées depuis le Research Support Facility du NREL. | 2011 | Horaire | — | Open |

---

## 👤 Détection d'occupation

| Nom | Lien | Source | Description | Capteurs | Échantillons | Cité dans | Licence |
|-----|------|--------|-------------|---------|-------------|-----------|---------|
| **UCI Occupancy Detection** | [UCI](https://archive.ics.uci.edu/dataset/357/occupancy+detection) · [Kaggle](https://www.kaggle.com/datasets/robmarkcole/occupancy-detection-data-set-uci) | UCI / Kaggle | Détection d'occupation en bureau via lumière, température, humidité, CO₂. **Référence du domaine.** | T°, HR, lumière, CO₂ | 8 143 train / 12 417 test | barrett-linder-2015 | CC BY 4.0 |
| **Room Occupancy Estimation (UCI)** | [UCI](https://archive.ics.uci.edu/dataset/864/room+occupancy+estimation) | UCI | Estimation d'occupation multi-pièces avec capteurs environnementaux. | Env. multi | Variable | tinyml-esp32-2026 | Open |
| **Room Occupancy Detection (Kaggle IoT)** | [Kaggle](https://www.kaggle.com/datasets/kukuroo3/room-occupancy-detection-data-iot-sensor) | Kaggle | Température, humidité, lumière, CO₂, rapport d'humidité, détection d'occupation via IoT. | T°, HR, lumière, CO₂ | Variable | — | Open |
| **COD — Commercial Occupancy Dataset** | [Zenodo 996587](https://zenodo.org/records/996587) | Zenodo | 9 mois, 3 espaces commerciaux, 90 000+ événements entrée/sortie. Comptage par pièce. | Comptage | 90K+ events | — | Open |
| **Occupancy Presence & Trajectory Dataset** *(Denmark)* | [Zenodo 3451537](https://zenodo.org/records/3451537) | Zenodo | 5,5M de lectures sur 13 jours, espace public de 105 m² au Danemark. | Multi-capteurs | 5.5M | — | Open |
| **Occupancy Detection via Depth Sensor** *(CMU)* | [Zenodo 3404204](https://zenodo.org/records/3404204) | Zenodo | 4 salles CMU (salles de classe & conférence), 6 To de données de profondeur, 4 semaines (2017). | Capteur 3D | 6 To | — | Open |
| **Global Building Occupant Behavior Database** | [Nature Sci. Data 2022](https://www.nature.com/articles/s41597-022-01475-3) | Nature Sci. Data | **34 datasets** de 15 pays, 39 institutions, 10 zones climatiques. Comportement occupant et interactions humain-bâtiment. | Multi | ~34 études | — | Open |
| **High-Fidelity Residential Occupancy Detection** | [Nature Sci. Data 2021](https://www.nature.com/articles/s41597-021-01055-x) | Nature Sci. Data | Détection d'occupation résidentielle haute résolution. | Multi | Variable | — | CC BY 4.0 |
| **Smart Home Sensor Data** *(Université de Picardie)* | [HAL](https://u-picardie.hal.science/hal-04031663/) | HAL / Open | Données réelles d'une maison intelligente avec CO₂, bruit, température, humidité. Utilisé pour entraînement LSTM. | CO₂, bruit, T°, HR | Variable | occupancy-lstm-2023 | Open |
| **ECO Dataset** *(6 foyers suisses)* | [ETH Zurich](https://vs.inf.ethz.ch/res/show.html?what=eco-data) | ETH Zurich | 6 foyers suisses, 8 mois, 1 Hz : consommation agrégée + par prise, occupation depuis capteurs + labellisation manuelle. | Élec. + occupation | 8 mois | — | CC BY 4.0 |
| **Dormitory Retrofit Occupancy & IEQ** | [Nature Sci. Data 2025](https://www.nature.com/articles/s41597-025-05166-7) | Nature Sci. Data | 2 ans avant/après rénovation : comportement occupants, QAI, usage détaillé de l'énergie en dortoirs résidentiels. | QAI + énergie | 2 ans | — | CC BY 4.0 |
| **Indoor Air Quality Dataset China** | [Nature Sci. Data 2023](https://www.nature.com/articles/s41597-023-02640-y) | Nature Sci. Data | 1 an horaire, 100 purificateurs d'air, bâtiments résidentiels chinois : formaldéhyde, PM2.5, COV, T°, HR. | QAI multi | 1 an | — | CC BY 4.0 |
| **IoT Smart Building Dataset** | [Zenodo 12750891](https://zenodo.org/records/12750891) | Zenodo | Capteurs IoT : température, humidité, occupation, consommation dans bâtiment M5. | T°, HR, occ., énergie | Variable | — | Open |
| **Pecan Street Dataport** | [pecanstreet.org](https://www.pecanstreet.org/dataport/) | Pecan Street | 1 000+ foyers, résolution à la minute, données circuit par circuit : électricité, solaire, VE, HVAC. **Référence occupation/usage.** | Circuit-level | 2012+ | — | Académique gratuit |
| **PLEIAData** *(Consommation, HVAC, T°, Météo, Mouvement)* | [Nature Sci. Data 2023](https://www.nature.com/articles/s41597-023-02023-3) | Nature Sci. Data | Bâtiment intelligent : consommation, HVAC, température, météo, détecteurs de mouvement. | Multi | Variable | — | CC BY 4.0 |
| **SMART* Dataset** *(UMass Amherst)* | [UMass](https://lass.cs.umass.edu/projects/smart-energy-and-smart-building.html) | UMass | 3 maisons intelligentes avec énergie à la seconde, circuit par circuit, solaire, T°/HR par pièce, météo extérieure. | Circuit + env. | 2012+ | — | Open |

---

## 🌡️ Confort thermique

| Nom | Lien | Source | Description | Entrées | Nb mesures | Cité dans | Licence |
|-----|------|--------|-------------|---------|-----------|-----------|---------|
| **ASHRAE Global Thermal Comfort Database II** | [Dryad](https://datadryad.org/dataset/doi:10.6078/D1F671) · [Kaggle](https://www.kaggle.com/datasets/claytonmiller/ashrae-global-thermal-comfort-database-ii) | Dryad / Kaggle | **Base de référence mondiale.** 109 033+ entrées de mesures terrain avec données environnementales objectives et évaluations subjectives des occupants. | T°, HR, vit. air, vêtements, activité | 109K+ | cho-mh-lstm-2024, cnn-m-lstm-2025 | ODbL |
| **Thermal Sensation Classification Dataset** | [Zenodo 13884633](https://zenodo.org/records/13884633) | Zenodo | 10 618 lignes : T° air, vitesse air, HR, votes de sensation thermique. Extrait de ASHRAE II. | T°, HR, v_air | 10 618 | — | Open |
| **Longitudinal Personal Thermal Comfort Preference Data** | [Zenodo 5502441](https://zenodo.org/record/5502441) | Zenodo | **1 400+ réponses uniques** de 17 participants dans 3 bâtiments sur plusieurs années. Préférences personnalisées. | Multi | 1400+ | — | Open |
| **OccuTherm** *(Comfort + Body Shape)* | [Zenodo 3363987](https://zenodo.org/records/3363987) | Zenodo | 77 expériences individuelles de confort (CMU + Bosch, financé DOE). Biométrique + thermique. | Biom. + env. | 77 expériences | — | Open |
| **SinBerBEST Personal Comfort Models Dataset** | [GitHub](https://github.com/FedericoTartarini/dorn-longitudinal-tc-study) | GitHub | Étude terrain 180 jours, 20 participants, **1 000+ sondages RHRN** (Right-Here-Right-Now) via montre connectée + variables physiologiques. | Physio + env. | 1000+ | — | Open |
| **Chinese Thermal Comfort Field Measurements** | [Nature Sci. Data 2023](https://www.nature.com/articles/s41597-023-02568-3) | Nature Sci. Data | Mesures terrain complètes de confort thermique depuis la Chine. Complément géographique à ASHRAE II. | Multi | Variable | — | CC BY 4.0 |
| **Berkeley Center for the Built Environment (CBE) Comfort Tool Data** | [comfort.cbe.berkeley.edu](https://comfort.cbe.berkeley.edu) | UC Berkeley | Outil en ligne + données sous-jacentes pour calcul PMV/PPD et confort adaptatif. Référence académique. | T°, HR, v_air | En ligne | barrett-linder-2015, cho-mh-lstm-2024 | Open |
| **HEMStoEC Dataset** *(Home Energy Management → Energy Communities)* | [Zenodo 8096648](https://zenodo.org/records/8096648) | Zenodo | Données HEMS pour test de stratégies de contrôle HVAC et prévision du confort thermique. | HVAC + confort | Variable | — | Open |
| **Innovative Thermal Comfort Modelling Dataset** | [Zenodo 5906118](https://zenodo.org/records/5906118) | Zenodo | Approche physique du bâtiment + ML pour confort thermique intérieur en bureau. | Env. + physique | Variable | — | Open |
| **ASHRAE 55 / ISO 7730 Reference Data** | [ashrae.org](https://www.ashrae.org) | ASHRAE | Standards de référence PMV/PPD pour le confort thermique (pas un dataset mais la base des métriques utilisées). | Standard | — | pmv-drl-2024, cnn-m-lstm-2025, rl-pid-2025 | ASHRAE |

---

## 🏠 Smart home & IoT

| Nom | Lien | Source | Description | Fréquence | Cité dans | Licence |
|-----|------|--------|-------------|----------|-----------|---------|
| **Smart Home Dataset with Weather** | [Kaggle](https://www.kaggle.com/datasets/taranvee/smart-home-dataset-with-weather-information) | Kaggle | 500 910 instances, 18 features électricité + 10 features météo + 1 temporelle. | Variable | — | Open |
| **Open Smart Home IoT/IEQ/Energy** | [Kaggle](https://www.kaggle.com/datasets/claytonmiller/open-smart-home-iotieqenergy-data) | Kaggle | Données IoT, QAI et énergie d'une maison intelligente. Référence pour contrôle thermostat. | Variable | — | Open |
| **Smart Home's Temperature Time Series** *(Compétition)* | [Kaggle](https://www.kaggle.com/competitions/smart-homes-temperature-time-series-forecasting/data) | Kaggle Competition | Compétition de prévision de série temporelle de température dans des maisons intelligentes. Idéal LSTM/DL. | Variable | — | Competition |
| **Temperature Readings IoT Devices** | [Kaggle](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices) | Kaggle | Lectures de capteurs de température IoT. Simple et léger. | Variable | — | Open |
| **Indoor Temperature Prediction** *(Compétition)* | [Kaggle](https://www.kaggle.com/competitions/indoor-temperature-prediction) | Kaggle Competition | Multi-capteurs microclimat + station météo pour prédiction de T° intérieure. | Variable | — | Competition |
| **House Temperature Dataset** | [Kaggle](https://www.kaggle.com/datasets/thanos07/housetemp) | Kaggle | Données de température résidentielle. | Variable | — | Open |
| **Time Series Room Temperature** | [Kaggle](https://www.kaggle.com/datasets/vitthalmadane/ts-temp-1) | Kaggle | Série temporelle de température de pièce. | Variable | — | Open |
| **Smart Home Dataset (Pythonafroz)** | [Kaggle](https://www.kaggle.com/datasets/pythonafroz/smart-home-dataset) | Kaggle | Données capteurs et contrôle maison intelligente. | Variable | — | Open |
| **REFIT Smart Homes Dataset** *(UK, 20 foyers)* | [refitsmarthomes.org](https://www.refitsmarthomes.org/datasets/) | REFIT | 20 foyers UK, 2 ans, résolution 8 secondes : maison entière + 9 appareils. Données qualitatives incluses. | 8 secondes | — | CC BY 4.0 |
| **UK-DALE** *(UK Domestic Appliance-Level Electricity)* | [jack-kelly.com/data](https://jack-kelly.com/data/) | Jack Kelly / UKERC | 5 foyers UK, 16 kHz pour maison entière, 1/6 Hz par appareil. | 1-16 kHz | — | Open |
| **Chiller Energy Data** | [Kaggle](https://www.kaggle.com/datasets/chillerenergy/chiller-energy-data) | Kaggle | Données énergétiques de système HVAC chiller couplées à la météo. | Variable | — | Open |
| **Smart Building System** | [Kaggle](https://www.kaggle.com/datasets/ranakrc/smart-building-system) | Kaggle | Données capteurs et systèmes bâtiment intelligent complet. | Variable | — | Open |

---

## ⚡ Désagrégation de charge (NILM)

> Utile pour identifier la consommation du HVAC depuis la mesure agrégée.

| Nom | Lien | Source | Description | Résolution | Licence |
|-----|------|--------|-------------|-----------|---------|
| **REDD** *(Reference Energy Disaggregation Data Set)* | [redd.csail.mit.edu](http://redd.csail.mit.edu/) · [Kaggle](https://www.kaggle.com/datasets/pawelkauf/redd-part) | MIT CSAIL | **6 foyers US**, plusieurs semaines, 1s agrégé, 3s par appareil, haute fréq. pour 2 foyers. | 1 s | Open |
| **NILMTK** *(Toolkit + Datasets intégrés)* | [github.com/nilmtk/nilmtk](https://github.com/nilmtk/nilmtk) | GitHub | Framework NILM intégrant REDD, UK-DALE, PECAN Street, ECO, etc. en format unifié. | Variable | Apache 2.0 |
| **SynD** *(Synthetic Energy Dataset)* | [github.com/klemenjak/SynD](https://github.com/klemenjak/SynD) | GitHub | 180 jours simulés, foyer avec 21 appareils pour recherche NILM. | Variable | Open |
| **SmartNIALMeter** | [ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S2352340924008187) | ScienceDirect | **20 bâtiments**, 100 appareils électriques, jusqu'à 2 ans à intervalles de 5 secondes. | 5 s | Open |
| **PLAID** *(Plug Load Appliance Identification Dataset)* | [Figshare](https://figshare.com/articles/dataset/PLAID_-_A_Voltage_and_Current_Measurement_Dataset_for_Plug_Load_Appliance_Identification_in_Households/10084619) | Figshare | 1 876 enregistrements d'appareils à 30 kHz, 17 types, 330 marques/modèles, 65 sites (Pittsburgh). | 30 kHz | Open |
| **Smart Meter Electricity Consumption** | [Kaggle](https://www.kaggle.com/datasets/ziya07/smart-meter-electricity-consumption-dataset) | Kaggle | Patterns de consommation compteurs intelligents résidentiels et commerciaux. | Variable | Open |
| **UK Electrical Load (REFIT)** | [Kaggle](https://www.kaggle.com/datasets/kyleahmurphy/uk-electrical-load) | Kaggle | Charge électrique REFIT depuis foyers UK. | 8 s | Open |
| **Pecan Street Circuit-Level** | [pecanstreet.org](https://www.pecanstreet.org/dataport/) | Pecan Street | 1 000+ foyers, minute par minute, niveau circuit : électricité, solaire, VE, **HVAC séparé**. | 1 min | Académique |
| **German Heat Pump Load Profiles** | [ResearchGate](https://www.researchgate.net/publication/358610468) | ResearchGate | Profils de charge électrique et pompe à chaleur depuis bâtiments résidentiels allemands. | Variable | Open |
| **REDD Part (Kaggle)** | [Kaggle](https://www.kaggle.com/datasets/pawelkauf/redd-part) | Kaggle | Extrait REDD formaté pour Kaggle. Idéal pour prototypage rapide. | 1 s | Open |

---

## 🏛️ Benchmarks & données gouvernementales

| Nom | Lien | Source | Pays | Description | Licence |
|-----|------|--------|------|-------------|---------|
| **EIA — Energy Information Administration** | [eia.gov/consumption](https://www.eia.gov/consumption/data.php) | EIA US | 🇺🇸 | Consommation énergétique US complète (bâtiments, industrie, transport) depuis 1990. | Domaine public |
| **NYC Building Energy Disclosure (LL87)** | [opendata.cityofnewyork.us](https://opendata.cityofnewyork.us) | NYC Open Data | 🇺🇸 | Consommation des bâtiments new-yorkais depuis 2012. | Open |
| **UK Energy Performance Certificates (EPC)** | [epc.opendatacommunities.org](https://epc.opendatacommunities.org/) | MHCLG UK | 🇬🇧 | Certificats de performance énergétique d'Angleterre et Pays de Galles. | Open |
| **UK NEED** *(National Energy Efficiency Data Framework)* | [data.gov.uk](https://www.data.gov.uk/dataset/473afefd-9028-48d1-a959-c865c1387a9d/national_energy_efficiency_data-framework_need) | UK Gov. | 🇬🇧 | Consommation énergétique bâtiments résidentiels et non-résidentiels UK (2012-2021). | Open |
| **IEA Energy Efficiency Indicators** | [iea.org](https://www.iea.org/data-and-statistics/data-product/energy-efficiency-indicators) | IEA | 🌍 | Indicateurs d'efficacité énergétique globaux par secteur (mis à jour déc. 2024). | Gratuit |
| **NREL National Solar Radiation Database (NSRDB)** | [nsrdb.nrel.gov](https://nsrdb.nrel.gov/) | NREL | 🇺🇸 | Données météo horaires (TMY) pour simulation bâtiment et HVAC. Référence pour EnergyPlus. | Domaine public |
| **Irish Building Efficiency Retrofit Dataset** | [ScienceDirect 2020](https://www.sciencedirect.com/science/article/pii/S2352340920301414) | Elsevier | 🇮🇪 | Caractéristiques d'efficacité et données de rénovation bâtiments résidentiels irlandais. | Open |
| **Building Fault Detection Dataset (LBNL/ASHRAE RP-1312)** | [data.openei.org/submissions/910](https://data.openei.org/submissions/910) | OpenEI | 🇺🇸 | Datasets pour test d'algorithmes de détection de pannes HVAC. | Open |
| **Engineering Science Building Dataset (MIT)** | [iahmed.me/EngineeringScienceBuilding](https://iahmed.me/EngineeringScienceBuilding/datasets/v1/dataset.html) | MIT | 🇺🇸 | Systèmes et performance d'un bâtiment campus MIT. | Open |

---

## 🔌 Edge AI / TinyML spécifique

> Datasets conçus spécifiquement pour ou utilisés dans des déploiements embarqués.

| Nom | Lien | Source | Description | Hardware cible | Cité dans | Licence |
|-----|------|--------|-------------|--------------|-----------|---------|
| **TinyML Occupancy ESP32 Dataset** | *(voir papier tinyml-esp32-2026)* | ScienceDirect 2026 | CO₂, T°, HR, lumière, PIR depuis ESP32. Random Forest R²=0.923, latence inférence 997 µs. Directement embarqué. | ESP32 | tinyml-esp32-2026 | Open |
| **IoT Smart Building (Edge Odroid N+2)** | [Zenodo 12750891](https://zenodo.org/records/12750891) | Zenodo | Capteurs IoT avec edge computing Odroid N+2. T°, HR, occupation. | Odroid N+2 | — | Open |
| **Edge-IIoTset** *(Cybersécurité IoT/IIoT)* | [Kaggle](https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot) | Kaggle | Données capteurs IoT complètes pour apprentissage fédéré centralisé et décentralisé. | IoT général | — | Open |
| **TinyML Benchmark Datasets** *(MLPerf Tiny)* | [github.com/mlperf/tiny](https://github.com/mlcommons/tiny) | MLCommons | Benchmarks officiels TinyML : Visual Wake Words, Keyword Spotting, Anomaly Detection (DCASE), Image Classification. | MCU générique | tinyml-cities-2025 | Apache 2.0 |

---

## 📊 Synthèse par usage

### Pour la prédiction de température intérieure
> ✅ Recommandés : BDG2 · Smart Home Temperature Kaggle · UCI Energy Efficiency · RICO · CU-BEMS

### Pour la détection d'occupation
> ✅ Recommandés : UCI Occupancy · ECO · SMART* · Smart Home Picardie · COD · TinyML ESP32

### Pour le confort thermique
> ✅ Recommandés : ASHRAE Global TC DB II · SinBerBEST · Longitudinal Comfort Data · OccuTherm

### Pour entraîner un agent DRL HVAC
> ✅ Recommandés : EnergyPlus + Sinergym · ResStock · ComStock · BPD

### Pour déploiement Edge / TinyML
> ✅ Recommandés : TinyML ESP32 2026 · IoT Zenodo 12750891 · MLPerf Tiny

### Pour l'analyse de charge HVAC
> ✅ Recommandés : Pecan Street · REDD · NILMTK · SmartNIALMeter · PLAID

---

## 🔎 Sources explorées

| Plateforme | Nb datasets trouvés | URL |
|-----------|-------------------|-----|
| Kaggle | ~25 | [kaggle.com/datasets](https://www.kaggle.com/datasets) |
| UCI ML Repository | ~5 | [archive.ics.uci.edu](https://archive.ics.uci.edu) |
| Zenodo | ~12 | [zenodo.org](https://zenodo.org) |
| Nature Scientific Data | ~18 | [nature.com/sdata](https://www.nature.com/sdata/) |
| OpenEI / NREL | ~8 | [data.openei.org](https://data.openei.org) |
| Pecan Street | 1 (large) | [pecanstreet.org](https://www.pecanstreet.org/dataport/) |
| GitHub Research | ~6 | [github.com](https://github.com) |
| IEEE DataPort | En exploration | [ieee-dataport.org](https://ieee-dataport.org) |
| Gouvernements (UK, US, IEA) | ~7 | Multiples |
| ScienceDirect / Elsevier | ~5 | [sciencedirect.com](https://www.sciencedirect.com) |

---

*Catalogue généré le 2026-02-19 — Recherche exhaustive sur 10+ plateformes publiques*
