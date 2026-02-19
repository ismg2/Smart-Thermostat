# 📥 Guide de téléchargement des modèles
### Smart Thermostat Edge AI — Modèles pré-entraînés

> **Comment utiliser ce guide :** pour chaque modèle, une seule action à faire (git clone ou téléchargement direct), un seul dossier de destination.

---

## 📁 Structure des dossiers

```
Source_Models/
├── TensorFlow_Keras/     ← fichiers .h5 · .tflite · .keras · .pb
├── PyTorch/              ← fichiers .pt · .pth · .zip (SB3)
└── ONNX/                 ← fichiers .onnx
```

---

## 🟠 PyTorch / Stable-Baselines3
### → Dossier cible : `Source_Models/PyTorch/`

---

### 1. Gnu-RL — Agent RL pré-entraîné pour HVAC ⭐
> Contrôle HVAC avec politique MPC différentiable. **Modèle pré-entraîné inclus dans le repo.** C'est le plus directement utilisable.

```bash
git clone https://github.com/INFERLab/Gnu-RL.git
```
🔗 **Repo :** https://github.com/INFERLab/Gnu-RL
📄 **Papier :** [Gnu-RL: A Precocial Reinforcement Learning Solution (2019)](https://arxiv.org/abs/1910.12204)

---

### 2. PEARL — Contrôle bâtiment zéro-shot (émissions)
> Agent RL pour réduction d'émissions dans les bâtiments. Entraîné sans simulateur (real-world ready).

```bash
git clone https://github.com/enjeeneer/PEARL.git
```
🔗 **Repo :** https://github.com/enjeeneer/PEARL
📄 **Papier :** [PEARL: Zero-Shot Reward Specification (2023)](https://arxiv.org/abs/2308.05614)

---

### 3. CLUE — Contrôle HVAC sûr (Safe RL)
> Agent RL avec estimation d'incertitude epistémique. Converge en 7 jours de données réelles.

```bash
git clone https://github.com/ryeii/CLUE.git
```
🔗 **Repo :** https://github.com/ryeii/CLUE

---

### 4. DRL-Building-Energy-Ctr — Agent HEMS (pompe à chaleur)
> Agent DRL pour Home Energy Management System, contrôle pompe à chaleur + stockage thermique.

```bash
git clone https://github.com/ULudo/DRL-Building-Energy-Ctr.git
```
🔗 **Repo :** https://github.com/ULudo/DRL-Building-Energy-Ctr

---

### 5. ComfortGPT — Transformer pour prédiction de confort thermique ⭐
> Modèle transformer pré-entraîné pour prédire la température de confort préférée par l'occupant.

```bash
git clone https://github.com/Building-Robotics-Lab/ComfortGPT.git
```
🔗 **Repo :** https://github.com/Building-Robotics-Lab/ComfortGPT

---

### 6. LSTM Prédiction d'énergie — PyTorch (données PJM)
> LSTM/GRU pré-entraîné sur données horaires d'énergie PJM. Fichiers `.pt` dans `/models`.

```bash
git clone https://github.com/iamirmasoud/energy_consumption_prediction.git
```
🔗 **Repo :** https://github.com/iamirmasoud/energy_consumption_prediction

---

### 7. DeepLearning Energy Forecasting — LSTM + Transformer (PyTorch Lightning)
> LSTM et Transformer pour prévision horaire d'énergie. Modèles sauvegardés dans le repo.

```bash
git clone https://github.com/AhmetZamanis/DeepLearningEnergyForecasting.git
```
🔗 **Repo :** https://github.com/AhmetZamanis/DeepLearningEnergyForecasting

---

### 8. Thermal Comfort CNN-LSTM (Transfer Learning)
> CNN-LSTM pour prédiction de confort thermique en bâtiments avec peu de données. Transfer learning inclus.

```bash
git clone https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings.git
```
🔗 **Repo :** https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings

---

### 9. RF-LSTM-CEEMDAN — Random Forest + LSTM hybride
> Modèle hybride RF-LSTM avec décomposition CEEMDAN pour prédiction d'énergie bâtiment.

```bash
git clone https://github.com/irenekarijadi/RF-LSTM-CEEMDAN.git
```
🔗 **Repo :** https://github.com/irenekarijadi/RF-LSTM-CEEMDAN

---

### 10. CCM — Cohort Comfort Models (confort personnalisé)
> Prédit les préférences thermiques personnelles par similarité de cohorte. Inclut données + modèles.

```bash
git clone https://github.com/buds-lab/ccm.git
```
🔗 **Repo :** https://github.com/buds-lab/ccm

---

### 11. ComfortLearn — Environnement Gym pour confort occupant (entraînement RL)
> OpenAI Gym environment pour entraîner un agent RL centré sur le confort. Utile pour re-entraînement.

```bash
git clone https://github.com/buds-lab/ComfortLearn.git
```
🔗 **Repo :** https://github.com/buds-lab/ComfortLearn

---

### 12. PDE-HVAC Control — RL (Stable-Baselines3)
> Contrôle HVAC basé sur RL avec Stable-Baselines3. Modèles checkpoints dans le repo.

```bash
git clone https://github.com/alwaysbyx/PDE-HVAC-control.git
```
🔗 **Repo :** https://github.com/alwaysbyx/PDE-HVAC-control

---

## 🔵 TensorFlow / Keras / TFLite
### → Dossier cible : `Source_Models/TensorFlow_Keras/`

---

### 13. LSTM Load Forecasting — Fichiers .h5 disponibles ⭐
> LSTM entraîné sur données de charge suisses. **Modèles .h5 directement dans le dossier `/models` du repo.**

```bash
git clone https://github.com/dafrie/lstm-load-forecasting.git
```
🔗 **Repo :** https://github.com/dafrie/lstm-load-forecasting
📌 **Fichiers modèles :** dans `lstm-load-forecasting/models/` après clonage

---

### 14. YOLOv4-tiny TFLite — Détection de personnes (occupation) ⭐
> Modèle TFLite pré-entraîné pour détection de personnes. **Fichier `.tflite` directement téléchargeable.**

```bash
git clone https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection.git
```
🔗 **Repo :** https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection
📌 **Fichier modèle :** `yolov4-tiny-416.tflite` dans le repo

---

### 15. TFLite Object Detection — Détection de personnes (Raspberry Pi / MCU)
> Collection de modèles TFLite pré-entraînés (COCO) pour détection sur edge devices.

```bash
git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
```
🔗 **Repo :** https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi
📌 **Modèles :** téléchargeables via le script `get_pi_requirements.sh` dans le repo

---

### 16. CNN-LSTM Energy Forecasting — Keras
> Prédiction multi-step de consommation d'énergie avec CNN-LSTM. Modèle Keras inclus.

```bash
git clone https://github.com/muntasirhsn/CNN-LSTM-model-for-energy-usage-forecasting.git
```
🔗 **Repo :** https://github.com/muntasirhsn/CNN-LSTM-model-for-energy-usage-forecasting

---

### 17. HVAC Predictive Control — Machine Learning interprétable
> Prédiction de température de pièce avec ML interprétable (données bâtiment réel).

```bash
git clone https://github.com/JianqiaoMao/Interpretable-machine-learning-for-HVAC-predictive-control.git
```
🔗 **Repo :** https://github.com/JianqiaoMao/Interpretable-machine-learning-for-HVAC-predictive-control

---

### 18. ComfortGAN — GAN pour dataset de confort thermique
> GAN pour générer et équilibrer des datasets de confort thermique (augmentation de données).

```bash
git clone https://github.com/buds-lab/comfortGAN.git
```
🔗 **Repo :** https://github.com/buds-lab/comfortGAN

---

## 🟣 ONNX
### → Dossier cible : `Source_Models/ONNX/`

---

### 19. ONNX Model Zoo — Modèles de référence
> Collection officielle de modèles pré-entraînés au format ONNX (ResNet, LSTM, etc.). Utile comme point de départ pour conversion.

```bash
git clone https://github.com/onnx/models.git --depth 1
```
🔗 **Repo :** https://github.com/onnx/models
📌 **Note :** repo très large — utiliser `--depth 1` pour ne prendre que la dernière version

---

### 20. Build2Vec — GNN pour confort thermique (ONNX exportable)
> Graph Neural Network prédit les préférences thermiques à partir des données BIM + localisation. Exportable en ONNX.

```bash
git clone https://github.com/buds-lab/build2vec-thermal-comfort.git
```
🔗 **Repo :** https://github.com/buds-lab/build2vec-thermal-comfort

---

## 🛠️ Environnements d'entraînement (à installer séparément)

> Ce ne sont pas des modèles mais les **environnements** nécessaires pour entraîner ou ré-entraîner des agents RL.

| Outil | Quoi | Commande |
|-------|------|---------|
| **Sinergym** | EnergyPlus + RL Gym (standard de facto) | `pip install sinergym` |
| **CityLearn** | Multi-agent RL pour bâtiments | `pip install citylearn` |
| **Stable-Baselines3** | Algorithmes RL (DQN, PPO, SAC…) | `pip install stable-baselines3` |
| **PyThermalComfort** | Calcul PMV/PPD physique | `pip install pythermalcomfort` |

🔗 Sinergym : https://github.com/ugr-sail/sinergym
🔗 CityLearn : https://github.com/intelligent-environments-lab/CityLearn

---

## ⚡ Script tout-en-un

> Copie ce bloc dans un terminal pour tout cloner d'un coup dans les bons dossiers.

```bash
# --- PyTorch ---
cd "/chemin/vers/Smart Thermostat/Source_Models/PyTorch"

git clone https://github.com/INFERLab/Gnu-RL.git
git clone https://github.com/enjeeneer/PEARL.git
git clone https://github.com/ryeii/CLUE.git
git clone https://github.com/ULudo/DRL-Building-Energy-Ctr.git
git clone https://github.com/Building-Robotics-Lab/ComfortGPT.git
git clone https://github.com/iamirmasoud/energy_consumption_prediction.git
git clone https://github.com/AhmetZamanis/DeepLearningEnergyForecasting.git
git clone https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings.git
git clone https://github.com/irenekarijadi/RF-LSTM-CEEMDAN.git
git clone https://github.com/buds-lab/ccm.git
git clone https://github.com/buds-lab/ComfortLearn.git
git clone https://github.com/alwaysbyx/PDE-HVAC-control.git

# --- TensorFlow / Keras / TFLite ---
cd "/chemin/vers/Smart Thermostat/Source_Models/TensorFlow_Keras"

git clone https://github.com/dafrie/lstm-load-forecasting.git
git clone https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection.git
git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
git clone https://github.com/muntasirhsn/CNN-LSTM-model-for-energy-usage-forecasting.git
git clone https://github.com/JianqiaoMao/Interpretable-machine-learning-for-HVAC-predictive-control.git
git clone https://github.com/buds-lab/comfortGAN.git

# --- ONNX ---
cd "/chemin/vers/Smart Thermostat/Source_Models/ONNX"

git clone https://github.com/onnx/models.git --depth 1
git clone https://github.com/buds-lab/build2vec-thermal-comfort.git
```

> **Remplace** `/chemin/vers/Smart Thermostat/` par le chemin réel sur ton ordinateur.

---

## 📊 Récapitulatif

| # | Modèle | Framework | Usage principal | Modèle dispo ? |
|---|--------|-----------|----------------|---------------|
| 1 | Gnu-RL | PyTorch/SB3 | Contrôle HVAC RL | ✅ Pré-entraîné |
| 2 | PEARL | PyTorch/SB3 | Contrôle bâtiment | ✅ Pré-entraîné |
| 3 | CLUE | PyTorch/SB3 | Safe HVAC RL | ✅ Pré-entraîné |
| 4 | DRL-Building-Energy-Ctr | PyTorch/SB3 | HEMS pompe à chaleur | ⚠️ À vérifier |
| 5 | ComfortGPT | PyTorch | Confort thermique | ✅ Pré-entraîné |
| 6 | LSTM PJM Energy | PyTorch | Prédiction énergie | ✅ Fichiers .pt |
| 7 | DL Energy Forecasting | PyTorch Lightning | Prédiction énergie | ✅ Checkpoints |
| 8 | Thermal Comfort CNN-LSTM | PyTorch | Confort thermique | ✅ Pré-entraîné |
| 9 | RF-LSTM-CEEMDAN | PyTorch | Prédiction énergie | ⚠️ Code + données |
| 10 | CCM | PyTorch | Confort personnalisé | ✅ Modèles inclus |
| 11 | ComfortLearn | PyTorch/SB3 | Env. RL confort | 🔧 Entraînement |
| 12 | PDE-HVAC | PyTorch/SB3 | Contrôle HVAC | ⚠️ Checkpoints |
| 13 | LSTM Load Forecasting | TF/Keras .h5 | Prédiction charge | ✅ Fichiers .h5 |
| 14 | YOLOv4-tiny TFLite | TFLite | Détection occupation | ✅ Fichier .tflite |
| 15 | TFLite Object Detection | TFLite | Détection personnes | ✅ Modèles COCO |
| 16 | CNN-LSTM Energy | Keras | Prédiction énergie | ⚠️ Code + notebook |
| 17 | HVAC Predictive Control | TF/Keras | Prédiction T° | ⚠️ Code + données |
| 18 | ComfortGAN | TF/Keras | Augmentation données | ⚠️ Code + données |
| 19 | ONNX Model Zoo | ONNX | Référence générale | ✅ Fichiers .onnx |
| 20 | Build2Vec | PyTorch/ONNX | Confort thermique | ⚠️ Code + données |

**Légende :** ✅ Modèle directement utilisable · ⚠️ Nécessite entraînement/données · 🔧 Environnement d'entraînement

---

*Mis à jour le 2026-02-19 — Sources : GitHub, HuggingFace, publications académiques*
