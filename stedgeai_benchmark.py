#!/usr/bin/env python3
"""
┌──────────────────────────────────────────────────────────────┐
│  stedgeai_benchmark.py — Smart Thermostat Edge AI            │
│  Benchmark interactif via ST Edge AI Developer Cloud         │
├──────────────────────────────────────────────────────────────┤
│  Usage :                                                     │
│    python stedgeai_benchmark.py                              │
│    python stedgeai_benchmark.py --model mon_modele.tflite    │
│    python stedgeai_benchmark.py --model m.tflite --board ... │
│    python stedgeai_benchmark.py --no-benchmark               │
├──────────────────────────────────────────────────────────────┤
│  Dépendances SDK (à faire une fois) :                        │
│    git clone https://github.com/STMicroelectronics/          │
│              stm32ai-modelzoo-services.git                   │
│    pip install -r stm32ai-modelzoo-services/requirements.txt │
├──────────────────────────────────────────────────────────────┤
│  Variables d'env (optionnelles) :                            │
│    STEDGEAI_USERNAME   → email myST                          │
│    STEDGEAI_PASSWORD   → mot de passe myST                   │
└──────────────────────────────────────────────────────────────┘
"""

import sys
import os
import argparse
import getpass
import json
import importlib
import traceback
from pathlib import Path
from datetime import datetime


# ══════════════════════════════════════════════════════════════
# 🔑 IDENTIFIANTS — À remplir une bonne fois pour toutes
# ══════════════════════════════════════════════════════════════
#
#  Remplis juste les deux lignes ci-dessous et tu n'auras plus
#  jamais à les retaper. Le script les lit en priorité.
#
#  ⚠️  Ne committe pas ce fichier avec tes vrais identifiants !
#      (ajoute stedgeai_benchmark.py à ton .gitignore si besoin)
#
STEDGEAI_USERNAME = "ismail.guedira@gmail.com"   # ← ton email myST  (ex: "prenom.nom@gmail.com")
STEDGEAI_PASSWORD = "LAxdWDhk22#sB!q8"   # ← ton mot de passe myST
#
#  Alternative : variables d'environnement dans ton shell
#  (plus propre si tu partages le repo)
#
#    export STEDGEAI_USERNAME="ton@email.com"
#    export STEDGEAI_PASSWORD="ton_mot_de_passe"
#
#  Ou dans un fichier ~/.zshrc / ~/.bash_profile pour que ce
#  soit permanent :
#    echo 'export STEDGEAI_USERNAME="ton@email.com"' >> ~/.zshrc
#    echo 'export STEDGEAI_PASSWORD="ton_mdp"'       >> ~/.zshrc
#
# ══════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════
# Couleurs terminal (compatible macOS/Linux)
# ══════════════════════════════════════════════════════════════

class C:
    BOLD   = "\033[1m"
    CYAN   = "\033[0;36m"
    GREEN  = "\033[0;32m"
    YELLOW = "\033[1;33m"
    RED    = "\033[0;31m"
    BLUE   = "\033[0;34m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"


def banner(text):
    w = 62
    print(f"\n{C.BOLD}{C.CYAN}╔{'═'*w}╗{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}║  {text:<{w-2}}║{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}╚{'═'*w}╝{C.RESET}")


def section(n, text):
    print(f"\n{C.BOLD}{C.YELLOW}── [{n}] {text} {'─'*(50-len(text))}{C.RESET}")


def ok(text):     print(f"  {C.GREEN}✅ {text}{C.RESET}")
def warn(text):   print(f"  {C.YELLOW}⚠️  {text}{C.RESET}")
def err(text):    print(f"  {C.RED}❌ {text}{C.RESET}")
def info(text):   print(f"  {C.BLUE}ℹ  {text}{C.RESET}")
def dim(text):    print(f"  {C.DIM}{text}{C.RESET}")


def table_row(label, value, width=32):
    print(f"  {C.BOLD}{label:<{width}}{C.RESET}{value}")


# ══════════════════════════════════════════════════════════════
# Recherche du SDK stm32ai_dc
# ══════════════════════════════════════════════════════════════

SDK_CANDIDATES = [
    # Relatifs au dossier du script
    Path(__file__).parent / "stm32ai-modelzoo-services" / "common",
    Path(__file__).parent.parent / "stm32ai-modelzoo-services" / "common",
    # Dossier courant
    Path.cwd() / "stm32ai-modelzoo-services" / "common",
    Path.cwd() / "common",
    # Home
    Path.home() / "stm32ai-modelzoo-services" / "common",
    Path.home() / "Code" / "stm32ai-modelzoo-services" / "common",
    Path.home() / "code" / "stm32ai-modelzoo-services" / "common",
]

# Noms possibles du module (ST a renommé en cours de route)
SDK_MODULE_NAMES = ["stm32ai_dc", "stedgeai_dc", "stm32ai"]


def find_sdk():
    """Cherche le dossier 'common/' contenant le module SDK."""
    for candidate in SDK_CANDIDATES:
        for mod in SDK_MODULE_NAMES:
            if (candidate / mod).exists() or (candidate / f"{mod}.py").exists():
                return candidate, mod
    return None, None


def import_sdk(sdk_path, module_name):
    """Importe les classes principales du SDK ST Edge AI.

    IMPORTANT : Stm32Ai et CliParameters doivent venir du même chemin d'import.
    Si Stm32Ai vient de 'common.stm32ai_dc' mais CliParameters de 'stm32ai_dc',
    le SDK lève une erreur de type mismatch. On force donc 'common.stm32ai_dc'
    en priorité (chemin canonique).
    """
    parent = sdk_path.parent
    sys.path.insert(0, str(sdk_path))   # pour import stm32ai_dc direct
    sys.path.insert(0, str(parent))     # pour from common.X import Y en interne

    # Priorité : common.stm32ai_dc (chemin canonique que Stm32Ai utilise en interne)
    # → garantit que Stm32Ai et CliParameters partagent le même module
    import_attempts = [
        (f"common.{module_name}", ["Stm32Ai", "CloudBackend", "CliParameters"]),
        (f"common.{module_name}", ["Stm32Ai", "CloudBackend", "AnalyzeParameters"]),
        (module_name,             ["Stm32Ai", "CloudBackend", "CliParameters"]),
        (module_name,             ["Stm32Ai", "CloudBackend", "AnalyzeParameters"]),
        (module_name,             ["STM32AI", "Cloud", "Parameters"]),
    ]

    last_error = None
    for mod_name, class_names in import_attempts:
        try:
            mod = __import__(mod_name, fromlist=class_names)
            classes = {name: getattr(mod, name) for name in class_names if hasattr(mod, name)}
            if "Stm32Ai" in classes or "STM32AI" in classes:
                return classes, None
        except ImportError as e:
            last_error = e
            continue

    return None, last_error


# ══════════════════════════════════════════════════════════════
# Helpers pour lire les résultats (dataclass, dict, objet)
# ══════════════════════════════════════════════════════════════

def safe_get(obj, *keys, default="—"):
    """Lit un champ depuis un objet (dataclass, dict, ou attribut)."""
    if obj is None:
        return default
    for k in keys:
        try:
            if isinstance(obj, dict):
                v = obj.get(k)
            else:
                v = getattr(obj, k, None)
            if v is not None:
                return v
        except Exception:
            pass
    return default


def fmt_bytes(val, default="—"):
    """Formate des bytes en KB/MB lisible."""
    if val == "—" or val is None:
        return default
    try:
        v = int(val)
        if v >= 1024 * 1024:
            return f"{v:,} bytes ({v/1024/1024:.2f} MB)"
        elif v >= 1024:
            return f"{v:,} bytes ({v/1024:.1f} KB)"
        return f"{v:,} bytes"
    except (ValueError, TypeError):
        return str(val)


