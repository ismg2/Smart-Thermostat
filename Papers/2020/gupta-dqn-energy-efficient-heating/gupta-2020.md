---
title: "Energy-efficient heating control for smart buildings with deep reinforcement learning"
authors:
  - "Gupta, Anchal"
  - "Badr, Youakim"
  - "Negahban, Ashkan"
  - "Qiu, Robin G."
year: 2021
venue: "Journal of Building Engineering"
publisher: "Elsevier"
doi: "10.1016/j.jobe.2020.101739"
url: "https://www.sciencedirect.com/science/article/abs/pii/S2352710220333726"
pdf_url: null
tags:
  - hvac
  - dqn
  - deep-reinforcement-learning
  - heating
  - smart-building
  - thermal-comfort
  - energy-efficiency
domains:
  - "HVAC Control"
  - "Building Energy Management"
methods:
  - "Deep Q-Network (DQN)"
  - "Reinforcement Learning"
hardware_targets: []
datasets:
  - name: "EnergyPlus Simulation"
    url: "https://energyplus.net"
    description: "Building energy simulation environment"
read: false
relevance: 4
category: "RL-HVAC"
date_added: 2026-02-19
---

# Energy-efficient heating control for smart buildings with deep reinforcement learning

> **Source :** [Journal of Building Engineering - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2352710220333726) | **Année :** 2021 | **Auteurs :** Gupta, Badr, Negahban, Qiu

---

## 📄 Résumé

This paper presents a real-time decision-making algorithm for heating control in smart buildings using deep reinforcement learning. The approach employs a Deep Q-Network (DQN) controller to optimize both thermal comfort and energy consumption in building HVAC systems. The study demonstrates that DRL-based smart controllers can effectively balance conflicting objectives—maintaining occupant comfort while minimizing energy usage—in ways that traditional thermostat-based controllers cannot achieve.

**Résumé français :** Ce travail propose un algorithme d'apprentissage par renforcement profond pour le contrôle du chauffage dans les bâtiments intelligents. En utilisant une approche DQN, les chercheurs développent un contrôleur capable d'optimiser simultanément le confort thermique et la consommation d'énergie. L'étude montre que cette approche surpasse significativement les contrôleurs traditionnels en termes de confort des occupants et d'efficacité énergétique.

---

## 🎯 Contributions principales

1. **Algorithme de contrôle DQN pour le chauffage** — Présentation d'un contrôleur en temps réel basé sur DQN pour optimiser le chauffage des bâtiments intelligents, capable de gérer les compromis entre confort thermique et consommation énergétique.

2. **Amélioration du confort thermique** — Démonstration d'une amélioration de 15-30% du confort thermique (réduction de l'écart avec la température de consigne) comparé aux thermostats traditionnels.

3. **Réduction de la consommation énergétique** — Atteinte d'une réduction de 5-12% de la consommation d'énergie de chauffage tout en maintenant ou améliorant le confort des occupants.

4. **Analyse de contrôle centralisé vs décentralisé** — Étude comparative des stratégies de contrôle pour plusieurs bâtiments, montrant les avantages et limitations de chaque approche selon la configuration et le nombre de bâtiments.

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

Le papier utilise un **Deep Q-Network (DQN)**, un algorithme d'apprentissage par renforcement profond qui estime les valeurs optimales d'action (Q-values) pour chaque état du système. Le DQN combine:

- **Réseau de neurones profond** : Approche fonction-approximation pour estimer Q(s,a)
- **Experience replay** : Stockage et rééchantillonnage des transitions pour améliorer la stabilité de l'apprentissage
- **Target network** : Réseau séparé pour le calcul des cibles Q, réduisant les divergences

### Architecture du système

Le système de contrôle opère dans un cycle d'apprentissage et décision :

1. **État du système** : Température intérieure actuelle, température extérieure, historique des températures, présence occupants
2. **Espace d'actions** : Ajustements discrets du point de consigne de chauffage ou puissance de chauffage (contrôle multi-niveaux)
3. **Fonction de récompense** : Combinaison pondérée du confort thermique (écart minimal par rapport à la consigne) et de la consommation énergétique (minimisation)
4. **Processus d'apprentissage** : Interaction itérative avec l'environnement de simulation pour affiner la politique de contrôle

### Environnement de test / Simulation

