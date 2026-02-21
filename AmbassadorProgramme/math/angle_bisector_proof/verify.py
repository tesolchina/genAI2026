import math
import random

def verify(ac, bc, angle_C_deg, beta_deg):
    """
    Triangle with vertex C at origin, angle ACB = angle_C_deg.
    CF bisects angle C. CD, CE symmetric about CF with half-angle beta from CF.
    """
    angle_C = math.radians(angle_C_deg)
    alpha = angle_C / 2
    beta = math.radians(beta_deg)
    if beta >= alpha:
        return None

    cx, cy = 0, 0
    ax = ac * math.cos(angle_C / 2)
    ay = ac * math.sin(angle_C / 2)
    bx = bc * math.cos(angle_C / 2)
    by = -bc * math.sin(angle_C / 2)

    def line_intersect(p1, d1, p2, d2):
        det = d1[0]*d2[1] - d1[1]*d2[0]
        if abs(det) < 1e-15:
            return None
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        t = (dx*d2[1] - dy*d2[0]) / det
        return (p1[0]+t*d1[0], p1[1]+t*d1[1])

    ab_dir = (bx - ax, by - ay)

    cd_angle = beta
    cd_dir = (math.cos(cd_angle), math.sin(cd_angle))
    D = line_intersect((cx,cy), cd_dir, (ax,ay), ab_dir)

    ce_angle = -beta
    ce_dir = (math.cos(ce_angle), math.sin(ce_angle))
    E = line_intersect((cx,cy), ce_dir, (ax,ay), ab_dir)

    if D is None or E is None:
        return None

    t_d = (D[0]-ax)/ab_dir[0] if abs(ab_dir[0])>1e-12 else (D[1]-ay)/ab_dir[1]
    t_e = (E[0]-ax)/ab_dir[0] if abs(ab_dir[0])>1e-12 else (E[1]-ay)/ab_dir[1]
    if not (0 < t_d < 1 and 0 < t_e < 1):
        return None

    A = (ax, ay)
    B = (bx, by)
    C = (cx, cy)

    AD = math.dist(A, D)
    DB = math.dist(D, B)
    AE = math.dist(A, E)
    BE = math.dist(B, E)
    CD = math.dist(C, D)
    CE = math.dist(C, E)
    AC = math.dist(A, C)
    BC = math.dist(B, C)

    LHS = AC * BC
    RHS = math.sqrt(AD * DB * BE * AE) + CD * CE
    return {'LHS': LHS, 'RHS': RHS, 'diff': abs(LHS-RHS),
            'AC': AC, 'BC': BC, 'AD': AD, 'DB': DB, 'AE': AE, 'BE': BE, 'CD': CD, 'CE': CE}

print("=== Numerical Verification ===")
print("Proving: AC·BC = √(AD·DB·BE·EA) + CD·CE\n")

fixed_tests = [
    (5, 4, 60, 10, "AC=5,BC=4,C=60°,β=10°"),
    (3, 7, 80, 20, "AC=3,BC=7,C=80°,β=20°"),
    (6, 6, 90, 30, "AC=6,BC=6,C=90°,β=30°"),
    (4, 5, 40, 5,  "AC=4,BC=5,C=40°,β=5°"),
    (8, 3, 120, 40, "AC=8,BC=3,C=120°,β=40°"),
    (10, 10, 50, 20, "AC=10,BC=10,C=50°,β=20°"),
]

all_pass = True
for ac, bc, angC, beta, label in fixed_tests:
    r = verify(ac, bc, angC, beta)
    if r is None:
        print(f"{label}: SKIPPED")
        continue
    ok = r['diff'] < 1e-8
    if not ok: all_pass = False
    print(f"{label}: LHS={r['LHS']:.10f} RHS={r['RHS']:.10f} diff={r['diff']:.2e} [{'PASS' if ok else 'FAIL'}]")

print()
random.seed(123)
p, f = 0, 0
for _ in range(1000):
    ac = random.uniform(1, 20)
    bc = random.uniform(1, 20)
    angC = random.uniform(20, 160)
    alpha = angC / 2
    beta = random.uniform(0.5, alpha - 0.5)
    r = verify(ac, bc, angC, beta)
    if r is None: continue
    if r['diff'] < 1e-6: p += 1
    else:
        f += 1
        if f <= 5:
            print(f"  FAIL: ac={ac:.2f} bc={bc:.2f} C={angC:.1f} β={beta:.1f} diff={r['diff']:.2e}")

print(f"Random: {p} pass, {f} fail / {p+f} valid")
print(f"\n{'ALL VERIFIED' if all_pass and f==0 else 'ISSUES FOUND'}")
