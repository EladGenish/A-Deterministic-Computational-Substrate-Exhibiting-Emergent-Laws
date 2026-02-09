# Methods: Admissibility Verification Framework

This document specifies the methodological principles used to verify RNSE
behavior without access to engine internals.

The framework is designed to prevent overfitting, narrative labeling, and
post-hoc interpretation.

---

## Surface-Only Design Principle

All verification relies exclusively on **externally observable artifacts**:

- Deterministic logs
- Acceptance / rejection traces
- Merkle roots
- Hash-verified replay bundles

No internal state, gradients, representations, or heuristics are accessed.

---

## Deterministic Replay

All tests are fully deterministic:

- Fixed seeds
- Fixed floating-point behavior
- Byte-stable logs
- SHA-256 hashes for all artifacts

Replay must produce identical hashes for validation to be considered valid.

---

## Metrics

### Constraint Violation Residual (CVR)

CVR measures whether a declared admissibility invariant remains satisfied
under replay.

General form:

CVR = |Observed − Baseline| / Baseline

Each test defines a specific CVR observable and a declared bound.

CVR > bound constitutes falsification.

---

### Realignment Cost Integral (RCI)

RCI measures the cumulative cost required to maintain admissibility.

Correction events are categorized and weighted:

- Rejection (wr = 1.0)
- Re-evaluation (we = 0.5)
- Rollback (wb = 5.0)
- Thread reweighting (wt = 0.3)
- Constraint relaxation (wc = 10.0)

RCI is integrated over time using a fixed rolling window.

RCI spikes indicate regime transitions or stress responses.

---

## Regime Detection

Regime shifts are **derived**, not labeled.

A regime shift is detected when either:

1. CVR exceeds its declared bound for N consecutive steps, or
2. d(RCI)/dt exceeds 3σ above its rolling mean.

---

## Baseline Selection

Baselines are selected conservatively:

- Diffusion / random walk for conservation tests
- PID control for adversarial sensing
- Perlin noise and ESN/DMD for classical benchmarks

---

## Interpretation Discipline

This framework does **not** assert:

- Physical realism
- Optimality
- Intelligence
- Consciousness
- Universality

Only **observable admissibility properties** are claimed.
