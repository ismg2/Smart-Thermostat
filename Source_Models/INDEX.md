# Source Models Index - Quick Reference Guide

## Quick Navigation

### By Task/Use Case

**HVAC Control & Optimization:**
- [Gnu-RL](https://github.com/INFERLab/Gnu-RL) - Precocial RL with differentiable MPC
- [PEARL](https://github.com/enjeeneer/PEARL) - Zero-shot emission reduction
- [CLUE](https://github.com/ryeii/CLUE) - Safe model-based RL (2024)
- [OCTOPUS](https://sites.ucmerced.edu/files/wdu/files/octopus.pdf) - Multi-system building control
- [DRL-Building-Energy-Ctr](https://github.com/ULudo/DRL-Building-Energy-Ctr) - Heat pump & storage control

**Energy Consumption Prediction:**
- [dafrie/lstm-load-forecasting](https://github.com/dafrie/lstm-load-forecasting) - Swiss load data (.h5)
- [iamirmasoud/energy_consumption_prediction](https://github.com/iamirmasoud/energy_consumption_prediction) - PJM grid data (.pt)
- [DeepLearningEnergyForecasting](https://github.com/AhmetZamanis/DeepLearningEnergyForecasting) - PyTorch Lightning
- [RF-LSTM-CEEMDAN](https://github.com/irenekarijadi/RF-LSTM-CEEMDAN) - Hybrid approach

**Temperature Forecasting:**
- [laserprec/temperature-rnn](https://github.com/laserprec/temperature-rnn) - LSTM temperature prediction
- [RobotGyal/Weather-Prediction](https://github.com/RobotGyal/Weather-Prediction) - Weather LSTM
- [sunjoshi1991/Time-Series-Forecasting-using-LSTM](https://github.com/sunjoshi1991/Time-Series-Forecasting-using-LSTM) - Univariate/multivariate

**Thermal Comfort Prediction:**
- [anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings](https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings) - CNN-LSTM transfer learning
- [buds-lab/build2vec-thermal-comfort](https://github.com/buds-lab/build2vec-thermal-comfort) - Graph Neural Network
- [buds-lab/ccm](https://github.com/buds-lab/ccm) - Cohort comfort models
- [Building-Robotics-Lab/ComfortGPT](https://github.com/Building-Robotics-Lab/ComfortGPT) - Transformer-based prediction

**Occupancy Detection:**
- [YOLOv4-TFLite for person detection](https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection) - Edge device compatible
- [YoushaaMurhij/OFMPNet](https://github.com/YoushaaMurhij/OFMPNet) - Urban occupancy prediction
- [EdjeElectronics/TensorFlow-Lite-Object-Detection](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi) - Google pre-trained models

---

### By Framework

**TensorFlow/Keras (.h5, .tflite, .pb):**
- LSTM Load Forecasting (dafrie)
- Temperature RNN (laserprec)
- Weather Prediction LSTM (RobotGyal)
- CNN-LSTM Energy (muntasirhsn)
- TensorFlow Hub person detection
- EnergyBench dataset

**PyTorch (.pt, .pth):**
- Energy Consumption LSTM/GRU (iamirmasoud)
- Electricity Demand (ritikdhame)
- DeepLearningEnergyForecasting (AhmetZamanis)
- RF-LSTM-CEEMDAN (irenekarijadi)
- Thermal Comfort LSTM (anirudhs123)
- Build2Vec GNN (buds-lab)
- ComfortGPT Transformer (Building-Robotics-Lab)

**Stable-Baselines3 (.zip agent files):**
- Gnu-RL (RL agents)
- PEARL (RL agents)
- CLUE (RL agents)
- DRL-Building-Energy-Ctr (RL agents)
- RL-Baselines3-Zoo (general agents)

**ONNX:**
- ONNX Model Zoo (general models)
- Graph Neural Networks (power grids - Figshare)

---

### By Maturity Level

**Production-Ready (Tested, Documented):**
- PyThermalComfort (physics-based calculation)
- CBE Thermal Comfort Tool (web + code)
- Stable-Baselines3 (RL framework)
- TensorFlow Hub (official models)
- Sinergym (simulation environment)

**Research-Grade (Published, Code Available):**
- Gnu-RL (ICLR/frontiers publication)
- PEARL (AAAI 2023)
- CLUE (2024)
- OCTOPUS (2019)
- CityLearn v2 (2024)

**Proof-of-Concept (Academic Projects):**
- Many thermal comfort prediction repos
- Building energy control experiments
- Occupancy detection prototypes

---

### By File Size

**Small (<50 MB) - Easy to Clone:**
- Most GitHub repositories (code without data)
- PyThermalComfort
- CBE Comfort Tool
- Small LSTM models

**Medium (50-200 MB):**
- Gnu-RL with agents
- PEARL with code
- Some pre-trained LSTM models

**Large (200-500 MB) - Limit of task:**
- EnergyBench dataset
- Full Sinergym with examples
- Complex RL agents

**Very Large (>500 MB) - Download separately:**
- Three-Year Building Operations (2.38 GB)
- HuggingFace EnergyBench dataset (2-5 GB)
- Multi-agent training datasets

---

## Quick Start Commands

```bash
# Clone high-priority HVAC control repos
git clone https://github.com/INFERLab/Gnu-RL
git clone https://github.com/enjeeneer/PEARL
git clone https://github.com/ryeii/CLUE

# Clone energy prediction models
git clone https://github.com/iamirmasoud/energy_consumption_prediction
git clone https://github.com/dafrie/lstm-load-forecasting

# Clone thermal comfort tools
git clone https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings
git clone https://github.com/buds-lab/build2vec-thermal-comfort

# Install simulation environments
pip install sinergym
pip install citylearn

# Install building control frameworks
pip install stable-baselines3
pip install tensorflow
pip install torch

# Download datasets from Zenodo
# Visit: https://zenodo.org/records/5951008 (3-year building ops)
# Visit: https://huggingface.co/datasets/ai-iot/EnergyBench (energy bench)
```

---

## Model Comparison Matrix

| Use Case | Best Option | Framework | Type | Edge Ready |
|----------|------------|-----------|------|-----------|
| HVAC Control | Gnu-RL | PyTorch | RL Agent | No |
| Energy Forecasting | dafrie/lstm | TensorFlow | LSTM | Yes (.tflite) |
| Temperature Forecast | laserprec/rnn | TensorFlow | LSTM | Yes (.tflite) |
| Thermal Comfort | anirudhs123 | PyTorch | CNN-LSTM | Partial |
| Occupancy Detection | YOLOv4-TFLite | TensorFlow | CNN | Yes |
| Multi-Agent Control | CityLearn | Python Env | Multi-agent | No |

---

## Data Requirements

- **Energy prediction models:** 1+ years of building data (hourly)
- **Temperature models:** 6+ months historical temperature
- **Comfort models:** 100+ comfort survey responses OR synthetic data
- **Occupancy models:** Occupancy sensor data (PIR, CO2, etc.)
- **HVAC agents:** Simulation environment (EnergyPlus/Sinergym) or real building

---

## Recommended Learning Path

1. **Start with understanding:** PyThermalComfort (physics) + CBE Comfort Tool
2. **Energy prediction:** dafrie LSTM (simple, works well) or iamirmasoud (PyTorch)
3. **Simulation setup:** Install Sinergym or CityLearn
4. **RL control:** Study Gnu-RL or PEARL papers + code
5. **Production:** Convert to TFLite for edge deployment

---

## Troubleshooting & Notes

**Issue: Large repository size**
- Solution: Clone only the models folder or use sparse checkout
- Alternative: Download via HTTPS instead of SSH

**Issue: Dependency conflicts**
- Solution: Create separate Python venv for each major framework
- Tip: Many models from 2019-2022 may need older TensorFlow/PyTorch versions

**Issue: Model doesn't converge**
- Reason: Training data distribution different from your building
- Solution: Use transfer learning, fine-tune on your building data
- Tip: Start with simple LSTM, progress to complex RL agents

**Issue: Performance degrades in deployment**
- Reason: Seasonal variation, occupancy patterns differ
- Solution: Retrain quarterly or implement adaptive learning
- Tip: Edge models (.tflite) need quantization-aware training

---

## Contributing

To extend this list:
1. Add new model to README.md table
2. Include all metadata (source, task, framework, size, license)
3. Add link to GitHub repo or paper
4. Note if pre-trained weights are available
5. Include usage example if possible

---

**Last Updated:** February 2025
**Total Models Documented:** 45+
**Total Repositories Surveyed:** 50+
**Geographic Coverage:** Switzerland, US, Singapore, Global
