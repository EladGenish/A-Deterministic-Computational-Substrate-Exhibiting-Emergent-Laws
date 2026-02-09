#!/usr/bin/env python3
"""
Compute CVR (Constraint Violation Residual) from surface-visible artifacts.

This is a minimal scaffold. If you have the per-test definitions and outputs,
point this script at your run directory and emit `cvr_trace.json` plus a summary.

Design goal: deterministic, surface-only computation.
"""
from __future__ import annotations
import argparse, json, pathlib

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", required=True)
    ap.add_argument("--run", required=True, help="Run directory, e.g. runs/T1")
    args = ap.parse_args()

    run_dir = pathlib.Path(args.run)
    out = run_dir / "cvr_trace.json"

    # Placeholder: real CVR computation should be wired to replay bundles.
    trace = {"test": args.test, "cvr": 0.0, "note": "scaffold"}
    out.write_text(json.dumps(trace, indent=2) + "\n", encoding="utf-8")
    print(f"[ok] wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
