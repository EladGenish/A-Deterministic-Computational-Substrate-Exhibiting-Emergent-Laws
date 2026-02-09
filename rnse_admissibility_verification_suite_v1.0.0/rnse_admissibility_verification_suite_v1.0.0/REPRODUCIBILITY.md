# Reproducibility

This repository is intended for **byte-stable third-party replay**.

## 1) Verify hashes

```bash
sha256sum -c hashes.json
```

If any file fails hash verification, replay results are invalid.

## 2) Run a replay

```bash
python scripts/replay_script.py --test T1 --out runs/T1
```

This produces deterministic outputs for the selected test in `runs/T1/`.

## 3) Recompute metrics (CVR / RCI)

```bash
python scripts/compute_cvr.py --test T1 --run runs/T1
python scripts/compute_rci.py --test T1 --run runs/T1
```

## 4) Compare to declared bounds

Declared bounds are stored in `bounds.json`.

## Determinism notes

- All scripts use fixed seeds.
- Use Python 3.10+.
- Numpy floating-point behavior can vary across platforms. For strict replay,
  use the provided Dockerfile (optional) or a fixed environment.

(If you publish a replay violation, include your platform + Python + numpy versions.)
