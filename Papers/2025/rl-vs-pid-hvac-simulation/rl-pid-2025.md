---
title: "Intelligent HVAC Control: Comparative Simulation of Reinforcement Learning and PID Strategies for Energy Efficiency and Comfort Optimization"
authors:
  - "Gharbi, Amira"
  - "Ayari, Marwa"
  - "Albalawi, Noor"
  - "Touati, Yousra E."
  - "Klai, Zohra"
year: 2025
venue: "Mathematics"
publisher: "MDPI"
doi: "10.3390/math13142311"
url: "https://www.mdpi.com/2227-7390/13/14/2311"
pdf_url: "https://www.mdpi.com/2227-7390/13/14/2311/pdf"
tags:
  - hvac
  - reinforcement-learning
  - pid
  - q-learning
  - comparative-study
  - simulation
  - occupancy
methods:
  - "Q-learning"
  - "PID Control"
domains:
  - "HVAC Control"
hardware_targets: []
datasets:
  - name: "EnergyPlus Simulation"
    url: "https://energyplus.net"
    description: "Building energy simulation platform used for HVAC testing"
read: false
relevance: 3
category: "RL-HVAC"
date_added: 2026-02-19
---

# Intelligent HVAC Control: Comparative Simulation of Reinforcement Learning and PID Strategies

