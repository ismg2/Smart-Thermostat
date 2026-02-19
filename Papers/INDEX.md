# Smart Thermostat AI Bibliography - Complete Index

## Overview

This collection contains comprehensive Obsidian-compatible research notes for 8 papers on AI and Machine Learning for Smart Thermostat Control and Edge AI applications. All papers published 2025-2026 (latest research).

**Total Papers:** 8
**Total Content:** ~110 KB of detailed notes
**Format:** Markdown with YAML frontmatter
**Language:** Bilingual (English + French)
**Last Updated:** 2026-02-19

---

## Navigation by Relevance to Edge AI Thermostat

### TIER 1: CRITICAL FOR IMPLEMENTATION (⭐⭐⭐⭐⭐ Relevance 5)

#### 1. Paper 3: Lightweight LSTM Temperature Forecasting
- **File:** `2025/ml-indoor-temp-lightweight/ml-indoor-temp-2025.md`
- **Title:** Innovative machine learning approaches for indoor air temperature forecasting in smart infrastructure
- **Publisher:** Scientific Reports (Nature)
- **Key Metric:** 50,851 parameters (~203.4 KB) - FITS MICROCONTROLLER
- **Impact:** Real-time temperature prediction for MPC on ESP32/STM32
- **Why Critical:** Only LSTM model sized for embedded devices with >0.90 R² accuracy

#### 2. Paper 7: Real-time Occupancy on ESP32
- **File:** `2026/tinyml-occupancy-esp32/tinyml-esp32-2026.md`
- **Title:** Optimizing room occupancy estimation on the edge: A TinyML and sensor network approach
- **Publisher:** ScienceDirect/Elsevier
- **Key Metric:** R²=0.923, 997µs latency, 1.426 MB storage
- **Impact:** Production-ready occupancy detection (Random Forest)
- **Why Critical:** Direct implementation guide for occupancy-aware HVAC control

#### 3. Paper 8: Sub-Kilobyte Green AI for Occupancy
- **File:** `2026/sustainability-tiny-deep-learning/sustainability-tdl-2026.md`
- **Title:** Sustainability-driven tiny deep learning empowering green edge intelligence for smart environments
- **Publisher:** Springer Nature (Discover Sustainability)
- **Key Metric:** <1 KB models, >85% accuracy, <10 mJ per inference
- **Impact:** Scalable to billion-device deployments, carbon-neutral AI
- **Why Critical:** Alternative to Paper 7 if extreme memory constraints; green AI perspective

---

### TIER 2: HIGHLY RELEVANT (⭐⭐⭐⭐ Relevance 4)

#### 4. Paper 2: Expert-Guided Reinforcement Learning for HVAC
- **File:** `2025/efficient-rl-expert-guided-hvac/expert-rl-2025.md`
- **Title:** Efficient and assured reinforcement learning-based building HVAC control with heterogeneous expert-guided training
- **Publisher:** Scientific Reports (Nature)
- **Key Metric:** 8.8X speedup in DRL training via expert guidance
- **Impact:** On-device learning with safety guarantees (runtime shielding)
- **Why Important:** Enables thermostat to learn occupant preferences without cloud

#### 5. Paper 4: CNN-M-LSTM for Comfort + Load Prediction
- **File:** `2025/bayesian-cnn-m-lstm-comfort/cnn-m-lstm-2025.md`
- **Title:** Bayesian Optimized CNN-M-LSTM for Thermal Comfort Prediction and Load Forecasting
- **Publisher:** MDPI (Designs)
- **Key Metric:** Dual-output (PMV + load), Bayesian hyperparameter optimization
- **Impact:** Occupant comfort prediction (PMV/PPD indices) + energy forecasting
- **Why Important:** Personalized comfort model beyond simple temperature setpoint

