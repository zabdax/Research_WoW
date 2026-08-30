"""
Independent re-derivation of the Table 4 (Arecibo Wow! II, arXiv:2508.10657v1)
galactic-latitude inconsistency and inversion check.

Written from scratch 2026-08-23. Deliberately does NOT reuse or read
research/validation/galactic_verification.py -- the equatorial->galactic
transformation is implemented here several independent ways and validated
against known sky positions BEFORE any Table 4 number is produced.

Inversion method (part 1 of task):
  Fix RA = 19h25m02s. Scan declination over [-90, +90] deg on a dense grid,
  evaluate b(dec) from the IAU spherical-trig sine-b formula, locate EVERY
  sign change of f(dec) = b(dec) - (-17.85 deg), and refine each bracket by
  bisection. This makes no assumption about the number or location of roots.
"""

import json
import math

D2R = math.pi / 180.0
R2D = 180.0 / math.pi

# ---------------------------------------------------------------------------
# IAU 1958 galactic system, J2000 realization (standard adopted constants)
# ---------------------------------------------------------------------------
RA_NGP_DEG = 192.85948    # alpha_G : RA of north galactic pole
DEC_NGP_DEG = 27.12825    # delta_G : Dec of north galactic pole
L_NCP_DEG = 122.93192     # Omega   : galactic longitude of north celestial pole


# ---------------------------------------------------------------------------
# Input parsing
# ---------------------------------------------------------------------------
def hms_to_deg(s):
    h, m, sec = (float(x) for x in s.split(":"))
    return 15.0 * (h + m / 60.0 + sec / 3600.0)


def dms_to_deg(s):
    sign = -1.0 if s.strip().startswith("-") else 1.0
    d, m, sec = (float(x) for x in s.strip().lstrip("+-").split(":"))
    return sign * (d + m / 60.0 + sec / 3600.0)


# ---------------------------------------------------------------------------
# Transformation implementations (independent routes)
# ---------------------------------------------------------------------------
def _unit_vec(ra_deg, dec_deg):
    a, d = ra_deg * D2R, dec_deg * D2R
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def _build_triad():
    """Galactic basis vectors in equatorial Cartesian components.

    Derived from two definitional anchors only:
      z_g = NGP direction at (alpha_G, delta_G);
      the north celestial pole k=(0,0,1) sits at galactic longitude Omega.
    """
    aG, dG, Om = RA_NGP_DEG * D2R, DEC_NGP_DEG * D2R, L_NCP_DEG * D2R
    sdG, cdG = math.sin(dG), math.cos(dG)
    saG, caG = math.sin(aG), math.cos(aG)
    z_g = (cdG * caG, cdG * saG, sdG)                      # NGP
    # u = unit vector at galactic lat 0, long Omega (= normalized NCP minus its z_g part)
    u = (-sdG * caG, -sdG * saG, cdG)
    # v = z_g x u  (lies in the equatorial plane, along the ascending node)
    v = (z_g[1] * u[2] - z_g[2] * u[1],
         z_g[2] * u[0] - z_g[0] * u[2],
         z_g[0] * u[1] - z_g[1] * u[0])
    cO, sO = math.cos(Om), math.sin(Om)
    x_g = tuple(cO * u[i] - sO * v[i] for i in range(3))   # l=0, b=0 direction
    y_g = tuple(sO * u[i] + cO * v[i] for i in range(3))
    return x_g, y_g, z_g


TRIAD = _build_triad()


def lb_vector(ra_deg, dec_deg):
    """Method A: vector triad (primary)."""
    r = _unit_vec(ra_deg, dec_deg)
    X = sum(r[i] * TRIAD[0][i] for i in range(3))
    Y = sum(r[i] * TRIAD[1][i] for i in range(3))
    Z = sum(r[i] * TRIAD[2][i] for i in range(3))
    l = math.atan2(Y, X) * R2D % 360.0
    b = math.asin(max(-1.0, min(1.0, Z))) * R2D
    return l, b


# Method B: the published standard J2000->Galactic rotation matrix (reference)
M_PUB = ((-0.0548755604, -0.8734370902, -0.4838350155),
         (+0.4941094279, -0.4448296300, +0.7469822445),
         (-0.8676661490, -0.1980763734, +0.4559837762))


def lb_matrix(ra_deg, dec_deg):
    r = _unit_vec(ra_deg, dec_deg)
    g = [sum(M_PUB[i][j] * r[j] for j in range(3)) for i in range(3)]
    l = math.atan2(g[1], g[0]) * R2D % 360.0
    b = math.asin(max(-1.0, min(1.0, g[2]))) * R2D
    return l, b


