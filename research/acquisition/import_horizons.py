"""CLI to retrieve or parse a configured public Horizons response."""
from __future__ import annotations

import argparse
from pathlib import Path

from research.acquisition.horizons import parse_observer_ephemeris, retrieve, write_processed

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(ROOT / "configs" / "acquisition" / "horizons_266p_1977.yaml"))
    parser.add_argument("--raw", default=str(ROOT / "research" / "data" / "raw" / "horizons_266p_1977_geocentric.txt"))
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    raw = Path(args.raw)
    if args.fetch:
        manifest = retrieve(args.config, raw)
        url = manifest["url"]
        config = manifest["config"]
    else:
        import yaml
        config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
        url = "retrieved_prior_to_import; see raw response manifest if present"
    records = parse_observer_ephemeris(raw, url, str(config["command"]), str(config["center"]))
    destination = ROOT / "research" / "data" / "processed" / "horizons_266p_1977_geocentric.json"
    write_processed(records, destination)
    print(destination)

if __name__ == "__main__": main()
