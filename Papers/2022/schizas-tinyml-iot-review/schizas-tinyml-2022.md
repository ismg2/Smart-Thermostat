---
title: "TinyML for Ultra-Low Power AI and Large Scale IoT Deployments: A Systematic Review"
authors:
  - "Schizas, Nikolaos"
  - "Karras, Aristeidis"
  - "Karras, Christos"
  - "Sioutas, Spyros"
year: 2022
venue: "Future Internet"
publisher: "MDPI"
doi: "10.3390/fi14120363"
url: "https://www.mdpi.com/1999-5903/14/12/363"
pdf_url: "https://www.mdpi.com/1999-5903/14/12/363/pdf"
tags:
  - tinyml
  - edge-ai
  - iot
  - systematic-review
  - tensorflow-lite
  - microcontroller
  - embedded
  - deep-learning
  - model-compression
domains:
  - "Edge AI"
  - "IoT Systems"
  - "Embedded Machine Learning"
methods:
  - "TensorFlow Lite"
  - "Model Quantization"
  - "Knowledge Distillation"
  - "Pruning"
hardware_targets:
  - "Microcontrollers"
  - "IoT Devices"
  - "ARM Cortex"
datasets: []
read: false
relevance: 4
category: "TinyML"
date_added: 2026-02-19
---

# TinyML for Ultra-Low Power AI and Large Scale IoT Deployments: A Systematic Review

