---
title: "The Personalized Thermal Comfort Prediction Using an MH-LSTM Neural Network Method"
authors:
  - "Cho, Jaeyoun"
  - "Shin, Hyunkyu"
  - "Ahn, Yonghan"
  - "Ho, Jongnam"
year: 2024
venue: "Advances in Civil Engineering"
publisher: "Wiley/Hindawi"
doi: "10.1155/2024/2106137"
url: "https://onlinelibrary.wiley.com/doi/10.1155/2024/2106137"
pdf_url: "https://www.researchgate.net/publication/379930580_The_Personalized_Thermal_Comfort_Prediction_Using_an_MH-LSTM_Neural_Network_Method"
tags:
  - lstm
  - multi-head
  - thermal-comfort
  - personalization
  - prediction
  - classification
  - deep-learning
domains:
  - "Thermal Comfort Prediction"
methods:
  - "Multi-Head LSTM"
  - "Deep Learning"
  - "Time Series Prediction"
hardware_targets: []
datasets:
  - name: "Controlled Experiments"
    url: null
    description: "Individual thermal comfort measurements from 6 participants under controlled conditions"
read: false
relevance: 4
category: "CNN-LSTM"
date_added: 2026-02-19
---

# The Personalized Thermal Comfort Prediction Using an MH-LSTM Neural Network Method