def fmt_macc(val):
    """Formate les MACCs en M/K."""
    if val == "—" or val is None:
        return "—"
    try:
        v = int(val)
        if v >= 1_000_000:
            return f"{v:,}  ({v/1e6:.2f} M MACs)"
        elif v >= 1_000:
            return f"{v:,}  ({v/1e3:.1f} K MACs)"
        return f"{v:,}"
    except (ValueError, TypeError):
        return str(val)


def fmt_status_md(tried: bool, ok) -> str:
    """Emoji de statut Markdown pour les tableaux de bilan."""
    if not tried:
        return "🟡 Non tenté"
    return "🟢 Succès" if ok else "🔴 Échec"


# ══════════════════════════════════════════════════════════════
# Historique global des benchmarks (master tracker)
# ══════════════════════════════════════════════════════════════

TRACKER_FILENAME = "benchmark_history.md"

TRACKER_HEADER = """\
# 📊 Historique des benchmarks — ST Edge AI Developer Cloud

*Mis à jour automatiquement par `stedgeai_benchmark.py`*

| Date | Modèle | Board | Format | Optim. | NPU | Upload | Analyze RAM | Analyze Flash | MACs | Bench. ms | FPS | Statut | Rapport |
|------|--------|-------|--------|--------|-----|--------|-------------|---------------|------|-----------|-----|--------|---------|
"""


def update_master_tracker(script_dir: Path, run_info: dict):
    """
    Ajoute une ligne dans benchmark_history.md (à la racine du projet).
    Crée le fichier avec son en-tête s'il n'existe pas encore.

    run_info attendu :
        date, model, board, fmt, optimization,
        npu_cell, upload_tried, upload_ok,
        a_ram, a_flash, a_macc,
        b_ms, b_fps,
        analyze_ok, bench_ok,
        report_path
    """
    tracker_path = script_dir / TRACKER_FILENAME

    upload_cell = fmt_status_md(
        run_info.get("upload_tried", False),
        run_info.get("upload_ok", False),
    )

    # Statut global
    if run_info.get("bench_ok"):
        global_status = "🟢 Complet"
    elif run_info.get("analyze_ok"):
        global_status = "🟡 Analyze seul"
    else:
        global_status = "🔴 Échec"

    # Lien relatif vers le rapport individuel
    report_path = run_info.get("report_path", "")
    try:
        rel = Path(report_path).relative_to(script_dir)
        report_link = f"[→]({rel})"
    except (ValueError, TypeError):
        report_link = f"[→]({Path(report_path).name})" if report_path else "—"

    row = (
        f"| {run_info.get('date','—')} "
        f"| `{run_info.get('model','—')}` "
        f"| `{run_info.get('board','—')}` "
        f"| `{run_info.get('fmt','—')}` "
        f"| {run_info.get('optimization','—')} "
        f"| {run_info.get('npu_cell','—')} "
        f"| {upload_cell} "
        f"| {run_info.get('a_ram','—')} "
        f"| {run_info.get('a_flash','—')} "
        f"| {run_info.get('a_macc','—')} "
        f"| {run_info.get('b_ms','—')} "
        f"| {run_info.get('b_fps','—')} "
        f"| {global_status} "
        f"| {report_link} |\n"
    )

    if not tracker_path.exists():
        tracker_path.write_text(TRACKER_HEADER + row, encoding="utf-8")
    else:
        tracker_path.write_text(
            tracker_path.read_text(encoding="utf-8") + row,
            encoding="utf-8"
        )

    return tracker_path


# ══════════════════════════════════════════════════════════════
# Détection et configuration NPU
# ══════════════════════════════════════════════════════════════

# Patterns de boards avec NPU et leur type
# Clé = sous-chaîne à chercher dans le nom de board (insensible à la casse)
NPU_BOARD_PATTERNS = {
    "N6":   "neural_art",      # STM32N6* — Neural-ART NPU (600 GOPS, 4 Compute Arrays)
    "MP2":  "hw_accelerator",  # STM32MP2* — MPU avec GPU/HW accelerator
    "MP13": "hw_accelerator",  # STM32MP13*
    "MP15": "hw_accelerator",  # STM32MP15*
    "MP25": "hw_accelerator",  # STM32MP25*
}

NPU_TYPE_LABELS = {
    "neural_art":     "🔮 Neural-ART NPU (STM32N6) — 600 GOPS, 4 Compute Arrays",
    "hw_accelerator": "⚡ HW Accelerator / GPU (STM32MP*)",
}

# Valeurs par défaut "classiques" recommandées pour Neural-ART
NEURAL_ART_CLASSIC_DEFAULTS = {
    "enable_epoch_controller":  True,   # améliore le débit NPU (recommandé)
    "cache_maintenance":        True,   # cohérence cache/NPU (recommandé)
    "enable_virtual_mem_pools": True,   # utilise la RAM externe efficacement
    "Oauto":                    True,   # laisse le compilateur Neural-ART optimiser
    "Omax_ca_pipe":             0,      # 0 = auto (1-4 = nb max de Compute Arrays)
    "disable_sw_fallback":      False,  # False = fallback CPU activé pour ops non supportées
    "no_hw_sw_parallelism":     False,  # False = parallélisme CPU/NPU autorisé
    "max_ram_size":             None,   # None = pas de limite de RAM NPU
}


def detect_npu(board_name: str):
    """Retourne le type NPU détecté pour une board, ou None si pas de NPU."""
    board_upper = board_name.upper()
    for pattern, npu_type in NPU_BOARD_PATTERNS.items():
        if pattern.upper() in board_upper:
            return npu_type
    return None


def _ask_bool(prompt: str, default: bool) -> bool:
    """Demande oui/non avec valeur par défaut."""
    default_str = "Y/n" if default else "y/N"
    ans = input(f"    {prompt} [{default_str}] : ").strip().lower()
    if ans == "":
        return default
    return ans in ("y", "yes", "o", "oui", "1", "true")


def _ask_int(prompt: str, default, allow_none=False):
    """Demande un entier avec valeur par défaut."""
    default_str = str(default) if default is not None else "auto"
    ans = input(f"    {prompt} [{default_str}] : ").strip()
    if ans == "":
        return default
    if allow_none and ans.lower() in ("none", "auto", "-", ""):
        return None
    try:
        return int(ans)
    except ValueError:
        warn(f"Valeur invalide '{ans}', utilisation de {default}")
        return default