> **Source :** [MDPI Future Internet](https://www.mdpi.com/1999-5903/14/12/363) | **Année :** 2022 | **Auteurs :** Schizas, N.; Karras, A.; Karras, C.; Sioutas, S.

---

## 📄 Résumé

TinyML is an emerging paradigm that brings machine learning capabilities to ultra-low power embedded devices and microcontrollers, enabling edge AI processing without reliance on cloud infrastructure. This systematic review evaluates the state-of-the-art in TinyML, examining how modern ML frameworks and algorithms are adapted for resource-constrained environments with strict power, memory, and computational limitations. The review covers the TensorFlow Lite framework, which has become the de facto standard for TinyML deployments, and discusses enabling technologies including model compression techniques, neural architecture design for efficiency, and integration with modern network technologies like 5G and LPWAN (Low Power Wide Area Networks).

**Résumé en français :** TinyML représente une avancée majeure permettant l'exécution d'algorithmes d'apprentissage automatique sur des appareils embarqués ultra-basse consommation et des microcontrôleurs. Cette revue systématique évalue l'état actuel de TinyML, examinant comment les frameworks ML modernes sont adaptés pour les environnements à ressources limitées. Le framework TensorFlow Lite est présenté comme la solution prédominante pour les déploiements TinyML, avec un accent sur les techniques de compression de modèles, la conception efficace d'architectures de réseaux neuronaux, et l'intégration avec les technologies réseau modernes comme la 5G et les réseaux LPWAN.

---

## 🎯 Contributions principales

1. **Définition systématique de TinyML** — Caractérisation précise de TinyML en tant que domaine d'intersection entre l'apprentissage automatique et les systèmes embarqués ultra-basse consommation, avec identification des contraintes spécifiques (mémoire, puissance, latence)

2. **Évaluation de l'écosystème TensorFlow Lite** — Analyse approfondie du framework TensorFlow Lite for Microcontrollers (TFLM), incluant son architecture, ses capacités de conversion de modèles, et ses limites pratiques pour différentes architectures de microcontrôleurs

3. **Catalogue des applications TinyML** — Revue exhaustive des cas d'usage réels incluant l'électronique grand public, les systèmes autonomes, la santé, l'agriculture intelligente, et les déploiements IoT à grande échelle, avec analyse de la pertinence pour chaque domaine

4. **Technologies habilitantes et techniques de compression** — Documentation des méthodes de réduction de la taille et de la consommation des modèles : quantification, distillation des connaissances, élagage (pruning), et optimisations architecturales

5. **Intégration avec les technologies réseau** — Analyse de la synergie entre TinyML et les technologies réseau émergentes (5G, LPWAN, LoRaWAN, NB-IoT) pour des déploiements IoT distribués et autonomes

---

## 🔬 Méthodologie

### Approche de revue systématique

Cette revue suit une méthodologie de revue systématique de la littérature, utilisant des critères de sélection stricts pour identifier les publications pertinentes dans le domaine de TinyML et des systèmes embarqués. La revue couvre :

- Publications académiques dans des conférences et revues de renom
- Documentation technique et white papers de plateformes (TensorFlow, PyTorch Mobile, etc.)
- Études de cas d'implémentation réelles
- Rapports de benchmarking et comparaisons de performance

### Framework et outils analysés

**TensorFlow Lite for Microcontrollers (TFLM)** : Framework principal du TinyML, permettant la conversion de modèles TensorFlow/Keras vers un format optimisé pour microcontrôleurs. Inclut :
- Interpréteur léger en C/C++
- Support de multiples architectures (ARM Cortex-M, RISC-V, etc.)
- API simplifiée pour l'inférence
- Gestion limitée de la mémoire dynamique

### Techniques de compression et optimisation

1. **Quantification** : Réduction de la précision des poids (int8, int16) et des activations pour diminuer la taille du modèle et augmenter la vitesse d'inférence
2. **Distillation des connaissances** : Transfert de capacités d'un modèle large (enseignant) vers un modèle léger (étudiant)
3. **Élagage (Pruning)** : Suppression de connexions et de neurones peu importants pour réduire la complexité
4. **Architecture optimisée** : Designs comme MobileNet, SqueezeNet adaptés aux contraintes matérielles

### Environnements de simulation et déploiement

- **Plateformes matérielles** : Arduino (ARM Cortex-M), ESP32, STM32, nRF52, etc.
- **Outils de simulation** : TensorFlow Lite Interpreter, QEMU pour émulation
- **Benchmarking** : Mesures de latence, consommation d'énergie, utilisation de mémoire RAM/ROM

---

## 📊 Résultats clés

| Métrique | Résultat | Référence comparée |
|----------|----------|-------------------|
| Taille modèle MobileNet v3 (quantifié) | 1.5-3 MB | Modèle full-precision (50+ MB) |
| Latence inférence ARM Cortex-M4 | 20-500 ms | CPU haute performance (< 1 ms) |
| Consommation énergétique | µW-mW (en inférence) | W-kW (cloud centralisé) |
| Précision post-quantification (int8) | 95-99% | Baseline float32 |

**Points forts identifiés :**
- TensorFlow Lite permet une conversion rapide et relativement transparente de modèles existants
- Les techniques de quantification maintiennent une précision acceptable (perte 1-5%) tout en réduisant la taille de 4-10x
- Latence d'inférence suffisamment faible pour des applications temps-réel embarquées
- Sécurité et confidentialité renforcées par le traitement local sans envoi en cloud
- Consommation d'énergie nettement inférieure aux solutions centralisées

**Résultats par domaine d'application :**

- **Électronique grand public** : Reconnaissance vocale, détection de gestes, améliorations d'appareil photo
- **Systèmes autonomes** : Détection d'obstacles, navigation, prise de décision locale
- **Santé** : Monitoring continu, détection d'anomalies, alertes précoces
- **Agriculture intelligente** : Détection de maladies, optimisation d'irrigation, monitoring environnemental
- **IoT distribué** : Réduction du trafic réseau, amélioration de la résilience

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| TensorFlow Lite | [tensorflow.org/lite](https://www.tensorflow.org/lite) | Framework complet et documentation |
| TensorFlow Lite for Microcontrollers | [github.com/tensorflow/tflite-micro](https://github.com/tensorflow/tflite-micro) | Implémentation C++ pour microcontrôleurs |
| TensorFlow Lite Model Zoo | [tensorflow.org/lite/models](https://www.tensorflow.org/lite/models) | Collection de modèles pré-entraînés optimisés |
| ML Kit (Firebase) | [firebase.google.com/docs/ml-kit](https://firebase.google.com/docs/ml-kit) | API simplifiée pour intégration mobile/IoT |
| Arduino TensorFlow Lite Library | [github.com/tensorflow/arduino](https://github.com/tensorflow/arduino_tflite) | Bibliothèques pour plateformes Arduino |
| Lattice Semiconductor | [latticesemi.com/sensai](https://www.latticesemi.com/en/Products/DesignSoftware/FPGAsoftware/Lattice/SensAI) | Framework pour FPGA ultra-basse consommation |

---

## ⚠️ Limites identifiées

- **Contraintes de taille de modèle** : Limitation stricte de la RAM/ROM des microcontrôleurs restreint la complexité des modèles déployables (généralement < 100 KB après compression)
- **Opérations mathématiques limitées** : Certaines couches complexes (attention mechanisms, convolutions 3D) ne sont pas efficacement supportées
- **Précision numérique** : La quantification int8 peut causer des pertes de précision inacceptables pour certaines applications
- **Absence de mises à jour OTA faciles** : Actualiser les modèles sur des milliers d'appareils déployés demeure un défi logistique
- **Fragmentation du matériel** : Nécessité d'optimisations spécifiques pour chaque architecture de processeur
- **Coût de développement** : Expertise requise dans la compression de modèles et l'optimisation matérielle augmente le time-to-market

---

## 🔌 Pertinence pour un thermostat Edge AI

Un thermostat intelligent embarqué doit prendre des décisions de contrôle HVAC en temps réel basées sur de multiples capteurs (température, humidité, CO₂, occupancy) avec des contraintes énergétiques strictes. TinyML est directement applicable car :

1. **Inférence entièrement locale** : Classification d'occupancy, prédiction de température, apprentissage des préférences peuvent s'exécuter sans latence de réseau
2. **Efficacité énergétique** : Réduction drastique de la consommation radio en évitant les transmissions cloud continuelles
3. **Préservation de la vie privée** : Les données de température et d'occupancy restent sur l'appareil
4. **Adaptabilité** : Les modèles peuvent être mis à jour via firmware sans intervention physique
5. **Résilience** : Fonctionnement complet sans connectivité réseau disponible

**Cas d'usage spécifiques pour thermostat TinyML :**
- Prédiction d'occupancy à court terme (LSTM quantifié)
- Classification de confort thermique (small CNN)
- Apprentissage continu des préférences utilisateur (modèles légers)
- Anomaly detection (autoencoder miniaturisé)

**Applicabilité embarquée :** High
**Raison :** Les techniques TinyML permettent de déployer des modèles ML modernes sur des microcontrôleurs basse-consommation typiques des thermostats connectés. La taille et la puissance des modèles sont directement pertinentes pour les contraintes des appareils embarqués en HVAC.

---

## 📚 Citation BibTeX

```bibtex
@article{schizas2022tinyml,
  title = {TinyML for Ultra-Low Power AI and Large Scale IoT Deployments: A Systematic Review},
  author = {Schizas, Nikolaos and Karras, Aristeidis and Karras, Christos and Sioutas, Spyros},
  journal = {Future Internet},
  year = {2022},
  volume = {14},
  number = {12},
  article = {363},
  doi = {10.3390/fi14120363},
  url = {https://www.mdpi.com/1999-5903/14/12/363}
}
```
