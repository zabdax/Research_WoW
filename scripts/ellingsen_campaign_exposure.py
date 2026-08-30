"""Build research/sources/ellingsen_hobart/extracted/campaign_exposure.csv.

Aggregates the per-spectrum header index (analysis/spectrum_header_index.csv)
into one row per observing session/container. Every field is either directly
established from the harvested headers/donor documentation or explicitly set to
UNKNOWN / NOT_APPLICABLE / NOT_RECOVERABLE. No sensitivity, threshold, or RFI
values are invented.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE = REPO_ROOT / "research" / "sources" / "ellingsen_hobart"

FIELDS = [
    "campaign", "session", "date", "start_time", "end_time", "usable_duration",
    "pointing_ra", "pointing_dec", "frequency_start", "frequency_end",
    "bandwidth", "channel_count", "spectral_resolution", "polarization",
    "scan_id", "data_product", "rfi_status", "calibration_status",
    "sensitivity_status", "detection_threshold", "provenance", "uncertainty",
    "source_file",
]


def clean(v: str | None) -> str:
    return re.sub(r"[\s#]+$", "", v or "").strip()


def parse_time(v: str):
    v = clean(v)
    m = re.match(r"^(\d{4})/(\d{2})/(\d{2})/(\d{2}):(\d{2}):(\d{2})$", v)
    if not m:
        return None
    return datetime(*map(int, m.groups()))


def session_label(container: str, name_counts: dict) -> tuple[str, str]:
    """Return (campaign, session) for a container path."""
    if "spectra.tar.gz" in container:
        return ("SKIP_DUP", "")  # duplicate packaging of loose 2010obs
    if "/2010obs/" in container:
        return ("2010_followup", "2010-08-16_ut0930-1542")
    m = re.search(r"(wow_\w+_\d{4}doy\d+)", container.replace("\\", "/"))
    tag = m.group(1) if m else Path(container).stem
    year = tag.split("_")[-1][:4]
    if "test" in tag:
        return (f"{year}_tests", tag)
    return (f"{year}_followup", tag)


def main() -> int:
    rows_by_session: dict[tuple[str, str], dict] = defaultdict(
        lambda: {
            "times": [], "pos": set(), "res": set(), "chan": set(),
            "n": 0, "names": defaultdict(int),
        }
    )
    with open(BASE / "analysis" / "spectrum_header_index.csv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            container = r["container"] or r["origin"].split("::")[0]
            camp, sess = session_label(container, {})
            if camp == "SKIP_DUP":
                continue
            a = rows_by_session[(camp, sess)]
            t = parse_time(r.get("Time"))
            if t:
                a["times"].append(t)
            p = clean(r.get("Position"))
            if p:
                a["pos"].add(p)
            wcs = clean(r.get("WCS")).split()
            if len(wcs) >= 4:
                a["res"].add(wcs[3])
                a["chan"].add(wcs[2])
            a["n"] += 1
            nm = clean(r.get("Name"))
            if nm:
                a["names"][nm] += 1

    out_rows = []
    for (camp, sess), a in sorted(rows_by_session.items()):
        times = sorted(a["times"])
        dates = sorted({t.strftime("%Y-%m-%d") for t in times})
        span = (times[-1] - times[0]).total_seconds() / 3600 if len(times) >= 2 else None
        pos = sorted(a["pos"])
        on_pos = [p for p in pos if "-26." in p or "-26:" in p]
        off_pos = [p for p in pos if p not in on_pos]
        res = "/".join(sorted(a["res"])) + " kHz"
        chans = "/".join(sorted(a["chan"]))
        bw_mhz = sorted({float(r) * 2048 / 1000 for r in a["res"]})
        names = ", ".join(f"{k} x{v}" for k, v in sorted(a["names"].items()))
        out_rows.append(
            {
                "campaign": camp,
                "session": sess,
                "date": "; ".join(dates) if dates else "UNKNOWN",
                "start_time": times[0].strftime("%Y-%m-%dT%H:%M:%SZ") if times else "UNKNOWN",
                "end_time": times[-1].strftime("%Y-%m-%dT%H:%M:%SZ") if times else "UNKNOWN",
                "usable_duration": f"{span:.3f}_h_span_first_to_last_spectrum" if span else "UNKNOWN",
                "pointing_ra": "; ".join(on_pos) if on_pos else "UNKNOWN",
                "pointing_dec": "",
                "frequency_start": "TOPO_axis_see_header_index",
                "frequency_end": "TOPO_axis_see_header_index",
                "bandwidth": f"{bw_mhz[0]:g}_MHz_per_2048ch" if len(bw_mhz) == 1 else "MIXED:" + "/".join(f"{b:g}" for b in bw_mhz) + "_MHz",
                "channel_count": chans or "UNKNOWN",
                "spectral_resolution": res,
                "polarization": "linear_pol1_pol2",
                "scan_id": "per_file_names_in_index",
                "data_product": f"ASAP_ASCII_spectra_n={a['n']} ({names})",
                "rfi_status": "UNKNOWN",
                "calibration_status": (
                    "DOCUMENTED_2010_CAL_3C348_SEFD450/433Jy_CAL49.4/53.7Jy_FWHM34-37arcmin"
                    if camp.startswith("2010")
                    else "NOT_ESTABLISHED_IN_ARCHIVE_fixtsys_Tsys500K_normalization_no_Jy_chain_documented"
                ),
                "sensitivity_status": "UNKNOWN",
                "detection_threshold": "UNKNOWN",
                "provenance": "DONOR_SUPPLIED|PROCESSED_OBSERVATION",
                "uncertainty": (
                    "header_Time_is_first_row_of_dump_not_integration_midpoint; "
                    "antenna_drive_freeze_12:54-13:25UT_documented_for_2010"
                    if camp.startswith("2010")
                    else "header_Time_is_first_row_of_dump_not_integration_midpoint"
                ),
                "source_file": sess,
            }
        )

    # ---- documented 1998/99 correlator-era sessions (top-level README) ------
    readme_1999 = [
        # (session, date(s), position B1950, onsource window, overhead, notes)
        ("1999_doy076_077", "1999-03-17/18", "19 22 22 -27 18 00", "076-14:54:05 to 077-05:04:00", "-/077-05:10:00",
         "offsource 22:12-22:19UT Y-drive left off during maintenance"),
        ("1999_doy077", "1999-03-18", "19 25 12 -27 18 00", "077-15:02:13 to 077-23:? ", "077-15:00:00/-",
         "correlator disk full; antenna onsource to end"),
        ("1999_doy079_080", "1999-03-20/21", "19 25 12 -27 18 00", "079-15:02:09 to 080-04:50:00", "079-15:00:00/080-04:52:20",
         "02-03UT concatenation error; original deleted -> data lost"),
        ("1999_doy081_082", "1999-03-22/23", "19 22 22 -26 48 00 (correlator command mislabelled 19 25 12 -27 18 00)", "081-14:40:07? to 082-04:43:00", "081-14:30:00/082-04:46:00",
         "~1.5kHz Doppler error from wrong commanded position"),
        ("1999_doy091_092", "1999-04-01/02", "19 25 12 -26 48 00", "091-13:56:10 to 091-23:00:00?", "091-13:53:51/-",
         "ACT crashed; end time uncertain"),
        ("1999_doy099_100", "1999-04-09/10", "19 25 12 -26 48 00", "099-13:27:07 to 100-03:40:00", "099-13:22:48/100-03:42:23",
         "no known problems"),
    ]
    for sess, date, posb1950, onsrc, overhead, notes in readme_1999:
        out_rows.append(
            {
                "campaign": "1998-99_correlator_era",
                "session": sess,
                "date": date,
                "start_time": onsrc,
                "end_time": "see_start_field_format_DOY-UT",
                "usable_duration": f"overhead:{overhead}; {notes}",
                "pointing_ra": posb1950.split()[0] + "_(B1950)",
                "pointing_dec": posb1950.split()[1] + "_(B1950)",
                "frequency_start": "UNKNOWN_in_file",
                "frequency_end": "UNKNOWN_in_file",
                "bandwidth": "UNKNOWN_in_file",
                "channel_count": "1024_lag_ACF_dumps_per_extension",
                "spectral_resolution": "NOT_RECOVERABLE_without_correlator_config",
                "polarization": "UNKNOWN_in_file",
                "scan_id": "wYYDOYNNN.fit.gz_sequence",
                "data_product": "UTAS_correlator_ACF_FITS_gz",
                "rfi_status": "UNKNOWN",
                "calibration_status": "UNKNOWN_in_archive",
                "sensitivity_status": "UNKNOWN",
                "detection_threshold": "UNKNOWN",
                "provenance": "DONOR_SUPPLIED|RAW_OBSERVATIONAL|DOCUMENTED_SESSION_NOTES",
                "uncertainty": notes,
                "source_file": "original/...-001/README + data/w*.fit.gz",
            }
        )

    out = BASE / "extracted" / "campaign_exposure.csv"
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out_rows)
    print(f"[exposure] wrote {len(out_rows)} session rows -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
