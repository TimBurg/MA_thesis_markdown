
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
They are computed using the pdelib library developed at the Weierstraß Institute and contain contributions from multiple authors.
The parameters $\gamma$ and $\varepsilon$ as well as the Lamé-coefficients were set according to [@ebeling-rump_topology_2019].

For reference, the models were calculated with the Lamé-coefficients set to those of the 3d-printing plastic PLA:
$$\lambda = 1599 \cdot 10^6 \quad \mu = 685 \cdot 10^6$$


For the calculations the gravitational volume force was set to zero since it had no visible influence for the small sized structures 
that were calculated.
The time stepping parameter $\tau$ was generally set to $\tau = 0.01$.

### The bridge
The mesh for the bridge model posesses an x-y mirror symmetry and has a force square on top. 
The force square with a Neumann load is depicted as the green square on the top of the domain in [@fig:bridge_gridA].
The symmetry is imposed by a homogeneous Dirichlet condition in the x direction on the orange and in the y-direction on the green part of the domain
also visible in the first picture.
[@fig:bridge_gridB] shows the Dirichlet clamp on the bottom (in blue) where x and y displacements are penalized.


The dimensions of the domain are 5cm in the x-direction, 1.5cm in the y-direction and 2cm in the z-direction.
The force square has a size of 1cm by 1cm and a load density of 2400 N/m² in the z-direction resulting in a total load of 0.24N or approximately 24g.

The model was calculated using 294231 tetrahedra
with the parameters for the Ginzburg-Landau term set to:
$\gamma = 6.25\cdot 10^{-5}$ and $\epsilon = 0.00175$ 


<!--$\gamma = 6.25e^{-5}$ and $\epsilon = 0.00175$ -->



