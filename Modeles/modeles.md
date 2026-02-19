---
title: "Catalogue des Modèles — IA pour Thermostats Intelligents"
description: "Inventaire exhaustif des architectures ML/DL/RL utilisées dans la littérature HVAC : paramètres, couches, quantisation, matériel d'entraînement et d'inférence, performances"
date_created: 2026-02-19
tags:
  - modeles
  - architecture
  - quantisation
  - edge-ai
  - benchmarks
  - hardware
categories_covered:
  - Reinforcement Learning (DQN, D3QN, DDPG, ED-DQN, BDQ, MAB)
  - LSTM & RNN
  - CNN-LSTM hybrides
  - TinyML / Edge embarqué
  - Baselines (PID, rule-based)
---

# 🧠 Catalogue des Modèles — IA pour Thermostats Intelligents

> **Mise à jour :** 2026-02-19 · **Modèles documentés :** 20+ architectures · **Sources :** papiers scientifiques + benchmarks matériels

---

## 🗺️ Navigation rapide

| Catégorie | Modèles | Aller à |
|-----------|---------|---------|
| 🎮 Reinforcement Learning | DQN · D3QN · DDPG · ED-DQN · BDQ · MAB · Q-Learning tabular | [→](#-reinforcement-learning) |
| 🔁 LSTM & RNN | LSTM basic · LSTM léger · MH-LSTM · GA-LSTM · PSO-LSTM | [→](#-lstm--rnn) |
| 🔀 CNN-LSTM hybrides | CNN-LSTM + Attention · BO CNN-M-LSTM · Digital Twin LSTM | [→](#-cnn-lstm-hybrides) |
| 🔌 TinyML / Edge AI | Random Forest ESP32 · TDL sub-KB · Frameworks | [→](#-tinyml--edge-ai) |
| 📏 Baselines | PID · Rule-based | [→](#-baselines) |
| 🖥️ Hardware benchmarks | ESP32 · STM32 · Arduino · Cortex-M | [→](#️-benchmarks-hardware) |
| 📊 Tableau comparatif | Tous les modèles | [→](#-tableau-comparatif-global) |

---

## 🎮 Reinforcement Learning

> Les modèles RL apprennent une politique de contrôle par interaction avec une simulation (EnergyPlus). L'inférence est légère — c'est l'entraînement qui est coûteux.

---

### DQN — Deep Q-Network (standard)

> **Papier séminal du domaine.** Introduit par Wei et al. (2017).

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | MLP 2 couches : [64 → 32] |
| **Paramètres** | ~3 000 – 5 000 |
| **Mémoire FP32** | ~12 – 20 KB |
| **Mémoire INT8** | ~3 – 5 KB |
| **Quantisation testée** | ❌ Non mentionnée dans les papiers |
| **Entraînement** | CPU/GPU + EnergyPlus (simulation) |
| **Inférence cible** | Serveur cloud |
| **Convergence** | ~2 000 épisodes |
| **Économie énergie** | 15–20 % vs thermostat classique |
| **Satisfaction confort** | >95 % des heures |

**Papier source :** [[Papers/2017/wei-deep-rl-building-hvac/wei-2017|Wei et al. 2017]] · [[Papers/2019/dqn-hvac-energyplus/dqn-hvac-2019|DQN HVAC 2019]] · [[Papers/2020/gupta-dqn-energy-efficient-heating/gupta-2020|Gupta 2020]]

---

### D3QN — Double Dueling DQN

> Combinaison de Double DQN (correction overestimation) et Dueling DQN (streams valeur + avantage). Architecture optimale selon Qin et al. (2024).

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | [64 → 12] avec Value stream + Advantage stream |
| **Paramètres** | ~4 000 – 5 000 |
| **Mémoire FP32** | ~16 – 20 KB |
| **Mémoire INT8** | ~4 – 5 KB |
| **Quantisation testée** | ❌ Non testée dans le papier |
| **Quantisation possible** | ✅ (INT8 → ~4 KB, bien adapté embarqué) |
| **Entraînement** | CPU/GPU + EnergyPlus, 8 760 h/an simulées |
| **Inférence cible** | Edge / MCU capable |
| **Convergence** | ~320 épisodes (29 % plus rapide que DQN) |
| **Économie énergie** | 24 % (projet 1) · 23 % · 20 % · 18 % |
| **Variance T°** | 0,4 °C (vs 0,8 °C DQN) |
| **Résidu Q-error std** | 0,9 (vs 2,5 DQN) |

**Architecture interne :**
```
Input → [FC 64] → ┬→ Value stream   [FC 32 → scalar V(s)]
                  └→ Advantage stream [FC 32 → A(s,a) pour chaque action]
                  └→ Q(s,a) = V(s) + A(s,a) - mean(A)
```

**Papier source :** [[Papers/2024/dqn-d3qn-hvac-comparison/dqn-d3qn-2024|DQN vs D3QN 2024]]

---

### ED-DQN — Event-Driven DQN

> Variante cruciale pour l'embarqué : ne déclenche une décision que lors d'un changement significatif. Réduit de 76 % le nombre d'ajustements.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | [64 → 64 → 32] + mécanisme event-triggering |
| **Paramètres** | ~6 000 – 8 000 |
| **Mémoire FP32** | ~24 – 32 KB |
| **Mémoire INT8** | ~6 – 8 KB |
| **Quantisation testée** | ❌ Non testée |
| **Quantisation possible** | ✅ Très adapté (faible nb de paramètres) |
| **Entraînement** | CPU/GPU + EnergyPlus, 365 jours simulés, 3-5 zones |
| **Inférence cible** | **Edge embarqué** (décisions sparses) |
| **Convergence** | ~800 épisodes (vs 1 200 DQN standard) |
| **Économie énergie** | 27 % vs thermostat baseline |
| **Réduction ajustements** | **76 %** vs DQN standard |
| **Confort** | 88 % des heures dans ±1 °C |
| **RMSE** | 0,35 °C |

**Mécanisme event-triggering :**
```
Déclenchement si : |T_actuelle - T_référence| > seuil ε
→ Calcul action RL uniquement lors des événements
→ Réduit drastiquement la charge CPU et les usures mécaniques
```

**Papier source :** [[Papers/2023/ed-dqn-event-driven-hvac/ed-dqn-2023|ED-DQN 2023]]

---

### DDPG — Deep Deterministic Policy Gradient

> Actor-Critic pour les espaces d'action **continus** (température en °C, pas discrète). Significativement plus complexe que DQN.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Actor [FC 256 → FC 128 → action continue] + Critic [FC 256 → FC 128 → Q-value] |
| **Paramètres** | ~15 000 – 20 000 (double réseau) |
| **Mémoire FP32** | ~60 – 80 KB |
| **Mémoire INT8** | ~15 – 20 KB |
| **Quantisation testée** | ❌ Non mentionnée |
| **Entraînement** | GPU/CPU + EnergyPlus multi-zones résidentielles |
| **Inférence cible** | Serveur ou edge haut de gamme |
| **Convergence** | 300 – 500 épisodes |
| **vs DQN** | **−15 % coût énergétique**, **−79 % violations confort** |
| **vs rule-based** | **−98 % violations confort** |
| **Précision T°** | ±0,5 °C |
| **Transfert** | Généralise sur de nouveaux bâtiments non vus |

**Papier source :** [[Papers/2024/du-ddpg-multizone-residential/du-ddpg-2024|Du DDPG multi-zones]]

---

### BDQ — Branching Dueling Q-Network (OCTOPUS)

> Architecture pour les espaces d'action très larges (2,3M+ combinaisons). Contrôle simultané HVAC + éclairage + stores + fenêtres.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Extraction partagée [FC 128 → FC 64] + 4 branches dueling indépendantes |
| **Paramètres** | ~25 000 – 35 000 |
| **Mémoire FP32** | ~100 – 140 KB |
| **Mémoire INT8** | ~25 – 35 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | GPU + EnergyPlus, LEED Gold, 10 ans météo, Merced CA + Chicago IL |
| **Inférence cible** | Serveur |
| **Espace d'action original** | 6,25 M combinaisons → réduit à ~8 000 via branches |
| **Convergence** | ~200 épisodes (~200 jours simulés) |
| **Économie énergie** | **14,26 %** vs rule-based |
| **Économie coût annuel** | 14,3 % ($307/an) |
| **Confort** | 82–88 % (vs 75–80 % baseline) |

**Papier source :** [[Papers/2024/octopus-holistic-building-drl/octopus-2024|OCTOPUS 2024]]

---

### Expert-Guided DRL

> DRL accéléré par 3 fonctions d'expertise hétérogènes : physique, données historiques, règles heuristiques.

| Propriété | Valeur |
|-----------|--------|
| **Base** | DQN ou PPO + 3 guidance functions |
| **Paramètres** | ~10 000 – 20 000 (dépend de la base) |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | GPU + EnergyPlus |
| **Accélération convergence** | **8,8× plus rapide** vs DRL non guidé |
| **Épisodes requis** | 100 – 300 (vs 1 000 – 3 000 baseline) |
| **Violations** | 2 – 5 % (vs 15 – 25 % sans guidage) |

**Papier source :** [[Papers/2025/efficient-rl-expert-guided-hvac/expert-rl-2025|Expert-guided RL 2025]]

---

### Event-Triggered TD — MIT LIDS (Hosseinloo 2020)

> Modèle **tabulaire** event-triggered. Converge en **1 semaine** de données réelles. Directement embarquable sur MCU.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Q-table ou V-table sparse + politique π |
| **Paramètres** | Tabulaire (adaptatif, ~quelques KB) |
| **Mémoire** | **<5 KB** |
| **Mémoire INT8** | **<2 KB** |
| **Quantisation** | ✅ N/A (tabulaire, nativement léger) |
| **Entraînement** | **Bâtiment réel** (campus MIT), données in-situ |
| **Inférence cible** | **Microcontrôleur** |
| **Convergence** | **1 semaine** de données réelles (exceptionnel) |
| **Réduction décisions** | **50 – 90 %** vs contrôle à temps fixe |

**Papier source :** [[Papers/2020/hosseinloo-mit-event-triggered-rl/hosseinloo-2020|Hosseinloo MIT 2020]]

---

### Multi-Armed Bandit — Thompson Sampling (Elehwany 2023)

> Apprentissage des préférences de température depuis les **overrides implicites** de l'occupant. Zéro feedback explicite requis.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Thompson Sampling, distributions Beta par action |
| **Paramètres** | ~11 distributions (1 par action) — **<1 KB** |
| **Mémoire** | **<5 KB** |
| **Quantisation** | ✅ N/A (modèle probabiliste) |
| **Entraînement** | **In-situ** (bâtiment réel via overrides) |
| **Inférence cible** | **Microcontrôleur** |
| **Convergence** | 45 – 60 jours |
| **Précision préférences** | 87 % (vs 82 % UCB) |
| **Économie hiver** | 15,2 % · **été** : 10,1 % · **annuel** : 12,6 % |

**Papier source :** [[Papers/2023/setpoint-preference-learning-rl/setpoint-preference-2023|Setpoint preference RL 2023]]

---

### Q-Learning tabulaire (Barrett 2015)

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Q-table + Bayesian occupancy inference |
| **Paramètres** | Tabulaire adaptatif |
| **Mémoire** | ~quelques KB |
| **Entraînement** | Données résidentielles réelles |
| **Inférence cible** | MCU / thermostat embarqué |
| **Économie** | 10 % vs thermostat programmable |

**Papier source :** [[Papers/2015/barrett-linder-autonomous-hvac-rl/barrett-linder-2015|Barrett & Linder 2015]]

---

## 🔁 LSTM & RNN

---

### LSTM léger — 50 851 paramètres (2025)

> ⭐ **Le plus important pour l'embarqué.** Conçu explicitement pour déploiement sur microcontrôleur.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | 1-2 couches LSTM [32-64 units] + Dense [16] + Dropout [0.2-0.5] |
| **Paramètres** | **50 851** |
| **Mémoire FP32** | **203,4 KB** |
| **Mémoire INT8 estimée** | **~51 KB** |
| **Mémoire FP16 estimée** | **~102 KB** |
| **Quantisation testée** | ❌ Non testée dans le papier (mais recommandée) |
| **Entraînement** | CPU/GPU, cross-validation rolling window (5-10 folds) |
| **Inférence cible** | **Microcontrôleur** (Cortex-M4/M7, ESP32-S3) |
| **Loss** | 0,0004709 – 0,0282 |
| **R²** | 0,90 – 0,95 |
| **Tâche** | Prédiction T° intérieure (1–4 h d'avance) |

**Note quantisation :** Si quantifié INT8 via TFLite Micro → ~51 KB, déployable sur ESP32 (520 KB SRAM) ou STM32 Cortex-M4 (128–256 KB RAM).

**Papier source :** [[Papers/2025/ml-indoor-temp-lightweight/ml-indoor-temp-2025|ML Indoor Temp Lightweight 2025]]

---

### LSTM standard — prédiction multi-zones (Mtibaa 2020)

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | 1-2 couches LSTM [64–256 units], Seq2Seq encodeur-décodeur |
| **Paramètres** | ~30 000 – 100 000 |
| **Mémoire FP32** | ~120 – 400 KB |
| **Mémoire INT8** | ~30 – 100 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | GPU/CPU, données réelles bâtiment VAV/CAV |
| **Inférence cible** | Serveur ou edge haut de gamme |
| **vs MLP** | −50 % d'erreur de prédiction |
| **RMSE** | 0,3 – 0,8 °C |
| **MAE** | 0,2 – 0,6 °C |
| **R²** | 0,90 – 0,95 |

**Papier source :** [[Papers/2020/lstm-indoor-temp-prediction/lstm-indoor-2020|LSTM Indoor Temp 2020]]

---

### MH-LSTM — Multi-Head LSTM (Cho et al. 2024)

> 3 têtes LSTM capturant des dynamiques court/moyen/long terme en parallèle. Confort thermique personnalisé.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | 3 têtes LSTM parallèles + fusion + Dense |
| **Tête 1 (court terme)** | 6 timesteps (~1-2 h), 64 units |
| **Tête 2 (moyen terme)** | 24 timesteps (~8 h), 64 units |
| **Tête 3 (long terme)** | 96 timesteps (~24 h+), 64 units |
| **Paramètres** | ~50 000 |
| **Mémoire FP32** | ~200 KB |
| **Mémoire INT8** | ~50 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | CPU/GPU, 6 participants × 4 semaines, ~10 000 pts/participant |
| **Inférence cible** | Edge (capable MCU) |
| **Précision classification** | **92 %** (vs 84–86 % LSTM standard) |
| **F1-Score** | 0,90 |
| **Sortie** | Échelle de sensation thermique 7 niveaux (−3 à +3) |

**Papier source :** [[Papers/2024/cho-mh-lstm-personalized-comfort/cho-mh-lstm-2024|MH-LSTM Thermal Comfort 2024]]

---

### GA-LSTM — Optimisation par Algorithme Génétique

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | LSTM [64 → 32] + Dense [16] + Dropout, poids optimisés par AG |
| **Paramètres** | ~30 000 – 40 000 |
| **Mémoire FP32** | ~120 – 160 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | Population 30 · 100 générations · mutation 0,1 · ~8 h |
| **vs LSTM standard** | −36 % RMSE |
| **Accuracy** | 93,2 % · F1 0,931 |
| **Tâche** | Prédiction d'occupation (15–30 min) |

**Papier source :** [[Papers/2023/occupancy-lstm-optimized/occupancy-lstm-2023|Occupancy LSTM 2023]]

---

### PSO-LSTM — Optimisation par Essaim de Particules

> ⭐ **Meilleure précision** des trois variantes (standard, GA, PSO). Convergence plus rapide que GA.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | LSTM [64 → 32] + Dense [16], poids optimisés par PSO |
| **Paramètres** | ~30 000 – 40 000 |
| **Mémoire FP32** | ~120 – 160 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | 20-30 particules · 200-500 itérations · ~3 h (vs 8 h GA) |
| **vs LSTM standard** | **−46 % RMSE** |
| **Accuracy** | **94,8 %** · F1 **0,946** · ROC-AUC **0,965** |
| **Réduction erreur 15 min** | −56 % |
| **Réduction erreur 30 min** | −34 % |

**Papier source :** [[Papers/2023/occupancy-lstm-optimized/occupancy-lstm-2023|Occupancy LSTM 2023]]

---

## 🔀 CNN-LSTM hybrides

---

### CNN-LSTM + Attention (Elmaz et al. 2021)

> Architecture encodeur-décodeur avec mécanisme d'attention. Optimisation bayésienne des hyperparamètres.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Conv1D [32 filtres] → Conv1D [64 filtres] → MaxPooling → BiLSTM [128] encodeur → LSTM [128] décodeur → Attention |
| **Paramètres** | ~50 000 – 70 000 |
| **Mémoire FP32** | ~200 – 280 KB |
| **Mémoire INT8** | ~50 – 70 KB |
| **Quantisation testée** | ❌ Non testée |
| **Optimisation HP** | Bayesian Optimization (TPE), 100-200 configurations |
| **Entraînement** | GPU, bâtiment réel Université d'Anvers, 1–5 min granularité |
| **Inférence cible** | Edge haut de gamme |
| **Gain vs LSTM (1 min)** | +15–25 % |
| **Gain vs LSTM (60 min)** | +25–40 % |
| **Gain vs LSTM (120 min)** | **+30–45 %** |

**Papier source :** [[Papers/2021/cnn-lstm-predictive-indoor-temp/cnn-lstm-2021|CNN-LSTM 2021]]

---

### BO CNN-M-LSTM — Bayesian Optimized (2025)

> CNN + LSTM multivarié avec optimisation bayésienne. Double sortie : prédiction de charge + confort PMV.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | Conv1D [filtres, kernel] → MaxPooling → M-LSTM multivarié → 2 têtes de sortie |
| **Paramètres** | ~40 000 – 60 000 |
| **Mémoire FP32** | ~160 – 240 KB |
| **Mémoire INT8** | ~40 – 60 KB |
| **Quantisation testée** | ❌ Non testée |
| **Espace de recherche HP** | Filtres CNN [16,32,64] · Kernel [3,5,7] · LSTM [32,64,128] · Dropout [0.1,0.3,0.5] · LR [1e-4,1e-3] |
| **Entraînement** | GPU, bâtiments commerciaux + ASHRAE DB, 1–2 ans données |
| **Inférence cible** | Serveur / edge haut de gamme |
| **Load forecast MAPE** | 5–10 % |
| **Confort PMV MAE** | ±0,3 unités |
| **R² load** | 0,85 – 0,92 |

**Papier source :** [[Papers/2025/bayesian-cnn-m-lstm-comfort/cnn-m-lstm-2025|Bayesian CNN-M-LSTM 2025]]

---

### Digital Twin LSTM-Attention (2025)

> Jumeau numérique physique couplé à un BiLSTM avec multi-head attention. Interprétabilité + précision.

| Propriété | Valeur |
|-----------|--------|
| **Architecture** | RC thermal model (physics) + BiLSTM [64-128 units] + Multi-head Attention [4-8 heads, dim 32-64] + 3 têtes sortie |
| **Paramètres** | ~80 000 – 120 000 |
| **Mémoire FP32** | ~320 – 480 KB |
| **Mémoire INT8** | ~80 – 120 KB |
| **Quantisation testée** | ❌ Non testée |
| **Entraînement** | GPU essentiel, EnergyPlus ou données réelles multi-zones |
| **Inférence cible** | Serveur / cloud (complexité élevée) |
| **Séquence d'entrée** | 168 timesteps (1 semaine historique) |
| **Horizon de prédiction** | 24 – 48 pas en avant |
| **Réduction énergie** | **14 %** vs setpoint fixe |
| **Productivité occupants** | **+22 %** estimé |
| **R²** | 0,85 – 0,92 |

**Papier source :** [[Papers/2025/digital-twin-lstm-hvac/digital-twin-lstm-2025|Digital Twin LSTM 2025]]

---

## 🔌 TinyML / Edge AI

---

### Random Forest sur ESP32 (TinyML 2026)

> ⭐ **Référence embarquée directe.** Déployé et mesuré sur ESP32 réel.

| Propriété | Valeur |
|-----------|--------|
| **Modèle** | Random Forest (6 candidats testés : LR, KNN, DT, Gradient Boosting, RF, XGBoost) |
| **Gagnant** | Random Forest |
| **Stockage** | **1,426 MB** (sur 4–16 MB Flash ESP32) |
| **Latence d'inférence** | **997 µs** (< 1 ms !) |
| **Quantisation** | ✅ Natif (arbres = opérations entières) |
| **Hardware** | ESP32 (Xtensa LX6/LX7, 240 MHz, 520 KB SRAM) |
| **Capteurs d'entrée** | CO₂, T°, Humidité, Lumière, Présence PIR |
| **R²** | **0,923** |
| **Framework** | micromlgen / scikit-learn → C |

**Outil de déploiement :**
```
scikit-learn → micromlgen → C/C++ statique → ESP32 flash
Taille FLASH : 1.4 MB  |  RAM : ~<50 KB  |  Latence : 997 µs
```

**Papier source :** [[Papers/2026/tinyml-occupancy-esp32/tinyml-esp32-2026|TinyML ESP32 2026]]

---

### TDL — Tiny Deep Learning sub-kilobyte (2026)

> Modèles dont l'empreinte mémoire est **inférieure à 1 KB**. Quantisation + pruning extrêmes.

| Propriété | Valeur |
|-----------|--------|
| **Modèle** | Réseau de neurones ultra-léger avec quantisation + pruning |
| **Taille modèle** | **< 1 KB** (sub-kilobyte) |
| **Quantisation** | ✅ INT8 ou moins (quantisation agressive) |
| **Pruning** | ✅ Sparsité élevée |
| **Hardware cible** | MCU ultra-contraints |
| **Énergie/inférence** | Évaluée (incl. émissions CO₂ éq.) |
| **Tâche** | Détection d'occupation temps réel |
| **Performance** | Haute performance maintenue malgré contraintes extrêmes |

**Papier source :** [[Papers/2026/sustainability-tiny-deep-learning/sustainability-tdl-2026|Sustainability TDL 2026]]

---

### Frameworks TinyML de référence

| Framework | Cible | Quantisation | Notes |
|-----------|-------|-------------|-------|
| **TensorFlow Lite Micro (TFLM)** | ARM Cortex-M, ESP32 | INT8 ✅ | Standard de facto, optimisé CMSIS-NN |
| **Edge Impulse** | ESP32, STM32, Arduino | INT8 ✅ | MLOps cloud → MCU, pipeline complet |
| **X-CUBE-AI (STM32)** | STM32 Cortex-M4/M7 | INT8 ✅ | Plus rapide que TFLM sur STM32 |
| **ESP-DL** | ESP32-S3 | INT8 ✅ | 4.5–6.25× accélération hardware |
| **micromlgen** | ESP32, Arduino | Natif ✅ | sklearn → C, parfait pour RF/DT |
| **emlearn** | MCU C99 | Natif ✅ | RF en ~2 KB FLASH |
| **CMSIS-NN** | Cortex-M4/M7 | INT8 ✅ | 4.6× speedup vs baseline |

**Papiers source :** [[Papers/2022/schizas-tinyml-iot-review/schizas-tinyml-2022|Schizas TinyML 2022]] · [[Papers/2025/edge-intelligence-tinyml-cities/tinyml-cities-2025|TinyML Cities 2025]]

---

## 📏 Baselines

---

### PID — Proportional-Integral-Derivative

| Propriété | Valeur |
|-----------|--------|
| **Paramètres** | 3 (K_p, K_i, K_d) |
| **Mémoire** | Négligeable |
| **Hardware** | Tout MCU, même 8 bits |
| **Tuning** | Ziegler-Nichols ou empirique |
| **Violations confort** | 1–2 °C de moyenne (vs <0,5 °C RL) |
| **Robustesse perturbations** | Bonne mais inférieure au RL |
| **Stabilité** | Excellente, prouvée |

**Papier source :** [[Papers/2025/rl-vs-pid-hvac-simulation/rl-pid-2025|RL vs PID 2025]]

---

### Thermostat à règles fixes

> Baseline systématique dans tous les papiers. Setpoint fixe ou planning jour/nuit.

| Résultat | Valeur |
|----------|--------|
| **vs DDPG** | +98 % violations confort |
| **vs Dueling DQN** | Économie énergie 4.8–39.58 % possible |
| **vs ED-DQN** | 27 % d'énergie supplémentaire consommée |

---

## 🖥️ Benchmarks Hardware

> Données issues de publications et benchmarks officiels (MLPerf Tiny, CMSIS-NN, etc.)

### Performances comparées des MCU cibles

| Plateforme | CPU | RAM | Flash | Latence LSTM typ. | Latence RF typ. | Quantisation |
|-----------|-----|-----|-------|-----------------|----------------|-------------|
| **ESP32** | Xtensa LX6 240 MHz | 520 KB | 4–16 MB | ~74 ms | **997 µs** | INT8 via TFLM |
| **ESP32-S3** | Xtensa LX7 240 MHz | 512 KB | 8 MB | ~55 ms | <1 ms | INT8 + ESP-DL |
| **STM32 Cortex-M4 @ 120 MHz** | ARM M4 120 MHz | 128–320 KB | 256–512 KB | 50–200 ms | <5 ms | INT8 CMSIS-NN |
| **STM32 Cortex-M7 @ 480 MHz** | ARM M7 480 MHz | 1 MB | 2 MB | 20–80 ms | <2 ms | INT8 CMSIS-NN |
| **Arduino Nano BLE 33** | ARM M4 64 MHz | 256 KB | 1 MB | 100–400 ms | <10 ms | INT8 TFLM |
| **Portenta H7** | M7 480 + M4 240 MHz | 1 MB | 2 MB | 20–60 ms | <2 ms | INT8 TFLM |
| **Ambiq Apollo3 (Cortex-M4F)** | ARM M4F 96 MHz | 384 KB | 1 MB | ~100 ms | <5 ms | INT8 FQT |

### Impact de la quantisation (résultats publiés)

| Technique | Réduction taille | Vitesse | Perte précision | Notes |
|-----------|----------------|---------|----------------|-------|
| **FP32 → INT8** | **4× – 10×** | **2–4×** | 1–5 % | Standard TinyML |
| **FP32 → FP16** | **2×** | 1,5× | <1 % | GPU principalement |
| **FP32 → INT8 (DQN)** | 4× | **2,2× – 5,4×** | Maintenue | Arxiv 2019 |
| **LSTM 16×8** | 2× | 1,5× | ~1 % | Meilleur pour RNN |
| **LSTM 8×8** | 4× | 3× | ⚠️ Dégradation notable | À éviter sans QAT |
| **Pruning 50 %** | 2× | 1,3× | 1–3 % | Combinable avec quant. |
| **CMSIS-NN (M4)** | = | **4,6×** | 0 % | Optimisation kernels ARM |

> **Recommandation pour LSTM :** Privilégier quantisation **16×8** (poids 16 bits, activations 8 bits) plutôt que 8×8 pure. Pour les modèles RL/DQN, INT8 fonctionne bien avec un entraînement aware (QAT).

### Latences d'inférence mesurées dans les papiers

| Modèle | Hardware | Latence | Source |
|--------|---------|---------|--------|
| Random Forest | ESP32 | **997 µs** | [[Papers/2026/tinyml-occupancy-esp32/tinyml-esp32-2026\|TinyML ESP32 2026]] |
| LSTM 1 couche (météo) | ESP32 | 74 ms | MDPI Sensors 2025 |
| LSTM 1 couche (météo) | ESP32-S3 | 55 ms | MDPI Sensors 2025 |
| NN (occupancy ToF) | MCU non spécifié | 275 ms | MDPI 2024 |
| TinyML général | ESP32 → Portenta | 21 ms – >1 s | [[Papers/2025/edge-intelligence-tinyml-cities/tinyml-cities-2025\|TinyML Cities 2025]] |
| CMSIS-NN CNN | Cortex-M4 | 3,47 – 14,98 ms | PMC 2021 |

---

## 📊 Tableau comparatif global

| Modèle | Type | Params | RAM FP32 | RAM INT8 | Quant. testée | HW train | HW inférence | Économie énergie | Précision / Confort | Papier |
|--------|------|--------|---------|---------|-------------|---------|-------------|-----------------|--------------------|----|
| **Event-Triggered TD** | RL tabulaire | <1 K | <5 KB | <2 KB | ✅ N/A | Bâtiment réel | **MCU** | Optimal | Excellent | [[Papers/2020/hosseinloo-mit-event-triggered-rl/hosseinloo-2020\|2020]] |
| **MAB Thompson** | RL bandit | <1 K | <5 KB | <2 KB | ✅ N/A | In-situ | **MCU** | 12,6 % | 87 % prefs | [[Papers/2023/setpoint-preference-learning-rl/setpoint-preference-2023\|2023]] |
| **DQN standard** | RL valeur | 3–5 K | 12–20 KB | 3–5 KB | ❌ | CPU/GPU | Serveur | 15–20 % | >95 % h. | [[Papers/2017/wei-deep-rl-building-hvac/wei-2017\|2017]] |
| **D3QN** | RL valeur | 4–5 K | 16–20 KB | 4–5 KB | ❌ | CPU/GPU | Edge | **24 %** | 0,4 °C var | [[Papers/2024/dqn-d3qn-hvac-comparison/dqn-d3qn-2024\|2024]] |
| **ED-DQN** | RL event | 6–8 K | 24–32 KB | 6–8 KB | ❌ | CPU/GPU | **Edge** | **27 %** | 88 % ±1 °C | [[Papers/2023/ed-dqn-event-driven-hvac/ed-dqn-2023\|2023]] |
| **Expert-Guided DRL** | RL guidé | 10–20 K | 40–80 KB | 10–20 KB | ❌ | GPU | Serveur | Optimal | 8,8× conv. | [[Papers/2025/efficient-rl-expert-guided-hvac/expert-rl-2025\|2025]] |
| **DDPG** | RL acteur-critique | 15–20 K | 60–80 KB | 15–20 KB | ❌ | GPU | Serveur | +15 % / DQN | ±0,5 °C | [[Papers/2024/du-ddpg-multizone-residential/du-ddpg-2024\|2024]] |
| **BDQ (OCTOPUS)** | RL branching | 25–35 K | 100–140 KB | 25–35 KB | ❌ | GPU | Serveur | 14,26 % | 82–88 % | [[Papers/2024/octopus-holistic-building-drl/octopus-2024\|2024]] |
| **Random Forest** | ML classique | ~N/A | 1,4 MB flash | ✅ natif | ✅ natif | CPU | **ESP32** | N/A | R²=0,923 | [[Papers/2026/tinyml-occupancy-esp32/tinyml-esp32-2026\|2026]] |
| **TDL sub-KB** | DL ultra-léger | <qq K | **<1 KB** | ✅ | ✅ | CPU | **Ultra-MCU** | N/A | Élevée | [[Papers/2026/sustainability-tiny-deep-learning/sustainability-tdl-2026\|2026]] |
| **LSTM léger** | RNN | **50 851** | **203 KB** | **~51 KB** | ❌ | CPU/GPU | **MCU** | N/A | R²=0,90–0,95 | [[Papers/2025/ml-indoor-temp-lightweight/ml-indoor-temp-2025\|2025]] |
| **PSO-LSTM** | RNN+métaheuristique | 30–40 K | 120–160 KB | 30–40 KB | ❌ | CPU | Edge | N/A | 94,8 % acc. | [[Papers/2023/occupancy-lstm-optimized/occupancy-lstm-2023\|2023]] |
| **MH-LSTM** | RNN multi-tête | 50 K | 200 KB | ~50 KB | ❌ | CPU/GPU | Edge | N/A | **92 %** class. | [[Papers/2024/cho-mh-lstm-personalized-comfort/cho-mh-lstm-2024\|2024]] |
| **CNN-LSTM + Attn** | Hybride | 50–70 K | 200–280 KB | 50–70 KB | ❌ | GPU | Edge haut | N/A | +30–45 % vs LSTM | [[Papers/2021/cnn-lstm-predictive-indoor-temp/cnn-lstm-2021\|2021]] |
| **BO CNN-M-LSTM** | Hybride | 40–60 K | 160–240 KB | 40–60 KB | ❌ | GPU | Serveur/edge | N/A | R²=0,85–0,92 | [[Papers/2025/bayesian-cnn-m-lstm-comfort/cnn-m-lstm-2025\|2025]] |
| **DT LSTM-Attention** | Hybride+physique | 80–120 K | 320–480 KB | 80–120 KB | ❌ | GPU | Serveur | **14 %** | R²=0,85–0,92 | [[Papers/2025/digital-twin-lstm-hvac/digital-twin-lstm-2025\|2025]] |
| **PID** | Contrôle classique | 3 params | Négligeable | ✅ natif | ✅ natif | N/A | **Tout MCU** | Référence 0 % | 1–2 °C violations | [[Papers/2025/rl-vs-pid-hvac-simulation/rl-pid-2025\|2025]] |

---

## 🔑 Constat clé sur la quantisation

> **Aucun des papiers HVAC analysés ne teste explicitement la quantisation de ses modèles.** C'est un **gap de recherche** majeur et une opportunité directe pour le projet de thermostat Edge AI.

La littérature générale TinyML montre que :
- **INT8** fonctionne très bien pour les modèles RL (DQN) : 2,2–5,4× speedup, précision maintenue.
- **LSTM 16×8** est préférable à 8×8 pur pour éviter la dégradation.
- **Random Forest** est nativement adapté au MCU (pas de quantisation nécessaire).
- **Pruning + quantisation combinés** peuvent réduire un modèle 10–20× tout en maintenant >95 % de précision.

---

*Catalogue généré le 2026-02-19 — Basé sur 27 papiers scientifiques + benchmarks matériels publiés*
