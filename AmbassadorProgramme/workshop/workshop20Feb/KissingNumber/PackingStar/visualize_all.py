"""
Generate all 8 visualizations from PackingStar data.
Outputs saved to ./viz/ folder.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('viz', exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.bbox': 'tight', 'font.size': 11})


# ── VIZ 1: Cosine-value distribution (histogram) ──
print("=== VIZ 1: Cosine-value distribution ===")
cos12 = np.load('New generalized kissing configurations/cosine_1:4/12D/12D_81_cosmat.npy')
cos13 = np.load('13D_rational_configurations/13D_rational_configurations/13D-1146-cosmatrix.npy')

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, mat, title in [
    (axes[0], cos12, '12D (81 spheres, cos≤1/4)'),
    (axes[1], cos13, '13D rational (1146 spheres, cos≤1/2)')
]:
    mask = ~np.eye(mat.shape[0], dtype=bool)
    vals = mat[mask]
    unique, counts = np.unique(np.round(vals, 4), return_counts=True)
    ax.bar(unique, counts, width=0.02, color='#e94560', edgecolor='white', linewidth=0.3)
    ax.set_xlabel('Cosine value')
    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.text(0.02, 0.95, f'{len(unique)} distinct values',
            transform=ax.transAxes, fontsize=10, va='top',
            bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.8))

fig.suptitle('VIZ 1: Cosine-value Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/01_cosine_distribution.png')
plt.close()
print("  Saved viz/01_cosine_distribution.png")


# ── VIZ 2: Gram matrix heatmap ──
print("=== VIZ 2: Gram matrix heatmap ===")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]
im = ax.imshow(cos12, cmap='coolwarm', vmin=-0.5, vmax=0.5, aspect='equal')
ax.set_title('12D (81 spheres, cos≤1/4)')
ax.set_xlabel('Sphere index')
ax.set_ylabel('Sphere index')
plt.colorbar(im, ax=ax, shrink=0.8, label='Cosine')

ax = axes[1]
im = ax.imshow(cos13[:200, :200], cmap='coolwarm', vmin=-0.5, vmax=0.5, aspect='equal')
ax.set_title('13D rational (first 200×200 of 1146)')
ax.set_xlabel('Sphere index')
ax.set_ylabel('Sphere index')
plt.colorbar(im, ax=ax, shrink=0.8, label='Cosine')

fig.suptitle('VIZ 2: Gram Matrix Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/02_gram_heatmap.png')
plt.close()
print("  Saved viz/02_gram_heatmap.png")


# ── VIZ 3: Eigenvalue spectrum ──
print("=== VIZ 3: Eigenvalue spectrum ===")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, mat, title, expected_dim in [
    (axes[0], cos12, '12D (81 spheres)', 12),
    (axes[1], cos13, '13D rational (1146 spheres)', 13)
]:
    eigvals = np.sort(np.linalg.eigvalsh(mat))[::-1]
    ax.bar(range(len(eigvals)), eigvals, color='#4d96ff', width=1.0)
    ax.axhline(y=0, color='red', linestyle='--', linewidth=0.8)
    ax.set_xlabel('Eigenvalue index')
    ax.set_ylabel('Eigenvalue')
    ax.set_title(title)
    rank = np.sum(np.abs(eigvals) > 1e-6)
    ax.text(0.6, 0.9, f'Rank = {rank}\n(expected ≤ {expected_dim})',
            transform=ax.transAxes, fontsize=10, va='top',
            bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.8))

fig.suptitle('VIZ 3: Eigenvalue Spectrum of Gram Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/03_eigenvalue_spectrum.png')
plt.close()
print("  Saved viz/03_eigenvalue_spectrum.png")


# ── VIZ 4: PCA 3D projection ──
print("=== VIZ 4: PCA 3D projection ===")
coord17 = np.load('New generalized kissing configurations/cosine_1:3/17D/17D_578_coordinates.npy')
norms = np.linalg.norm(coord17, axis=1, keepdims=True)
coord17_n = coord17 / norms

from numpy.linalg import svd
U, S, Vt = svd(coord17_n, full_matrices=False)
proj3 = coord17_n @ Vt[:3].T

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(proj3[:, 0], proj3[:, 1], proj3[:, 2],
                c=proj3[:, 2], cmap='viridis', s=8, alpha=0.7)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.set_title('17D → 3D PCA projection (578 spheres, cos≤1/3)')
plt.colorbar(sc, ax=ax, shrink=0.6, label='PC3 value')
fig.suptitle('VIZ 4: PCA 3D Projection of Sphere Centres', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/04_pca_projection.png')
plt.close()
print("  Saved viz/04_pca_projection.png")


# ── VIZ 5: Contact graph ──
print("=== VIZ 5: Contact graph ===")
try:
    import networkx as nx
    HAS_NX = True
except ImportError:
    HAS_NX = False
    print("  networkx not installed, using adjacency matrix visualization instead")

threshold = 0.25
adj = (np.abs(cos12 - threshold) < 1e-4).astype(int)
np.fill_diagonal(adj, 0)

if HAS_NX:
    G = nx.from_numpy_array(adj)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    pos = nx.spring_layout(G, seed=42, k=0.5)
    degrees = dict(G.degree())
    node_color = [degrees[n] for n in G.nodes()]
    nx.draw_networkx(G, pos, ax=ax, node_size=60, node_color=node_color,
                     cmap='YlOrRd', with_labels=False, edge_color='gray',
                     width=0.3, alpha=0.8)
    ax.set_title(f'Contact graph (81 nodes, {G.number_of_edges()} edges)\nEdge = cosine exactly 1/4')

    ax = axes[1]
    deg_vals = list(degrees.values())
    ax.hist(deg_vals, bins=range(min(deg_vals), max(deg_vals)+2), color='#6bcb77',
            edgecolor='white', align='left')
    ax.set_xlabel('Degree (number of contacts)')
    ax.set_ylabel('Count')
    ax.set_title('Degree distribution')

    fig.suptitle('VIZ 5: Contact Graph (12D, 81 spheres)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('viz/05_contact_graph.png')
    plt.close()
else:
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(adj, cmap='Greys', aspect='equal')
    ax.set_title('Adjacency matrix (cos = 1/4 contacts)\n12D, 81 spheres')
    ax.set_xlabel('Sphere index')
    ax.set_ylabel('Sphere index')
    fig.suptitle('VIZ 5: Contact Adjacency Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('viz/05_contact_graph.png')
    plt.close()
print("  Saved viz/05_contact_graph.png")


# ── VIZ 6: Old vs new kissing numbers ──
print("=== VIZ 6: Old vs new bar chart ===")
dims = [25, 26, 27, 28, 29, 30, 31]
k_prev = [197048, 198512, 199976, 204368, 208344, 219216, 232874]
k_new =  [197056, 198550, 200044, 204520, 209496, 220440, 238350]
delta_k = [n - p for n, p in zip(k_new, k_prev)]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]
x = np.arange(len(dims))
w = 0.35
bars1 = ax.bar(x - w/2, k_prev, w, label='Previous best', color='#a0a0a0', edgecolor='white')
bars2 = ax.bar(x + w/2, k_new, w, label='PackingStar (new)', color='#e94560', edgecolor='white')
ax.set_xticks(x)
ax.set_xticklabels([f'{d}D' for d in dims])
ax.set_ylabel('Kissing number (lower bound)')
ax.set_title('Previous vs. PackingStar records')
ax.legend()
for bar, val in zip(bars2, k_new):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
            f'{val:,}', ha='center', va='bottom', fontsize=7, color='#e94560')

ax = axes[1]
colors = plt.cm.Reds(np.linspace(0.3, 0.9, len(dims)))
ax.bar([f'{d}D' for d in dims], delta_k, color=colors, edgecolor='white')
ax.set_ylabel('ΔK = K_new − K_prev')
ax.set_title('Improvement per dimension')
for i, v in enumerate(delta_k):
    ax.text(i, v + 50, f'+{v:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')

fig.suptitle('VIZ 6: Old vs. New Kissing Numbers (25D–31D)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/06_old_vs_new.png')
plt.close()
print("  Saved viz/06_old_vs_new.png")


# ── VIZ 7: Partitioned sub-structure ──
print("=== VIZ 7: Partitioned sub-structures ===")
d5 = np.load('25D-31D/partitioned_D5.npy')  # 40×5 int
e7 = np.load('25D-31D/partitioned_E7.npy')  # 126×7 float

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax, data, title, expected_tri in [
    (axes[0], d5, 'D5 partition (40 vectors in 5D)\n→ 12 triangles for 29D', 12),
    (axes[1], e7, 'E7 partition (126 vectors in 7D)\n→ 42 triangles for 31D', 42)
]:
    norms = np.linalg.norm(data.astype(float), axis=1, keepdims=True)
    data_n = data.astype(float) / norms
    cos_mat = data_n @ data_n.T

    edges = []
    for i in range(len(data_n)):
        for j in range(i+1, len(data_n)):
            if np.abs(cos_mat[i, j] - 0.5) < 1e-4:
                edges.append((i, j))

    if HAS_NX:
        G = nx.Graph()
        G.add_nodes_from(range(len(data_n)))
        G.add_edges_from(edges)

        triangles = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]
        node_tri_map = {}
        for idx, tri in enumerate(triangles):
            for node in tri:
                node_tri_map[node] = idx

        node_colors = [node_tri_map.get(n, -1) for n in G.nodes()]
        pos = nx.spring_layout(G, seed=42, k=0.8)
        nx.draw_networkx(G, pos, ax=ax, node_size=40, node_color=node_colors,
                         cmap='tab20', with_labels=False, edge_color='gray',
                         width=0.5, alpha=0.85)
        ax.set_title(f'{title}\n{len(triangles)} triangles found, {len(edges)} edges (cos=0.5)')
    else:
        ax.imshow(cos_mat, cmap='coolwarm', vmin=-0.5, vmax=1.0)
        ax.set_title(title)
        ax.set_xlabel('Vector index')
        ax.set_ylabel('Vector index')

fig.suptitle('VIZ 7: Partitioned Sub-structures (Building Blocks)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/07_partitioned_substructures.png')
plt.close()
print("  Saved viz/07_partitioned_substructures.png")


# ── VIZ 8: Rational 13D cosine analysis ──
print("=== VIZ 8: Rational 13D cosine analysis ===")
cos13_full = np.load('13D_rational_configurations/13D_rational_configurations/13D-1146-cosmatrix.npy')
mask = ~np.eye(cos13_full.shape[0], dtype=bool)
offdiag = cos13_full[mask]
offdiag_round = np.round(offdiag, 6)
unique_vals, counts = np.unique(offdiag_round, return_counts=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]
ax.barh(range(len(unique_vals)), counts, color='#4d96ff', edgecolor='white', height=0.6)
ax.set_yticks(range(len(unique_vals)))
from fractions import Fraction
labels = []
for v in unique_vals:
    try:
        f = Fraction(v).limit_denominator(100)
        labels.append(f'{f} ≈ {v:.4f}')
    except:
        labels.append(f'{v:.4f}')
ax.set_yticklabels(labels, fontsize=8)
ax.set_xlabel('Count')
ax.set_title(f'13D rational: {len(unique_vals)} distinct cosine values')

ax = axes[1]
small_block = cos13_full[:30, :30]
im = ax.imshow(small_block, cmap='coolwarm', vmin=-0.5, vmax=0.5)
ax.set_title('Top-left 30×30 of 13D Gram matrix')
ax.set_xlabel('Sphere index')
ax.set_ylabel('Sphere index')
plt.colorbar(im, ax=ax, shrink=0.8, label='Cosine (rational)')

fig.suptitle('VIZ 8: Rational Structure Analysis (13D, 1146 spheres)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('viz/08_rational_13D.png')
plt.close()
print("  Saved viz/08_rational_13D.png")

print("\n=== ALL 8 VISUALIZATIONS COMPLETE ===")
print("Files saved in ./viz/")
for f in sorted(os.listdir('viz')):
    print(f"  {f}")
