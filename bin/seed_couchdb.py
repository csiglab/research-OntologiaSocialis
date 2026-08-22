#!/usr/bin/env python3
"""
Seed CouchDB from the dataset files under docs/data/<dataset>/data.json.

Loads every dataset (e.g. 'idx' and 'prd') into the CouchDB database, one
document per node with ids namespaced as '{dataset}:{node_id}'. Idempotent:
re-running updates existing docs and inserts missing ones. The data.json
files stay in place — they are NOT deleted.

    python bin/seed_couchdb.py
    python bin/seed_couchdb.py --docs-root docs --dataset idx
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sync import CouchClient, discover_datasets  # noqa: E402

import os  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(prog="seed_couchdb.py")
    here = Path(__file__).resolve().parent
    repo = here.parent
    p.add_argument("--docs-root", default=str(repo / "docs"))
    p.add_argument(
        "--dataset",
        default=None,
        help="Seed only this dataset (default: all datasets under docs/data/).",
    )
    args = p.parse_args(argv)

    datasets = discover_datasets(args.docs_root)
    if not datasets:
        print(
            f"ERROR: no datasets found under {args.docs_root}/data/*/data.json",
            file=sys.stderr,
        )
        return 1
    if args.dataset:
        if args.dataset not in datasets:
            print(
                f"ERROR: unknown dataset '{args.dataset}'. "
                f"Known: {', '.join(sorted(datasets))}",
                file=sys.stderr,
            )
            return 1
        datasets = {args.dataset: datasets[args.dataset]}

    couch = CouchClient(
        os.environ.get("COUCHDB_URL", "http://localhost:5984"),
        os.environ.get("COUCHDB_DB", "sociognosis"),
        user=os.environ.get("COUCHDB_USER"),
        password=os.environ.get("COUCHDB_PASSWORD"),
    )

    try:
        couch.ensure_db()
    except Exception as exc:
        print(f"ERROR: cannot reach CouchDB: {exc}", file=sys.stderr)
        return 1

    failed = False
    for name, data_file in sorted(datasets.items()):
        print(f"Seeding {data_file} -> {couch.base_url}/{couch.db} ({name})")
        try:
            with open(data_file, "r", encoding="utf-8") as fh:
                seed = json.load(fh)
        except Exception as exc:
            print(f"ERROR: cannot read {data_file}: {exc}", file=sys.stderr)
            failed = True
            continue

        nodes = [n for n in seed if isinstance(n, dict) and n.get("id")]
        if not nodes:
            print(f"ERROR: no node records with an id in {data_file}",
                  file=sys.stderr)
            failed = True
            continue

        try:
            written = couch.bulk_upsert(name, nodes)
        except Exception as exc:
            print(f"ERROR: seeding '{name}' failed: {exc}", file=sys.stderr)
            failed = True
            continue
        print(f"  seeded '{name}': {written}/{len(nodes)} docs ok")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