def _neural_art_power_user_menu(aton: dict) -> dict:
    """Menu interactif détaillé pour les paramètres AtonParameters (Neural-ART NPU)."""
    print()
    print(f"  {C.BOLD}{C.YELLOW}━━━ Neural-ART Power User — Compilateur NPU STM32N6 ━━━{C.RESET}")
    print()
    print(f"  {C.DIM}Les options suivantes contrôlent le compilateur Neural-ART.")
    print(f"  Appuyez sur Entrée pour garder la valeur par défaut (entre crochets).{C.RESET}")
    print()

    aton = aton.copy()

    # Options booléennes avec leurs explications
    bool_options = [
        ("enable_epoch_controller",
         "Epoch Controller (pipeline NPU — améliore le débit, recommandé)",
         True),
        ("cache_maintenance",
         "Cache Maintenance (cohérence mémoire cache/NPU, recommandé)",
         True),
        ("enable_virtual_mem_pools",
         "Virtual Memory Pools (utilise la RAM externe pour les tenseurs)",
         True),
        ("Oauto",
         "Auto-optimisation (laisse Neural-ART choisir les meilleures options)",
         True),
        ("disable_sw_fallback",
         "Désactiver fallback CPU (les ops non-NPU lèveront une erreur)",
         False),
        ("no_hw_sw_parallelism",
         "Désactiver parallélisme CPU/NPU (debug uniquement)",
         False),
    ]

    print(f"  {C.BOLD}▸ Options booléennes :{C.RESET}")
    for key, label, default in bool_options:
        current = aton.get(key, default)
        aton[key] = _ask_bool(label, current)

    print()
    print(f"  {C.BOLD}▸ Options numériques :{C.RESET}")
    print(f"  {C.DIM}  Omax_ca_pipe : nombre max de Compute Arrays dans le pipeline")
    print(f"                 0 = automatique (recommandé), 1–4 = valeur fixe{C.RESET}")
    aton["Omax_ca_pipe"] = _ask_int("Omax_ca_pipe (0=auto, 1-4=fixe)", aton.get("Omax_ca_pipe", 0))

    print()
    print(f"  {C.DIM}  max_ram_size : limite max de RAM allouée au NPU (en bytes)")
    print(f"                 0 ou vide = aucune limite{C.RESET}")
    aton["max_ram_size"] = _ask_int("max_ram_size en bytes (vide=illimité)", aton.get("max_ram_size"), allow_none=True)

    print()
    ok("Configuration Neural-ART power user appliquée :")
    print()
    for k, v in aton.items():
        if v is not None:
            color = C.GREEN if v is True else (C.YELLOW if v is False else C.CYAN)
            print(f"    {C.DIM}{k:<35}{C.RESET} {color}{v}{C.RESET}")
    print()

    return aton


def _hw_accelerator_power_user_menu(npu_config: dict) -> dict:
    """Menu interactif pour les paramètres MpuParameters (HW Accelerator STM32MP*)."""
    print()
    print(f"  {C.BOLD}{C.YELLOW}━━━ HW Accelerator Power User — STM32MP* ━━━{C.RESET}")
    print()

    print(f"  {C.BOLD}▸ Moteur d'exécution :{C.RESET}")
    print(f"    1. HW_ACCELERATOR  (GPU/NPU matériel)  ← recommandé")
    print(f"    2. CPU             (fallback pure CPU)")
    ans = input(f"    Choix [1] : ").strip()
    npu_config["mpu_engine"] = "CPU" if ans == "2" else "HW_ACCELERATOR"

    print()
    nb = _ask_int("Nombre de cœurs CPU utilisés (1-8)", npu_config.get("mpu_nb_cores", 2))
    npu_config["mpu_nb_cores"] = max(1, min(8, nb if nb else 2))

    print()
    ok(f"Config : moteur={npu_config['mpu_engine']}, cœurs={npu_config['mpu_nb_cores']}")
    return npu_config


# Formats incompatibles avec le compilateur Neural-ART NPU
NPU_INCOMPATIBLE_FORMATS = {".h5", ".keras"}
# TFLite et ONNX sont les formats supportés par le NPU
NPU_REQUIRED_FORMATS = {".tflite", ".onnx"}


def configure_npu_interactive(board: str, model_path: Path = None) -> dict | None:
    """
    Détecte le NPU de la board et propose une configuration interactive.

    Retourne un dict de config NPU, ou None si NPU non activé.
    Structure du dict retourné :
    {
        "npu_type": "neural_art" | "hw_accelerator",
        "enabled": True,
        # Pour neural_art :
        "stNeuralArt": "default",
        "series": "stm32n6",
        "aton": { ... }  # kwargs pour AtonParameters
        # Pour hw_accelerator :
        "mpu_engine": "HW_ACCELERATOR",
        "mpu_nb_cores": 2,
    }
    """
    npu_type = detect_npu(board)
    if npu_type is None:
        info("Pas de NPU détecté pour cette board — exécution sur CPU standard.")
        return None

    print()
    print(f"  {C.BOLD}{C.CYAN}NPU détecté !{C.RESET}  {NPU_TYPE_LABELS.get(npu_type, npu_type)}")
    print()

    # ── Vérification de compatibilité format/NPU ──────────────
    if model_path is not None and npu_type == "neural_art":
        ext = model_path.suffix.lower()
        if ext in NPU_INCOMPATIBLE_FORMATS:
            warn(f"Format '{ext}' incompatible avec le Neural-ART NPU !")
            warn("Le compilateur Neural-ART n'accepte que .tflite ou .onnx.")
            print()
            print(f"  {C.DIM}Pour utiliser le NPU, convertissez d'abord le modèle :")
            print(f"  {C.CYAN}  # Keras → TFLite (Python)  :{C.RESET}")
            print(f"  {C.DIM}  import tensorflow as tf")
            print(f"  {C.DIM}  converter = tf.lite.TFLiteConverter.from_keras_model(model)")
            print(f"  {C.DIM}  tflite_model = converter.convert()")
            print(f"  {C.DIM}  open('model.tflite', 'wb').write(tflite_model)")
            print()
            info("→ L'analyze sera lancé sans NPU (CPU uniquement).")
            info("→ Le benchmark sera tenté sans NPU.")
            return None
        elif ext not in NPU_REQUIRED_FORMATS:
            warn(f"Format '{ext}' — compatibilité NPU incertaine (recommandé : .tflite ou .onnx).")

    if npu_type == "neural_art":
        info("Le Neural-ART NPU peut accélérer significativement l'inférence.")
        info("Config classique : epoch controller + virtual mem pools + cache maintenance.")
        info("STM32N6 Neural-ART : 600 GOPS — 4 Compute Arrays @ 800 MHz.")
    elif npu_type == "hw_accelerator":
        info("Le HW Accelerator (GPU) peut accélérer l'inférence sur STM32MP*.")
        info("Config classique : moteur HW_ACCELERATOR, 2 cœurs.")

    print()
    ans = input("  Activer le NPU ? [Y/n] : ").strip().lower()
    if ans in ("n", "no", "non"):
        info("NPU désactivé — exécution sur CPU uniquement.")
        return None

    # Construire la config de base (valeurs classiques)
    npu_config = {"npu_type": npu_type, "enabled": True}

    if npu_type == "neural_art":
        npu_config.update({
            "stNeuralArt": "default",
            "series":      "stm32n6",   # lowercase attendu par le SDK
            "aton":        NEURAL_ART_CLASSIC_DEFAULTS.copy(),
        })
        print()
        ok("Config Neural-ART classique sélectionnée :")
        print()
        for k, v in npu_config["aton"].items():
            if v is not None:
                color = C.GREEN if v is True else (C.YELLOW if v is False else C.CYAN)
                print(f"    {C.DIM}{k:<35}{C.RESET} {color}{v}{C.RESET}")
        print()

        ans_pu = input("  Ouvrir le menu power user NPU pour modifier ces valeurs ? [y/N] : ").strip().lower()
        if ans_pu in ("y", "yes", "o", "oui"):
            npu_config["aton"] = _neural_art_power_user_menu(npu_config["aton"])

    elif npu_type == "hw_accelerator":
        npu_config.update({
            "mpu_engine":   "HW_ACCELERATOR",
            "mpu_nb_cores": 2,
        })
        ok("Config HW Accelerator classique : moteur=HW_ACCELERATOR, 2 cœurs.")

        print()
        ans_pu = input("  Ouvrir le menu power user NPU ? [y/N] : ").strip().lower()
        if ans_pu in ("y", "yes", "o", "oui"):
            npu_config = _hw_accelerator_power_user_menu(npu_config)

    return npu_config


