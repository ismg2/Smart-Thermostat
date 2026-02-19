---
title: "Reinforcement learning for HVAC control in intelligent buildings: A technical and conceptual review"
authors:
  - "Al Sayed, Khalil"
  - "Boodi, Abhinandana"
  - "Sadeghian Broujeny, Roozbeh"
  - "Beddiar, Karim"
year: 2024
venue: "Journal of Building Engineering"
publisher: "Elsevier"
doi: "10.1016/j.jobe.2024.110085"
url: "https://www.sciencedirect.com/science/article/pii/S235271022401653X"
pdf_url: null
tags:
  - hvac
  - reinforcement-learning
  - survey
  - review
  - building-control
  - intelligent-buildings
domains:
  - "HVAC Control"
methods:
  - "DQN"
  - "Actor-Critic"
  - "Policy Gradient"
  - "Meta-RL"
hardware_targets: []
datasets:
  - name: "EnergyPlus"
    url: "https://energyplus.net"
    description: "Building energy simulation platform"
read: false
relevance: 5
category: "Survey"
date_added: 2026-02-19
---

# Reinforcement Learning for HVAC Control in Intelligent Buildings: A Technical and Conceptual Review

> **Source:** [Journal of Building Engineering](https://www.sciencedirect.com/science/article/pii/S235271022401653X) | **Volume:** 95, pp. 110085 | **Year:** 2024 | **Authors:** Al Sayed et al.

---

## 📄 Résumé

Ce travail de revue technique et conceptuelle fait un état des lieux complet de l'application de l'apprentissage par renforcement (RL) pour le contrôle des systèmes HVAC dans les bâtiments intelligents. Les auteurs explorent les limites des contrôleurs HVAC traditionnels et montrent comment le RL offre une optimisation supérieure. La revue systématique couvre les applications du RL aux systèmes de contrôle HVAC, explique les fondations théoriques du RL et l'impact de ces concepts sur le choix des algorithmes pour différents problèmes de contrôle. Le travail aborde également les défis et solutions pour implémenter le RL dans des bâtiments réels, et suggère des directions futures incluant le meta-RL pour avancer le domaine du contrôle HVAC.

This comprehensive technical review examines reinforcement learning applications for HVAC control in intelligent buildings, exploring traditional controller limitations and demonstrating how RL provides superior optimization capabilities. The paper systematically reviews RL applications, explains theoretical foundations, addresses implementation challenges in real buildings, and proposes meta-RL as a future direction.

---

## 🎯 Contributions principales

1. **État des lieux complet** — Revue systématique et exhaustive des travaux de recherche appliquant le RL au contrôle HVAC depuis 2019, offrant une perspective panoramique du domaine
2. **Analyse théorique et conceptuelle** — Explication des fondations du RL et démonstration de comment les concepts théoriques influencent le choix des algorithmes pour différents problèmes de contrôle de bâtiments
3. **Identification des algorithmes appropriés** — Classement et recommandation des algorithmes RL les plus adaptés selon le type de problème (mono-zone vs multi-zone, déterministe vs stochastique)
4. **Analyse des défis pratiques** — Discussion approfondie des obstacles à l'implémentation du RL dans des bâtiments réels, incluant la simulation, la validation et le déploiement
5. **Direction future avec Meta-RL** — Proposition d'utiliser le meta-RL pour améliorer l'adaptabilité et la généralisation des contrôleurs RL dans différents environnements de bâtiments

---

## 🔬 Méthodologie

### Approche de revue
La revue adopte une approche structurée combinant:
- Analyse critique de la littérature publiée depuis 2019
- Catégorisation des travaux selon les types de problèmes (mono-zone, multi-zone, multi-objectifs)
- Classification des algorithmes RL utilisés et leur pertinence selon le contexte
- Identification des approches théoriques et conceptuelles sous-jacentes

### Fondations théoriques couvertes
- Processus de décision markovien (MDP)
- Value-based methods (DQN, Double DQN, Dueling DQN)
- Policy-based methods (Actor-Critic, PPO, DDPG)
- Actor-Critic methods
- Meta-RL approaches

### Environnements de test / Simulation
- **EnergyPlus** — Principal simulateur d'énergie de bâtiment pour évaluer les performances
- **BCVTB** (Building Controls Virtual Test Bed) — Plateforme pour test des contrôleurs
- **Simulateurs commerciaux** — TRNSYS, MATLAB/Simulink
- **Données réelles de bâtiments** — Validation expérimentale des stratégies de contrôle

### Catégories de problèmes étudiées
1. **Contrôle mono-zone** — Bâtiments simples avec un seul espace conditionné
2. **Contrôle multi-zone** — Bâtiments complexes avec zones interdépendantes
3. **Problèmes multi-objectifs** — Optimisation simultanée d'énergie et de confort
4. **Systèmes distribués** — Contrôle multi-agents pour bâtiments interconnectés

---

## 📊 Résultats clés

| Aspect | Résultat | Implication |
|--------|----------|------------|
| État du domaine | Croissance exponentielle depuis 2019 | Domaine actif et en développement |
| Algorithmes prédominants | DQN et ses variantes (DDPG, A3C) | Approches value-based dominantes |
| Améliorations énergétiques | 10-30% réduction consommation typique | Gains significatifs vs contrôle classique |
| Défis identifiés | Simulation vs réalité, échelle, déploiement | Brèche recherche-industrie importante |

**Points forts:**
- Panorama complet de la littérature actuelle depuis 2019
- Analyse théorique solide des concepts de RL appliqués au contrôle HVAC
- Recommandations pratiques sur le choix d'algorithmes selon le problème
- Identification claire des gaps entre recherche académique et déploiement industriel

**Limites de la revue:**
- Peu de données sur les déploiements réels en bâtiments commerciaux existants
- Variations importantes dans les méthodologies d'évaluation entre études
- Nécessité d'étudier plus systématiquement l'impact du transfer learning et de l'adaptabilité

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| EnergyPlus | [https://energyplus.net](https://energyplus.net) | Simulateur de performance énergétique des bâtiments |
| BCVTB | [https://simulationcores.nrel.gov/bcvtb/](https://simulationcores.nrel.gov/bcvtb/) | Virtual Test Bed pour contrôle de bâtiments |
| Journal of Building Engineering | [https://www.sciencedirect.com/journal/journal-of-building-engineering](https://www.sciencedirect.com/journal/journal-of-building-engineering) | Revue publiée par Elsevier |

---

## ⚠️ Limites identifiées

- **Brèche simulation-réalité** — Écart important entre performance en simulation et en déploiement réel
- **Disponibilité des données** — Manque de données de bâtiments réels accessibles publiquement pour l'entraînement
- **Scalabilité** — Difficulté à généraliser les contrôleurs d'un bâtiment à un autre
- **Complexité d'intégration** — Défis techniques et organisationnels pour intégrer RL dans les systèmes existants
- **Validité des modèles** — Fiabilité insuffisante des modèles thermiques utilisés dans la simulation
- **Absence de standards** — Manque de méthodologies standardisées pour évaluer et comparer les approches

---

## 🔌 Pertinence pour un thermostat Edge AI

Cette revue est **fondamentale** pour concevoir un thermostat intelligent embarqué car elle fournit:

1. **Recommandations d'algorithmes** — Analyse de quel algorithme RL choisir selon les contraintes de ressources et la complexité du problème (mono-zone vs multi-zone)
2. **Aperçu du paysage scientifique** — Compréhension du state-of-the-art pour éviter de réinventer la roue
3. **Leçons apprises** — Erreurs communes et approches éprouvées pour intégrer RL dans des systèmes réels
4. **Métriques de performance** — Standards d'évaluation pour benchmarker un prototype de thermostat
5. **Directions futures** — Meta-RL pour adapter un modèle pré-entraîné aux préférences thermiques individuelles sans réentraînement

**Applicabilité embarquée:** High
**Raison:** En tant que revue comprehensive et récente (2024), elle guide les choix technologiques pour un thermostat Edge AI: DQN pour réseau léger, Actor-Critic pour meilleure stabilité, et meta-RL pour adaptabilité personnalisée aux préférences individuelles tout en minimisant les ressources de calcul embarquées.

---

## 📚 Citation BibTeX

```bibtex
@article{AlSayed2024,
  title = {Reinforcement learning for {HVAC} control in intelligent buildings: {A} technical and conceptual review},
  author = {Al Sayed, Khalil and Boodi, Abhinandana and Sadeghian Broujeny, Roozbeh and Beddiar, Karim},
  journal = {Journal of Building Engineering},
  volume = {95},
  pages = {110085},
  year = {2024},
  publisher = {Elsevier},
  doi = {10.1016/j.jobe.2024.110085}
}
```