#### 6. Paper 5: Digital Twin + Attention-LSTM
- **File:** `2025/digital-twin-lstm-hvac/digital-twin-lstm-2025.md`
- **Title:** Digital twin based deep learning framework for personalized thermal comfort prediction and energy efficient operation
- **Publisher:** Scientific Reports (Nature)
- **Key Metric:** 14% energy reduction + 22% productivity improvement
- **Impact:** Anticipatory HVAC control via virtual building model
- **Why Important:** Long-term trajectory for advanced thermostat intelligence

#### 7. Paper 6: TinyML Systematic Review (66 papers)
- **File:** `2025/edge-intelligence-tinyml-cities/tinyml-cities-2025.md`
- **Title:** Edge Intelligence in Urban Landscapes: Reviewing TinyML Applications for Connected and Sustainable Smart Cities
- **Publisher:** MDPI (Electronics)
- **Key Metric:** Hardware comparison (ESP32, STM32, Arduino), inference latencies 21ms-1s
- **Impact:** Best practices guide for embedded ML deployment
- **Why Important:** Essential reference for hardware selection and optimization techniques

---

### TIER 3: FOUNDATIONAL (⭐⭐⭐ Relevance 3)

#### 8. Paper 1: Q-Learning vs PID Control Comparison
- **File:** `2025/rl-vs-pid-hvac-simulation/rl-pid-2025.md`
- **Title:** Intelligent HVAC Control: Comparative Simulation of Reinforcement Learning and PID Strategies
- **Publisher:** MDPI (Mathematics)
- **Key Metric:** Q-learning outperforms PID by 15-25% under disturbances
- **Impact:** Theoretical validation of RL for HVAC
- **Why Important:** Justifies shift from classical control to learning-based approaches

---

## Navigation by Topic

### Machine Learning Methods

- **Reinforcement Learning:** Papers 1, 2
- **LSTM Networks:** Papers 3, 4, 5
- **Convolutional Neural Networks:** Paper 4, 5
- **Decision Tree Ensembles:** Paper 7, 8
- **Attention Mechanisms:** Paper 5
- **Bayesian Optimization:** Paper 4

### Application Domains

- **Temperature Forecasting:** Papers 3, 4, 5
- **Occupancy Detection:** Papers 2, 7, 8
- **Comfort Prediction:** Papers 4, 5
- **Load Forecasting:** Papers 4, 5
- **HVAC Control:** Papers 1, 2, 5
- **Energy Efficiency:** Papers 1, 2, 8

### Hardware & Implementation

- **ESP32:** Papers 6, 7, 8
- **STM32:** Papers 6, 7
- **Arduino:** Papers 6, 8
- **Microcontroller-Specific:** Papers 3, 6, 7, 8
- **TinyML Frameworks:** Papers 6, 7, 8

### Key Methodologies

- **Model Quantization:** Papers 3, 6, 7, 8
- **Network Pruning:** Papers 6, 7, 8
- **Knowledge Distillation:** Paper 8
- **Transfer Learning:** Paper 2
- **Digital Twin:** Paper 5
- **Sensor Fusion:** Paper 7

---

## Quick Reference: Key Metrics & Results

| Paper | Model | Accuracy | Latency | Size | Hardware |
|-------|-------|----------|---------|------|----------|
| 3 | LSTM | R²=0.90-0.95 | <100ms | 203 KB | ESP32/STM32 |
| 7 | Random Forest | R²=0.923 | 997µs | 1.4 MB | ESP32 |
| 8 | TinyML | >85% | <10ms | <1 KB | Arduino Nano |
| 2 | DRL+Expert | Optimal | 50-100ms | Variable | Any CPU |
| 4 | CNN-M-LSTM | R²=0.85-0.92 | <50ms | 5-10 MB | GPU needed |
| 5 | Attention-LSTM | High | 50-200ms | 10-20 MB | GPU needed |
| 1 | Q-Learning | 15-25% better | Variable | Variable | Simulation |
| 6 | Review | N/A | 21ms-1s | <10 MB | Various |

---

## Implementation Roadmap for Smart Thermostat

