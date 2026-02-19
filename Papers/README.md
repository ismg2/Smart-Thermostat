# 📚 Bibliothèque — IA pour Thermostats Intelligents

> **Domaine :** Edge AI · Reinforcement Learning · CNN/LSTM · HVAC embarqué
> **Mise à jour :** 2026-02-19 · **Total :** 27 articles · **Couverture :** 2015–2026

---

## 🗂️ Structure des dossiers

```
Papers/
├── README.md              ← Ce fichier : guide de navigation
├── INDEX.md               ← Index détaillé par catégorie et pertinence
├── 2015/
│   └── barrett-linder-autonomous-hvac-rl/
├── 2016/
│   └── deepmind-datacenter-cooling-40pct/
├── 2017/
│   └── wei-deep-rl-building-hvac/         ← PAPIER SÉMINAL ⭐
├── 2018/
│   └── deepmind-safety-first-cooling/
├── 2019/
│   └── dqn-hvac-energyplus/
├── 2020/
│   ├── gupta-dqn-energy-efficient-heating/
│   ├── hosseinloo-mit-event-triggered-rl/  ← Très pertinent Edge ⭐
│   └── lstm-indoor-temp-prediction/
├── 2021/
│   └── cnn-lstm-predictive-indoor-temp/
├── 2022/
│   └── schizas-tinyml-iot-review/
├── 2023/
│   ├── ed-dqn-event-driven-hvac/           ← Très pertinent Edge ⭐
│   ├── setpoint-preference-learning-rl/
│   └── occupancy-lstm-optimized/
├── 2024/
│   ├── survey-rl-hvac-intelligent-buildings/ ← SURVEY de référence ⭐
│   ├── du-ddpg-multizone-residential/
│   ├── drl-pmv-dynamic-comfort/
│   ├── cho-mh-lstm-personalized-comfort/
│   ├── dqn-d3qn-hvac-comparison/
│   └── octopus-holistic-building-drl/
├── 2025/
│   ├── rl-vs-pid-hvac-simulation/
│   ├── efficient-rl-expert-guided-hvac/
│   ├── ml-indoor-temp-lightweight/         ← Modèle 50k params ⭐
│   ├── bayesian-cnn-m-lstm-comfort/
│   ├── digital-twin-lstm-hvac/
│   └── edge-intelligence-tinyml-cities/
└── 2026/
    ├── tinyml-occupancy-esp32/             ← ESP32 997µs ⭐
    └── sustainability-tiny-deep-learning/  ← Sub-kilobyte ⭐
```

---

## 🔍 Recherche dans Obsidian

### Par propriété YAML (Dataview)

```dataview
TABLE authors, year, relevance, category
FROM "Papers"
WHERE read = false
SORT relevance DESC, year DESC
```

```dataview
TABLE year, methods, hardware_targets
FROM "Papers"
WHERE contains(tags, "edge-ai") OR contains(tags, "tinyml")
SORT year DESC
```

### Tags disponibles

| Domaine | Tags |
|---------|------|
| Contrôle HVAC | `#hvac` `#building-control` `#thermostat` |
| Algorithmes RL | `#reinforcement-learning` `#dqn` `#d3qn` `#ddpg` `#q-learning` |
| Modèles DL | `#lstm` `#cnn` `#attention` `#encoder-decoder` |
| Edge / TinyML | `#tinyml` `#edge-ai` `#embedded` `#esp32` `#stm32` |
| Confort | `#thermal-comfort` `#pmv` `#personalization` `#occupancy` |
| Type de papier | `#survey` `#foundational` `#comparative-study` |

---

## 📋 Liste complète des articles

### 🏛️ Papiers fondateurs

| Année | Fichier | Auteurs | Méthode | Pertinence |
|-------|---------|---------|---------|-----------|
| 2015 | [barrett-linder-2015](2015/barrett-linder-autonomous-hvac-rl/barrett-linder-2015.md) | Barrett & Linder | Q-Learning + Bayesian | ⭐⭐⭐⭐ |
| 2016 | [deepmind-cooling-2016](2016/deepmind-datacenter-cooling-40pct/deepmind-cooling-2016.md) | DeepMind | Deep NN | ⭐⭐⭐ |
| 2017 | [wei-2017](2017/wei-deep-rl-building-hvac/wei-2017.md) | Wei, Wang, Zhu | **DQN + EnergyPlus** | ⭐⭐⭐⭐⭐ |
| 2018 | [deepmind-safety-2018](2018/deepmind-safety-first-cooling/deepmind-safety-2018.md) | DeepMind | DNN + Safety layers | ⭐⭐⭐ |
| 2019 | [dqn-hvac-2019](2019/dqn-hvac-energyplus/dqn-hvac-2019.md) | (voir fichier) | DQN multi-HVAC | ⭐⭐⭐⭐ |

