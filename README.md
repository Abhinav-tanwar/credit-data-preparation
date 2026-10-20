# Credit Data Preparation

A schema-aware preprocessing pipeline with a clearly labeled synthetic credit dataset.

## Data and scope

**Synthetic demonstration data.** The original input is unavailable. The CSV in data/ is newly generated using seed 42; it is not reconstructed original data and cannot reproduce the original notebook's historical results.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/analysis.py
python -m unittest discover -s tests -v
```

Outputs are written to `outputs/`. The clean notebook in `notebooks/analysis.ipynb` calls the same tested module. See `docs/provenance.md` for changes from the source notebook and `docs/validation.md` for actual execution results.

Regenerate the clearly labeled demo CSV with `python scripts/generate_demo_data.py`. Supply your own legitimately obtained data using `--input path/to/file.csv`.

## Synthetic demonstration results

1200 generated rows; 960 training and 240 held out. The train-fitted pipeline produces 21 finite encoded features. No predictive performance is claimed. Column-specific missing-value checks and outlier counts are recorded in `docs/metrics.json`.
