# PackingStar — What it does and what we can visualize

## What this repository contains

This is the data repository for [PackingStar](https://arxiv.org/abs/2511.13391), a multi-agent reinforcement learning system that discovers new kissing number configurations. The repo does **not** contain the training code or the AI system itself — only the **results** (sphere configurations) and **verification scripts**.

### Data files

| Folder | Contents | Format |
|---|---|---|
| `25D-31D/` | New record-breaking configurations in dimensions 25–31 | Coordinate vectors (`.npy`, shape `N × D`) |
| `13D_rational_configurations/` | Improved rational constructions in 13D (1146 spheres, surpassing the 1971 record of 1130) | Gram/cosine matrices (`.npy`, shape `N × N`) |
| `12D_14D_15D/` | Diverse configuration families in 12D, 14D, 15D | Gram/cosine matrices |
| `New generalized kissing configurations/` | Records under tighter angular constraints (cosine ≤ 1/3, 1/4, 1/5) | Gram/cosine matrices + some coordinate files |
| `25D-31D/partitioned_D5.npy` | Partitioned 5D kissing config (40 vectors, integer), used to build 29D record | Integer vectors (40 × 5) |
| `25D-31D/partitioned_E7.npy` | Partitioned 7D kissing config (126 vectors), used to build 31D record | Float vectors (126 × 7) |

### Two data representations

1. **Coordinate files** (`_coordinates.npy`): Each row is a unit vector in R^D — the centre of a surrounding sphere. Shape: `(N, D)` where N = number of spheres, D = dimension.
2. **Cosine/Gram matrix files** (`_cosmatrix.npy` or `_cosmat.npy`): An `N × N` symmetric matrix where entry (i,j) is the cosine of the angle between sphere centres i and j. Diagonal = 1.0; off-diagonal ≤ threshold (0.5 for standard kissing, or 1/3, 1/4, 1/5 for generalised).

### Verification scripts

- **`verify_coordinates.py`** — Takes a coordinate file; normalises vectors; checks all pairwise cosines ≤ threshold; reports the set of distinct cosine values found.
- **`verify_cosmatrix.py`** — Takes a Gram matrix file; checks diagonal = 1, off-diagonal ≤ threshold, positive semi-definiteness, and matrix rank (should ≤ dimension).

### Key image

- **`results_all.png`** — Summary chart of all new lower bounds vs. previous records across dimensions.

---

## What visualizations can be done

### 1. Cosine-value distribution (histogram / bar chart)
**Data:** Any cosine matrix file.  
**What it shows:** The distribution of pairwise cosine values between all sphere pairs. PackingStar's configurations often converge to a small, clean set of cosine values (e.g., the 12D config under 1/4 constraint has only 3 distinct off-diagonal values: {−0.5, 0.0, 0.25}). This reveals the hidden algebraic regularity the AI discovers.  
**How:** Load `.npy`, mask the diagonal, plot `plt.hist()` or `np.unique()` with counts as a bar chart.

### 2. Gram matrix heatmap
**Data:** Any cosine matrix file.  
**What it shows:** The N × N cosine matrix as a colour map. Block-diagonal or banded patterns reveal the internal sub-structure (fragments, symmetry groups). Reordering rows/columns by clustering can make hidden structure more visible.  
**How:** `plt.imshow(cosmatrix, cmap='coolwarm', vmin=-0.5, vmax=0.5)`.

### 3. Eigenvalue spectrum of the Gram matrix
**Data:** Any cosine matrix file.  
**What it shows:** The eigenvalues of the Gram matrix. The rank equals the dimension of the embedding space, so most eigenvalues should be zero or near-zero. The non-zero eigenvalue distribution reveals the geometric "shape" of the configuration. Comparing spectra across dimensions or between old and new configurations shows how PackingStar's solutions differ structurally.  
**How:** `np.linalg.eigvalsh(cosmatrix)`, plot sorted eigenvalues.

### 4. 2D/3D projection of sphere centres (PCA or t-SNE)
**Data:** Coordinate files (25D–31D, or 17D generalised).  
**What it shows:** A low-dimensional projection of the high-dimensional sphere arrangement. While it loses geometric accuracy, it gives an intuitive sense of clustering, symmetry, and density. PCA preserves global structure; t-SNE preserves local neighbourhoods.  
**How:** `sklearn.decomposition.PCA(n_components=3)` on the coordinate array, then 3D scatter plot.

### 5. Contact graph / adjacency network
**Data:** Any cosine matrix file.  
**What it shows:** A graph where each sphere is a node, and an edge connects two spheres whose cosine equals the maximum allowed value (i.e., they are "touching" or at minimum separation). The graph structure reveals the combinatorial skeleton of the packing — degree distribution, cliques, community structure.  
**How:** Threshold the cosine matrix to build an adjacency matrix; visualise with `networkx` or `igraph`.

### 6. Comparison bar chart: old vs. new kissing numbers
**Data:** Table from the paper + `results_all.png`.  
**What it shows:** Side-by-side bars for previous best known lower bound vs. PackingStar's new lower bound in each dimension. The increment ΔK highlights the scale of improvement.  
**How:** Simple grouped bar chart from manually entered data.

### 7. Partitioned sub-structure visualisation (29D, 31D)
**Data:** `partitioned_D5.npy` (40 × 5, integer) and `partitioned_E7.npy` (126 × 7).  
**What it shows:** These are the lower-dimensional "building blocks" that PackingStar assembles into the 29D and 31D records. The 31D solution partitions a 7D kissing configuration into 42 disjoint equilateral triangles. Visualising these triangles as a graph or coloured partition shows the novel assembly pattern.  
**How:** Compute pairwise distances within the partition; identify the 42 (or 12) triangles; colour-code or display as a graph with triangle-edges highlighted.

### 8. Rational vs. non-rational structure comparison (13D)
**Data:** `13D_rational_configurations/`.  
**What it shows:** The rational 13D configurations (1146 spheres) can be compared to earlier structures. Since all cosine values are rational, a table or heatmap of the exact fractional cosine values is possible — something unique to this data.  
**How:** Load the Gram matrix; display as a fraction grid using `fractions.Fraction` for exact rational display, or heatmap with rational tick labels.

---

## Quick-start: run verification

```bash
pip install numpy
# Unzip a configuration
unzip ./25D-31D/25D-31D_new_bounds_configurations.zip -d ./25D-31D/
# Verify a 25D configuration
python verify_coordinates.py --file-path ./25D-31D/25D-31D_new_bounds_configurations/25D_197056_coordinates.npy --threshold 0.5
```

## Dependencies for visualisation

```
numpy
matplotlib
seaborn          # heatmaps
scikit-learn     # PCA / t-SNE
networkx         # contact graphs
```
