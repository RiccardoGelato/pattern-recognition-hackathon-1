"""Small, student-safe data helpers for the teaching notebooks."""

from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRAIN_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "train.csv"
NUMERIC_FEATURES = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
TARGET = "species"


def load_penguins(path: str | Path | None = None) -> pd.DataFrame:
    """Load the labeled training data available to students."""
    return pd.read_csv(path or TRAIN_DATA_PATH)

