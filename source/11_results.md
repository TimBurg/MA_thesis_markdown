
# Results

<!--As mentioned before there is a fundamental challenge in the surface interpolation with radial basis functions that is due to the fact that the surface is given implicitly by the zero-level of the 3-dimensional interpolant. Since the interpolant is only guaranteed to have a zero crossing at the interpolation points and not in between them, the surface can be non-contiguous. More precisely there is no topological guarantee for a manifold surface over a cluster of islands.-->

<!--Sevel parameters influcence that situation. Those being:-->

<!--* the spacing and values of the offset points and if they are uniform or not-->
<!--* the scale-factor(s) of the radial-basis-functions and if they are uniform or not-->

<!--To assess the acceptance of different parameter-combinations in that regard I conducted a parameter-survey. The aim was to have a general heuristic for an always working or at least 'as good as it gets' parameter set for the following remeshings.-->

<!--As a essential feature the values of the RBF-interpolant along an outward line through the triangle-centroids were probed for:-->
<!--a) the existence of a zero-crossing (mandatory)-->
<!--b) the witdh between minima and maxima adjacent to the zero crossing (convergence area of the projection)-->


<!--![At the vertices of the mesh in between the offset interpolation points the RBF-interpolant is well behaved.-->
<!--The offset interpolation points are located at $\pm$ 0.78 in units of the actual mesh  \label{my_label}](source/figures/vertex_normal_plot.png){ width=100% }-->

## The topology optimization models
The implementations for the following calculations were provided by Moritz Ebeling-Rump from the Weierstraß Institute.
They are computed using the pdelib library developed at the Weiserstraß Institute and contain contributions from multiple authors.
The parameters $\gamma$ and $\varepsilon$ as well as the lamé-coefficients were set according to [@ebeling-rump_topology_2019].

For reference the models were calculated with the lamé-coefficients set to that of the 3d-printing plastic PLA:
$$\lambda = 1599e^6 \quad \mu = 685e^6$$

And the parameters for the Ginzburg-Landau term were set to:
$\gamma = 6.25e^{-5}$ $\epsilon = 0.00175$ $\tau = 0.01$


### The bridge
The bride model posesses an x-y mirror symmetry and has a force square on top, visible in figure \ref{fig:bridge_grid}.
The force square with a Neumann load is visible as the green square on the top of the domain in the first picture.
The symmetry is imposed by a homogeneous dirichlet condition in the x direction on the orange and in the y-direction on the green part of the domain
also visible in the first picture.
The second picture shows the dirichlet clamp on the bottom (in blue) where x and y movements are penalized.

The dimensions of the domain are 5cm in the x-direction, 1.5cm in the y-direction and 2cm in the z-direction.
The force square has a size of 1 by 1 cm and a load density of 2400 N/m² in the z-direction resulting in a total load of 0.24N or approximately 24g.

The model was calculated using 294231 tetrahedra.

After 60 iterations the mesh in [@fig:bridge_raw] was extracted.
In the closeup [@fig:closeup_bridge] the it can be seen that the triangle size and shape is very unregular.

![](./source/figures/bridge_grid_front.png){width=50%}
![](./source/figures/bridge_grid_back.png){width=50%}
\begin{figure}[!h]
\caption{The grid for the bridge model from the front and the back}
\label{fig:bridge_grid}
\end{figure}

Subsequently the mesh was mirrored at the symmetry axes and merged into one stl model.

![Isosurface of the bridge model after extraction](./source/figures/bridge_solo_raw.png){#fig:bridge_raw width=90%}

![Closeup of the bridges isosurface](./source/figures/closeup_bridge.png){#fig:closeup_bridge width=90%}

![Bridge model after accounting for the mirror symmetry](./source/figures/bridge_raw.png)

![After remeshing with $l^{6d} =$2x longest edge and doing 10 iterations](./source/figures/bridge_with_zoom2.png)

### The table
The table model has a large force rectangle with non-homogeneous neumann conditions on top and 4 x-y sliding dirichlet conditions on the bottom.
The rest of the boundary has a homogeneous Neumann condition.

The domain has size 9.6cm(x) by 2.8cm(y) by 2cm(z) and the force square is 8 x 2cm with a force density of 2400 N/m² resulting in a load of 384g.

The model was calculated with 1120591 tetrahedra and ran for 60 iterations.

![](./source/figures/tisch3d_grid_bottom.png){width=50%}
![](./source/figures/tisch3d_grid_top.png){width=50%}
\begin{figure}[!h]
\caption{The table model with a large force rectangle on the top and 4 x-y sliding dirichlet conditions on the bottom}
\label{fig:table_grid}
\end{figure}


![The extracted table isosurface](./source/figures/tisch_raw.png){#fig:tisch_raw}

### The tower

<div id="fig:tower_grid">
![From the bottom](./source/figures/turm_bottom_grid.png){width=50%}
![From the top](./source/figures/turm_top_grid.png){width=50%}\

The grid for the tower model.
</div>


## Analysis of the results and problem 

- The unstructured graph datastructure scaled very poorly to larger meshes ie. excessive cache misses yielded a poor performance.
  This is a fundamental problem for pliant remeshing and may be adressed with good datastructures that preserve neighborhood to some degree. 
- fitting with RBFs would have been more appropiate to incorporate the smoothing and reduce the number of RBFs.
  However, projections might not work so well without offset constraints.
- 6d flips work poorly for refinement due to mesh normals being a limited indicator of mesh accuracy -> some long edges remain due to equal normals.
- surface interpolation works well and projections were fast and reliable.

Immediate requirement for a practicable method: faster datastructure and mesh fitting.
