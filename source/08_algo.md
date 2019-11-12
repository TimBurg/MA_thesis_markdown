
# Algorithm description and implemenation details

## interpolation 
The vertices of the extracted isosurface are the principal points for the interpolation.

As stated in [@sec:surface_interpol], additionally, the off-surface values both in the positive as well as the negative direction are 
incorporated into the interpolation. These are calculated via the original meshes vertices $v$ and triangle normals $n_T$ as follows:

\begin{equation} \vec{v_{\text{off}}} = \vec{v} \pm \varepsilon \frac{\vec{n_v}}{\lVert \vec{n_v} \rVert} \label{eq:offsites}\end{equation}

where $\vec{n_v}$ is assembled of the triangles $\mathcal{N}_T$ containing $v$ as a vertex:

$$\vec{n_v} = \sum_{T \in \mathcal{N}_T} \frac{1}{\lVert \vec{v} - \vec{v^T_\text{cent}} \rVert} \vec{n}_T$$

Here $\vec{v^T_{\text{cent}}}$ is the centroid of the triangle.

Since the normals of the triangles point outward of the structure as in the stl specification we have higher interpolant values outside
the object and a gradient pointing outwards.

Experimentation with $\varepsilon$ only yielded surfaces that were vertiable for projection for small values.
I settled with a general forumla setting $\varepsilon$ as the average between the longest edge in the mesh and the smallest edge 
divided by 10, ie.:
$$\varepsilon = \frac{e_{\text{longest}} + e_{\text{shortest}}}{20}$$

The scale factor of the rbf functions was set to 2.5 times the longest edge in the mesh where lower values would disrupt the contiguous 
surface.


## surface conditioning{#sec:surf_cond}
A principal problem is that of the values of the interpolant in between the datasites.
In the case of an implicitly defined surface this influences not only the shape of the zero level set but also the slope
at the zero crossing.
As an illustration take a look at [@fig:centroid_normalprobe].
Displayed are the interpolant values along the triangle normals of the initial model which were centered at each triangles centroid.
The zero crossing mostly occur in the neighborhood of zero as is to be expected from the intended smoothness of the surface.
However, for some normal traces or plots a stronger deviation can be made out and the existence of a zero crossing is questionable.
If in fact the scale parameter is chosen too small then there might be no zero crossings at all for some triangles which,
in the best case will only inhibit refinement in that area as the vertex projection cannot converge. 
In the worst case though the projection might yield a vertex that results in an invalid mesh 
(flipped triangle or non-manifold surface or self intersection). 




