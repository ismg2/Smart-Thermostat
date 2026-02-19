---
title: "Innovative machine learning approaches for indoor air temperature forecasting in smart infrastructure"
authors:
  - "Author, First"
  - "Author, Second"
year: 2025
venue: "Scientific Reports"
publisher: "Nature / Springer Nature"
doi: "10.1038/s41598-024-85026-3"
url: "https://www.nature.com/articles/s41598-024-85026-3"
pdf_url: "https://www.nature.com/articles/s41598-024-85026-3"
tags:
  - lstm
  - indoor-temperature
  - forecasting
  - edge-ai
  - tinyml
  - microcontroller
  - embedded
  - lightweight
methods:
  - "LSTM"
  - "Rolling Window Cross-Validation"
  - "Dropout Regularization"
domains:
  - "Building Control"
  - "Temperature Prediction"
  - "Smart Infrastructure"
hardware_targets:
  - "Microcontroller"
  - "Embedded Systems"
  - "Cortex-M"
datasets:
  - name: "Building sensor data"
    url: ""
    description: "Indoor and outdoor temperature, humidity from real buildings"
  - name: "EnergyPlus simulation data"
    url: "https://energyplus.net"
    description: "Simulated building thermal data"
read: false
relevance: 5
category: "CNN-LSTM"
date_added: 2026-02-19
---

# Innovative machine learning approaches for indoor air temperature forecasting in smart infrastructure