- **Plateforme de simulation** : EnergyPlus, un simulateur de performance énergétique des bâtiments largement utilisé
- **Configuration expérimentale** : Modèles de bâtiments simples à complexes avec différentes configurations de chauffage
- **Données météorologiques** : Profils typiques de température extérieure pour différents climats
- **Durée d'apprentissage** : Plusieurs périodes de chauffage (jours/semaines) de simulation pour permettre la convergence du DQN

### Hyperparamètres clés

- **Taille du réseau Q** : Architecture multicouche (détails spécifiques non pleinement disponibles)
- **Taux d'apprentissage** : Optimisé pour convergence stable du DQN
- **Facteur de discount (gamma)** : Typiquement 0.99 pour équilibrer les récompenses immédiates et futures
- **Epsilon-greedy exploration** : Décroissance progressive de l'exploration pour exploitation progressive

---

## 📊 Résultats clés

| Métrique | Résultat | Référence comparée |
|----------|----------|-------------------|
| Amélioration confort thermique | 15-30% | Thermostat traditionnel |
| Réduction consommation énergétique | 5-12% | Thermostat traditionnel |
| Gestion multi-bâtiments | Meilleure avec décentralisation | Contrôle centralisé |

**Points forts :**
- Le contrôleur DQN optimise simultanément deux objectifs conflictuels (confort vs énergie)
- Amélioration substantielle du confort sans sacrifice énergétique majeur
- Approche adaptée au contrôle en temps réel dans bâtiments complexes
- Montre l'applicabilité de DRL à des problèmes réels de gestion énergétique

**Limitations observées :**
- Les résultats sont basés sur simulation (EnergyPlus) plutôt que déploiement réel
- Performance dépendante de la qualité et complétude des états observés
- Convergence du DQN peut nécessiter temps d'apprentissage significatif en pratique

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| EnergyPlus | [https://energyplus.net](https://energyplus.net) | Simulateur de performance énergétique des bâtiments, standard pour validation |

---

## ⚠️ Limites identifiées

- **Validation simulation uniquement** : Les résultats proviennent de simulations EnergyPlus, pas de déploiements réels avec données de bâtiments réels
- **État d'observation limité** : Performance dépend de la qualité de l'observation complète des états (température, conditions météo)
- **Temps d'entraînement** : Convergence du DQN peut nécessiter périodes d'apprentissage étendues
- **Scalabilité** : Approche centralisée complexe pour très grands bâtiments ou réseaux multi-bâtiments
- **Coûts de calcul** : Entraînement et inférence du DQN plus coûteux que contrôle traditionnel

---

## 🔌 Pertinence pour un thermostat Edge AI

Ce papier est hautement pertinent pour le design d'un thermostat Edge AI car il démontre comment les techniques d'apprentissage par renforcement profond peuvent optimiser simultanément confort et efficacité énergétique—deux objectifs critiques pour tout système de thermostat intelligent.

L'approche DQN offre un bon équilibre entre performance et complexité computationnelle. Les résultats montrent que même avec une optimisation relativement simple (DQN vs algorithmes plus avancés), on peut obtenir des gains significatifs. L'utilisation d'EnergyPlus pour la validation fournit un benchmark standard dans l'industrie.

Cependant, pour un déploiement Edge AI, il faudrait considérer :
- **Réduction du modèle** : Quantification ou distillation du DQN pour exécution sur matériel embarqué
- **Apprentissage en ligne** : Adaptation continue aux patterns thermiques spécifiques du bâtiment
- **Observation partielle** : Gestion des états partiellement observables typiques dans les thermostats réels

**Applicabilité embarquée :** Medium
**Raison :** Le DQN est relativement simple comparé à des approches plus avancées (Actor-Critic, PPO), ce qui le rend candidat pour optimisation embarquée. Cependant, les temps d'entraînement et les besoins mémoire devront être validés pour les contraintes d'un thermostat edge.

---

## 📚 Citation BibTeX

```bibtex
@article{Gupta2021,
  title = {Energy-efficient heating control for smart buildings with deep reinforcement learning},
  author = {Gupta, Anchal and Badr, Youakim and Negahban, Ashkan and Qiu, Robin G.},
  journal = {Journal of Building Engineering},
  year = {2021},
  volume = {34},
  pages = {101739},
  doi = {10.1016/j.jobe.2020.101739},
  publisher = {Elsevier}
}
```