![Interpolant values along the normal direction sampled at the triangle centroids](./source/figures/centroid_normalprobe.png){#fig:centroid_normalprobe}






The interpolation matrix \ref{eq:interpolation_matrix} is then constructed as a sparse matrix with a scale factor $c$ as explained in
[@sec:rbf_interpol] and the system \ref{eq:interpolation_system} is subsequently solved for the coefficients.


Throughout the implementation of the algorithm a cat model was used that is pictured in figure \ref{fig:cat_model} 
together with it's interpolated surface (the isosurface was generated with marching cubes).


![](./source/figures/cat_raw.png){width=50%}
![](./source/figures/cat_cubes_isosurf.png){width=50%}
\begin{figure}[!h]
\caption{An isosurface extracted via marching cubes of an interpolated cat model}
\label{fig:cat_model}
\end{figure}

An intersection through the cat surface is shown in [@fig:cat_isolines]. The isolines show that the surface 
is generally well behaved with the isolines being mostly parallel. 
Deviations can occur in areas of high curvature of the original mesh (the feet) and where other parts of the model 
are in proximity (this is no issue in this case).

For models with very close proximity of parts in relation to a coarser original mesh the slope around zero
given by equation \ref{eq:offsites} should be adapted.


![An 2d section through the interpolant of the cat model with 7 isolines around 0](./source/figures/cat_isolines.png){#fig:cat_isolines}

## Smoothing
The resulting isosurfaces of the topology optimization generally had rough surfaces with seemingly random small 
surface features like bumbs dents. Since an interpolation rather than a fit were used, these features would be preserved and result
in small refinement for those features.

To circumvent this, a mesh smoothing method was employed to smooth the isosruface mesh.
Since the often used laplace smoothing diminishes volume I opted for taubin smoothing as described in [@taubin_curve_1995].

The smoothing is very similar to the introduced vertex-smoothing above. For a vertex $v_i$ and neighbors $v_j$, the position
of the vertex is shifted with a weighed average of the neigbors positions:
$$\Delta v_i = \sum_{j \in \mathcal{N}_i} w_{ij} (v_j - v_i)$$
Where the weights $w_{ij}$ are just set as the inverse number of neighbors $w_{ij}=1/|\mathcal{N}_i|$. The shift is then added partially to the original vertex.
$$v_i' = v_i + \lambda \Delta v_i \qquad 0<\lambda<1$$

For taubin smoothing an analogous second smoothing step is introduced with a negative $\lambda$ ie. an expansion.
The coefficient for this is denoted $\mu$ with the restriction that $0< \lambda < -\mu$.
In [@taubin_curve_1995] taubin shows that this acts as a lowpass filter and limits shrinkage of the model.

For the application I used values of $\lambda = 0.40$, $\mu=-0.50$ and made 40 smoothing iterations.
The smoothing effect is displayed in figure [@fig:dragon].


![The mesh smoothing method applied to a dragon test model](./source/figures/dragon_smoothing.png){#fig:dragon} 


## Projection step

Inserting a new vertex in an edge split and smoothing a vertex requires a projection of a midpoint onto the surface.
For sufficiently small distances to the surface this projection is assumed to be orthogonal since the gradient has no components
in the tangent plane to the isosurface.
This is however no requirement since vertex smoothing will take care of adjusting the positions of the vertices on the surface later on.

![Fast convergence of the gradient descent onto the surface for a steplength of 1](./source/figures/projection_steps.png){#fig:projection} 


## Remeshing 

Generally, points on the boundary are not included in the remeshing procedure as the coplanarity of points on the boundary 
could not be preserved.

The remeshing algorithm is implemented as in [@dassi_novel_2016]:

\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoLined
\SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}
\Input{Target edge length $l_{6d}$ and  $\sigma$ for HDE}
\BlankLine
i=0 \;
\While{$i<$maxiter}{
    smalledges=\{$l_{6d}^e < 0.5 \cdot l_{6d}$ for e in edges \}\;
    j=0\;
    \While{ smalledges and $j<10$}
	    {
	    collapse smalledges \;
	    smooth random 30\% of vertices \;
	    flip all edges \;
	    update smalledges\;
	    j+=1 \;
	    }
     longedges=\{$l_{6d}^e > 1.5 \cdot l_{6d}$ for e in edges \}\;
     split long edges \;
     flip all edges;\
     smooth all vertices \;
     flip all edges \;

}
\caption{The remeshing procedure}
\end{algorithm} 

## Higher dimensional embedding

The parameter for the embedding is $\sigma$. By the nature of the extension, the additional edgelength due to the normals
is independent of the scaling of the original mesh. Therefor the values of $\sigma$ depend on the input mesh.
A good default value is set with the following formula utilizing an enclosing box (or bounding box) $B$ of a model $m$.
$$\sigma_{default} = \frac{\text{size}_x(B) + \text{size}_y(B) +\text{size}_z(B) +}{10}$$
The value 10 was obtained heuristically but depending on the model proportions and desired refinement,
values as low as 5 or as high as 15 might be used.

The effect of different $\sigma$ are shown in ...


<div id="fig:sigma_values">
![$\sigma=20$](./source/figures/fox_nose_sigma=20.png){width=50%}
![$\sigma=28$](./source/figures/fox_nose_sigma=28.png){width=50%}\
![$\sigma=36$](./source/figures/fox_nose_sigma=36.png){width=50%}
![$\sigma=50$](./source/figures/fox_nose_sigma=50.png){width=50%}

Greater values of $\sigma$ yield a refinement of curved surfaces. However, due to the irregularities due to small variation in normals
can occur.
</div>



## Implementation details

The programming language Python was used to build a datastructure for the mesh (that is called Trimesh) and implement 
the remeshing operations from [@sec:remeshing_ops] with it.
This Trimesh is an undirected graph made up of points with asociated pointnormals and references to their neighbors. Additionally each point
stores references to the edges and triangles it takes part in.

Also in the Trimesh are lists of edge and triangle objects that each hold references to their points and to each other. More so, a triangle has labels A,B,C for its points and a,b,c for its edges where the lower letter edge is located opposite to the respective capital letter Point.

Also, the order of points in a triangle not only determines the normal vector but is used in finding 
triangles left and right to an edge (looking from the outside).
Therefor the correctness of these information is of fundamental importance.

The richness of this datastructure has the benefit that the remeshing operations could be written in a relatively compact form.

To then optimize the performance of this datastructure it was ported to the C-language with the cython transpiler where additional datatypes were added.

However, performance was not a consideration from the beginning. And it was discovered that 
unstructured graphs of relatively large python objects have a bad cache performance.
Adding to this, for large input meshes, the calculation of interpolant values takes a lot of time since the distances to each 
center need to be computed. 
That is to say, the topology optimization meshes that were remeshed in the following section took
several hours to remesh even though smaller meshes of only a few thousand vertices could be remeshed in acceptable times like 5 to 10 minutes.

I will reconsider this issue in the outlook section.

<!--As mentioned in [@sec:edge_flip] a too large angle condition for the 6d-angles on the opposing points of a to-be-flipped edge can lead to-->
<!--very few flips being done at all.-->
<!--For why this is consider the triangle depicted in [@fig:tri_strip]. The triangle angle $\beta$ at the point B is calculated with the following forumla.-->
<!--Let $A^{6d}$ be the vector $(\text{A}, \sigma \text{n}_\text{A})$ and analogously for B and C. Then-->
<!--$$\beta = \text{arccos}\Big( \frac{(A-B, C-B)_{3d} + \sigma^2 (n_A - n_B, n_C - n_B )}{\lVert A^{6d} - B^{6d} \rVert_{6d} \lVert C^{6d} - B^{6d}\rVert_{6d}}\Big)$$-->

<!--Take a look at the scalar product after $\sigma^2$. For a n angle of $\pi/2$ this term would need to become zero. This will can only happen if-->
<!--$n_A = n_B \text{ or } n_C = n_B$ or $n_A - n_B \perp n_C - n_B$ which-->

<!--![A thin strip triangle on a curved surface](./source/figures/triangle_strip.svg){#fig:tri_strip width=50%}-->


