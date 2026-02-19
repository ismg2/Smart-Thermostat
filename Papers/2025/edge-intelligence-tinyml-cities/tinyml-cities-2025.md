---
title: "Edge Intelligence in Urban Landscapes: Reviewing TinyML Applications for Connected and Sustainable Smart Cities"
authors:
  - "Trigkas, Marios"
  - "Piromalis, Dimitrios"
year: 2025
venue: "Electronics"
publisher: "MDPI"
doi: "10.3390/electronics14142890"
url: "https://www.mdpi.com/2079-9292/14/14/2890"
pdf_url: "https://www.mdpi.com/2079-9292/14/14/2890/pdf"
tags:
  - tinyml
  - edge-ai
  - smart-city
  - esp32
  - stm32
  - quantization
  - pruning
  - systematic-review
  - embedded
  - iot
methods:
  - "Model Quantization (INT8)"
  - "Network Pruning"
  - "Architectural Simplification"
domains:
  - "Smart Cities"
  - "Urban IoT"
  - "Edge Computing"
hardware_targets:
  - "ESP32"
  - "STM32 Nucleo"
  - "Arduino BLE 33"
  - "Portenta H7"
  - "ESP-EYE"
datasets:
  - name: "Literature Review Database"
    url: ""
    description: "66 peer-reviewed studies (2019-2024)"
read: false
relevance: 4
category: "TinyML"
date_added: 2026-02-19
---

# Edge Intelligence in Urban Landscapes: Reviewing TinyML Applications for Connected and Sustainable Smart Cities