def _try_load_aton_cls(sdk_module_name: str):
    """Tente de charger la classe AtonParameters depuis le SDK."""
    for mod_name in [
        f"common.{sdk_module_name}",
        sdk_module_name,
        "common.stm32ai_dc",
        "common.stedgeai_dc",
        "stm32ai_dc",
        "stedgeai_dc",
    ]:
        try:
            mod = importlib.import_module(mod_name)
            if hasattr(mod, "AtonParameters"):
                return mod.AtonParameters
        except ImportError:
            continue
    return None


def _make_params(model_name: str, board: str, optimization: str,
                  extra_kwargs: dict, Params_cls) -> object:
    """Construit un objet CliParameters avec fallback de compatibilité."""
    base = {"model": model_name, "target": board, "optimization": optimization}
    base.update(extra_kwargs)
    try:
        return Params_cls(**base)
    except TypeError:
        # Certaines versions utilisent 'board' au lieu de 'target'
        try:
            fb = {k: v for k, v in base.items() if k != "target"}
            fb["board"] = board
            return Params_cls(**fb)
        except TypeError:
            return Params_cls(model=model_name)


def build_analyze_params(model_name: str, board: str, optimization: str, Params_cls):
    """
    Paramètres SANS config NPU pour l'étape d'analyze.

    L'endpoint /analyze du cloud n'accepte pas les champs NPU (stNeuralArt,
    series, atonnOptions). On passe uniquement les params de base.
    Le fichier doit avoir été uploadé au préalable (model = basename uniquement).
    """
    return _make_params(model_name, board, optimization, {}, Params_cls)


def build_benchmark_params(model_name: str, board: str, optimization: str,
                            npu_config, Params_cls, sdk_module_name="stm32ai_dc"):
    """
    Paramètres AVEC config NPU pour l'étape de benchmark.

    L'endpoint /benchmark accepte stNeuralArt, series et atonnOptions.
    Le fichier doit avoir été uploadé (model = basename uniquement).
    """
    extra = {}

    if npu_config and npu_config.get("enabled"):
        npu_type = npu_config.get("npu_type")

        if npu_type == "neural_art":
            extra["stNeuralArt"] = npu_config.get("stNeuralArt", "default")
            extra["series"]      = npu_config.get("series", "stm32n6")

            # AtonParameters — optionnel selon la version du SDK
            aton_kwargs = npu_config.get("aton", {})
            if aton_kwargs:
                AtonCls = _try_load_aton_cls(sdk_module_name)
                if AtonCls:
                    filtered = {k: v for k, v in aton_kwargs.items() if v is not None}
                    try:
                        extra["atonnOptions"] = AtonCls(**filtered)
                        info(f"AtonParameters appliqué ({len(filtered)} options NPU)")
                    except Exception as e:
                        warn(f"AtonParameters incompatible avec cette version SDK : {e}")
                        warn("→ stNeuralArt='default' sera quand même transmis.")
                else:
                    warn("AtonParameters introuvable dans le SDK — options avancées ignorées.")

        elif npu_type == "hw_accelerator":
            info("Boards STM32MP* : l'accélérateur HW est sélectionné côté cloud.")

    return _make_params(model_name, board, optimization, extra, Params_cls)


# ══════════════════════════════════════════════════════════════
# Génération du rapport Markdown
# ══════════════════════════════════════════════════════════════

