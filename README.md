# 🌡️ Smart Thermostat — Edge AI sur STM32

Projet de recherche et prototypage autour de l'**intelligence artificielle embarquée pour thermostats intelligents**, ciblant les microcontrôleurs **STMicroelectronics STM32** (Cortex-M, STM32N6 avec NPU).

L'objectif : démontrer qu'un agent RL ou un modèle LSTM de prédiction thermique peut tourner directement sur un MCU basse consommation, sans cloud, pour réduire la consommation énergétique HVAC de 15 à 27 %.

---

## Structure du projet

```
Smart Thermostat/
├── Papers/                     # Bibliographie scientifique (2015–2026)
│   ├── INDEX.md                # Index par pertinence
│   └── 20XX/                   # Notes Obsidian par année
├── Modeles/
│   └── modeles.md              # Catalogue des architectures (DQN, LSTM, CNN-LSTM…)
├── Datasets/
│   └── datasets.md             # Catalogue de 85+ datasets publics (ASHRAE, Kaggle…)
├── Source_Models/               # Modèles source téléchargés
│   ├── TensorFlow_Keras/       # LSTM, HVAC predictive control, YOLOv4-tiny…
│   ├── PyTorch/                # ComfortGPT, Gnu-RL, DRL-Building-Energy…
│   └── ONNX/                   # Build2Vec, GNN power flow…
├── stm32ai-modelzoo-services/  # SDK ST Edge AI Developer Cloud (submodule)
├── stedgeai_benchmark.py       # Script de benchmark interactif (analyze + benchmark)
├── benchmark_history.md        # Historique cumulatif des runs de benchmark
└── SYNTHESE-STMicro.md         # Synthèse business pour STMicroelectronics
```

## Benchmark — `stedgeai_benchmark.py`

Script interactif pour évaluer un modèle TFLite/ONNX/Keras sur le cloud ST Edge AI :

```bash
python stedgeai_benchmark.py
python stedgeai_benchmark.py --model mon_modele.tflite
python stedgeai_benchmark.py --model mon_modele.tflite --board STM32N6570-DK
python stedgeai_benchmark.py --no-benchmark   # analyze seul
```

Ce qu'il fait :

1. Upload du modèle sur le cloud ST
2. **Analyze** — estimation RAM, Flash, MACs (complexité)
3. **Benchmark** — mesure du temps d'inférence réel sur la board cible
4. Génération d'un **rapport Markdown** avec statut coloré (🟢🟡🔴) et détails complets
5. Mise à jour automatique de `benchmark_history.md`

Boards supportées : STM32H7B3I-DK, STM32N6570-DK (avec NPU Neural-ART), et toutes celles du cloud ST.

### Prérequis

```bash
git clone https://github.com/STMicroelectronics/stm32ai-modelzoo-services.git
pip install -r stm32ai-modelzoo-services/requirements.txt
```

Un compte [myST](https://www.st.com/content/st_com/en.html) est nécessaire. Les identifiants peuvent être renseignés directement dans le script (variables `STEDGEAI_USERNAME` / `STEDGEAI_PASSWORD`) ou via les variables d'environnement correspondantes.

## Synthèse

Le fichier `SYNTHESE-STMicro.md` contient l'analyse complète :

- État de l'art scientifique (10 ans de recherche RL/LSTM pour HVAC)
- Opportunité marché (6 Mds USD, croissance 12 %/an)
- Proposition de valeur STMicroelectronics
- Feuille de route technique

## Stack technique

- **Hardware cible** : STM32H7 (Cortex-M7), STM32N6 (Cortex-M55 + NPU Neural-ART)
- **Formats modèles** : TFLite, ONNX, Keras (.h5)
- **SDK** : ST Edge AI Developer Cloud (`stm32ai_dc`)
- **Documentation** : Obsidian (Markdown + YAML frontmatter + wikilinks)

## Licence

Projet de recherche interne.
