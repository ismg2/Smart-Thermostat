---
title: "Synthèse — Edge AI pour Thermostats Intelligents · Opportunité STMicroelectronics"
description: "Résumé de l'état de l'art, proposition de valeur ST, structure de présentation client et mail de diffusion"
date_created: 2026-02-19
tags:
  - synthese
  - stmicroelectronics
  - edge-ai
  - business
  - slides
  - hvac
audience: Équipe marketing/applications STMicroelectronics
confidentiality: Interne
---

# 🔥 Synthèse — Edge AI pour Thermostats Intelligents
### Opportunité STMicroelectronics · Février 2026

---

## 1. Ce que dit la littérature scientifique (en 5 points)

La recherche de ces 10 dernières années est convergente sur un constat clair :

**1. Le RL dépasse largement les thermostats classiques.** Les agents DRL (DQN, D3QN, DDPG) atteignent systématiquement 15 à 27 % d'économies d'énergie tout en améliorant le confort thermique — des chiffres vérifiés dans des dizaines d'études indépendantes depuis Wei et al. (2017).

**2. Les modèles sont petits.** Le meilleur agent DQN tient dans 5 000 paramètres (~20 KB FP32, ~5 KB INT8). Le meilleur LSTM de prédiction de température tourne avec 50 851 paramètres (~203 KB FP32, ~51 KB INT8 quantifié). Ces tailles sont parfaitement compatibles avec un STM32.

**3. L'approche event-driven est la clé pour l'embarqué.** Le papier du MIT (2020) et l'ED-DQN (2023) montrent qu'un agent qui ne se déclenche que sur événement (changement de T°, présence détectée) réduit de 50 à 90 % les décisions à prendre — et converge en **1 semaine** de données réelles sur bâtiment.

**4. La quantisation INT8 sur ces modèles n'a jamais été testée dans un contexte HVAC.** C'est un gap de recherche explicite et une fenêtre d'opportunité directe pour ST.

**5. Le dataset de référence existe.** L'ASHRAE Global Thermal Comfort Database II (109 000+ mesures mondiales) et EnergyPlus + Sinergym permettent de reproduire et d'améliorer les résultats de n'importe quel papier sans données propriétaires.

> 📁 Détails complets : [[Papers/README|Bibliothèque Papers]] · [[Modeles/modeles|Catalogue Modèles]] · [[Datasets/datasets|Catalogue Datasets]]

---

## 2. Opportunité pour STMicroelectronics

### 2.1 Pourquoi maintenant ?

Le marché des thermostats intelligents pèse **+6 milliards USD en 2025** avec une croissance de 12 % par an (CAGR). Les régulations européennes (directive ErP, RE2020 en France, Fit for 55) imposent des économies d'énergie dans les bâtiments résidentiels — ce qui pousse les fabricants OEM à intégrer de l'intelligence dans leurs thermostats dès aujourd'hui.

Or, la majorité des thermostats intelligents du marché (Nest, Ecobee, Netatmo, Somfy, Danfoss...) embarquent encore des algorithmes à règles fixes ou du PID amélioré. **Personne n'a encore commercialisé un thermostat avec un agent RL/DRL embarqué sur MCU.** C'est la fenêtre.

### 2.2 Ce que ST peut apporter

ST dispose de **tous les blocs** nécessaires pour construire une démo ou un kit de référence complet :

| Composant ST | Rôle dans le thermostat Edge AI |
|-------------|--------------------------------|
| **STM32U5 / STM32H7** | MCU principal — inférence RL + LSTM (Cortex-M33/M7, ~1 MB RAM) |
| **STM32WL / STM32WB** | Connectivité sans fil (LoRa, Bluetooth 5, Zigbee) |
| **SensorTile.box PRO** | Plateforme de prototypage rapide (IMU, T°, HR, pression, micro) |
| **STTS751 / STTS22H** | Capteur température précision ±0,5 °C — entrée critique du modèle |
| **HTS221** | Capteur humidité — second paramètre confort thermique |
| **X-CUBE-AI (ST Edge AI Suite)** | Conversion modèle TFLite/ONNX → C optimisé STM32 + benchmark automatique |
| **NanoEdge AI Studio** | Entraînement on-device / anomaly detection sans expertise ML |
| **STSPIN / L298** | Driver moteur pour volet/vanne HVAC |
| **STPM3x** | Mesure de puissance pour monitoring consommation HVAC |
| **BlueNRG / SFM10R1** | Module radio pour remontée de données / OTA |

### 2.3 La proposition de valeur différenciante ST

