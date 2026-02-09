#!/usr/bin/env python3
"""
Deterministic replay executor (scaffold).

This repository is designed to be surface-only and replayable.
If you already have per-test replay bundles (e.g., *.npy, *.json),
place them under data/ and implement the loader paths below.

This scaffold is intentionally minimal to avoid implying engine internals.
"""
from __future__ import annotations
import argparse, json, os, pathlib, sys, hashlib

def sha256_file(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", required=True, help="Test ID: T1..T8")
    ap.add_argument("--out", default="runs", help="Output directory")
    args = ap.parse_args()

    out_dir = pathlib.Path(args.out) / args.test
    out_dir.mkdir(parents=True, exist_ok=True)

    # For now, we emit a minimal manifest that ties the run to the canonical PDF and bounds.
    manifest = {
        "test": args.test,
        "note": "Replay scaffold: attach real replay bundles under data/ and extend as needed.",
        "artifacts_expected": ["cvr_trace.json", "rci_trace.json"],
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"[ok] wrote {out_dir/'manifest.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