> **Source :** [MDPI Electronics](https://www.mdpi.com/2079-9292/14/14/2890) | **Year :** 2025 | **Authors :** Trigkas, Piromalis

---

## 📄 Résumé

This comprehensive systematic review analyzes 66 peer-reviewed studies (2019-2024) on TinyML applications in smart cities, providing a state-of-the-art assessment of edge intelligence technologies for urban environments. The review covers hardware-software co-design strategies with emphasis on INT8 quantization, network pruning, and architectural simplification techniques that enable deep learning deployment on severely resource-constrained microcontrollers. Detailed analysis of hardware platforms includes ESP32, STM32 Nucleo, Arduino BLE 33, Portenta H7, and ESP-EYE, with measured inference latencies ranging from 21ms to >1s depending on model complexity. Application domains analyzed include urban mobility (29 studies), public safety (17 studies), environmental monitoring (10 studies), waste management (6 studies), and infrastructure health (4 studies). The review demonstrates steady growth in TinyML adoption, with peak research activity in 2024, and highlights key techniques for achieving sub-kilobyte to kilobyte-scale memory footprints while maintaining acceptable prediction accuracy for real-time urban IoT deployments.

Cet examen systématique exhaustif analyse 66 études (2019-2024) sur les applications TinyML dans les villes intelligentes. La revue couvre des stratégies de co-conception matériel-logiciel, avec emphasis sur quantification INT8, élagage réseau, et simplification architecturale. Les latences d'inférence mesurées varient de 21ms à >1s selon complexité. Les domaines vont de la mobilité urbaine (29 études) à la surveillance environnementale (10 études).

---

## 🎯 Contributions principales

1. **Revue systématique TinyML (2019-2024)** — Analyse exhaustive de 66 études peer-reviewed couvrant tous aspects du déploiement deep learning sur microcontrôleurs contraints, identification de tendances et bonnes pratiques
2. **Techniques Hardware-Software Co-design** — Documentation complète de stratégies pratiques (quantization INT8, pruning, architecture simplification) avec métriques d'efficacité (latence, mémoire, accuracy)
3. **Mapping Applications → Hardware → Performance** — Tableau de correspondance détaillé entre use-cases urbains, plateformes matérielles déployées, et métriques de performance réelle (21ms-1000ms latences)

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

**Hardware-Software Co-Design Techniques:**

1. **INT8 Quantization (Full Integer):**
   - Conversion weights/activations : FP32 → INT8
   - Réduction taille mémoire : 4X (ex. 4 MB → 1 MB)
   - Réduction d'inférence latence : 1.5-3X (integer ops plus rapides)
   - Perte accuracy : typiquement <2-5% si bien calibré

   ```
   Quantization = (value - min) / (max - min) × 255 (INT8 range)
   ```

2. **Network Pruning :**
   - Removal poids < threshold
   - Structured pruning : supprime canaux entiers (plus matériel-friendly)
   - Unstructured pruning : supprime weights individuels
   - Compression réalisable : 30-70% réduction paramètres avec <2% accuracy loss

3. **Architectural Simplification :**
   - Réduction depth (couches)
   - Réduction width (neurones par couche)
   - Utilisation MobileNet, SqueezeNet, ShuffleNet au lieu ResNet
   - Typical: 1-10 MB vs. 100+ MB full models

4. **Knowledge Distillation (optionnel):**
   - Teacher network grand (cloud) → Student network petit (edge)
   - Student appprend à matcher teacher outputs
   - Student + teacher perfor proche malgré réduction taille

### Architecture du système

**Platform Comparison Table (from Review):**

| Hardware | CPU | RAM | Flash | TinyML Framework | Typical Apps |
|----------|-----|-----|-------|------------------|--------------|
| ESP32 | Dual Xtensa LX7 240MHz | 520 KB SRAM | 4-16 MB | TFLite Micro | Motion, sound, sensors |
| STM32L476 | ARM Cortex-M4 80MHz | 128 KB | 256-512 KB | X-CUBE-AI | Industrial IoT |
| Arduino BLE 33 | ARM Cortex-M4 64MHz | 256 KB | 1 MB | TFLite Micro | Wearables, gesture |
| Portenta H7 | ARM Cortex-M7 480MHz | 1 MB | 2 MB | TFLite Micro | Complex models |
| ESP-EYE | ESP32 + OV2640 camera | 520 KB + PSRAM | 4 MB | TFLite Micro | Vision (face detect) |

**Deployment Pipeline (Typical):**

```
1. Full Model Training (Cloud)
   ├─ Dataset collection
   ├─ Architecture design
   └─ FP32 training & validation

2. Model Optimization
   ├─ Quantization (INT8)
   ├─ Pruning
   └─ Knowledge distillation (optional)

3. Framework Conversion
   ├─ Convert to TFLite (TensorFlow)
   ├─ Export to ONNX or .tflite
   └─ Validate accuracy post-conversion

4. Microcontroller Compilation
   ├─ TFLite Micro code generation
   ├─ Link with embedded runtime
   └─ Burn to device flash

5. Inference On-Device
   ├─ Read sensor input
   ├─ Pre-process (normalize)
   ├─ Run inference (<100ms typically)
   ├─ Post-process (argmax, threshold)
   └─ Execute control action
```

**TinyML Framework Ecosystem:**

- **TensorFlow Lite Micro :** Official, C++, minimal dependencies
- **X-CUBE-AI (STM32) :** Hardware-optimized for STM32 MCUs
- **Edge Impulse :** Graphical platform + auto-optimization
- **Apache TVM :** Compiler optimization for edge
- **ONNX Runtime :** Framework-agnostic model format

### Environnement de test / Simulation

**Literature Review Methodology:**

- **Search databases :** IEEE Xplore, arXiv, ACM, Springer, MDPI
- **Time period :** 2019-2024 (6 years)
- **Keywords :** TinyML, edge AI, IoT, microcontroller, embedded ML, quantization
- **Selection criteria :** Peer-reviewed, focuses on constrained devices (<10 MB flash)
- **Total papers screened :** ~500, final included : 66

**Application Domain Breakdown (66 studies):**

| Domain | Count | Examples |
|--------|-------|----------|
| Urban Mobility/Transport | 29 | Pedestrian detection, vehicle tracking, traffic lights |
| Public Safety | 17 | Fire/gas detection, intrusion alarms, emergency response |
| Environmental Monitoring | 10 | Air quality, noise level, pollution sensors |
| Waste Management | 6 | Trash bin level detection, waste sorting |
| Infrastructure Health | 4 | Bridge/building damage, pothole detection |

**Hardware Deployment Stats (from 66 studies):**

- 32 studies : constrained microcontrollers (<1 MB RAM)
- 36 studies : optimized models for resource-limited (<10 MB)
- Most common : ESP32 (appeared in 18 studies)
- Inference latency range : 21ms (simple model) to >1000ms (complex model)
- Accuracy retention post-quantization : 92-99% vs. baseline FP32

### Hyperparamètres clés

**Quantization Parameters:**

| Parameter | Value Range | Impact |
|-----------|-------------|--------|
| Bits (INT8) | 8 bits | Standard for embedded |
| Calibration method | Min-max, KL-divergence | Affects accuracy post-quant |
| Calibration data | 100-1000 samples | Need representative samples |
| Per-channel vs. per-layer | Both | Per-channel better but slower |

**Pruning Parameters:**

| Parameter | Value Range | Impact |
|-----------|-------------|--------|
| Pruning ratio | 30-70% | Balance compression vs. accuracy |
| Pruning method | Magnitude, gradient-based | Magnitude simpler, gradient better |
| Fine-tuning after pruning | 5-20 epochs | Restore accuracy post-pruning |

**Model Architecture Parameters (for Embedded):**

- MobileNet v3 Small : ~2.5 M parameters, ~5 MB FP32
- SqueezeNet : ~1.2 M parameters, ~5 MB FP32
- ShuffleNet : ~2.3 M parameters, ~9 MB FP32
- Typical target : <1-10 M parameters for edge
- Post-quantization INT8 : 4X reduction (2.5 MB → 625 KB)

---

## 📊 Résultats clés

| Métrique | Range | Notes |
|----------|-------|-------|
| Inference Latency | 21ms - 1000+ ms | Dépend hardware + model complexity |
| Model Size (post-quant) | 100 KB - 10 MB | After INT8 + pruning |
| Accuracy Retention | 92-99% | vs. FP32 baseline |
| Energy per inference | 0.1-10 mJ | Depends on hardware |
| Memory overhead | 50-500 KB | Runtime buffers |

**Key Findings from Literature:**

1. **Growth Trajectory:** Research publications peaked in 2024 (15+ new studies), showing exponential adoption curve

2. **Quantization Effectiveness:**
   - INT8 quantization achieves 4X memory reduction
   - Accuracy typically drops <2-5% for vision/audio
   - Fine-tuning post-quantization critical (recovers 80-90% lost accuracy)

3. **Hardware Popularity:**
   - ESP32: Most cited due to cost (<$10), dual-core, PSRAM options
   - STM32: Industrial applications, hardened libraries
   - Arduino BLE 33: Wearables, Bluetooth integration
   - Portenta H7: Complex models requiring more compute

4. **Latency Insights:**
   - Simple gesture recognition : 21-50 ms (ESP32)
   - Audio classification : 50-200 ms (keyword spotting)
   - Image classification : 200-1000+ ms (depends on resolution, model)
   - Video processing : >1000 ms (typically not real-time on single MCU)

5. **Framework Maturity:**
   - TensorFlow Lite Micro: Most studied, mature, multi-platform
   - Edge Impulse: Growing adoption due to ease-of-use
   - X-CUBE-AI: Strong in industrial/STM32 ecosystem

**Accuracy vs. Latency Trade-offs:**

- Higher accuracy models → larger → slower inference
- Quantization reduces latency but risks accuracy
- Sweet spot often at 85-95% accuracy retention, 3-5X latency improvement

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| TensorFlow Lite Micro | [https://www.tensorflow.org/lite/microcontrollers](https://www.tensorflow.org/lite/microcontrollers) | Official ML framework for microcontrollers |
| Edge Impulse | [https://edgeimpulse.com](https://edgeimpulse.com) | End-to-end ML platform for embedded |
| X-CUBE-AI (STM32) | [https://www.st.com](https://www.st.com) | STM32 AI framework & libraries |
| Arduino IoT Cloud | [https://create.arduino.cc](https://create.arduino.cc) | Arduino development & deployment |
| ONNX Format | [https://onnx.ai](https://onnx.ai) | Model interchange format for portability |

---

## ⚠️ Limites identifiées

- Nécessité d'accès aux architectures détaillées des modèles (souvent propriétaires)
- Pas tous les frameworks opensource (certains propriétaires à constructeurs MCU)
- Calibration quantization complexe : requires sufficient representative data
- Transferabilité modèles entre plateformes (ex. ESP32 → STM32) nécessite recompilation
- Pas d'analyse approfondie coûts énergétiques réels (estimations seulement)
- Sécurité & privacy aspects peu couverts dans littérature

---

## 🔌 Pertinence pour un thermostat Edge AI

**Très pertinent comme guide de déploiement pratique.**

Cette revue systématique fournit le "roadmap" exact pour transformer un modèle ML complexe en application embarquée sur thermostat intelligent :

**Applications directes :**

1. **Occupancy Detection (TinyML):**
   - Utiliser motion sensor + audio classification (keyword spotting)
   - Model taille : ~200-500 KB post-quantization
   - Latence : 50-100 ms acceptable
   - Hardware : ESP32 sufficient

2. **Temperature Forecasting Lightweight :**
   - Déployer LSTM quantized (~300 KB)
   - Latency : <100 ms
   - Memory : <500 KB runtime

3. **Comfort Prediction (Simplified) :**
   - Utiliser architecture légère (ex. MobileNet-like)
   - Entrées : temp, humidity, hour-of-day
   - Output : comfort index (-3 to +3)
   - Taille : <1 MB

**Hardware Recommendations (based on review):**

- **Budget ($15-25) :** ESP32 + INT8 quantized model
- **Mid-range ($30-50) :** STM32H7 Nucleo + TinyML
- **Premium ($50-100) :** Portenta H7 + complex model + Bluetooth

**Applicabilité embarquée :** Very High
**Raison :** Cette revue est fundamentale pour thermostat Edge AI. Couvre toutes techniques (quantization, pruning, framework selection). Hardware comparisons directement applicables. Performance metrics (latence, accuracy, memory) permettent trade-off design decisions.

---

## 📚 Citation BibTeX

```bibtex
@article{trigkas2025edge,
  title={Edge Intelligence in Urban Landscapes: Reviewing TinyML Applications for Connected and Sustainable Smart Cities},
  author={Trigkas, Marios and Piromalis, Dimitrios},
  journal={Electronics},
  volume={14},
  number={14},
  pages={2890},
  year={2025},
  doi={10.3390/electronics14142890},
  publisher={MDPI}
}
```