def build_markdown(model_path, board, optimization, analyze_result, bench_result=None, logs="", npu_config=None, run_status=None):
    now        = datetime.now().strftime("%Y-%m-%d %H:%M")
    model_name = Path(model_path).name
    p          = Path(model_path)
    model_size_kb = p.stat().st_size / 1024 if p.exists() else 0.0

    # Champs analyze
    a_ram    = safe_get(analyze_result, "ram_size",   "estimated_ram_size",   "ram")
    a_flash  = safe_get(analyze_result, "flash_size", "estimated_flash_size", "flash")
    a_macc   = safe_get(analyze_result, "macc",       "total_macc",           "macs")
    a_params = safe_get(analyze_result, "weights",    "params_count",         "parameters")
    a_layers = safe_get(analyze_result, "num_layers", "layers_count")

    # Champs benchmark
    b_ram      = safe_get(bench_result, "ram_size",      "ram")
    b_flash    = safe_get(bench_result, "flash_size",    "flash")
    b_infer_ms = safe_get(bench_result, "inference_time","latency_ms", "duration_ms")
    b_cpu_mhz  = safe_get(bench_result, "cpu_freq_mhz",  "cpu_frequency", "clock_mhz")
    b_cycles   = safe_get(bench_result, "cycles",        "clock_cycles")

    b_fps = "—"
    try:
        if b_infer_ms not in ("—", None) and float(b_infer_ms) > 0:
            b_fps = f"{1000 / float(b_infer_ms):.1f}"
    except (ValueError, TypeError):
        pass

    # Section NPU dans les tags YAML
    npu_tag = ""
    if npu_config and npu_config.get("enabled"):
        npu_tag = f'\nnpu: "{npu_config.get("npu_type", "unknown")}"'

    # Table de référence hardware
    hw_table = """| Carte | RAM | Flash | Famille |
|-------|-----|-------|---------|
| NUCLEO-H7A3ZI-Q | 1 400 KB | 2 MB | STM32H7 |
| B-L475E-IOT01A | 128 KB | 1 MB | STM32L4 |
| NUCLEO-L4R5ZI | 640 KB | 2 MB | STM32L4+ |
| NUCLEO-F401RE | 96 KB | 512 KB | STM32F4 |
| STM32N6570-DK | 4 200 KB | ext. Flash | STM32N6 (NPU) |
| NUCLEO-U5A5ZJ-Q | 2 500 KB | 4 MB | STM32U5 |"""

    # ── Bandeau de statut ──────────────────────────────────────
    rs = run_status or {}

    def _s(key):
        """Retourne l'emoji de statut pour une étape donnée."""
        step = rs.get(key, {})
        return fmt_status_md(step.get("tried", False), step.get("ok", False))

    def _d(key):
        """Retourne le détail textuel d'une étape."""
        return rs.get(key, {}).get("detail", "—")

    # Statut global du run
    if rs.get("benchmark", {}).get("ok"):
        run_global = "🟢 Complet — analyze + benchmark réussis"
    elif rs.get("analyze", {}).get("ok"):
        run_global = "🟡 Partiel — analyze réussi, benchmark non effectué ou en échec"
    else:
        run_global = "🔴 Échec — analyze non concluant"

    # Résumé RAM/Flash compact pour le bandeau
    a_ram_short  = fmt_bytes(a_ram)  if a_ram  not in ("—", None) else "—"
    a_flash_short= fmt_bytes(a_flash)if a_flash not in ("—", None) else "—"
    b_ms_val     = safe_get(bench_result, "duration_ms") if bench_result else "—"

    status_section = f"""\
## 📋 Statut du run

> {run_global}

| Étape | Statut | Résumé |
|-------|--------|--------|
| ☁️ Upload | {_s("upload")} | {_d("upload")} |
| 🧠 Analyze | {_s("analyze")} | {_d("analyze")} — [voir résultats](#-analyse-statique-analyze) |
| ⚡ Benchmark | {_s("benchmark")} | {_d("benchmark")} — [voir résultats](#-benchmark-sur-matériel-réel) |
| 🔮 NPU | {_s("npu")} | {_d("npu")} |

"""
    # ── /Bandeau de statut ─────────────────────────────────────

    md = f"""---
title: "Benchmark ST Edge AI — {model_name}"
date: "{now}"
model: "{model_name}"
board: "{board}"
optimization: "{optimization}"{npu_tag}
tags: [stedgeai, benchmark, edge-ai, stm32]
---

# 📊 Rapport ST Edge AI Developer Cloud

> **Modèle :** `{model_name}`  ({model_size_kb:.1f} KB sur disque)
> **Board :** `{board}`
> **Optimisation :** `{optimization}`
> **Date :** {now}

---

{status_section}---

## 🧠 Analyse statique (Analyze)

*Estimation des ressources nécessaires sans exécution réelle.*

| Métrique | Valeur brute | Lisible |
|----------|-------------|---------|
| RAM estimée | `{a_ram}` | {fmt_bytes(a_ram)} |
| Flash estimée | `{a_flash}` | {fmt_bytes(a_flash)} |
| MACCs totales | `{a_macc}` | {fmt_macc(a_macc)} |
| Paramètres (poids) | `{a_params}` | — |
| Nombre de couches | `{a_layers}` | — |

"""

    if bench_result is not None:
        md += f"""---

## ⚡ Benchmark sur matériel réel

*Mesures effectuées sur la board `{board}` hébergée dans la board farm ST.*

| Métrique | Valeur brute | Lisible |
|----------|-------------|---------|
| RAM réelle | `{b_ram}` | {fmt_bytes(b_ram)} |
| Flash réelle | `{b_flash}` | {fmt_bytes(b_flash)} |
| Temps d'inférence | `{b_infer_ms}` ms | — |
| Fréquence CPU | `{b_cpu_mhz}` MHz | — |
| Cycles | `{b_cycles}` | — |
| **Débit estimé** | **{b_fps} inf/sec** | — |

"""
    else:
        md += """---

## ⚡ Benchmark sur matériel réel

*Non exécuté (lancé avec `--no-benchmark` ou refusé interactivement).*

"""

    # Section NPU
    if npu_config and npu_config.get("enabled"):
        npu_type = npu_config.get("npu_type")
        npu_label = NPU_TYPE_LABELS.get(npu_type, npu_type)

        md += f"""---

## 🔮 Configuration NPU

**Type :** {npu_label}

"""
        if npu_type == "neural_art":
            st_na  = npu_config.get("stNeuralArt", "default")
            series = npu_config.get("series", "STM32N6")
            md += f"**stNeuralArt :** `{st_na}`  \n**series :** `{series}`\n\n"
            aton = npu_config.get("aton", {})
            if aton:
                md += "**AtonParameters (Neural-ART compiler) :**\n\n"
                md += "| Paramètre | Valeur |\n|-----------|--------|\n"
                for k, v in aton.items():
                    if v is not None:
                        icon = "✅" if v is True else ("⬜" if v is False else "🔢")
                        md += f"| `{k}` | {icon} `{v}` |\n"
                md += "\n"
        elif npu_type == "hw_accelerator":
            engine   = npu_config.get("mpu_engine", "HW_ACCELERATOR")
            nb_cores = npu_config.get("mpu_nb_cores", 2)
            md += f"**Moteur :** `{engine}`  \n**Cœurs :** `{nb_cores}`\n\n"
    else:
        md += """---

## 🔮 Configuration NPU

*NPU non utilisé pour ce benchmark — exécution sur CPU standard.*

"""

    md += f"""---

## 📌 Interprétation rapide

### Compatibilité mémoire estimée

| Cible | RAM dispo | Flash dispo | Compatible ? |
|-------|-----------|-------------|-------------|
| STM32H7 (NUCLEO-H7A3ZI-Q) | 1 400 KB | 2 048 KB | {"✅" if a_ram not in ("—", None) and isinstance(a_ram, (int,str)) else "?"} |
| STM32L4 (B-L475E-IOT01A)  | 128 KB   | 1 024 KB | — |
| STM32F4 (NUCLEO-F401RE)   | 96 KB    | 512 KB   | — |
| STM32U5 (NUCLEO-U5A5ZJ-Q) | 2 560 KB | 4 096 KB | — |
| STM32N6 (NPU)             | 4 200 KB | ext.     | — |

> ⚠️ Mettre à jour manuellement la colonne "Compatible ?" avec les valeurs RAM/Flash ci-dessus.

### Boards de référence ST

{hw_table}

"""

    if logs:
        md += f"""---

## 📋 Logs / Erreurs

```
{logs}
```

"""

    md += f"""---

## 🔗 Ressources

- [ST Edge AI Developer Cloud](https://stedgeai-dc.st.com)
- [stm32ai-modelzoo-services](https://github.com/STMicroelectronics/stm32ai-modelzoo-services)
- [Getting Started Wiki](https://wiki.st.com/stm32mcu/wiki/AI:Getting_started_with_ST_Edge_AI_Developer_Cloud)
- [Neural-ART NPU — STM32N6](https://wiki.st.com/stm32mcu/wiki/AI:Neural-ART_NPU)

---

*Généré automatiquement par `stedgeai_benchmark.py` le {now}*
"""
    return md


# ══════════════════════════════════════════════════════════════
# Scan des modèles disponibles
# ══════════════════════════════════════════════════════════════

SUPPORTED_EXT = {".tflite", ".h5", ".keras", ".onnx", ".pb", ".pt", ".pth"}


MIN_MODEL_SIZE_KB = 5   # Les stubs git-lfs font ~0.1 KB, les vrais modèles > 5 KB
MAX_DEPTH         = 5   # Profondeur max de recherche depuis le dossier racine


def scan_models(root: Path, max_depth: int = MAX_DEPTH) -> list:
    """Scanne récursivement root (jusqu'à max_depth) et retourne les vrais fichiers modèles.

    Filtre les stubs git-lfs (< MIN_MODEL_SIZE_KB).
    """
    seen   = set()
    result = []
    root_depth = len(root.parts)

    for ext in SUPPORTED_EXT:
        for p in sorted(root.rglob(f"*{ext}"), key=lambda x: str(x)):
            if p in seen:
                continue
            # Limite de profondeur
            if len(p.parts) - root_depth > max_depth:
                continue
            seen.add(p)
            try:
                if p.stat().st_size >= MIN_MODEL_SIZE_KB * 1024:
                    result.append(p)
            except OSError:
                pass
    return result