> **Source:** [Advances in Civil Engineering](https://onlinelibrary.wiley.com/doi/10.1155/2024/2106137) | **Volume:** 2024, Article 2106137 | **Year:** 2024 | **Authors:** Cho et al.

---

## 📄 Résumé

Cet article propose une approche innovante basée sur le Deep Learning pour prédire le confort thermique personnalisé des occupants. Les auteurs développent un modèle Multi-Head LSTM (MH-LSTM) capable de capturer les variations temporelles et environnementales à différentes échelles de temps pour prédire la sensation thermique individuelle avec précision. À la différence des modèles standards PMV qui supposent des occupants "moyens", cette approche apprend les préférences thermiques individuelles à partir de données mesurées. Avec une précision de classification de 92%, le modèle démontre le potentiel d'une prédiction personnalisée du confort thermique pour optimiser les systèmes HVAC.

This paper presents an innovative deep learning approach for personalized thermal comfort prediction using a Multi-Head LSTM (MH-LSTM) architecture. Unlike standard thermal comfort models (PMV) that assume average occupants, the MH-LSTM learns individual thermal comfort preferences from measured data across different temporal and environmental scales. With 92% classification accuracy, the approach demonstrates the potential for truly personalized HVAC control that adapts to individual occupant preferences.

---

## 🎯 Contributions principales

1. **Architecture Multi-Head LSTM** — Première application de l'approche multi-tête au LSTM pour capturer des dépendances temporelles à plusieurs échelles (courte, moyenne, longue durées)
2. **Gestion des variations individuelles** — Modèle capable de capturer comment différents individus réagissent différemment aux mêmes conditions thermiques
3. **Apprentissage de préférences personnalisées** — Entraînement par personne pour capturer préférences thermiques subjectives non modélisables mathématiquement
4. **Haute précision prédictive** — Atteinte de 92% de précision de classification de la sensation thermique subjective sur données expérimentales
5. **Architecture scalable** — Design modulaire permettant extraction de caractéristiques à différentes résolutions temporelles

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

**Multi-Head LSTM (MH-LSTM)**

Extension novatrice du LSTM standard utilisant plusieurs "têtes" parallèles:

**Architecture LSTM de base:**
- **Cell State (Ct)**: mémoire à long terme
- **Hidden State (ht)**: mémoire à court terme
- **Gates**: Input, Forget, Output (contrôlent flux information)

```
i_t = σ(W_ii · x_t + W_hi · h_(t-1) + b_i)    [Input gate]
f_t = σ(W_if · x_t + W_hf · h_(t-1) + b_f)    [Forget gate]
o_t = σ(W_io · x_t + W_ho · h_(t-1) + b_o)    [Output gate]
C̃_t = tanh(W_ic · x_t + W_hc · h_(t-1) + b_c) [Cell candidate]
C_t = f_t ⊙ C_(t-1) + i_t ⊙ C̃_t                [Cell state]
h_t = o_t ⊙ tanh(C_t)                           [Hidden state]
```

**Architecture Multi-Head:**
- **Head 1 (court terme)**: LSTM avec fenêtre 1-2 heures, capture variations rapides
- **Head 2 (moyen terme)**: LSTM avec fenêtre 4-8 heures, capture cycles activité
- **Head 3 (long terme)**: LSTM avec fenêtre 24+ heures, capture adaptations saisonnières
- **Fusion**: Concaténation des sorties multi-têtes → Couche dense pour classification

### Architecture du système

**Données d'entrée (Observation):**
- **Variables physiques:** Température extérieure, humidité, rayonnement solaire
- **Variables intérieures:** Température de l'air, température de surface (parois, fenêtres), humidité relative
- **Variables occupant:** Niveau d'activité, type/épaisseur vêtements (si capteur disponible)
- **Variables temporelles:** Heure du jour, jour de la semaine, saison

**Données de sortie (Label):**
- **Sensation thermique subjective** (7-point ASHRAE scale):
  - +3: Très chaud
  - +2: Chaud
  - +1: Légèrement chaud
  - 0: Neutre (confortable)
  - -1: Légèrement froid
  - -2: Froid
  - -3: Très froid

### Environnement de test / Simulation

**Protocole expérimental:**
- **Sujets:** 6 participants volontaires (3 hommes, 3 femmes, âge 20-40 ans)
- **Cadre:** Chambre contrôlée avec HVAC ajustable
- **Durée:** 4 semaines par participant, avec variations quotidiennes de température
- **Mesures collectées:**
  - Température ambiante: variations 18-28°C
  - Humidité relative: variations 30-80%
  - Votes de confort subjectif: 2-3 fois par jour
  - Vêtements portés (enregistrés)
  - Activité physique (enregistrée)

**Données collectées:**
- ~10,000 points de données par participant (mesures + labels)
- Séquences temporelles couvrant matin, après-midi, soir
- Variations saisonnières (tests en hiver et été pour certains sujets)

### Hyperparamètres clés

| Paramètre | Valeur |
|-----------|--------|
| Nombre de heads | 3 |
| Unités LSTM par head | 64-128 |
| Dropout | 0.2-0.3 |
| Batch Size | 32-64 |
| Learning Rate | 0.001-0.0005 |
| Optimizer | Adam |
| Fonction perte | Categorical Cross-entropy |
| Epochs | 50-100 |
| Early Stopping Patience | 10 epochs |
| Fenêtre temporelle Head 1 | 6 pas de temps (1-2h) |
| Fenêtre temporelle Head 2 | 24 pas de temps (8h) |
| Fenêtre temporelle Head 3 | 96 pas de temps (24h+) |

---

## 📊 Résultats clés

| Métrique | MH-LSTM | LSTM Standard | PMV Model |
|----------|---------|---------------|-----------|
| Précision Classification | 92% | 84-86% | 65-72% |
| Recall (classe 0: Neutre) | 89% | 78% | 58% |
| F1-Score | 0.90 | 0.81 | 0.63 |
| Erreur Prédiction ±1 classe | 95% | 88% | 72% |
| Temps inférence | <10ms | <8ms | <1ms |
| Paramètres modèle | ~50K | ~30K | 0 (analytique) |

**Points forts:**
- **Supériorité sur LSTM standard:** 6-8% amélioration de précision grâce aux heads multiples
- **Supériorité sur PMV:** 20-25% amélioration vs modèles standards mathématiques
- **Personnalisation:** Modèle spécifique par individu capture préférences singulières
- **Robustesse:** Erreurs dans ±1 classe (confort acceptable) pour 95% des prédictions
- **Efficacité:** Inférence rapide (<10ms) permet déploiement temps-réel
- **Apprentissage:** Convergence rapide en 50-100 epochs avec données individuelles

**Analyse détaillée par classe:**
- Classe "Neutre" (0): 92% rappel → bien identifie zone confort
- Classes extrêmes (±3): 85-90% rappel → bien capture intolérance
- Classes intermédiaires (±1, ±2): 88-90% rappel → bon gradient de transition

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| ASHRAE Thermal Comfort Standard 55 | [https://www.ashrae.org/](https://www.ashrae.org/) | Référence standard pour confort thermique et échelle de vote |
| Berkeley Comfort Database | [https://comfort.cbe.berkeley.edu/](https://comfort.cbe.berkeley.edu/) | Base de données ouverte de confort thermique |
| TensorFlow/Keras | [https://keras.io/](https://keras.io/) | Framework pour implémentation MH-LSTM |
| Données Expérimentales | Disponible sur demande | Dataset brut de 6 participants (4 semaines chacun) |

---

## ⚠️ Limites identifiées

- **Taille dataset limitée** — Seulement 6 participants; généralisation à population diverse à valider
- **Environnement contrôlé** — Chambre climatisée avec peu de facteurs externes; réalisme bâtiment réel à établir
- **Adaptabilité temporelle** — Pas d'étude de dérive long-terme (changement préférences dans mois/années)
- **Sensibilité paramètres** — Vêtements, activité supposés constants; impact de variations non étudié
- **Coût entraînement** — Entraînement par personne (6-8 jours données collecte) coûteux pour déploiement généralisé
- **Catégories discrètes** — Classification ordinale (7 classes) vs prédiction continue de sensation thermique
- **Méthodologie validation** — Split train/test temporel non clairement décrit

---

## 🔌 Pertinence pour un thermostat Edge AI

Cet article est **hautement pertinent** pour personnalisation fine d'un thermostat:

1. **Dépassement des limites PMV** — PMV standard ne capture pas variations individuelles; MH-LSTM le fait
2. **Apprentissage adaptatif** — Peut s'adapter aux préférences uniques après quelques jours d'utilisation
3. **Inférence légère** — 50K paramètres + <10ms inférence compatible thermostat mobile
4. **Validation empirique** — Validation sur humains réels vs simulation-only
5. **Combinaison avec RL** — Peut servir de reward signal pour RL (maximiser prédiction classe "Neutre")
6. **Sans capteurs externes** — Utilise température, humidité, temps (données usuelles thermostat)

**Applicabilité embarquée:** Medium-High
**Raison:** MH-LSTM est léger (50K params) et inférence rapide (<10ms). Peut s'exécuter sur thermostat ARM/Cortex-A avec 512MB RAM. Principal défi: collecte données personnalisées initiales (5-7 jours usage avec feedback utilisateur). Idéal combiné avec DDPG: DDPG décide setpoint, MH-LSTM prédit réaction utilisateur et informe reward.

---

## 📚 Citation BibTeX

```bibtex
@article{Cho2024,
  title = {The Personalized Thermal Comfort Prediction Using an {MH}-{LSTM} Neural Network Method},
  author = {Cho, Jaeyoun and Shin, Hyunkyu and Ahn, Yonghan and Ho, Jongnam},
  journal = {Advances in Civil Engineering},
  volume = {2024},
  pages = {2106137},
  year = {2024},
  publisher = {Wiley},
  doi = {10.1155/2024/2106137}
}
```
