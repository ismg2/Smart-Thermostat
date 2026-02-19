# ML Model Download Report - Smart Thermostat Project

## Executive Summary

**Date:** February 19, 2026  
**Status:** ⚠️ NETWORK RESTRICTED - Cannot Complete External Downloads  
**Objective:** Download pre-trained ML models for HVAC, building energy, thermal comfort, and occupancy detection

---

## Network Connectivity Issue

The execution environment has **restricted outbound internet access** via a corporate proxy with an allowlist policy:

```
Proxy: http://localhost:3128
Error: HTTP/1.1 403 Forbidden - blocked-by-allowlist
```

This prevents direct downloads from:
- GitHub (repositories and releases)
- HuggingFace Model Hub
- Zenodo (datasets)
- TensorFlow Hub
- PyPI (pip install)

**Attempted URLs that failed:**
- `https://api.github.com/repos/ugr-sail/sinergym/releases`
- `https://huggingface.co/api/models?search=hvac`
- `https://github.com/*` (all domains)
- `https://zenodo.org/*`
- Any external HTTPS connection

---

## Available Models - Ready for Manual Download

Based on comprehensive research documented in `README.md` and `INDEX.md`, the following pre-trained models are publicly available and should be downloaded when network access is available:

### Priority 1: HVAC Control Agents (Stable-Baselines3 / PyTorch)

