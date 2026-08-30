"""Build HOBART_SESSION_MASTER_TABLE.csv — canonical Hobart session table.

One row per RPFITS archive (the raw observational unit) plus the documented
1998-99 correlator-era sessions. Every populated cell traces to a locator;
absent evidence is the literal string UNKNOWN. Nothing here infers observing
intent, sensitivity, or outcomes.

Inputs (all previously generated, read-only):
    analysis/rpfits_card_inventory.json   (OBS/OBJECT/EPOCH/CRVAL4/CDELT4/NAXIS4 cards)
    analysis/rpfits_su_widescan.json      (SU target tables)
    analysis/dump_spacing_stats.json      (5 s cadence)
    extracted/HOBART_XLS_PLAN_TEXT.txt    (Jaekle plan: Tint=5 s, configs)

Output:
    research/sources/ellingsen_hobart/extracted/HOBART_SESSION_MASTER_TABLE.csv
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE = REPO_ROOT / "research" / "sources" / "ellingsen_hobart"

FIELDS = [
    "session_id", "date_utc", "start_time_utc", "end_time_utc",
    "duration_first_to_last_spectrum_h", "target_names_su", "field_identifier",
    "ra_j2000_commanded", "dec_j2000_commanded", "coordinate_epoch",
    "center_frequency_mhz", "bandwidth_mhz", "channel_count_pol1",
    "dump_cadence_s", "integration_time_s", "calibration_state",
    "file_provenance", "rpfits_association", "spectrum_association",
    "pointing_association", "scanlog_association", "source_locators",
]

XLS = "original/…-001/2013obs/Mt Pleasant 2013 Observing PLAN (draft 2013-07-22).xls (text render: extracted/HOBART_XLS_PLAN_TEXT.txt)"
CAD = "analysis/dump_spacing_stats.json"


def main() -> int:
    cards = json.load(open(BASE / "analysis" / "rpfits_card_inventory.json"))
    su = json.load(open(BASE / "analysis" / "rpfits_su_widescan.json"))

    def field_of(names: list[str]) -> str:
        joined = " ".join(n["name"] for n in names)
        if "wow_f1" in joined:
            return "field1_EastBeam"
        if "wow_f2" in joined:
            return "field2_WestBeam"
        if "wow_off" in joined or "wow" in joined:
            return "pre-field_2010_position"
        return "UNKNOWN"

    def ra_dec(names: list[str]) -> tuple[str, str]:
        on = [n for n in names if n["name"].startswith("wow")]
        if not on:
            return "UNKNOWN", "UNKNOWN"
        return f"{on[0]['ra_h']}h", f"{on[0]['dec_deg']}deg"

    rows = []
    for name, c in sorted(cards.items()):
        try:
            cdelt_hz = float(c.get("CDELT4", "nan"))
            naxis4 = int(float(c.get("NAXIS4", "nan")))
            bw_mhz = cdelt_hz * (naxis4 - 1) / 1e6 if naxis4 > 1 else None
        except ValueError:
            bw_mhz = None
        names = su.get(name, {}).get("entries", [])
        tgt = ", ".join(f"{n['name']}({n['ra_h']}h,{n['dec_deg']})" for n in names[:4])
        fid = field_of(names)
        ra, dec = ra_dec(names)
        obs = c.get("OBS", "").strip()
        yydd = name[1:7]  # YYMMDD? no: c<YY><DDD><HHMM> -> name[1:3]=YY name[3:6]=DDD
        doy_tag = f"{name[1:3]}-{name[3:6]}"
        assoc = {
            "c10228": "bruce_10228.log/ricky_10228.log; spectra.tar.gz+loose 2010obs txt",
            "c13189": "bruce_13189.log; wow_test_2013doy189.tar.gz",
            "c13192": "bruce_13192.log; wow_test_2013doy192.tar.gz",
            "c13218052x": "wow_field1_2013doy218.tar.gz",
            "c13219": "wow_field2_2013doy219.tar.gz (+0518/0742 short archives)",
            "c13256": "wow_field1_2013doy256/258.tar.gz",
            "c14205": "wow_field2_2014doy205.tar.gz",
            "c14283": "wow_field1_2014doy283.tar.gz",
        }
        sa = assoc.get(name[:7], assoc.get(name[:6], "UNKNOWN"))
        rows.append(
            {
                "session_id": name.replace(".rpf", ""),
                "date_utc": obs or "UNKNOWN",
                "start_time_utc": f"~{name[6:8]}:{name[8:10]}UT (from filename convention; DERIVED)",
                "end_time_utc": "UNKNOWN",
                "duration_first_to_last_spectrum_h": (
                    f"{su.get(name,{}).get('span_h')}" if su.get(name, {}).get("span_h") else "UNKNOWN"
                ),
                "target_names_su": tgt or "UNKNOWN",
                "field_identifier": fid,
                "ra_j2000_commanded": ra,
                "dec_j2000_commanded": dec,
                "coordinate_epoch": c.get("EPOCH", "").strip() or "UNKNOWN",
                "center_frequency_mhz": float(c["CRVAL4"]) / 1e6 if c.get("CRVAL4") else "UNKNOWN",
                "bandwidth_mhz": round(bw_mhz, 4) if bw_mhz else "UNKNOWN",
                "channel_count_pol1": f"{naxis4 - 1} (rpf header)" if naxis4 > 1 else "UNKNOWN",
                "dump_cadence_s": "5.0 median (session-matched tarballs)",
                "integration_time_s": "5.0 per plan (Tint col, XLS Sensitivity sheet); executed value UNCONFIRMED",
                "calibration_state": (
                    "DOCUMENTED_2010_chain(CAL49.4/53.7Jy,SEFD450/433Jy)"
                    if name.startswith("c10228")
                    else "RELATIVE_NORMALIZATION_PROVISIONAL_classC"
                ),
                "file_provenance": "DONOR_SUPPLIED|RPFITS_RAW_OBSERVATIONAL",
                "rpfits_association": f"analysis/rpfits_card_inventory.json#{name}",
                "spectrum_association": sa,
                "pointing_association": f"analysis/rpfits_su_widescan.json#{name}",
                "scanlog_association": sa,
                "source_locators": f"rpf header cards; SU table; {CAD}; plan: {XLS}",
            }
        )

    readme_1999 = [
        ("hobart_1999_doy076_077", "1999-03-17/18", "19:22:22 -27:18 B1950", "Y-drive off 22:12-22:19 UT"),
        ("hobart_1999_doy077", "1999-03-18", "19:25:12 -27:18 B1950", "correlator disk full"),
        ("hobart_1999_doy079_080", "1999-03-20/21", "19:25:12 -27:18 B1950", "02-03UT data lost"),
        ("hobart_1999_doy081_082", "1999-03-22/23", "19:22:22 -26:48 B1950 (command mislabelled)", "~1.5 kHz Doppler error"),
        ("hobart_1999_doy091_092", "1999-04-01/02", "19:25:12 -26:48 B1950", "ACT crash"),
        ("hobart_1999_doy099_100", "1999-04-09/10", "19:25:12 -26:48 B1950", "none noted"),
    ]
    for sid, date, pos, incident in readme_1999:
        rows.append(
            {
                "session_id": sid,
                "date_utc": date,
                "start_time_utc": "README_DOY_window",
                "end_time_utc": "UNKNOWN",
                "duration_first_to_last_spectrum_h": "README window",
                "target_names_su": pos,
                "field_identifier": "1999_grid (East/West-beam precursors)",
                "ra_j2000_commanded": "UNKNOWN (B1950 recorded)",
                "dec_j2000_commanded": pos.split()[1],
                "coordinate_epoch": "B1950 (DOCUMENTED)",
                "center_frequency_mhz": "UNKNOWN_in_file",
                "bandwidth_mhz": "UNKNOWN_in_file",
                "channel_count_pol1": "1024-lag ACF dumps",
                "dump_cadence_s": "UNKNOWN",
                "integration_time_s": "UNKNOWN",
                "calibration_state": "NOT_ESTABLISHED_IN_ARCHIVE",
                "file_provenance": "DONOR_SUPPLIED|RAW_OBSERVATIONAL(fit.gz)+DOCUMENTATION(README)",
                "rpfits_association": "NOT_APPLICABLE",
                "spectrum_association": "data/w*.fit.gz sequences",
                "pointing_association": "top-level README",
                "scanlog_association": "none archived",
                "source_locators": f"top-level README; incident: {incident}",
            }
        )

    out = BASE / "extracted" / "HOBART_SESSION_MASTER_TABLE.csv"
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"[master] wrote {len(rows)} rows -> {out}")
    print(f"[master] bandwidth check sample: "
          f"{rows[0]['session_id']}: {rows[0]['bandwidth_mhz']} MHz, "
          f"{rows[0]['channel_count_pol1']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