### 🤖 Algorithmes DRL

| Année | Fichier | Auteurs | Méthode | Pertinence |
|-------|---------|---------|---------|-----------|
| 2020 | [gupta-2020](2020/gupta-dqn-energy-efficient-heating/gupta-2020.md) | Gupta et al. | DQN chauffage | ⭐⭐⭐⭐ |
| 2020 | [hosseinloo-2020](2020/hosseinloo-mit-event-triggered-rl/hosseinloo-2020.md) | Hosseinloo (MIT) | **Event-triggered RL** | ⭐⭐⭐⭐⭐ |
| 2023 | [ed-dqn-2023](2023/ed-dqn-event-driven-hvac/ed-dqn-2023.md) | Fu et al. | **ED-DQN event-driven** | ⭐⭐⭐⭐⭐ |
| 2023 | [setpoint-preference-2023](2023/setpoint-preference-learning-rl/setpoint-preference-2023.md) | Elehwany et al. | Off-policy MAB | ⭐⭐⭐⭐⭐ |
| 2024 | [du-ddpg-2024](2024/du-ddpg-multizone-residential/du-ddpg-2024.md) | Du et al. | **DDPG multi-zones** | ⭐⭐⭐⭐⭐ |
| 2024 | [pmv-drl-2024](2024/drl-pmv-dynamic-comfort/pmv-drl-2024.md) | Shi et al. | Dueling DQN + PMV | ⭐⭐⭐⭐ |
| 2024 | [dqn-d3qn-2024](2024/dqn-d3qn-hvac-comparison/dqn-d3qn-2024.md) | Qin et al. | DQN vs D3QN | ⭐⭐⭐⭐ |
| 2024 | [octopus-2024](2024/octopus-holistic-building-drl/octopus-2024.md) | Ding, Du, Cerpa | Branching DQN | ⭐⭐⭐⭐ |
| 2025 | [rl-pid-2025](2025/rl-vs-pid-hvac-simulation/rl-pid-2025.md) | (voir fichier) | Q-learning vs PID | ⭐⭐⭐ |
| 2025 | [expert-rl-2025](2025/efficient-rl-expert-guided-hvac/expert-rl-2025.md) | (voir fichier) | Expert-guided RL | ⭐⭐⭐⭐ |

### 🧠 Réseaux CNN / LSTM

| Année | Fichier | Auteurs | Méthode | Pertinence |
|-------|---------|---------|---------|-----------|
| 2020 | [lstm-indoor-2020](2020/lstm-indoor-temp-prediction/lstm-indoor-2020.md) | Mtibaa et al. | LSTM seq-to-seq | ⭐⭐⭐⭐ |
| 2021 | [cnn-lstm-2021](2021/cnn-lstm-predictive-indoor-temp/cnn-lstm-2021.md) | Elmaz et al. | CNN-LSTM + Attention | ⭐⭐⭐⭐ |
| 2023 | [occupancy-lstm-2023](2023/occupancy-lstm-optimized/occupancy-lstm-2023.md) | Mahjoub et al. | LSTM + GA/PSO | ⭐⭐⭐⭐ |
| 2024 | [cho-mh-lstm-2024](2024/cho-mh-lstm-personalized-comfort/cho-mh-lstm-2024.md) | Cho et al. | Multi-Head LSTM | ⭐⭐⭐⭐ |
| 2025 | [ml-indoor-temp-2025](2025/ml-indoor-temp-lightweight/ml-indoor-temp-2025.md) | (voir fichier) | **LSTM 50k params** | ⭐⭐⭐⭐⭐ |
| 2025 | [cnn-m-lstm-2025](2025/bayesian-cnn-m-lstm-comfort/cnn-m-lstm-2025.md) | (voir fichier) | CNN + M-LSTM Bayesian | ⭐⭐⭐⭐ |
| 2025 | [digital-twin-lstm-2025](2025/digital-twin-lstm-hvac/digital-twin-lstm-2025.md) | (voir fichier) | Digital Twin + LSTM | ⭐⭐⭐⭐ |

### 🔌 TinyML / Edge AI

