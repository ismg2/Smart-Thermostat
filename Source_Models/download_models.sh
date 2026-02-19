#!/usr/bin/env bash
# ╔══════════════════════════════════════════════════════════╗
# ║  download_models.sh — Smart Thermostat Edge AI           ║
# ║  Clone 20 modèles pré-entraînés dans les bons dossiers   ║
# ║                                                          ║
# ║  Usage :                                                 ║
# ║    bash download_models.sh            ← mode interactif  ║
# ║    bash download_models.sh --dry-run  ← aperçu seul      ║
# ║    bash download_models.sh --all      ← tout cloner      ║
# ╚══════════════════════════════════════════════════════════╝

set -euo pipefail

# ── Couleurs ──────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

# ── Chemins ───────────────────────────────────────────────────
# Le script s'exécute depuis son propre dossier (Source_Models/)
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PT_DIR="$BASE_DIR/PyTorch"
TF_DIR="$BASE_DIR/TensorFlow_Keras"
ONNX_DIR="$BASE_DIR/ONNX"

# ── Options ───────────────────────────────────────────────────
DRY_RUN=false
AUTO_YES=false

for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --all)     AUTO_YES=true ;;
    esac
done

# ── Compteurs ─────────────────────────────────────────────────
TOTAL=0
CLONED=0
SKIPPED=0
FAILED=0

# ══════════════════════════════════════════════════════════════
# Fonctions
# ══════════════════════════════════════════════════════════════

create_dirs() {
    if [[ "$DRY_RUN" == false ]]; then
        mkdir -p "$PT_DIR" "$TF_DIR" "$ONNX_DIR"
    fi
}

# clone_one <nom> <description> <dossier_dest> <url> [extra_flags] [badge]
clone_one() {
    local name="$1"
    local desc="$2"
    local dest="$3"
    local url="$4"
    local extra="${5:-}"
    local badge="${6:-}"

    TOTAL=$((TOTAL + 1))

    # Nom du repo (dernier segment de l'URL, sans .git)
    local repo_name
    repo_name="$(basename "$url" .git)"

    echo ""
    echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
    echo -e "${CYAN}[${TOTAL}/20] ${BOLD}${name}${RESET}  ${badge}"
    echo -e "       📝 ${desc}"
    echo -e "       📁 $(basename "$dest")/${repo_name}/"
    if [[ -n "$extra" ]]; then
        echo -e "       ▶  ${GREEN}git clone ${extra} ${url}${RESET}"
    else
        echo -e "       ▶  ${GREEN}git clone ${url}${RESET}"
    fi

    # Déjà cloné ?
    if [[ -d "$dest/$repo_name" ]]; then
        echo -e "       ${YELLOW}⚠️  Dossier déjà présent → ignoré${RESET}"
        SKIPPED=$((SKIPPED + 1))
        return
    fi

    # Mode dry-run : aucune action
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "       ${BLUE}[DRY-RUN] Pas d'action réelle.${RESET}"
        return
    fi

    # Demander confirmation (sauf --all)
    local answer="y"
    if [[ "$AUTO_YES" == false ]]; then
        echo ""
        printf "       → Cloner maintenant ? [y=oui / n=ignorer / q=quitter] : "
        read -r answer
    fi

    case "${answer,,}" in
        y|yes|o|oui)
            echo -e "       ${BLUE}⏳ Clonage en cours…${RESET}"
            if git clone $extra "$url" "$dest/$repo_name" 2>&1 | sed 's/^/          /'; then
                echo -e "       ${GREEN}✅ Succès → ${dest/$BASE_DIR\//}/${repo_name}${RESET}"
                CLONED=$((CLONED + 1))
            else
                echo -e "       ${RED}❌ Échec (repo privé, auth requise, ou réseau ?)${RESET}"
                FAILED=$((FAILED + 1))
            fi
            ;;
        q|quit|quitter|exit)
            echo -e "\n${YELLOW}⛔ Arrêt demandé.${RESET}"
            print_summary
            exit 0
            ;;
        *)
            echo -e "       ${YELLOW}⏭  Ignoré.${RESET}"
            SKIPPED=$((SKIPPED + 1))
            ;;
    esac
}