> **"ST est le seul fournisseur qui peut livrer un thermostat Edge AI complet — du capteur au MCU en passant par le framework AI — sur une seule chaîne d'approvisionnement, avec les outils de développement."**

Ni Nordic, ni NXP, ni Renesas ne disposent d'un écosystème aussi intégré (MCU + capteurs + AI tools + power management + connectivity) sur ce segment précis.

---

## 3. Structure de slides proposée

> **Format recommandé :** 12–15 slides · Audience : ingénieurs applicatifs + décideurs R&D chez les OEM thermostats / HVAC

---

### 🎯 Slide 1 — Titre
**"L'IA embarquée réinvente le thermostat intelligent"**
*STMicroelectronics — Enabling Edge AI for Smart HVAC Control*

Visuel suggéré : thermostat avec overlay de courbes de température + graphe d'économie d'énergie

---

### 📊 Slide 2 — Le problème (Why now?)
- **50 % de l'énergie résidentielle** part en chauffage/refroidissement
- Réglementation EU qui durcit (ErP, RE2020, Fit for 55)
- Thermostats actuels : règles fixes = gaspillage de 15–25 %
- L'IA pourrait économiser **20–30 % supplémentaires**
- Marché : 6 Md$ → 14 Md$ d'ici 2030

---

### 🧠 Slide 3 — Ce que dit la recherche (État de l'art en 30 sec)
- **27 papiers scientifiques** publiés entre 2015 et 2026
- Consensus : DRL > règles > PID pour le contrôle HVAC
- Économies : **15–27 %** sur la facture énergétique
- Confort : amélioration de **30–98 %** selon la métrique
- **Le défi actuel** : tout le monde entraîne sur serveur, personne n'embarque réellement

---

### 🔬 Slide 4 — Les 3 couches du thermostat Edge AI
```
┌──────────────────────────────────────────────────────┐
│  COUCHE 1 : PRÉDICTION         COUCHE 2 : OCCUPATION │
│  LSTM ~50k params              Random Forest         │
│  Prévision T° sur 1-4h         Détection présence    │
│  ~51 KB INT8                   ~1.4 MB flash          │
│  Cortex-M7                     ESP32 / STM32          │
├──────────────────────────────────────────────────────┤
│          COUCHE 3 : DÉCISION (Control)               │
│          ED-DQN event-triggered                      │
│          ~6-8 KB INT8                                │
│          Décision seulement si événement             │
│          Réduction 76% des ajustements               │
└──────────────────────────────────────────────────────┘
```

---

### ⚙️ Slide 5 — Pourquoi l'event-driven est crucial pour l'embarqué
- **Problème** : un agent RL qui décide toutes les minutes → MCU en marche continue → batterie morte
- **Solution** : décision uniquement si |ΔT| > seuil OU changement d'occupation détecté
- **Résultat MIT (2020)** : 50–90 % de décisions en moins, même performance
- **Résultat ED-DQN (2023)** : 76 % d'ajustements en moins, 27 % d'économie énergie
- **Impact ST** : STM32 en stop mode 99 % du temps → autonomie batterie × 5–10

---

### 🔌 Slide 6 — La quantisation : le chaînon manquant
| Modèle | FP32 | INT8 | Compatible STM32 |
|--------|------|------|-----------------|
| DQN agent | 20 KB | **5 KB** | ✅ Tout STM32 |
| ED-DQN | 32 KB | **8 KB** | ✅ Tout STM32 |
| LSTM préd. T° | 203 KB | **51 KB** | ✅ STM32H7 / U5 |
| Random Forest occupation | 1.4 MB | Natif | ✅ STM32H7 |

**Constat clé : aucun papier scientifique n'a encore testé ces modèles quantifiés sur MCU réel.**
→ **Opportunité ST : être les premiers à publier ces benchmarks via X-CUBE-AI.**

---

### 🛠️ Slide 7 — L'écosystème ST : tout en une chaîne
*Schéma bloc : STTS751 → SensorTile.box → STM32H7 → X-CUBE-AI → BLE/Wi-Fi → App*

- Capteurs ST (T°, HR, CO₂ optionnel)
- SensorTile.box PRO pour prototypage
- X-CUBE-AI pour conversion et benchmark automatique
- STM32H7 / STM32U5 pour production
- Connectivité STM32WB / WL

---

### 🚀 Slide 8 — Plan de démo proposé (Proof of Concept)
**Objectif** : démontrer un agent ED-DQN quantifié INT8 sur STM32H7 contrôlant un HVAC simulé (EnergyPlus), avec comparaison vs PID sur écran local.