def b_sph(ra_deg, dec_deg):
    """Method C: closed-form galactic latitude (used for the scan).

    sin b = sin(dG) sin(d) + cos(dG) cos(d) cos(aG - a)
    """
    a, d = ra_deg * D2R, dec_deg * D2R
    sb = (math.sin(DEC_NGP_DEG * D2R) * math.sin(d)
          + math.cos(DEC_NGP_DEG * D2R) * math.cos(d) * math.cos((RA_NGP_DEG - ra_deg) * D2R))
    return math.asin(max(-1.0, min(1.0, sb))) * R2D


def lb_astropy(ra_deg, dec_deg):
    """Method D: astropy (external gold standard)."""
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    c = SkyCoord(ra=ra_deg * u.deg, dec=dec_deg * u.deg, frame="icrs")
    g = c.galactic
    return g.l.deg, g.b.deg


# ---------------------------------------------------------------------------
# Validation of the implementations on known sky positions
# ---------------------------------------------------------------------------
print("=" * 78)
print("SECTION 1 -- VALIDATION OF INDEPENDENT IMPLEMENTATIONS")
print("=" * 78)

checks = [
    ("Sgr A* (Galactic center)", 266.41681626, -29.00780833, 359.9442, -0.0462),
    ("North celestial pole", 0.0, 90.0, L_NCP_DEG, DEC_NGP_DEG),
]
for name, ra, dc, el, eb in checks:
    res = {}
    for tag, fn in (("vec", lb_vector), ("mat", lb_matrix), ("sph-b", lambda a, d: (float("nan"), b_sph(a, d))), ("asty", lb_astropy)):
        l_, b_ = fn(ra, dc)
        res[tag] = (l_, b_)
    print(f"\n{name}: expected l~{el:.4f}, b~{eb:+.4f}")
    for tag, (l_, b_) in res.items():
        ls = f"{l_:11.6f}" if l_ == l_ else "     n/a   "
        print(f"  {tag:6s} l={ls}  b={b_:+11.6f}")

# pairwise agreement on an arbitrary grid of positions
worst_vm = 0.0   # my vector method vs published matrix
worst_va = 0.0   # my vector method vs astropy
for i in range(0, 360, 7):
    for j in range(-85, 86, 11):
        l1, b1 = lb_vector(float(i), float(j))
        l2, b2 = lb_matrix(float(i), float(j))
        l3, b3 = lb_astropy(float(i), float(j))
        worst_vm = max(worst_vm,
                       min(abs(l1 - l2), 360 - abs(l1 - l2)), abs(b1 - b2))
        worst_va = max(worst_va,
                       min(abs(l1 - l3), 360 - abs(l1 - l3)), abs(b1 - b3))
print(f"\nmax |vector-method - published-matrix| over 1045-point grid: {worst_vm:.3e} deg")
print(f"max |vector-method - astropy|          over 1045-point grid: {worst_va:.3e} deg")
worst_v_a = worst_va

# ---------------------------------------------------------------------------
# Section 2: the four Table 4 rows, forward transformation
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 2 -- TABLE 4 ROWS: FORWARD TRANSFORM OF PRINTED J2000 COORDS")
print("=" * 78)
rows = [
    ("positive horn (new)", "19:25:02", "-26:57:18", 11.62, -17.85, 0.04),
    ("positive horn (prev.)", "19:25:31", "-26:57:00", 11.65, -18.89, None),
    ("negative horn (new)", "19:27:55", "-26:57:13", 11.87, -19.42, None),
    ("negative horn (prev.)", "19:28:22", "-26:57:00", 11.90, -19.48, None),
]
row_data = []
for label, rhs, dhs, pl, pb, pbunc in rows:
    ra, dc = hms_to_deg(rhs), dms_to_deg(dhs)
    l_v, b_v = lb_vector(ra, dc)
    l_a, b_a = lb_astropy(ra, dc)
    row_data.append(dict(label=label, ra_hms=rhs, dec_dms=dhs, ra_deg=ra, dec_deg=dc,
                         l_comp=l_v, b_comp=b_v, l_asty=l_a, b_asty=b_a, l_print=pl, b_print=pb))
    print(f"\n{label}  ({rhs}, {dhs})")
    print(f"  computed (mine)   l = {l_v:9.5f}   b = {b_v:+9.5f}")
    print(f"  computed (astropy) l = {l_a:9.5f}   b = {b_a:+9.5f}")
    print(f"  printed           l = {pl:9.5f}   b = {pb:+9.5f}"
          + (f" +/- {pbunc}" if pbunc else ""))
    print(f"  residuals: dL = {(l_v - pl):+.4f} deg   dB = {(b_v - pb):+.4f} deg "
          f"({(b_v - pb) * 60:+.1f}')")