<div id="fig:bridge_grid">
![](./source/figures/bridge_grid1.png){#fig:bridge_gridA width=50%}
![](./source/figures/bridge_grid3.png){#fig:bridge_gridB width=50%}

The mesh for the bridge model from the top-front and the bottom-back.
</div>

After 60 iterations the mesh in [@fig:bridge_raw] was extracted.
In the closeup [@fig:closeup_bridge] the it can be seen that the triangle size and shape is very unregular and not curvature adapted.

![Isosurface of the bridge model after extraction. The Dirichlet clamp is located on the bottom right part](./source/figures/bridge_solo_raw.png){#fig:bridge_raw width=90%}

![Closeup of the bridges isosurface. Some irregularities can be made out and the use of triangles is inefficient.](./source/figures/closeup_bridge.png){#fig:closeup_bridge width=90%}

Subsequently the mesh was mirrored at the symmetry axes and merged into one stl model visible in [@fig:bridge_merged].

![Bridge model after accounting for the mirror symmetry](./source/figures/bridge_raw.png){#fig:bridge_merged}

The mesh was remeshed with 10 iterations and the target edge length set to
two times the longest edgelength of the original mesh.
The embedding parameter $\sigma$ was automatically set to the value of $\sigma=1.28$.
The low value is due to the fact that the domain dimensions are expressed in meters and are therefor very small.
The sparse interpolation matrix that resulted had a size of 128628 x 128628 with 58 million values in the case of an RBF scale factor of 2.5 times
the longest edge length (of the input mesh) and 20 million values when set to 1.5 (of the longest edge length).
Consequently the evaluation of the interpolant was slow and the remeshing took over 12 hours.
The remeshed mesh is shown in [@fig:bridge_remeshed] where the chosen target edge length
 is reflected in the triangle sizes of the flat areas.

![After remeshing with $l^{6d} =$ 2x longest edge and doing 10 iterations](./source/figures/bridge_with_zoom2.png){#fig:bridge_remeshed}

![Closeup of the remeshed bridge](./source/figures/bridge_closeup.png){#fig:bridge_closeup}


### The table
The table domain has a large force rectangle with a non-homogeneous Neumann condition on top and 4 Dirichlet conditions on the bottom.
On the Dirichlet part only the z-direction was penalized(clamped) which results in the inclusion of x-y support structures.
This is called a sliding condition.

The domain is sizeed 9.6cm(x) by 2.8cm(y) by 2cm(z) and the force square is 8cm x 2cm with a force density of 2400N/m² resulting in a load of 
3.84N or approximately 384g in graviational terms.

<div id="fig:table_grid">
![](./source/figures/tisch3d_grid_bottom.png){width=50%}
![](./source/figures/tisch3d_grid_top.png){width=50%}

The table mesh with a large force rectangle on the top and 4 x-y sliding Dirichlet conditions on the bottom.
</div>

The resulting isosurface is depicted in [@fig:tisch_raw].
The model was calculated using 1120591 tetrahedra
with the parameters for the Ginzburg-Landau term set to:
$\gamma = 0.008$ and $\epsilon = 0.0035$ 


![The extracted table isosurface](./source/figures/table_raw.png){#fig:tisch_raw}

![Zoom in on the smoothed table isosurface](./source/figures/table_smoothed_section.png){#fig:table_smoothed}

The surface was remeshed with $\sigma = 0.014$ and ran for 10 iterations.
However, the remeshed surface did display erroneous behaviour in form of a roughening and strongly distorted triangles.
Why this happend was not known at the time of finishing this thesis.
As can be seen the smoothed input mesh in [@fig:table_smoothed] is not unusual and the condition number of the interpolation matrix was 
calculated to be 21401790124 which seemed acceptable. 

Unfortunately since the remeshing was conducted on the WIAS servers, the programmed graphic tools were unavailable during the remeshing procedure.
To know exactly what happend further analysis is needed.

![The remeshed table model.](./source/figures/table_remeshed.png){#fig:tisch_remeshed}

![Closeup of the problematic remeshed table mesh.](./source/figures/table_fuckup.png){#fig:table_fuckup}

### The tower
The tower model has a similar layout to the table model above. A small force square on top applies a pressing force in the negative x-direction and
4 clamped Dirichlet squares function as force sinks.

The dimensions of the domain are 6cm by 2cm by 2cm and the force and Dirichlet squares were each sized .4cm by .4cm.
The load density was set to 240000 N/m² such that again a resulting load of 3.84N or ~384g was applied.

<div id="fig:tower_grid">
![From the bottom](./source/figures/turm_grid2.png){width=50%}
![From the top](./source/figures/turm_grid1.png){width=50%}\

The grid for the tower model.
</div>


## Analysis of the results and problem 

### General problems with normals as refinement markers
A general problem with normal based refinement is that normals are not a reliable marker
for the mesh error i.e. the difference between interpolant and the triangular mesh.
To see this consider the ear of the cat model from [@sec:surf_cond] in [@fig:cat_ear]. The normals at the bottom of the ear point
in the same direction as the ones on the top of the ear. Furthermore the long neighboring edges then exibit a sawtooth or cliff like pattern stemming from
strong normal variations of the triangle normals. This feature is depicted in [@fig:cat_ear2].

However this problem was lessend when the edge flips were set to flip based on the normal angles instead of the 6d angles. 
This prevented elongated triangles by applying flips but in effect the flips then compete with the remaining meshoperations.

![Coinciding normals at the bottom and the top of the cat ear.](./source/figures/cat_ear.png){#fig:cat_ear}

![The cat ear in rendered with triangle normal based lightning that highlights the obliqueness of the triangles.](./source/figures/cat_ear_cliff.png){#fig:cat_ear2}


Another possibility to generate a well adapted mesh without relying on the normals would be to use the interpolants values as an indicator for
accuracy of triangles. This is possible because close to the surface the interpolant has the shape of the signed distance function.
Using quadrature points on triangles/edges the volume/area under the surface defined by the approximant/interpolant and the mesh entity could be calculated. 
However this would rely heavily on evaluations of the interpolant which therefor has to be cheap to evaluate.

![In the case of parallel normals a refinement is inhibited and the mesh error pertains.](./source/figures/cat_foot.png){#fig:cat_foot}


