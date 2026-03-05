from pathlib import Path

# Project root = parent of this file's parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Core folders
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
MODELS_DIR = PROJECT_ROOT / "models"
CONFIG_DIR = PROJECT_ROOT / "models"


# PHB-specific
PHB_RESULTS_DIR = RESULTS_DIR / "phb"
PHB_FIGURES_DIR = PHB_RESULTS_DIR / "figures"
PHB_SUPP_DIR = PHB_RESULTS_DIR / "supplementary"
PHB_MODEL_DIR = MODELS_DIR / "phb"

# Create automatically
for path in [
    DATA_DIR,
    CONFIG_DIR,
    PHB_RESULTS_DIR,
    PHB_FIGURES_DIR,
    PHB_SUPP_DIR,
    PHB_MODEL_DIR
]:
    path.mkdir(parents=True, exist_ok=True)






