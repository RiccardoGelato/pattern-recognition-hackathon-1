"""Evaluation helpers kept consistent across notebooks."""

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score


def summarize_classifier(y_true, y_pred) -> dict[str, float]:
    """Return metrics suitable for comparing the course methods."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro"),
    }


def confusion_table(y_true, y_pred) -> pd.DataFrame:
    """Return a labeled confusion matrix as a DataFrame."""
    labels = sorted(set(y_true) | set(y_pred))
    return pd.DataFrame(
        confusion_matrix(y_true, y_pred, labels=labels),
        index=pd.Index(labels, name="actual"),
        columns=pd.Index(labels, name="predicted"),
    )


def print_report(y_true, y_pred) -> None:
    """Print the detailed report used in the final challenge."""
    print(classification_report(y_true, y_pred))