### Phase 1: Core Functionality (Minimum Viable Product)
**Focus:** Papers 7 & 3
- Implement occupancy detection (Random Forest, Paper 7)
- Implement temperature forecasting (LSTM, Paper 3)
- Basic eco/comfort mode switching
- Hardware: ESP32

### Phase 2: Safety & Adaptation (Production Ready)
**Focus:** Papers 2 & 6
- Add expert-guided learning (Paper 2)
- Runtime shielding for safety (Paper 2)
- Optimize for hardware constraints (Paper 6)
- Cloud-free operation validation

### Phase 3: User Comfort (Premium Features)
**Focus:** Papers 4 & 5
- Add comfort metrics (PMV/PPD, Paper 4)
- Personalization via learning (Paper 2)
- Optional: Digital twin for prediction (Paper 5)
- Optional: WiFi connectivity for cloud analytics

### Phase 4: Sustainability (Long-term Vision)
**Focus:** Paper 8
- Ultra-lightweight TDL models
- Energy-per-inference optimization
- Green AI reporting (CO₂ emissions)
- Billion-device scale feasibility

---

## File Organization

```
Papers/
├── 2025/
│   ├── rl-vs-pid-hvac-simulation/
│   │   └── rl-pid-2025.md
│   ├── efficient-rl-expert-guided-hvac/
│   │   └── expert-rl-2025.md
│   ├── ml-indoor-temp-lightweight/
│   │   └── ml-indoor-temp-2025.md
│   ├── bayesian-cnn-m-lstm-comfort/
│   │   └── cnn-m-lstm-2025.md
│   ├── digital-twin-lstm-hvac/
│   │   └── digital-twin-lstm-2025.md
│   └── edge-intelligence-tinyml-cities/
│       └── tinyml-cities-2025.md
├── 2026/
│   ├── tinyml-occupancy-esp32/
│   │   └── tinyml-esp32-2026.md
│   └── sustainability-tiny-deep-learning/
│       └── sustainability-tdl-2026.md
├── INDEX.md (this file)
└── README.md (general overview)
```

---

## How to Use These Notes in Obsidian

1. **Open folder in Obsidian** as new vault
2. **Use tags for filtering:** Click any tag (#hvac, #lstm, #esp32) to find related papers
3. **Enable graph view:** Visualize connections between papers by topic
4. **Create links:** Add `[[Paper Title]]` references between notes
5. **Use templates:** Copy methodology sections for your own research
6. **Search:** Use full-text search (Ctrl+Shift+F) across all papers
7. **Export:** Select papers, export as LaTeX/PDF for writing

---

## Citation & Attribution

All papers are properly cited in BibTeX format within each note's bottom section. To cite a paper:

1. Open relevant note
2. Scroll to "📚 Citation BibTeX" section
3. Copy the bibtex entry
4. Paste into your bibliography manager

---

## Notes & Disclaimers

- **Accuracy:** Paper metadata verified against official publisher websites (Feb 2026)
- **Open Access:** All included papers available via open/legal access paths
- **Relevance Scores:** Based on direct applicability to embedded smart thermostat design
- **Completeness:** Each note contains abstract, full methodology, results, and custom "Edge AI Thermostat Relevance" analysis
- **Language:** Content primarily French with English quotes/abstracts preserved
- **Updates:** New papers can be added following the same template

---

## Authors & Contributors

**Bibliography Compiled:** 2026-02-19
**Format:** Obsidian Markdown + YAML Frontmatter
**Template:** Custom (AI for Smart Thermostats specialization)

---

## Quick Links

- **Smart Thermostat Project:** [Project Directory]
- **Hardware Reference:** See Paper 6 for ESP32/STM32/Arduino details
- **Implementation Guide:** See Papers 3 & 7 for immediate deployment options
- **Research Foundation:** See Papers 1 & 2 for theoretical background

---

**Happy researching! Use these notes to design the next generation of edge-AI-powered smart thermostats.**
