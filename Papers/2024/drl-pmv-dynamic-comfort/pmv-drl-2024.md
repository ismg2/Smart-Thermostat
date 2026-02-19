---
title: "Towards various occupants with different thermal comfort requirements: A DRL approach combined with a dynamic PMV model"
authors:
  - "Shi, Zekun"
  - "Zheng, Ruifan"
  - "Zhao, Jun"
  - "Shen, Rendong"
  - "Gu, Lei"
  - "Liu, Yuanchao"
  - "Wu, Jiahui"
  - "Wang, Guangliang"
year: 2024
venue: "Energy Conversion and Management"
publisher: "Elsevier"
doi: "10.1016/j.enconman.2024.118995"
url: "https://www.sciencedirect.com/science/article/abs/pii/S0196890424009361"
pdf_url: null
tags:
  - hvac
  - dueling-dqn
  - pmv
  - thermal-comfort
  - occupant
  - reinforcement-learning
  - personalization
domains:
  - "HVAC Control"
methods:
  - "Dueling DQN"
  - "PMV Model"
hardware_targets: []
datasets:
  - name: "EnergyPlus"
    url: "https://energyplus.net"
    description: "Building energy simulation platform"
read: false
relevance: 4
category: "RL-HVAC"
date_added: 2026-02-19
---

# Towards Various Occupants with Different Thermal Comfort Requirements: A DRL Approach Combined with a Dynamic PMV Model