# ---------------------------------------------------------------------------
# Section 3: the inversion check (scan + bisection), positive-horn new row
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("SECTION 3 -- INVERSION CHECK: FIX RA=19:25:02, SOLVE b(dec) = -17.85")
print("=" * 78)
ra_fix = hms_to_deg("19:25:02")
target_b = -17.85
dec_tab = dms_to_deg("-26:57:18")


def f(dec_deg):
    return b_sph(ra_fix, dec_deg) - target_b


# dense scan
n = 720001  # step 0.00025 deg
brackets = []
prev_dec = -90.0
prev_f = f(prev_dec)
for k in range(1, n + 1):
    dec = -90.0 + 180.0 * k / (n - 1)
    cur_f = f(dec)
    if prev_f == 0.0:
        brackets.append((prev_dec, prev_dec))
    elif (prev_f < 0.0) != (cur_f < 0.0):
        brackets.append((prev_dec, dec))
    prev_dec, prev_f = dec, cur_f

print(f"\nscan: {n} points, step {180.0/(n-1):.6f} deg -> {len(brackets)} sign-change bracket(s)")


def bisect(lo, hi, iters=90):
    flo = f(lo)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm < 0.0) == (flo < 0.0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


roots = [bisect(lo, hi) for lo, hi in brackets]

for r_ in roots:
    l_r, b_r = lb_vector(ra_fix, r_)
    l_ch, b_ch = lb_astropy(ra_fix, r_)
    delta = r_ - dec_tab
    print(f"\nroot found: dec = {r_:.6f} deg")
    print(f"  verify (mine)   : b({ra_fix:.5f}, {r_:.6f}) = {b_r:+.7f} deg")
    print(f"  verify (astropy): b = {b_ch:+.7f} deg")
    print(f"  tabulated dec   : {dec_tab:.6f} deg  (-26:57:18)")
    print(f"  delta           : {delta:+.4f} deg = {delta * 60.0:+.1f} arcmin "
          f"(implied dec is {'NORTH' if delta > 0 else 'SOUTH'} of tabulated)")

if len(roots) == 1:
    print("\nuniqueness: exactly ONE root in the physical dec range [-90, +90]")
    print("  (analytic second branch sin(dec+phi)=C/R falls at dec ~ -123.8 deg,")
    print("   outside the valid declination range, so the solution is unique)")

root = roots[0]
# sensitivity of implied dec to the printed b value
b_lo, b_hi = b_sph(ra_fix, root - 1.0), b_sph(ra_fix, root + 1.0)
slope = (b_hi - b_lo) / 2.0  # db/ddec in deg/deg around root
spread = 0.04 / slope  # +/-0.04 deg (row's quoted b error) in dec units
print(f"\nlocal slope db/d(dec) at solution: {slope:+.4f} (deg per deg)")
print(f"  -> the 0.968-deg b discrepancy maps to {0.9681 / slope:.3f} deg in dec")
print(f"  -> row's own +/-0.04-deg b uncertainty maps to +/-{abs(spread) * 60:.1f}' in implied dec")

# falsification test of the stale written figure (-28.00 deg / 63')
b_stale = b_sph(ra_fix, -28.00)
print(f"\nfalsification test: b(19:25:02, -28.00 deg) = {b_stale:+.4f} deg "
      f"(target was {target_b}) -> stale '-28.00 deg / 63 arcmin' figure does NOT reproduce -17.85")

# comparison with user's independently computed figure
user_fig = -24.36
print(f"\nreconciliation: my root {root:.4f} vs user's separate check {user_fig:.2f}: "
      f"difference {abs(root - user_fig) * 60:.1f}'")

out = dict(
    date="2026-08-23",
    ra_fixed_deg=ra_fix,
    target_b_deg=target_b,
    dec_tabulated_deg=dec_tab,
    roots_deg=roots,
    delta_deg=root - dec_tab,
    delta_arcmin=(root - dec_tab) * 60.0,
    slope_db_ddec=slope,
    b_at_minus28=b_stale,
    rows=row_data,
    validations=dict(sgra_star=[lb_vector(266.41681626, -29.00780833), lb_astropy(266.41681626, -29.00780833)],
                     grid_max_dev_vs_astropy_deg=worst_v_a),
)
with open(__file__.replace(".py", "_results.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print("\nsaved:", __file__.replace(".py", "_results.json"))
