
# Results

As mentioned before there is a fundamental challenge in the surface interpolation with radial basis functions that is due to the fact that the surface is given implicitly by the zero-level of the 3-dimensional interpolant. Since the interpolant is only guaranteed to have a zero crossing at the interpolation points and not in between them, the surface can be non-contiguous. More precisely there is no topological guarantee for a manifold surface over a cluster of islands.

Sevel parameters influcence that situation. Those being:

* the spacing and values of the offset points and if they are uniform or not
* the scale-factor(s) of the radial-basis-functions and if they are uniform or not

To assess the acceptance of different parameter-combinations in that regard I conducted a parameter-survey. The aim was to have a general heuristic for an always working or at least 'as good as it gets' parameter set for the following remeshings.

As a essential feature the values of the RBF-interpolant along an outward line through the triangle-centroids were probed for:
a) the existence of a zero-crossing (mandatory)
b) the witdh between minima and maxima adjacent to the zero crossing (convergence area of the projection)


![At the vertices of the mesh in between the offset interpolation points the RBF-interpolant is well behaved.
The offset interpolation points are located at $\pm$ 0.78 in units of the actual mesh  \label{my_label}](source/figures/vertex_normal_plot.png){ width=100% }

## The topology optimization models


### The bridge

![The boundary conditions of the bridge model](./source/figures/bridge_grid.png)

![Isosurface of bridge after extraction](./source/figures/bridge_raw.png)

![After remeshing with $l^{6d} =$2x longest edge and doing 10 iterations](./source/figures/bridge_remeshed.png)

- parameters: gamma, eps
- domain description and boundary conditions
- how many tetrahedra

### The table
![The boundary conditions of the bridge model](./source/figures/tisch3d_grid_bottom.png)
![The boundary conditions of the bridge model](./source/figures/tisch3d_grid_top.png)

### The tower
<!--![The boundary conditions of the bridge model](./source/figures/bridge_grid.png)-->

## Analysis of the results and problem 
