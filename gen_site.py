#!/usr/bin/env python3
"""Regenerate README.md (and LaTeX fragments) from assets/catalog.json.
Usage: python gen_site.py   (run from repo root)
index.html reads assets/catalog.json directly at load time, so it needs no regeneration."""
import json, subprocess, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
# point the generators at the in-repo catalog
os.environ["CATALOG"] = os.path.join(HERE, "assets", "catalog.json")
print("Edit assets/catalog.json, then this script rebuilds README.md.")
print("(LaTeX appendix is regenerated in the paper repo via gen_tables.py.)")
