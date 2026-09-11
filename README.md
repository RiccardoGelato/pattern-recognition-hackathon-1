# Pattern Recognition Hackathon 1

Teaching repository for the [FYS-3012 Pattern Recognition](https://github.com/Wickstrom/pattern-recognition-handbook) course at UiT The Arctic University of Norway.

## The task

Predict penguin `species` from morphological measurements using the Palmer Penguins dataset. The data is deliberately imperfect — missing values, correlated features, unequal class sizes — so your model choices have to be justified, not just benchmarked.

## Competition data

The prepared competition data is already included in `data/processed/`:

- `train.csv` contains features and `species` labels.
- `test.csv` contains features only.
- `sample_submission.csv` provides the required submission format.

Missing values are intentionally retained. Decide how to handle them in your preprocessing pipeline. Do not change the row order of `test.csv` when creating predictions.

## Submit your predictions

**Competition link: [TBA]**

- **Format:** a CSV file with a single `species` column, one row per test sample, in the same order as `test.csv` (see `sample_submission.csv`).
- **Leaderboard metric:** macro F1.
- **Deadline:** TBA.

## Repository layout

```text
notebooks/   # scaffolded exercises: EDA, Bayes/densities, linear, SVM/NN, final method
src/         # student-safe data helpers and evaluation metrics
data/processed/  # committed training data, test data, and submission template
```

## Setup

```bash
python -m pip install -r requirements.txt
```

`environment.yml` provides the equivalent Conda environment. Run notebooks and scripts from the repository root.