print_summary() {
    echo ""
    echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
    echo -e "${BOLD}📊 Bilan${RESET}"
    echo -e "   Total traité  : ${TOTAL}/20"
    echo -e "   ${GREEN}✅ Clonés      : ${CLONED}${RESET}"
    echo -e "   ${YELLOW}⏭  Ignorés     : ${SKIPPED}${RESET}"
    echo -e "   ${RED}❌ Échecs      : ${FAILED}${RESET}"
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "\n   ${BLUE}Mode DRY-RUN — aucune action n'a été effectuée.${RESET}"
    fi
    echo ""
    if [[ "$CLONED" -gt 0 ]]; then
        echo -e "   ${GREEN}Modèles disponibles dans :${RESET}"
        echo -e "   ${YELLOW}${BASE_DIR}/PyTorch/${RESET}"
        echo -e "   ${YELLOW}${BASE_DIR}/TensorFlow_Keras/${RESET}"
        echo -e "   ${YELLOW}${BASE_DIR}/ONNX/${RESET}"
    fi
    echo ""
}

# ══════════════════════════════════════════════════════════════
# DÉBUT
# ══════════════════════════════════════════════════════════════

echo -e "${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║   Smart Thermostat Edge AI — Téléchargement modèles     ║"
echo "║   20 repos GitHub → organisés par framework             ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${RESET}"
echo -e "   Dossier cible : ${YELLOW}${BASE_DIR}${RESET}"
echo ""

if [[ "$DRY_RUN" == true ]]; then
    echo -e "   ${BLUE}Mode DRY-RUN — aperçu uniquement, aucun téléchargement.${RESET}"
elif [[ "$AUTO_YES" == true ]]; then
    echo -e "   ${YELLOW}Mode --all — tous les repos seront clonés automatiquement.${RESET}"
else
    echo -e "   Mode interactif : répondre [y] oui  [n] ignorer  [q] quitter"
fi

create_dirs

# ══════════════════════════════════════════════════════════════
# 🟠 PyTorch / Stable-Baselines3  →  Source_Models/PyTorch/
# ══════════════════════════════════════════════════════════════

echo ""
echo -e "${BOLD}${YELLOW}════════════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}🟠  PyTorch / Stable-Baselines3${RESET}"
echo -e "${BOLD}${YELLOW}════════════════════════════════════════════════════════${RESET}"

clone_one \
    "Gnu-RL" \
    "Agent RL pré-entraîné pour HVAC — MPC différentiable (2019)" \
    "$PT_DIR" \
    "https://github.com/INFERLab/Gnu-RL.git" \
    "" \
    "⭐ Directement utilisable"

clone_one \
    "PEARL" \
    "Contrôle bâtiment zéro-shot pour réduction des émissions CO2 (2023)" \
    "$PT_DIR" \
    "https://github.com/enjeeneer/PEARL.git" \
    "" \
    "✅ Pré-entraîné"

clone_one \
    "CLUE" \
    "Safe RL pour HVAC avec estimation d'incertitude épistémique" \
    "$PT_DIR" \
    "https://github.com/ryeii/CLUE.git" \
    "" \
    "✅ Pré-entraîné"

clone_one \
    "DRL-Building-Energy-Ctr" \
    "Agent DRL pour pompe à chaleur + stockage thermique (HEMS)" \
    "$PT_DIR" \
    "https://github.com/ULudo/DRL-Building-Energy-Ctr.git" \
    "" \
    "⚠️ À vérifier"

clone_one \
    "ComfortGPT" \
    "Transformer pour prédiction de la T° de confort préférée par l'occupant" \
    "$PT_DIR" \
    "https://github.com/Building-Robotics-Lab/ComfortGPT.git" \
    "" \
    "⭐ Pré-entraîné"

clone_one \
    "energy_consumption_prediction" \
    "LSTM/GRU sur données horaires PJM — fichiers .pt dans /models" \
    "$PT_DIR" \
    "https://github.com/iamirmasoud/energy_consumption_prediction.git" \
    "" \
    "✅ Fichiers .pt"

clone_one \
    "DeepLearningEnergyForecasting" \
    "LSTM + Transformer prévision horaire d'énergie (PyTorch Lightning)" \
    "$PT_DIR" \
    "https://github.com/AhmetZamanis/DeepLearningEnergyForecasting.git" \
    "" \
    "✅ Checkpoints"

clone_one \
    "Thermal-comfort-prediction-in-low-resourced-buildings" \
    "CNN-LSTM confort thermique avec transfer learning (peu de données)" \
    "$PT_DIR" \
    "https://github.com/anirudhs123/Thermal-comfort-prediction-in-low-resourced-buildings.git" \
    "" \
    "✅ Pré-entraîné"