| Année | Fichier | Auteurs | Méthode | Pertinence |
|-------|---------|---------|---------|-----------|
| 2022 | [schizas-tinyml-2022](2022/schizas-tinyml-iot-review/schizas-tinyml-2022.md) | Schizas et al. | Survey TinyML/TFLM | ⭐⭐⭐⭐ |
| 2025 | [tinyml-cities-2025](2025/edge-intelligence-tinyml-cities/tinyml-cities-2025.md) | (voir fichier) | Review 66 études | ⭐⭐⭐⭐ |
| 2026 | [tinyml-esp32-2026](2026/tinyml-occupancy-esp32/tinyml-esp32-2026.md) | (voir fichier) | **Random Forest ESP32** | ⭐⭐⭐⭐⭐ |
| 2026 | [sustainability-tdl-2026](2026/sustainability-tiny-deep-learning/sustainability-tdl-2026.md) | (voir fichier) | **TDL sub-kilobyte** | ⭐⭐⭐⭐⭐ |

### 📖 Surveys

| Année | Fichier | Couverture | Pertinence |
|-------|---------|-----------|-----------|
| 2024 | [survey-rl-hvac-2024](2024/survey-rl-hvac-intelligent-buildings/survey-rl-hvac-2024.md) | RL HVAC depuis 2019 | ⭐⭐⭐⭐⭐ |
| 2022 | [schizas-tinyml-2022](2022/schizas-tinyml-iot-review/schizas-tinyml-2022.md) | TinyML / IoT | ⭐⭐⭐⭐ |
| 2025 | [tinyml-cities-2025](2025/edge-intelligence-tinyml-cities/tinyml-cities-2025.md) | Edge AI villes | ⭐⭐⭐⭐ |

---

## 🏗️ Architecture cible (synthèse des papiers)

```
┌─────────────────────────────────────────────────────────┐
│               THERMOSTAT EDGE AI                        │
├─────────────┬───────────────────┬───────────────────────┤
│  COUCHE 1   │     COUCHE 2      │       COUCHE 3        │
│  Prédiction │    Occupation     │   Décision contrôle   │
├─────────────┼───────────────────┼───────────────────────┤
│ LSTM ~50k   │ Random Forest     │ DQN / ED-DQN          │
│ params      │ ou CNN léger      │ (event-triggered)     │
│ (2025 paper)│ (2026 ESP32 paper)│ (2023 ED-DQN / 2020   │
│             │                   │  MIT RL paper)        │
├─────────────┼───────────────────┼───────────────────────┤
│ Cortex-M4/7 │ ESP32 / STM32     │ Cortex-M4/7           │
│ ~203 KB     │ 997µs, 1.4 MB     │ Entraîn. offline      │
└─────────────┴───────────────────┴───────────────────────┘
```

**Gap identifié :** peu de papiers combinent les 3 couches sur un seul système embarqué. Vrai défi de recherche : agent DQN quantifié sur Cortex-M4/M7 (256 Ko – 1 Mo SRAM).

---

## 🏷️ Format des fiches (YAML Properties Obsidian)

Chaque fiche suit ce format pour permettre la recherche Dataview :

```yaml
---
title: "Titre complet"
authors:
  - "Nom, Prénom"
year: 2024
venue: "Nom du journal / conférence"
publisher: "Éditeur"
doi: "10.xxxx/xxxxx"
url: "https://..."
pdf_url: "https://..."
tags:
  - hvac
  - reinforcement-learning
domains:
  - "HVAC Control"
methods:
  - "DQN"
hardware_targets:
  - "ESP32"
datasets:
  - name: "Nom du dataset"
    url: "https://..."
    description: "Description courte"
read: false        # ← marquer true après lecture
relevance: 5       # ← 1 à 5 étoiles
category: "RL-HVAC | CNN-LSTM | TinyML | Survey | Foundational"
date_added: 2026-02-19
---
```

---

## 📊 Statistiques

| Catégorie | Nombre |
|-----------|--------|
| RL / DRL pour HVAC | 14 |
| CNN / LSTM prédiction | 7 |
| TinyML / Edge AI | 4 |
| Surveys | 3 (dont 2 aussi dans d'autres catégories) |
| **TOTAL** | **27** |

| Période | Articles |
|---------|---------|
| 2015–2019 | 5 |
| 2020–2022 | 5 |
| 2023 | 4 |
| 2024 | 6 |
| 2025–2026 | 8 |

---

*Bibliothèque générée automatiquement le 2026-02-19 — État de l'art IA pour thermostats intelligents*
