# src/paths.py
import os
from pathlib import Path

# ------------------------------
# Determine project root
# ------------------------------
# Default: parent of this file's parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Override if running in Colab and mounted in Google Drive
try:
    import google.colab
    DRIVE_ROOT = Path("/content/drive/MyDrive/metabolic_modelling/phb-optimization-rpalustris")
    if DRIVE_ROOT.exists():
        PROJECT_ROOT = DRIVE_ROOT
except ImportError:
    pass  # Not running in Colab, keep default PROJECT_ROOT

# ------------------------------
# Core folders
# ------------------------------
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"

# ------------------------------
# PHB-specific folders
# ------------------------------
PHB_MODEL_DIR = MODELS_DIR / "phb"
PHB_RESULTS_DIR = RESULTS_DIR / "phb"
PHB_CHECKPOINTS_DIR = PHB_RESULTS_DIR / "checkpoints"
PHB_GEM_EXPERIMENTAL_DIR = PHB_RESULTS_DIR / "gem_experimental"
PHB_GEM_AUGMENTATION_DIR = PHB_RESULTS_DIR / "gem_augmentation"
PHB_CATBOOST_DIR = PHB_RESULTS_DIR / "catboost"
PHB_PARETO_DIR = PHB_RESULTS_DIR / "pareto"
PHB_FIGURES_DIR = PHB_RESULTS_DIR / "figures"
PHB_TFA_DIR = PHB_RESULTS_DIR / "tfa"
PHB_MODEL_TFA_DIR = PHB_MODEL_DIR / "tfa"
PHBV_MODEL_DIR = MODELS_DIR / "phbv"



# ------------------------------
# Auto-create folders if missing
# ------------------------------
for path in [DATA_DIR, RESULTS_DIR, MODELS_DIR,
             PHB_RESULTS_DIR, PHB_FIGURES_DIR, PHB_GEM_EXPERIMENTAL_DIR,
            PHB_GEM_AUGMENTATION_DIR, PHB_CHECKPOINTS_DIR, PHB_CATBOOST_DIR, 
            PHB_PARETO_DIR, PHB_MODEL_DIR, PHB_TFA_DIR, PHB_MODEL_TFA_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# ------------------------------
# Optional: print paths for verification
# ------------------------------
if __name__ == "__main__":
    print("Project root:", PROJECT_ROOT)
    print("Data dir:", DATA_DIR)
    print("Results dir:", RESULTS_DIR)
    print("PHB results dir:", PHB_RESULTS_DIR)
    print("PHB figures dir:", PHB_FIGURES_DIR)
    print("PHB checkpoints dir:", PHB_CHECKPOINTS_DIR)
    print("PHB model dir:", PHB_MODEL_DIR)
    print("PHB TFA dir:", PHB_TFA_DIR)