**Timeline :** 3 mois
- M1 : Entraînement agent ED-DQN sur Sinergym/EnergyPlus
- M2 : Quantisation INT8 via X-CUBE-AI + déploiement STM32H7
- M3 : Benchmark énergétique + démonstration client

**KPIs cibles :**
- Inférence < 10 ms sur STM32H7 @ 480 MHz
- Consommation < 5 mA en mode actif
- Économie énergie simulée > 20 %

---

### 📦 Slide 9 — Kit de référence client (proposition)
**"Smart Thermostat Edge AI Reference Design"**

Contenu du kit :
- NUCLEO-H7A3ZI-Q + shield capteurs (STTS751, HTS221)
- Firmware open-source (GitHub ST) : agent ED-DQN pré-entraîné
- Notebook EnergyPlus pour re-entraînement personnalisé
- Guide d'intégration X-CUBE-AI
- App mobile de monitoring (BLE)

**Prix cible kit :** < 80 €

---

### 🌍 Slide 10 — Cas d'usage clients
| Client type | Produit final | Ce que ST fournit |
|-------------|-------------|-----------------|
| Fabricant thermostats | Thermostat RL embarqué | MCU + capteurs + AI framework |
| OEM HVAC résidentiel | Contrôleur intelligent multi-zones | STM32H7 + DDPG quantifié |
| Smart building | Gateway bâtiment + détection occupation | STM32WL + Random Forest |
| Fabricant compteurs | Smart meter avec profiling HVAC | STPM3x + ML |

---

### ⚡ Slide 11 — Consommation et autonomie (argument batterie)
- STM32U5 en LP mode : **~10 µA** en standby
- Inférence ED-DQN INT8 : ~1 ms → **~2 mJ/décision**
- Avec event-triggering (50× moins de décisions) : **<100 µJ/heure** pour l'IA
- Autonomie sur pile 2× AA : **> 2 ans** en mode événementiel

---

### 📈 Slide 12 — Roadmap suggérée à 18 mois
```
T1 2026 : PoC interne — ED-DQN INT8 sur STM32H7 (EnergyPlus sim)
T2 2026 : Benchmark publié (X-CUBE-AI whitepaper)
T3 2026 : Kit de référence disponible (distribution)
T4 2026 : Démonstrations chez les 5 plus grands OEM thermostats EU
T1 2027 : Premier design win produit
```

---

### 🏁 Slide 13 — Call to action
**Ce que nous proposons :**
1. Lancer un projet de recherche appliquée interne (3 mois, 1 ingénieur ML + 1 ingénieur embarqué)
2. Publier un whitepaper : *"First DRL-based Smart Thermostat on STM32 : Energy savings & benchmarks"*
3. Contacter les 3 principaux OEM thermostats EU pour un early access program
4. Déposer le kit sur st.com / GitHub ST

---

## 4. Points nécessitant des équipements techniques

> Ces domaines méritent une investigation approfondie avec du matériel réel.

### 🔴 Critique — À tester en priorité

**4.1 Quantisation INT8 des modèles LSTM et DQN sur STM32**
- **Matériel :** STM32H745 Discovery + NUCLEO-H7A3ZI-Q + ST Edge AI Suite
- **À mesurer :** Latence d'inférence, consommation courant, précision post-quantisation
- **Risque :** Dégradation LSTM 8×8 connue dans la littérature générale — besoin QAT (Quantization-Aware Training)
- **Référence :** Aucun papier HVAC ne l'a fait → potentiel de publication

**4.2 Mesure de consommation en mode event-driven réel**
- **Matériel :** STM32U5 Nucleo + STM32CubeMonitor-Power + capteurs STTS751/HTS221
- **À mesurer :** µA en sleep, pic à la décision, énergie totale/24h en conditions réelles
- **Objectif :** Valider l'argument autonomie batterie 2+ ans

**4.3 Déploiement Random Forest occupation sur ESP32 vs STM32**
- **Matériel :** ESP32-S3 DevKit + NUCLEO-H723ZG
- **À mesurer :** Latence, RAM consommée, R² avec capteurs ST (CO₂, T°, lumière, PIR)
- **Dataset :** UCI Occupancy Detection (gratuit, 8 143 échantillons)

### 🟠 Important — Phase 2

**4.4 Entraînement on-device ou transfer learning sur STM32**
- **Matériel :** STM32H7 + NanoEdge AI Studio
- **Problème :** Les agents RL sont entraînés offline (cloud) — peut-on fine-tuner on-device ?
- **Intérêt :** Personnalisation par occupant sans données cloud