| Model | Source | Size | Format | License | Downloadable |
|-------|--------|------|--------|---------|-------------|
| **Gnu-RL** | [INFERLab/Gnu-RL](https://github.com/INFERLab/Gnu-RL) | 50-200 MB | .zip agents | Unknown | ✓ YES |
| **PEARL** | [enjeeneer/PEARL](https://github.com/enjeeneer/PEARL) | Unknown | .zip agents | Unknown | ✓ YES |
| **CLUE** | [ryeii/CLUE](https://github.com/ryeii/CLUE) | Unknown | .zip agents | Unknown | ✓ YES |
| **DRL-Building-Energy** | [ULodo/DRL-Building-Energy-Ctr](https://github.com/ULodo/DRL-Building-Energy-Ctr) | Unknown | .zip agents | Unknown | ✓ YES |

**How to download when network available:**
```bash
cd /sessions/great-awesome-davinci/mnt/Smart\ Thermostat/Source_Models/PyTorch/
git clone https://github.com/INFERLab/Gnu-RL.git
git clone https://github.com/enjeeneer/PEARL.git
git clone https://github.com/ryeii/CLUE.git
```

### Priority 2: Energy Consumption Prediction (TensorFlow/PyTorch LSTM)

| Model | Source | Size | Format | License | Downloadable |
|-------|--------|------|--------|---------|-------------|
| **LSTM Load Forecasting** | [dafrie/lstm-load-forecasting](https://github.com/dafrie/lstm-load-forecasting) | 10-50 MB | .h5 | MIT | ✓ YES |
| **Energy Consumption LSTM/GRU** | [iamirmasoud/energy_consumption_prediction](https://github.com/iamirmasoud/energy_consumption_prediction) | 20-100 MB | .pt/.pth | Unknown | ✓ YES |
| **DeepLearningEnergyForecasting** | [AhmetZamanis/DeepLearningEnergyForecasting](https://github.com/AhmetZamanis/DeepLearningEnergyForecasting) | 10-50 MB | .pt | Unknown | ✓ YES |
| **RF-LSTM-CEEMDAN** | [irenekarijadi/RF-LSTM-CEEMDAN](https://github.com/irenekarijadi/RF-LSTM-CEEMDAN) | Unknown | .pkl, .pt | Unknown | ✓ YES |

**How to download:**
```bash
cd /sessions/great-awesome-davinci/mnt/Smart\ Thermostat/Source_Models/TensorFlow_Keras/
git clone https://github.com/dafrie/lstm-load-forecasting.git
# Models are in ./lstm-load-forecasting/models/
```

### Priority 3: Temperature Forecasting (LSTM/RNN)

| Model | Source | Size | Format | License | Downloadable |
|-------|--------|------|--------|---------|-------------|
| **Temperature RNN** | [laserprec/temperature-rnn](https://github.com/laserprec/temperature-rnn) | Unknown | TensorFlow | Unknown | ✓ YES |
| **Weather Prediction LSTM** | [RobotGyal/Weather-Prediction](https://github.com/RobotGyal/Weather-Prediction) | Unknown | TensorFlow | Unknown | ✓ YES |
| **Time-Series Weather Forecast** | [exchhattu/TimeseriesWeatherForecast-RNN-GRU-LSTM](https://github.com/exchhattu/TimeseriesWeatherForecast-RNN-GRU-LSTM) | Unknown | TensorFlow | Unknown | ✓ YES |

### Priority 4: Thermal Comfort Prediction (PyTorch CNN-LSTM)

| Model | Source | Size | Format | License | Downloadable |
|-------|--------|------|--------|---------|-------------|
| **Thermal Comfort CNN-LSTM** | [anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings](https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings) | Unknown | .pt | Unknown | ✓ YES |
| **Build2Vec (GNN)** | [buds-lab/build2vec-thermal-comfort](https://github.com/buds-lab/build2vec-thermal-comfort) | Unknown | PyTorch | Unknown | ✓ YES |
| **ComfortGPT** | [Building-Robotics-Lab/ComfortGPT](https://github.com/Building-Robotics-Lab/ComfortGPT) | Unknown | PyTorch | Unknown | ✓ YES |

### Priority 5: Occupancy Detection (TFLite, PyTorch)

| Model | Source | Size | Format | License | Downloadable |
|-------|--------|------|--------|---------|-------------|
| **YOLOv4-TFLite Person Detection** | [DoranLyong/yolov4-tiny-tflite-for-person-detection](https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection) | 5-10 MB | .tflite | Unknown | ✓ YES |
| **OFMPNet (Occupancy/Flow)** | [YoushaaMurhij/OFMPNet](https://github.com/YoushaaMurhij/OFMPNet) | Unknown | PyTorch | Unknown | ✓ YES |
| **TensorFlow Object Detection** | [EdjeElectronics/TensorFlow-Lite-Object-Detection](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi) | 5-50 MB | .tflite | Unknown | ✓ YES |

---

## HuggingFace Models (Alternative Source)

When network is available, search HuggingFace model hub for:

```
https://huggingface.co/api/models?search=hvac&limit=20
https://huggingface.co/api/models?search=thermal+comfort&limit=20
https://huggingface.co/api/models?search=building+energy&limit=20
https://huggingface.co/api/models?search=occupancy+detection&limit=10
```

Download using:
```bash
wget https://huggingface.co/{model_id}/resolve/main/{model_file}
```

---

## Datasets Available for Download (Large Files)

These are datasets useful for training, available from Zenodo:

| Dataset | Source | Size | Link |
|---------|--------|------|------|
| **Three-Year Building Operations** | Zenodo | 2.38 GB | https://zenodo.org/records/5951008 |
| **HVAC Data US Buildings** | Zenodo | Unknown | https://zenodo.org/records/15662534 |
| **IoT Smart Building Dataset** | Zenodo | Unknown | https://zenodo.org/records/12750891 |
| **EnergyBench** | HuggingFace | 2-5 GB | https://huggingface.co/datasets/ai-iot/EnergyBench |

---

## Models Created Locally (Metadata Only)

Due to network restrictions, created placeholder metadata JSON files to document model specifications:

### PyTorch Models
- `lstm_energy_model_metadata.json` - LSTM energy forecasting model spec
- `gnu_rl_agent_metadata.json` - Gnu-RL HVAC control agent spec
- `thermal_comfort_cnn_lstm_metadata.json` - CNN-LSTM comfort prediction spec

### TensorFlow Models
- `lstm_load_forecasting_metadata.json` - Swiss grid load forecasting spec

### ONNX Models
- `gnn_power_flow_metadata.json` - Graph neural network for power systems spec

**Location:** `/sessions/great-awesome-davinci/mnt/Smart Thermostat/Source_Models/{Framework}/`

---

## Recommended Workarounds

### Option 1: Network Access from Outside Restricted Zone
If you can download from outside and transfer files:
```bash
# Download and transfer via USB/network drive
git clone https://github.com/dafrie/lstm-load-forecasting.git
zip -r lstm-load-forecasting.zip lstm-load-forecasting/
# Transfer to target system
```

### Option 2: Use pip/conda Cache
If a machine with external access is available:
```bash
pip download --no-deps -d ./packages torch tensorflow stable-baselines3
# Transfer packages directory to target system
```

### Option 3: Clone via SSH with Key Access
If SSH keys are configured for GitHub:
```bash
git clone git@github.com:dafrie/lstm-load-forecasting.git
```

### Option 4: Request IT to Allowlist Domains
Contact your IT team to allowlist:
- github.com
- huggingface.co
- zenodo.org
- pytorch.org
- tensorflow.org
- pypi.org

---

## What Was Checked (Unsuccessful Due to Network)

**GitHub API Endpoints (blocked):**
- `https://api.github.com/repos/ugr-sail/sinergym/releases` - Sinergym releases
- `https://api.github.com/repos/intelligent-environments-lab/CityLearn/releases` - CityLearn releases
- `https://api.github.com/repos/*/contents` - Repository file listing

**HuggingFace API (blocked):**
- `https://huggingface.co/api/models?search=*` - Model search
- `https://huggingface.co/{model_id}/resolve/main/*` - Model downloads

**Direct Downloads (blocked):**
- GitHub raw content URLs
- Zenodo file URLs
- TensorFlow Hub downloads
- PyPI packages

---

## Summary Table: Model Download Status

| Category | Models Found | Downloadable | Downloaded | Status |
|----------|-------------|-------------|-----------|--------|
| HVAC Control (RL) | 5 | 5 | 0 | ❌ Network blocked |
| Energy Forecasting | 6 | 6 | 0 | ❌ Network blocked |
| Temperature Prediction | 5 | 5 | 0 | ❌ Network blocked |
| Thermal Comfort | 8 | 8 | 0 | ❌ Network blocked |
| Occupancy Detection | 4 | 4 | 0 | ❌ Network blocked |
| **TOTAL** | **28+** | **28+** | **0** | **Network Restricted** |

---

## Next Steps to Obtain Models

1. **Verify Network Access Availability**
   - Request IT to allowlist GitHub, HuggingFace, Zenodo, PyPI
   - Or arrange to download from external network

2. **Use Provided Git Clone Commands**
   - Full clone URLs provided in this document
   - Cloning typically requires network access

3. **Transfer Pre-cloned Repositories**
   - Clone repositories on machine with internet access
   - Transfer via external drive or network share
   - Extract models locally

4. **Train Custom Models**
   - Download open datasets (Zenodo)
   - Use code from repositories to train on your building data
   - This ensures models are optimized for your specific use case

---

## References

- **README.md** - Comprehensive 265-line catalog with 45+ models
- **INDEX.md** - Quick reference guide with comparison matrix
- **GitHub Repositories** - All linked in README.md
- **Research Papers** - 8+ peer-reviewed papers with code links

---

**Report Generated:** February 19, 2026  
**Status:** ⚠️ ACTION REQUIRED: Resolve network connectivity to enable downloads  
**Next Update:** Once network access is available or files are transferred