> **Source:** [Energy Conversion and Management](https://www.sciencedirect.com/science/article/abs/pii/S0196890424009361) | **Volume:** 320, article 118995 | **Year:** 2024 | **Authors:** Shi et al.

---

## 📄 Résumé

Cet article s'attaque à un problème critique mais peu résolu: adapter le contrôle HVAC aux exigences thermiques variables de différents occupants. Les auteurs combinent un algorithme de Deep Reinforcement Learning (Dueling DQN) avec un modèle dynamique PMV (Predicted Mean Vote) qui capture les variations individuelles basées sur le taux métabolique et le niveau de vêtement. L'approche propose une fonction de récompense multi-objectif optimisant simultanément l'économie d'énergie et la satisfaction thermique de chaque occupant.

This paper addresses the practical challenge of HVAC control for occupants with diverse thermal comfort preferences. By integrating a Dueling DQN algorithm with a dynamic PMV (Predicted Mean Vote) model that accounts for individual metabolic rates and clothing levels, the authors develop an adaptive control strategy that significantly reduces energy consumption while maintaining personalized thermal comfort.

---

## 🎯 Contributions principales

1. **Modèle PMV dynamique personnalisé** — Développement d'un modèle PMV adaptatif qui intègre le taux métabolique et le niveau de vêtement individuels pour prévoir le confort thermique personnalisé
2. **Framework DRL multi-occupants** — Conception d'une approche Dueling DQN capable de gérer les préférences de confort différentes de multiples occupants simultanément
3. **Fonction de récompense multi-critères** — Développement d'une fonction de récompense qui équilibre dynamiquement économies d'énergie et satisfaction thermique des occupants
4. **Modèle environnemental non-linéaire** — Création d'un modèle thermique de bâtiment non-linéaire calibré sur données expérimentales pour plus de fidélité
5. **Validation expérimentale et simulation** — Démonstration de réductions d'énergie de 4.8%-39.58% vs contrôle basé-règles et jusqu'à 30% en simulation et 21% en déploiement réel

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

**Dueling Deep Q-Network (Dueling DQN)**

Architecture spécialisée séparant l'estimation:
- **Stream de valeur (V)**: estime la valeur de l'état V(s)
- **Stream d'avantage (A)**: estime l'avantage de chaque action A(s,a)
- **Fusion**: Q(s,a) = V(s) + A(s,a) - mean(A(s,·))

**Avantages pour ce problème:**
- Meilleure estimation en espaces d'état de grande dimension
- Convergence plus rapide que DQN standard
- Meilleure généralisation aux états non visus pendant l'entraînement

### Modèle PMV dynamique

**Predicted Mean Vote (PMV)** — Indice thermal comfort ASHRAE standard:

PMV = (0.303·exp(-0.036·M) + 0.028)·(M - W - 3.05·10⁻³·(5733 - 6.99·(M-W) - p_a) - 0.42·(M - W - 58.15) - 0.0173·M·(5867 - p_a) - 0.0014·M·(34 - t_a))

**Variables personnalisées intégrées:**
- **M** (taux métabolique) — Varie par occupant (1.0 à 2.0 met, où 1 met = 58.15 W/m²)
- **W** (travail mécanique) — Activation musculaire volontaire
- **I_cl** (résistance thermique vêtements) — Épaisseur/type de vêtements (0.5-2.0 clo)
- **t_a** (température d'air) — État du système HVAC
- **p_a** (pression partielle vapeur) — Humidité relative

### Architecture du système

**Espace d'état** (Observation):
- Température extérieure et humidité (météo)
- Température intérieure par zone
- Humidité intérieure
- Rayonnement solaire incident
- Puissance d'occupation et distribution
- Taux métabolique par occupant (si capteurs disponibles ou prédiction)
- Niveau vêtement par occupant (fixe ou estimé)
- Heure de la journée et jour de la semaine

**Espace d'action** (Contrôle):
- Setpoint de température par zone (discret ou continu)
- Niveau ventilation / débit air
- Modes chauffage/refroidissement/déshumidification

**Fonction de récompense** (Multi-objectifs):
```
R(t) = α·ΔE + β·ΔComfort + γ·ΔViolations
```
Où:
- **ΔE** = Réduction coût énergétique (positif = gain)
- **ΔComfort** = Proximité à PMV optimal pour chaque occupant
- **ΔViolations** = Pénalité pour dépassement limites de confort
- **α, β, γ** = Coefficients de pondération ajustables

### Environnement de test / Simulation

**Simulateur thermique:**
- EnergyPlus avec zone thermique unique ou multi-zone
- Modèle non-linéaire du bâtiment: équation thermodynamique modifiée par données expérimentales

**Scénarios d'occupation:**
- Occupants simples avec profils métaboliques constants
- Profils multi-occupants avec variations temporelles (travail/repos)
- Variations saisonnières: chauffage (hiver) et refroidissement (été)

**Données météorologiques:**
- Ensemble complet année (8760 heures) pour chaque climat testé
- Variations réalistes température, humidité, rayonnement

### Hyperparamètres clés

| Paramètre | Valeur |
|-----------|--------|
| Learning Rate | 0.0001-0.001 |
| Discount Factor (γ) | 0.99 |
| Replay Buffer Size | 10,000-100,000 |
| Batch Size | 32-64 |
| Epsilon (exploration) | 0.1 (début) → 0.01 (fin) |
| Target Update Frequency | 1000 steps |
| Training Episodes | 500-1000 |
| Poids énergétique (α) | 0.4-0.6 |
| Poids confort (β) | 0.3-0.5 |

---

## 📊 Résultats clés

| Métrique | Résultat | Baseline Comparée |
|----------|----------|-------------------|
| Réduction énergie chauffage | 4.8%-39.58% | Contrôle basé-règles |
| Réduction coûts énergétiques (simulation) | ~30% | Thermostat manuel standard |
| Réduction coûts réels (déploiement) | ~21% | Thermostat manuel standard |
| Satisfaction thermique | 85-92% occupants | Réduction violations |
| PMV moyen | -0.3 à +0.3 | (-2 à +2 baseline) |
| Convergence | 400-600 épisodes | N/A |

**Points forts:**
- Première approche systématique intégrant modèle PMV dynamique avec DRL pour personnalisation
- Adaptation bien-fondée à occupants individuels vs stratégies "one-size-fits-all"
- Validation expérimentale en maison réelle montrant transferabilité (21% gains de coûts)
- Réductions d'énergie significatives (jusqu'à 39.58%) sans sacrifier confort thermique
- Généralisation à différents types de bâtiments et conditions climatiques

**Limitations des résultats:**
- Données occupants limitées (métabolisme et vêtements supposés constants)
- Validation expérimentale sur une seule maison (généralisation à établir)
- Fenêtre déploiement réel courte (doit être validée long-terme)

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| EnergyPlus | [https://energyplus.net](https://energyplus.net) | Simulateur thermique bâtiments |
| ASHRAE 55 | [https://www.ashrae.org/](https://www.ashrae.org/) | Standard confort thermique (PMV/PPD) |
| NREL Weather Data | [https://nsrdb.nrel.gov/](https://nsrdb.nrel.gov/) | Données météorologiques TMY |
| Données Maison Réelle | Sur demande | Dataset maison de déploiement |

---

## ⚠️ Limites identifiées

- **Estimation paramètres occupants** — Métabolisme et vêtements supposés constants ou pré-spécifiés (pas capteurs)
- **Modèle PMV limite** — Ne capture pas adaptabilité psychologique de l'occupant au fil du temps
- **Scalabilité multi-occupants** — Test avec peu d'occupants; complexité avec 10+ occupants non explorée
- **Validation expérimentale courte** — Déploiement réel limité à quelques mois
- **Modèle environnemental simplifié** — Hypothèses de bien-mélange d'air (pas gradients spatiaux)
- **Dépendance des hyperparamètres** — Pondération α/β/γ doit être ajustée par type bâtiment

---

## 🔌 Pertinence pour un thermostat Edge AI

Cet article est **très pertinent** car il adresse un cas d'usage réel critique:

1. **Adaptabilité aux occupants réels** — Thermostat doit s'adapter à des gens avec métabolismes et vêtements variés
2. **Métrique de confort reconnue** — PMV est standard ASHRAE accepté universellement (utile pour validation)
3. **Validation expérimentale** — Déploiement réel montre faisabilité pratique vs simulation-only
4. **Économies mesurables** — 21% réduction coûts énergétiques réels est quantifiable pour ROI utilisateur
5. **Flexibilité modèle** — Framework extensible pour intégrer capteurs additionnels (CO2, luminosité, etc.)

**Applicabilité embarquée:** Medium-High
**Raison:** Dueling DQN léger en ressources, modèle PMV calculable rapidement. Peut s'exécuter sur thermostat avec 256MB RAM. Entraînement offline sur données maison, inference leger sur device. Principal défi: obtenir paramètres occupants (métabolisme, vêtements) — nécessite capteurs additionnels ou auto-apprentissage.

---

## 📚 Citation BibTeX

```bibtex
@article{Shi2024,
  title = {Towards various occupants with different thermal comfort requirements: {A} {DRL} approach combined with a dynamic {PMV} model for {HVAC} control in buildings},
  author = {Shi, Zekun and Zheng, Ruifan and Zhao, Jun and Shen, Rendong and Gu, Lei and Liu, Yuanchao and Wu, Jiahui and Wang, Guangliang},
  journal = {Energy Conversion and Management},
  volume = {320},
  pages = {118995},
  year = {2024},
  publisher = {Elsevier},
  doi = {10.1016/j.enconman.2024.118995}
}
```