def pick_model_interactive(source_models_dir: Path) -> Path:
    """Menu interactif en 2 étapes : 1) repo  2) fichier modèle."""

    # ── Étape A : lister les repos (sous-dossiers de niveau 2) ───
    # Structure : Source_Models/Framework/Repo/
    repos = []
    for framework_dir in sorted(source_models_dir.iterdir()):
        if not framework_dir.is_dir() or framework_dir.name.startswith("."):
            continue
        for repo_dir in sorted(framework_dir.iterdir()):
            if repo_dir.is_dir():
                repos.append(repo_dir)
        # Si le framework n'a pas de sous-repos, l'ajouter directement
        if not any(d.is_dir() for d in framework_dir.iterdir() if not d.name.startswith(".")):
            repos.append(framework_dir)

    if not repos:
        return None

    # Compter les modèles par repo pour affichage
    print(f"\n  {C.BOLD}Repos disponibles :{C.RESET}\n")
    repo_model_counts = {}
    for repo in repos:
        models = scan_models(repo, max_depth=4)
        repo_model_counts[repo] = models

    current_fw = None
    repo_idx = {}
    display_i = 1
    for repo in repos:
        fw = repo.parent.name
        if fw != current_fw:
            current_fw = fw
            fw_label = {"PyTorch": "🟠 PyTorch", "TensorFlow_Keras": "🔵 TensorFlow/Keras", "ONNX": "🟣 ONNX"}.get(fw, f"📁 {fw}")
            print(f"\n  {C.BOLD}{fw_label}{C.RESET}")
        count = len(repo_model_counts[repo])
        count_str = f"{C.GREEN}{count} modèle(s){C.RESET}" if count > 0 else f"{C.DIM}aucun modèle{C.RESET}"
        print(f"  {C.BOLD}{display_i:>3}.{C.RESET}  {repo.name:<50} {count_str}")
        repo_idx[display_i] = repo
        display_i += 1

    print()
    choice_repo = input("  Numéro du repo : ").strip()
    if not choice_repo.isdigit() or int(choice_repo) not in repo_idx:
        return None
    selected_repo = repo_idx[int(choice_repo)]

    # ── Étape B : lister les modèles dans ce repo ─────────────
    models = repo_model_counts[selected_repo]
    if not models:
        return None

    if len(models) == 1:
        ok(f"Un seul modèle trouvé → sélection automatique : {models[0].name}")
        return models[0]

    print(f"\n  {C.BOLD}Modèles dans {selected_repo.name}/ :{C.RESET}\n")
    for i, p in enumerate(models, 1):
        size_kb = p.stat().st_size / 1024
        try:
            rel = p.relative_to(selected_repo)
        except ValueError:
            rel = p.name
        print(f"  {C.BOLD}{i:>3}.{C.RESET}  {str(rel):<60} {C.DIM}{size_kb:>8.1f} KB{C.RESET}")

    print()
    choice_model = input("  Numéro du modèle : ").strip()
    if not choice_model.isdigit() or not (1 <= int(choice_model) <= len(models)):
        return None
    return models[int(choice_model) - 1]


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Benchmark interactif via ST Edge AI Developer Cloud",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--model",        "-m", help="Chemin du modèle (.tflite / .h5 / .onnx)")
    parser.add_argument("--board",        "-b", help="Nom de la board STM32 cible")
    parser.add_argument("--optimization", "-o",
                        choices=["balanced", "time", "ram"],
                        default="balanced",
                        help="Stratégie d'optimisation (défaut: balanced)")
    parser.add_argument("--no-benchmark", action="store_true",
                        help="Analyse statique uniquement, sans benchmark hardware")
    parser.add_argument("--output",       "-O",
                        help="Chemin du fichier Markdown de sortie (auto-généré si absent)")
    args = parser.parse_args()

    banner("ST Edge AI Developer Cloud — Benchmark interactif")
    print(f"  {C.DIM}Smart Thermostat Edge AI — {datetime.now().strftime('%Y-%m-%d %H:%M')}{C.RESET}")

    # ── [1] Localisation du SDK ───────────────────────────────
    section(1, "Localisation du SDK stm32ai_dc")

    sdk_path, module_name = find_sdk()

    if sdk_path:
        ok(f"SDK trouvé : {sdk_path}")
        info(f"Module : {module_name}")
    else:
        err("SDK stm32ai_dc introuvable dans les emplacements standard.")
        print(f"""
  {C.BOLD}Pour installer le SDK (une seule fois) :{C.RESET}

  {C.CYAN}# Depuis le dossier "Smart Thermostat/"{C.RESET}
  git clone https://github.com/STMicroelectronics/stm32ai-modelzoo-services.git
  pip install -r stm32ai-modelzoo-services/requirements.txt

  {C.CYAN}# Puis relancer :{C.RESET}
  python stedgeai_benchmark.py --model mon_modele.tflite
""")
        sys.exit(1)

    # ── [2] Import du SDK ─────────────────────────────────────
    section(2, "Import du SDK")

    sdk_classes, import_err = import_sdk(sdk_path, module_name)

    if not sdk_classes:
        err(f"Import échoué : {import_err}")
        info("Vérifiez les dépendances :")
        info("  pip install -r stm32ai-modelzoo-services/requirements.txt")
        sys.exit(1)

    Stm32Ai_cls   = sdk_classes.get("Stm32Ai") or sdk_classes.get("STM32AI")
    Backend_cls   = sdk_classes.get("CloudBackend") or sdk_classes.get("Cloud")
    Params_cls    = sdk_classes.get("CliParameters") or sdk_classes.get("AnalyzeParameters") or sdk_classes.get("Parameters")

    ok(f"SDK importé : {', '.join(sdk_classes.keys())}")

    # ── [3] Authentification myST ─────────────────────────────
    section(3, "Authentification myST")
    info("Compte sur https://my.st.com requis (gratuit)")

    username = (STEDGEAI_USERNAME.strip() or           # 1. hardcodé en haut du fichier
                os.environ.get("STEDGEAI_USERNAME") or  # 2. variable d'env
                os.environ.get("STM32AI_USERNAME")  or  # 3. ancien nom de variable
                input("  Email myST : ").strip())       # 4. saisie interactive

    password = (STEDGEAI_PASSWORD.strip() or
                os.environ.get("STEDGEAI_PASSWORD") or
                os.environ.get("STM32AI_PASSWORD")  or
                getpass.getpass("  Mot de passe myST : "))

    print("  Connexion en cours...")

    ai = None
    try:
        backend = Backend_cls(username=username, password=password)
        ai = Stm32Ai_cls(backend)
        ok("Connecté au ST Edge AI Developer Cloud")
    except Exception as e:
        err(f"Connexion échouée : {e}")
        info("→ Vérifiez vos identifiants sur https://stedgeai-dc.st.com")
        info("→ Si votre mot de passe contient des caractères spéciaux (@, :, etc.),")
        info("  utilisez les variables d'env STEDGEAI_USERNAME / STEDGEAI_PASSWORD")
        sys.exit(1)

    # ── [4] Sélection du modèle (scan arborescence) ───────────
    section(4, "Sélection du modèle")

    model_path = None

    if args.model:
        # Chemin fourni en argument : usage direct
        model_path = Path(args.model).expanduser().resolve()
        if not model_path.exists():
            err(f"Fichier introuvable : {model_path}")
            sys.exit(1)
    else:
        # Chercher le dossier Source_Models/
        script_dir = Path(__file__).parent.resolve()
        source_models_dir = None
        for candidate in [
            script_dir / "Source_Models",
            Path.cwd() / "Source_Models",
        ]:
            if candidate.exists() and candidate.is_dir():
                source_models_dir = candidate
                break

        if source_models_dir:
            info(f"Scan de {source_models_dir}")
            model_path = pick_model_interactive(source_models_dir)

        if model_path is None:
            # Fallback : saisie manuelle
            warn("Aucun modèle sélectionné via le menu.")
            model_path_raw = input("  Entrez le chemin complet du modèle : ").strip()
            if not model_path_raw:
                sys.exit(0)
            model_path = Path(model_path_raw).expanduser().resolve()

    if not model_path.exists():
        err(f"Fichier introuvable : {model_path}")
        sys.exit(1)

    model_size_kb = model_path.stat().st_size / 1024
    ok(f"{model_path.name}  ({model_size_kb:.1f} KB)")
    info(str(model_path))

    if model_path.suffix.lower() not in SUPPORTED_EXT:
        warn(f"Extension '{model_path.suffix}' non standard.")
        warn("Le modèle devra peut-être être converti en TFLite ou ONNX d'abord.")
        ans = input("  Continuer quand même ? [y/n] : ").strip().lower()
        if ans not in ("y", "yes", "o", "oui"):
            sys.exit(0)

    # ── [5] Sélection de la board ─────────────────────────────
    section(5, "Sélection de la board STM32")

    board = args.board
    board_list = []

    if not board:
        print("  Récupération des boards disponibles depuis le cloud...")
        try:
            raw_boards = ai.get_benchmark_boards()
            # Normaliser en liste de strings
            if isinstance(raw_boards, (list, tuple)):
                board_list = [
                    b if isinstance(b, str) else getattr(b, "name", str(b))
                    for b in raw_boards
                ]
            elif hasattr(raw_boards, "__iter__"):
                board_list = [
                    b if isinstance(b, str) else getattr(b, "name", str(b))
                    for b in raw_boards
                ]
            ok(f"{len(board_list)} boards disponibles")
        except Exception as e:
            warn(f"Impossible de récupérer la liste en ligne : {e}")
            warn("Utilisation de la liste statique.")

        # Fallback : liste statique connue
        if not board_list:
            board_list = [
                "B-L475E-IOT01A",
                "NUCLEO-H7A3ZI-Q",
                "NUCLEO-L4R5ZI",
                "NUCLEO-F401RE",
                "STM32N6570-DK",
                "NUCLEO-U5A5ZJ-Q",
                "B-U585I-IOT02A",
                "STM32MP257F-EV1",
            ]

        print(f"\n  {'#':<5} {'Board'}")
        print(f"  {'─'*5} {'─'*40}")
        for i, b in enumerate(board_list, 1):
            npu_marker = ""
            if detect_npu(b) == "neural_art":
                npu_marker = f" {C.CYAN}🔮 NPU Neural-ART{C.RESET}"
            elif detect_npu(b) == "hw_accelerator":
                npu_marker = f" {C.YELLOW}⚡ HW Accelerator{C.RESET}"
            elif "H7" in b or "U5" in b:
                npu_marker = " ⭐"
            print(f"  {i:<5} {b}{npu_marker}")

        print()
        choice = input("  Entrez le numéro ou le nom exact de la board : ").strip()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(board_list):
                board = board_list[idx]
            else:
                err(f"Numéro invalide : {choice}")
                sys.exit(1)
        else:
            board = choice

    ok(f"Board : {board}")

    # ── [6] Configuration NPU ─────────────────────────────────
    section(6, "Configuration NPU")

    npu_config = configure_npu_interactive(board, model_path)

    if npu_config and npu_config.get("enabled"):
        ok(f"NPU activé : {NPU_TYPE_LABELS.get(npu_config.get('npu_type'), 'inconnu')}")
    else:
        info("Exécution CPU standard (sans accélération NPU).")

    # ── [7] Options d'optimisation ────────────────────────────
    section(7, "Options d'optimisation")

    optimization = args.optimization
    print(f"  Stratégie : {C.BOLD}{optimization}{C.RESET}  (balanced | time | ram)")
    if optimization == "balanced":
        dim("  → Compromis équilibré RAM/Flash/vitesse (recommandé)")
    elif optimization == "time":
        dim("  → Priorité sur la vitesse d'inférence (plus de RAM)")
    else:
        dim("  → Priorité sur la réduction RAM (peut être plus lent)")

    run_benchmark = not args.no_benchmark
    if run_benchmark:
        print()
        ans = input("  Lancer le benchmark sur hardware réel ? (2-5 min) [y/n] : ").strip().lower()
        run_benchmark = ans in ("y", "yes", "o", "oui")

    # Initialisation du suivi de statut (alimenté au fil des étapes)
    run_status = {
        "upload":    {"tried": False, "ok": False, "detail": "—"},
        "analyze":   {"tried": False, "ok": False, "detail": "—"},
        "benchmark": {"tried": False, "ok": False, "detail": "—"},
        "npu":       {"tried": False, "ok": False, "detail": "—"},
    }

    # Statut NPU (déjà déterminé à l'étape [6])
    if npu_config and npu_config.get("enabled"):
        npu_label = NPU_TYPE_LABELS.get(npu_config.get("npu_type"), "NPU")
        run_status["npu"] = {"tried": True, "ok": True, "detail": npu_label}
    elif detect_npu(board):
        ext = model_path.suffix.lower()
        if ext in NPU_INCOMPATIBLE_FORMATS:
            run_status["npu"] = {"tried": False, "ok": False,
                                  "detail": f"Format `{ext}` incompatible — convertir en .tflite ou .onnx"}
        else:
            run_status["npu"] = {"tried": False, "ok": False, "detail": "Désactivé par l'utilisateur"}
    else:
        run_status["npu"] = {"tried": False, "ok": False, "detail": "Pas de NPU sur cette board"}

    # ── [8] Upload du modèle sur le cloud ─────────────────────
    section(8, "Upload du modèle sur le cloud")

    uploaded_model_name = model_path.name
    upload_logs = ""

    print(f"  Modèle : {uploaded_model_name}  ({model_size_kb:.1f} KB)")
    print("  Upload vers ST Edge AI Developer Cloud...")

    run_status["upload"]["tried"] = True
    try:
        cloud_models = [m.get("name", m) if isinstance(m, dict) else str(m)
                        for m in (ai.list_models() or [])]
        if uploaded_model_name in cloud_models:
            ok(f"Modèle déjà présent sur le cloud : {uploaded_model_name}")
            run_status["upload"]["ok"]     = True
            run_status["upload"]["detail"] = f"`{uploaded_model_name}` ({model_size_kb:.1f} KB) — déjà présent"
        else:
            uploaded = ai.upload_model(str(model_path))
            if uploaded:
                ok(f"Modèle uploadé : {uploaded_model_name}")
                run_status["upload"]["ok"]     = True
                run_status["upload"]["detail"] = f"`{uploaded_model_name}` ({model_size_kb:.1f} KB)"
            else:
                warn("Upload a échoué ou modèle déjà présent — on continue.")
                run_status["upload"]["detail"] = "Réponse ambiguë du serveur"
    except Exception as e:
        warn(f"Vérification cloud échouée : {e}")
        warn("→ Tentative d'upload quand même...")
        try:
            ai.upload_model(str(model_path))
            ok("Upload réussi.")
            run_status["upload"]["ok"]     = True
            run_status["upload"]["detail"] = f"`{uploaded_model_name}` ({model_size_kb:.1f} KB)"
        except Exception as e2:
            err(f"Upload échoué : {e2}")
            upload_logs = traceback.format_exc()
            run_status["upload"]["detail"] = f"Erreur : {e2}"

    # ── [9] Analyze (analyse statique) ────────────────────────
    section(9, "Analyse statique (analyze)")
    print("  Envoi de la requête analyze au cloud...")
    print(f"  {C.DIM}(sans params NPU — l'endpoint /analyze ne les supporte pas){C.RESET}")

    analyze_result = None
    analyze_logs   = ""
    run_status["analyze"]["tried"] = True

    try:
        params = build_analyze_params(uploaded_model_name, board, optimization, Params_cls)

        # analyze(options) — 1 seul argument (+ self).
        # Ne pas catcher TypeError : le SDK interne en lève une quand le serveur
        # retourne None (bug cloud.py:101 : 'message' in None). On laisse remonter.
        analyze_result = ai.analyze(params)

        if analyze_result is None:
            raise RuntimeError("Le serveur a retourné une réponse vide. "
                               "Vérifiez les logs du terminal pour l'erreur serveur.")

        ok("Analyse terminée !")
        a_ram_v   = safe_get(analyze_result, "ram_size",   "estimated_ram_size", "ram")
        a_flash_v = safe_get(analyze_result, "flash_size", "estimated_flash_size","flash")
        a_macc_v  = safe_get(analyze_result, "macc",       "total_macc",          "macs")
        run_status["analyze"]["ok"]     = True
        run_status["analyze"]["detail"] = (
            f"RAM {fmt_bytes(a_ram_v)} · Flash {fmt_bytes(a_flash_v)} · {fmt_macc(a_macc_v)}"
        )

        # Affichage des résultats
        print()
        fields = [
            ("RAM estimée",       ["ram_size",   "estimated_ram_size",   "ram"]),
            ("Flash estimée",     ["flash_size", "estimated_flash_size", "flash"]),
            ("MACCs",             ["macc",       "total_macc",           "macs"]),
            ("Paramètres",        ["weights",    "params_count",         "parameters"]),
            ("Nombre de couches", ["num_layers", "layers_count",         "n_layers"]),
        ]
        for label, keys in fields:
            val = safe_get(analyze_result, *keys)
            if label in ("RAM estimée", "Flash estimée"):
                table_row(label, fmt_bytes(val))
            elif label == "MACCs":
                table_row(label, fmt_macc(val))
            else:
                table_row(label, str(val))

    except Exception as e:
        err(f"Analyse échouée : {e}")
        analyze_logs = traceback.format_exc()
        run_status["analyze"]["detail"] = f"Erreur : {str(e)[:120]}"
        warn("Le rapport Markdown contiendra le log d'erreur complet.")

    # ── [10] Benchmark (optionnel) ────────────────────────────
    bench_result = None
    bench_logs   = ""

    if run_benchmark:
        section(10, f"Benchmark sur {board}")
        print("  Envoi vers la board farm... (peut prendre 2–5 minutes)")
        print("  Chaque board est physiquement disponible dans les locaux ST.")
        if npu_config and npu_config.get("enabled"):
            npu_lbl = NPU_TYPE_LABELS.get(npu_config.get("npu_type"), "NPU")
            print(f"  {C.CYAN}Config NPU : {npu_lbl}{C.RESET}")

        run_status["benchmark"]["tried"] = True
        try:
            params = build_benchmark_params(
                uploaded_model_name, board, optimization,
                npu_config, Params_cls, module_name
            )

            bench_result = ai.benchmark(params, board)

            if bench_result is None:
                raise RuntimeError("Le serveur a retourné une réponse vide pour le benchmark.")

            ok(f"Benchmark terminé sur {board} !")
            b_ms_v = safe_get(bench_result, "duration_ms", "inference_time", "latency_ms")
            b_fps_v = "—"
            try:
                if b_ms_v not in ("—", None) and float(b_ms_v) > 0:
                    b_fps_v = f"{1000/float(b_ms_v):.1f} inf/s"
            except (ValueError, TypeError):
                pass
            run_status["benchmark"]["ok"]     = True
            run_status["benchmark"]["detail"] = (
                f"{b_ms_v} ms · {b_fps_v}" if b_ms_v not in ("—", None) else "OK"
            )

            # Affichage
            print()
            b_fields = [
                ("RAM réelle",          ["ram_size",      "ram"]),
                ("Flash réelle",        ["flash_size",    "flash"]),
                ("Temps d'inférence",   ["inference_time","latency_ms","duration_ms"]),
                ("Fréquence CPU (MHz)", ["cpu_freq_mhz",  "cpu_frequency","clock_mhz"]),
                ("Cycles",              ["cycles",        "clock_cycles"]),
            ]
            for label, keys in b_fields:
                val = safe_get(bench_result, *keys)
                if label in ("RAM réelle", "Flash réelle"):
                    table_row(label, fmt_bytes(val))
                elif label == "Temps d'inférence" and val not in ("—", None):
                    try:
                        fps = f"{1000 / float(val):.1f} inf/sec"
                        table_row(label, f"{val} ms  →  {fps}")
                    except (ValueError, TypeError):
                        table_row(label, str(val))
                else:
                    table_row(label, str(val))

        except Exception as e:
            err(f"Benchmark échoué : {e}")
            bench_logs = traceback.format_exc()
            run_status["benchmark"]["detail"] = f"Erreur : {str(e)[:120]}"
            warn("Le rapport Markdown contiendra le log d'erreur complet.")
    else:
        run_status["benchmark"] = {"tried": False, "ok": False, "detail": "Non demandé"}

    # ── [11] Génération du rapport Markdown ───────────────────
    step_n = 11 if run_benchmark else 10
    section(step_n, "Génération du rapport Markdown")

    all_logs = "\n\n".join(filter(None, [upload_logs, analyze_logs, bench_logs]))

    md_content = build_markdown(
        model_path     = str(model_path),
        board          = board,
        optimization   = optimization,
        analyze_result = analyze_result,
        bench_result   = bench_result if run_benchmark else None,
        logs           = all_logs,
        npu_config     = npu_config,
        run_status     = run_status,
    )

    # Fichier de sortie
    if args.output:
        out_path = Path(args.output).expanduser().resolve()
    else:
        ts       = datetime.now().strftime("%Y%m%d_%H%M")
        out_name = f"benchmark_{model_path.stem}_{board}_{ts}.md"
        out_path = model_path.parent / out_name

    out_path.write_text(md_content, encoding="utf-8")
    ok(f"Rapport sauvegardé : {out_path}")

    # ── [12] Mise à jour du master tracker ────────────────────
    section(step_n + 1, "Mise à jour de l'historique global")

    script_dir = Path(__file__).parent.resolve()
    a_ram_r  = safe_get(analyze_result, "ram_size",   "estimated_ram_size",  "ram")
    a_fla_r  = safe_get(analyze_result, "flash_size", "estimated_flash_size","flash")
    a_mac_r  = safe_get(analyze_result, "macc",       "total_macc",          "macs")
    b_ms_r   = safe_get(bench_result,   "duration_ms","inference_time",      "latency_ms")
    b_fps_r  = "—"
    try:
        if b_ms_r not in ("—", None) and float(b_ms_r) > 0:
            b_fps_r = f"{1000/float(b_ms_r):.1f}"
    except (ValueError, TypeError):
        pass

    # Cellule NPU pour le tracker
    if npu_config and npu_config.get("enabled"):
        npu_cell = f"🔮 {npu_config.get('npu_type','?')}"
    elif detect_npu(board):
        npu_cell = "⬜ NPU off"
    else:
        npu_cell = "—"

    tracker_path = update_master_tracker(script_dir, {
        "date":         datetime.now().strftime("%Y-%m-%d %H:%M"),
        "model":        model_path.name,
        "board":        board,
        "fmt":          model_path.suffix.lower(),
        "optimization": optimization,
        "npu_cell":     npu_cell,
        "upload_tried": run_status["upload"]["tried"],
        "upload_ok":    run_status["upload"]["ok"],
        "a_ram":        fmt_bytes(a_ram_r)  if a_ram_r  not in ("—", None) else "—",
        "a_flash":      fmt_bytes(a_fla_r)  if a_fla_r  not in ("—", None) else "—",
        "a_macc":       fmt_macc(a_mac_r),
        "b_ms":         f"{b_ms_r} ms"      if b_ms_r   not in ("—", None) else "—",
        "b_fps":        b_fps_r,
        "analyze_ok":   run_status["analyze"]["ok"],
        "bench_ok":     run_status["benchmark"]["ok"],
        "report_path":  str(out_path),
    })
    ok(f"Historique mis à jour : {tracker_path}")

    # ── Fin ───────────────────────────────────────────────────
    banner("✅ Terminé !")
    print(f"  Rapport    : {C.CYAN}{out_path}{C.RESET}")
    print(f"  Historique : {C.CYAN}{tracker_path}{C.RESET}")
    print()


if __name__ == "__main__":
    main()