clone_one \
    "RF-LSTM-CEEMDAN" \
    "Hybride Random Forest + LSTM avec décomposition CEEMDAN" \
    "$PT_DIR" \
    "https://github.com/irenekarijadi/RF-LSTM-CEEMDAN.git" \
    "" \
    "⚠️ Code + données"

clone_one \
    "ccm" \
    "Cohort Comfort Models — préférences thermiques personnalisées par similarité" \
    "$PT_DIR" \
    "https://github.com/buds-lab/ccm.git" \
    "" \
    "✅ Modèles inclus"

clone_one \
    "ComfortLearn" \
    "OpenAI Gym environment pour entraîner un agent RL sur le confort occupant" \
    "$PT_DIR" \
    "https://github.com/buds-lab/ComfortLearn.git" \
    "" \
    "🔧 Env. entraînement"

clone_one \
    "PDE-HVAC-control" \
    "Contrôle HVAC avec Stable-Baselines3 — checkpoints dans le repo" \
    "$PT_DIR" \
    "https://github.com/alwaysbyx/PDE-HVAC-control.git" \
    "" \
    "⚠️ Checkpoints"

# ══════════════════════════════════════════════════════════════
# 🔵 TensorFlow / Keras / TFLite  →  Source_Models/TensorFlow_Keras/
# ══════════════════════════════════════════════════════════════

echo ""
echo -e "${BOLD}${BLUE}════════════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}🔵  TensorFlow / Keras / TFLite${RESET}"
echo -e "${BOLD}${BLUE}════════════════════════════════════════════════════════${RESET}"

clone_one \
    "lstm-load-forecasting" \
    "LSTM charge électrique suisse — fichiers .h5 directement dans /models" \
    "$TF_DIR" \
    "https://github.com/dafrie/lstm-load-forecasting.git" \
    "" \
    "⭐ Fichiers .h5"

clone_one \
    "yolov4-tiny-tflite-for-person-detection" \
    "Détection de personnes (occupation) — yolov4-tiny-416.tflite inclus" \
    "$TF_DIR" \
    "https://github.com/DoranLyong/yolov4-tiny-tflite-for-person-detection.git" \
    "" \
    "⭐ Fichier .tflite"

clone_one \
    "TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi" \
    "Détection TFLite (COCO) pour edge devices — modèles via get_pi_requirements.sh" \
    "$TF_DIR" \
    "https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git" \
    "" \
    "✅ Modèles COCO"

clone_one \
    "CNN-LSTM-model-for-energy-usage-forecasting" \
    "CNN-LSTM multi-step prédiction consommation d'énergie (Keras)" \
    "$TF_DIR" \
    "https://github.com/muntasirhsn/CNN-LSTM-model-for-energy-usage-forecasting.git" \
    "" \
    "⚠️ Code + notebook"

clone_one \
    "Interpretable-machine-learning-for-HVAC-predictive-control" \
    "ML interprétable pour prédiction T° de pièce (données bâtiment réel)" \
    "$TF_DIR" \
    "https://github.com/JianqiaoMao/Interpretable-machine-learning-for-HVAC-predictive-control.git" \
    "" \
    "⚠️ Code + données"

clone_one \
    "comfortGAN" \
    "GAN pour générer et équilibrer des datasets de confort thermique" \
    "$TF_DIR" \
    "https://github.com/buds-lab/comfortGAN.git" \
    "" \
    "⚠️ Code + données"

# ══════════════════════════════════════════════════════════════
# 🟣 ONNX  →  Source_Models/ONNX/
# ══════════════════════════════════════════════════════════════

echo ""
echo -e "${BOLD}${RED}════════════════════════════════════════════════════════${RESET}"
echo -e "${BOLD}🟣  ONNX${RESET}"
echo -e "${BOLD}${RED}════════════════════════════════════════════════════════${RESET}"

clone_one \
    "models (ONNX Model Zoo)" \
    "Collection officielle ONNX — ResNet, LSTM… Clonage rapide avec --depth 1" \
    "$ONNX_DIR" \
    "https://github.com/onnx/models.git" \
    "--depth 1" \
    "✅ Fichiers .onnx"

clone_one \
    "build2vec-thermal-comfort" \
    "Graph Neural Network prédit le confort thermique à partir de données BIM" \
    "$ONNX_DIR" \
    "https://github.com/buds-lab/build2vec-thermal-comfort.git" \
    "" \
    "⚠️ Code + données"

# ══════════════════════════════════════════════════════════════
print_summary