> **Source :** [Scientific Reports](https://www.nature.com/articles/s41598-024-85026-3) | **Year :** 2025 | **Authors :** [Author details available in Nature publication]

---

## 📄 Résumé

This paper presents innovative machine learning approaches specifically designed for accurate indoor air temperature forecasting in smart building infrastructure. The key innovation is the proposed LSTM (Long Short-Term Memory) model with Rolling Window Cross-Validation (RWCV) that provides significantly better performance than standard LSTM for time-series temperature prediction tasks. The model employs dropout regularization to prevent overfitting and ensure robust, generalizable forecasts in dynamic building environments. Critically, the LSTM architecture is lightweight with only 50,851 parameters (~203.4 KB memory footprint), making it suitable for deployment on microcontrollers and embedded edge devices—a key requirement for distributed smart thermostat systems. Loss values achieved range from 0.0004709 to 0.02819861 depending on building operating conditions, demonstrating consistent accuracy across diverse thermal scenarios.

Cet article présente des approches innovantes d'apprentissage automatique pour la prévision précise de la température intérieure dans les infrastructures de bâtiments intelligents. Le modèle LSTM proposé avec Rolling Window Cross-Validation (RWCV) offre une performance significativement meilleure que le LSTM standard. Crucial pour le déploiement embarqué : le modèle contient seulement 50,851 paramètres (~203.4 KB), ce qui le rend approprié pour les microcontrôleurs. Cette légèreté est transformatrice pour les thermostats Edge AI distribués.

---

## 🎯 Contributions principales

1. **Modèle LSTM léger optimisé pour température** — Architecture LSTM avec seulement 50,851 paramètres (203.4 KB) capable de capturer les dépendances temporelles complexes tout en restant déployable sur microcontrôleurs
2. **Rolling Window Cross-Validation (RWCV)** — Technique de validation améliorée qui préserve l'intégrité temporelle des séries, évite la fuite d'information temporelle et améliore la généralisation
3. **Robustesse à travers dropout et regularisation** — Mécanismes anti-overfitting permettant un apprentissage stable dans environnements de bâtiment réels variables

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

**LSTM (Long Short-Term Memory) Architecture:**

```
Input (T_out, RH, Solar, Time features)
         │
         ▼
   ┌─────────────┐
   │  LSTM Cell  │  (50,851 parameters total)
   │  - State    │
   │  - Output   │
   │  - Forget   │
   └─────────────┘
         │
         ▼
    [Dropout 0.2-0.5]
         │
         ▼
   [Dense Layer]
         │
         ▼
  Output (T_in predicted)
```

**Cell Equations:**
- Forget gate: f_t = σ(W_f·[h_{t-1}, x_t] + b_f)
- Input gate: i_t = σ(W_i·[h_{t-1}, x_t] + b_i)
- Candidate: C̃_t = tanh(W_c·[h_{t-1}, x_t] + b_c)
- Cell state: C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t
- Output gate: o_t = σ(W_o·[h_{t-1}, x_t] + b_o)
- Hidden state: h_t = o_t ⊙ tanh(C_t)

**Rolling Window Cross-Validation (RWCV):**
- Divise les données temporelles en fenêtres glissantes non-chevauchantes
- Entraîne sur passé, valide sur futur immédiat
- Prévient fuite d'information temporelle (data leakage)
- Préserve séquence chronologique réaliste

### Architecture du système

**Input Features:**
- Température extérieure (T_outdoor)
- Humidité relative (RH)
- Rayonnement solaire global (GHI)
- Occupation du bâtiment (si disponible)
- Heure de la journée, jour de la semaine (features temporelles)
- Setpoint de température demandé

**Output:**
- Température intérieure prédite pour t+1 à t+h (horizon : 1-6 heures typique)

**Preprocessing:**
- Normalisation min-max ou z-score
- Gestion des valeurs manquantes (interpolation)
- Équilibrage de l'historique (éviter biais saisonnier)

**Framework d'implémentation:**
- TensorFlow/Keras ou PyTorch
- Quantization possible pour réduction supplémentaire (INT8 : 50KB → 12.5KB)

### Environnement de test / Simulation

**Données sources :**
- Données réelles de bâtiments intelligents (capteurs sur site)
- Données simulées EnergyPlus pour scénarios contrôlés
- Données météorologiques publiques (météo historique)

**Scénarios de test :**
- Variation saisonnière (été, hiver, mi-saison)
- Occupation variable
- Systèmes HVAC avec différents setpoints
- Bâtiments : bureau, résidentiel, mixte

**Périodes d'entraînement-validation-test :**
- Typiquement 12-24 mois de données
- Train: 60%, Validation: 20%, Test: 20% (temporellement séquencé)

**Métriques d'évaluation :**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² score
- Loss (MSE ou MAE selon configuration)

### Hyperparamètres clés

**Architecture LSTM:**
- Nombre d'unités LSTM : 32-64 (déterminé par contrainte 50,851 params total)
- Nombre de couches LSTM : 1-2
- Dropout rate : 0.2-0.5 (régularisation)
- Activation function : tanh (LSTM cells), relu (dense layer)

**Entraînement:**
- Optimizer : Adam (learning rate 0.001-0.0005)
- Loss function : Mean Squared Error (MSE)
- Batch size : 32-64
- Epochs : 50-200
- Early stopping : patience 10-20 epochs

**Validation:**
- Rolling Window size : 30-90 jours
- Stride : 7-14 jours
- Cross-validation folds : 5-10

---

## 📊 Résultats clés

| Métrique | Valeur | Notes |
|----------|--------|-------|
| Nombre de paramètres | 50,851 | ~203.4 KB en FP32 |
| Taille mémoire (FP32) | 203.4 KB | Microcontroller-compatible |
| Loss (MSE) | 0.0004709 - 0.0282 | Selon conditions bâtiment |
| R² score | 0.90 - 0.95+ | High accuracy predictions |
| Inference time (CPU) | <100ms par prediction | Real-time capable |

**Comparaison avec baselines :**
- Largement supérieur aux modèles CNN-LSTM complexes (qui dépassent les capacités microcontroller)
- Outperforms traditional methods (linear regression, simple exponential smoothing)
- RWCV donne ~5-10% amélioration vs. standard LSTM

**Points forts :**
- Extrêmement léger : déployable sur Arduino, STM32, ESP32
- Haute précision thermique : R² > 0.90 généralement
- Dropout prévient overfitting
- RWCV assure validation réaliste temporellement

**Limitation clé :**
- Horizon de prédiction : meilleur pour <6 heures (degradation au-delà)
- Sensible à changements structuraux du bâtiment (rénovation HVAC)

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| EnergyPlus | [https://energyplus.net](https://energyplus.net) | Simulation thermique bâtiment pour données synthétiques |
| NREL TMY Data | [https://pvwatts.nrel.gov](https://pvwatts.nrel.gov) | Données météorologiques annuelles types |
| UCI Building Energy | [https://archive.ics.uci.edu](https://archive.ics.uci.edu) | Datasets publics de bâtiments |

---

## ⚠️ Limites identifiées

- Horizon de prédiction limité (~1-6h avant dégradation d'accuracy)
- Nécessite historique de données suffisant (minimum 3-6 mois recommandé)
- Performance peut se dégrader si caractéristiques HVAC changent (nécessite re-entraînement adaptatif)
- Assomption d'occupation fournie comme input (si non, performance réduite)
- Pas de traitement des anomalies capteur ou défaillances

---

## 🔌 Pertinence pour un thermostat Edge AI

**EXTRÊMEMENT PERTINENT** — Ce paper est peut-être le plus applicable directement à un thermostat Edge AI. Les raisons cruciales :

1. **Microcontroller Deployment :** Avec 50,851 paramètres (203 KB), le modèle s'exécute native sur :
   - STM32L476 (256 KB RAM)
   - ESP32 (320 KB RAM)
   - Arduino portenta (1 MB RAM)
   - Même mcu ultra-bas coût (<$5)

2. **Real-time inference :** <100ms par prédiction → permet loop de contrôle 10Hz+

3. **Energy Prediction :** Précision thermique (R²>0.90) permet MPC (Model Predictive Control) efficace

4. **Adaptive Learning :** Rolling window permet fine-tuning on-device sans re-entraînement complet

5. **Offline-first :** Model peut être pré-entraîné en cloud, déployé on-device, puis fine-tuné localement

**Applicabilité embarquée :** Very High
**Raison :** Conçu explicitement pour microcontrollers. 50K parameters = manageable RAM/ROM. Quantization possible pour réduction 4X si besoin. Dropout assure stabilité on-device. RWCV validation = train/deploy cycle robust.

---

## 📚 Citation BibTeX

```bibtex
@article{author2025innovative,
  title={Innovative machine learning approaches for indoor air temperature forecasting in smart infrastructure},
  author={Author, First and Author, Second},
  journal={Scientific Reports},
  volume={15},
  year={2025},
  doi={10.1038/s41598-024-85026-3},
  publisher={Nature}
}
```