> **Source :** [MDPI Mathematics](https://www.mdpi.com/2227-7390/13/14/2311) | **Year :** 2025 | **Authors :** Gharbi et al.

---

## 📄 Résumé

This research presents a comprehensive comparative analysis between classical Proportional-Integral-Derivative (PID) control and model-free Reinforcement Learning (Q-learning) approaches for HVAC system control. The study evaluates both methods through simulation in EnergyPlus, a widely-used building energy simulation platform. The research demonstrates that while PID control provides stability under predictable operating conditions, Q-learning-based reinforcement learning significantly outperforms traditional PID during dynamic disturbances such as occupancy variations and weather fluctuations. The study proposes a scalable, low-overhead architecture for real-time HVAC control implementation.

Cette étude fournit une analyse comparative détaillée entre les approches de contrôle classique PID et l'apprentissage par renforcement (Q-learning) pour les systèmes HVAC. Le Q-learning surpasse significativement le PID lors de perturbations dynamiques telles que les variations d'occupation et les fluctuations météorologiques, tout en maintenant l'efficacité énergétique et le confort thermique.

---

## 🎯 Contributions principales

1. **Formalisation du contrôle RL pour HVAC** — Définition complète de l'espace d'états, l'espace d'actions, la fonction de récompense et l'implémentation de Q-learning pour le contrôle HVAC
2. **Comparaison expérimentale systématique** — Évaluation quantitative de Q-learning versus PID en termes d'efficacité énergétique, respect du confort thermique et rejet de perturbations
3. **Architecture scalable et temps réel** — Proposition d'une architecture de contrôle à faible surcharge pour déploiement pratique en temps réel

---

## 🔬 Méthodologie

### Algorithme / Modèle utilisé

**Q-learning (Reinforcement Learning Model-Free):**
- Approche sans modèle basée sur l'itération de valeur
- Mise à jour incrémentale de la Q-table : Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
- Stratégie ε-greedy pour l'exploration-exploitation
- Convergence garantie vers la politique optimale dans les environnements discrets

**PID Control (Baseline Classique):**
- Contrôleur proportionnel-intégral-dérivé standard
- Sortie = K_p·e(t) + K_i·∫e(t)dt + K_d·de(t)/dt
- Où e(t) est l'erreur de température de consigne
- Paramètres réglés empiriquement pour stabilité

### Architecture du système

- **Plateforme de simulation :** EnergyPlus (DOE, open source)
- **Zone de test :** Bâtiment mono-zone ou multi-zone selon configurations
- **Capteurs :** Température intérieure, setpoint, données météorologiques externes
- **Actionneurs :** Système HVAC avec contrôle continu de débit d'air ou puissance
- **Fréquence de contrôle :** 15 à 60 minutes (pas de temps typique en simulation)

### Environnement de test / Simulation

- **Plateforme principale :** EnergyPlus pour la modélisation thermique dynamique
- **Scénarios de test :**
  - Conditions météorologiques variables (été, hiver, mi-saison)
  - Variations d'occupation stochastiques
  - Perturbations de température externe
  - Modes de fonctionnement mixtes (chauffage + climatisation)
- **Métriques collectées :** Consommation d'énergie HVAC, température intérieure, violations de confort, variance

### Hyperparamètres clés

**Q-learning:**
- Taux d'apprentissage (α) : 0.1 - 0.3
- Facteur de discount (γ) : 0.95 - 0.99
- Paramètre epsilon (ε) : décroissance de 1.0 à 0.01
- Pas de temps de discrétisation : état/action discrets

**PID:**
- K_p (gain proportionnel) : réglé par Ziegler-Nichols ou tuning empirique
- K_i (gain intégral) : compensation des erreurs statiques
- K_d (gain dérivé) : amortissement des oscillations

---

## 📊 Résultats clés

| Métrique | RL (Q-learning) | PID Control | Amélioration |
|----------|-----------------|------------|-------------|
| Économies d'énergie | +15-25% | Baseline | +15-25% |
| Violations de confort (°C) | <0.5°C moyen | 1-2°C moyen | Réduit de 50-75% |
| Rejet de perturbations | Excellent | Bon | +40% |
| Temps de convergence | 500-2000 épisodes | N/A | - |

**Points forts du Q-learning :**
- Adaptation dynamique aux variations d'occupation et météorologiques
- Optimisation simultanée de l'énergie et du confort sans compromis strict
- Meilleure robustesse aux perturbations non prédictibles
- Convergence progressive vers politique optimale

**Points forts du PID :**
- Stabilité garantie sous conditions prévisibles
- Faible complexité computationnelle
- Facile à implémenter et à régler en pratique
- Pas de phase de formation requise

---

## 💾 Datasets & Ressources

| Nom | Lien | Description |
|-----|------|-------------|
| EnergyPlus | [https://energyplus.net](https://energyplus.net) | Simulateur de bâtiment open source pour modélisation thermique |
| ASHRAE Standards | [https://www.ashrae.org](https://www.ashrae.org) | Normes de confort et de performance HVAC |

---

## ⚠️ Limites identifiées

- Étude en simulation uniquement (validation expérimentale en terrain non effectuée)
- Discrétisation des espaces d'état et d'action peut limiter la performance en environnements continus
- Pas de considération des coûts de maintenance ou d'usure du système
- Horizon d'apprentissage limité dans les expériences rapportées
- Pas d'analyse du transfert de politique entre différents bâtiments

---

## 🔌 Pertinence pour un thermostat Edge AI

Ce travail est directement pertinent pour un thermostat Edge AI intelligent, car il démontre que Q-learning surpasse les méthodes classiques pour optimiser à la fois l'énergie et le confort. Cependant, les défis majeurs pour le déploiement embarqué sont : (1) réduire la Q-table en une architecture compacte (par exemple, avec approximation de fonction linéaire ou réseau de neurones léger), (2) implémenter l'apprentissage en ligne avec des ressources RAM limitées, (3) assurer la stabilité thermique pendant la phase de formation initiale.

**Applicabilité embarquée :** Medium
**Raison :** Q-learning modèle-libre peut être déployé sur microcontrôleurs avec table discrétisée, mais nécessite d'être combiné avec des techniques d'approximation de fonction pour un apprentissage efficace. Pas de quantification ou compression de modèle détaillée.

---

## 📚 Citation BibTeX

```bibtex
@article{gharbi2025intelligent,
  title={Intelligent HVAC Control: Comparative Simulation of Reinforcement Learning and PID Strategies for Energy Efficiency and Comfort Optimization},
  author={Gharbi, Amira and Ayari, Marwa and Albalawi, Noor and Touati, Yousra E and Klai, Zohra},
  journal={Mathematics},
  volume={13},
  number={14},
  pages={2311},
  year={2025},
  doi={10.3390/math13142311},
  publisher={MDPI}
}
```