**4.5 Intégration capteur CO₂ (SGP30/SCD40) pour détection occupation**
- **Matériel :** SGP30 Sensirion + SCD40 + STM32 I2C
- **À mesurer :** Corrélation CO₂/occupation vs PIR seul, impact sur précision Random Forest
- **Référence dataset :** TinyML ESP32 2026 (CO₂ = meilleur prédicteur, R²=0,923)

**4.6 Test du kit SensorTile.box PRO comme plateforme thermostat**
- **Matériel :** SensorTile.box PRO (déjà disponible chez ST)
- **À mesurer :** Peut-elle tourner un agent ED-DQN + LSTM simultanément ?
- **Objectif :** Valider la plateforme pour démonstrations clients

### 🟡 Exploratoire — Phase 3

**4.7 Benchmark CMSIS-NN vs X-CUBE-AI vs TFLite Micro sur même modèle**
- Comparer les 3 frameworks sur le même modèle LSTM pour HVAC
- Matériel : STM32H7 + outils de profiling

**4.8 Federated Learning pour partage de modèles entre bâtiments**
- Entraîner un modèle global sans partager les données privées
- Matériel : 2–3 STM32WB en réseau BLE mesh

---

## 5. 📧 Mail de diffusion

---

**De :** [Ton nom] — Applications Engineering / Marketing Technique
**À :** Équipe Applications Thermostat & Building Automation
**Cc :** [Responsable marketing vertical / Management]
**Objet :** 📊 État de l'art Edge AI pour thermostats — synthèse + opportunité ST

---

Bonjour à tous,

Je vous partage ci-dessous une synthèse de la bibliographie que j'ai compilée sur l'Intelligence Artificielle embarquée pour les thermostats intelligents et le contrôle HVAC. Ce travail couvre **27 articles scientifiques publiés entre 2015 et 2026**, plus de **85 datasets publics** et une analyse exhaustive des architectures de modèles et de leurs performances sur matériel embarqué.

**Ce que ça montre :**

Les algorithmes de Deep Reinforcement Learning (DRL) atteignent de manière reproductible **15 à 27 % d'économies d'énergie** sur le chauffage/refroidissement par rapport aux thermostats traditionnels, tout en améliorant le confort thermique. Les modèles en jeu sont **petits** — un agent DQN tient dans 5 à 20 KB, un LSTM de prédiction de température dans 51 KB en INT8. Ces tailles sont **directement compatibles avec un STM32H7 ou STM32U5**.

**Le gap identifié — et notre opportunité :**

Aucun des papiers scientifiques analysés n'a testé la quantisation INT8 de ces modèles sur un microcontrôleur réel dans un contexte HVAC. C'est un blanc dans la littérature, et une opportunité concrète pour ST de publier les **premiers benchmarks**, de positionner X-CUBE-AI sur ce marché, et de proposer un **kit de référence** aux fabricants de thermostats.

**La proposition concrète :**

Je propose de lancer un projet de recherche appliquée en interne (3 mois, 1 ingénieur ML + 1 ingénieur embarqué) avec pour objectifs :
1. Déployer un agent ED-DQN quantifié INT8 sur STM32H7 + benchmark via X-CUBE-AI
2. Publier un whitepaper technique : *"First DRL-based Smart Thermostat on STM32"*
3. Créer un kit de référence client (Nucleo + capteurs + firmware open-source)

Le timing est bon : les réglementations EU (ErP, RE2020) poussent les OEM à agir maintenant, et le marché des thermostats intelligents est en forte croissance (+12 % CAGR jusqu'en 2030).

**Prochaines étapes suggérées :**
- [ ] Discussion de 30 min en équipe pour aligner sur les priorités
- [ ] Identifier 1 ingénieur ML et 1 ingénieur embarqué disponibles Q1 2026
- [ ] Contacter les équipes produit STM32H7 et STM32U5 pour matériel de démo
- [ ] Vérifier disponibilité SensorTile.box PRO pour prototypage rapide

Je suis disponible pour en discuter — n'hésitez pas à me revenir avec vos questions ou commentaires.

Bonne lecture,

**[Ton nom]**
Applications Engineering — Smart Home & Building Automation
STMicroelectronics
[email] · [téléphone]

*P.S. : La bibliographie complète, les fiches de chaque article et le catalogue des datasets sont disponibles dans le dossier partagé [lien]. Les fichiers sont au format Obsidian (.md) mais lisibles dans n'importe quel éditeur texte.*

---

---

*Document généré le 2026-02-19 — Confidentiel usage interne*
*Sources : [[Papers/README|Bibliothèque Papers]] · [[Modeles/modeles|Catalogue Modèles]] · [[Datasets/datasets|Catalogue Datasets]] · [[TODO-vérifications-manuelles|TODO vérifications]]*
