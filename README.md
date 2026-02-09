# RNSE Admissibility Verification Suite (v1.0.0)

**Author:** Elad Genish  
**License:** CC BY-NC-ND 4.0  
**Version:** v1.0.0  
**DOI:** (assigned via Zenodo release)

This repository contains a complete, replayable verification suite for the
RNSE (Recursive Null Seed Engine) computational substrate.

The suite is designed for **third-party adversarial validation** without
access to engine internals. All tests rely exclusively on surface-visible,
deterministic artifacts.

No training.  
No objectives.  
No learned parameters.

Only admissibility, replay, and observable structure.

---

## What Is Being Verified

RNSE is evaluated as a **constraint-driven computational substrate**, not as
an optimizer, learner, or task-specific model.

This suite verifies whether RNSE exhibits the following properties under
adversarial replay:

1. **Dimension-Indifferent Coherence** — topological invariants preserved when
   dimensions are added and projected back (T1).
2. **Emergent Conservation Laws** — conserved quantities arise from admissibility
   constraints alone (T2).
3. **Long-Horizon Stability with Graceful Degradation** — structured → turbulent
   regimes without blow-up or freeze (T3).
4. **Cross-Domain Structural Transfer** — structural ordering persists when
   constraints are swapped across domains without re-init (T4).
5. **Adversarial Noise Rejection** — malicious sensors down-weighted via
   admissibility divergence (T5).
6. **Non-Trivial Seed Space Geometry** — seed perturbations exhibit interference
   and resonance (T6).
7. **Spontaneous Organization Without Objectives** — behavioral species emerge
   without goals or optimization (T7).
8. **Competitive Baselines Without Priors** — parity on selected structure
   benchmarks without inductive bias or training (T8).

---

## Metrics (Surface-Only)

All verification uses two orthogonal, externally observable metrics:

- **CVR — Constraint Violation Residual**
- **RCI — Realignment Cost Integral**

Regime shifts are **derived** from CVR breaks and RCI spikes.

---

## Repository Structure

```
.
├── README.md
├── RNSE_Verification_Suite_v1.0.pdf
├── METHODS.md
├── REPRODUCIBILITY.md
├── ADVERSARIAL_SCOPE.md
├── VERSION
├── LICENSE.txt
├── CITATION.cff
├── bounds.json
├── hashes.json
├── scripts/
│   ├── replay_script.py
│   ├── compute_cvr.py
│   └── compute_rci.py
└── data/
    ├── (place replay bundles here)
```

---

## Quick Replay (Minimal)

```bash
sha256sum -c hashes.json
python scripts/replay_script.py --test T1
python scripts/compute_cvr.py --test T1
python scripts/compute_rci.py --test T1
```

Expected CVR/RCI bounds are defined in `bounds.json`.

---

## What Counts as Failure

RNSE is considered falsified for a test if:

- CVR exceeds the declared bound under deterministic replay, or
- RCI diverges without recovery under declared admissibility constraints.

No qualitative interpretation is required.

---

## Citation

Please cite the Zenodo DOI associated with this release.

---

## Adversarial Invitation

This suite is intentionally designed to be attacked.

If you believe the claims fail:
- Fork the repo
- Replay the tests
- Publish the CVR/RCI violation

If the bounds break, the claim breaks.
