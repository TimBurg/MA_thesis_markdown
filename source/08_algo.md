
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
divided by 10, i.e.:
$$\varepsilon = \frac{e_{\text{longest}} + e_{\text{shortest}}}{20}$$

For the actual RBF interpolation the scale factor of the Wendland function was set to 2.5 times the longest edge in the mesh where lower values 
did reduce the convergence-rate of successfull projection onto the surface.


## surface conditioning{#sec:surf_cond}
A principal consideration is that of the values of the interpolant in between the datasites.
In the case of an implicitly defined surface this influences not only the shape of the zero level set but also the slope
at the zero crossing.
The latter is plotted in [@fig:centroid_normalprobe].
Displayed are the interpolant values along the triangle normals of the initial model which were centered at each triangles centroid.
The zero crossing mostly occur in the neighborhood of zero where shifts are expected from the smoothness of the surface.
However, for some normal traces or plots a stronger deviation can be made out and the existence of a zero crossing is questionable.
If in fact the scale parameter is chosen too small then there might be no zero crossings at all for some triangles which
in the best case will only inhibit refinement in that area as the vertex projection cannot converge. 
In the worst case though the projection might yield a vertex that results in an invalid mesh 
(flipped triangle or non-manifold surface or self intersection). 




![Interpolant values along the normal direction sampled at the triangle centroids for the cat model.](./source/figures/centroid_normalprobe.png){#fig:centroid_normalprobe}






The interpolation matrix \ref{eq:interpolation_matrix} is then constructed as a sparse matrix with a scale factor $c$ as explained in
[@sec:rbf_interpol] and the system \ref{eq:interpolation_system} is subsequently solved for the coefficients.


Throughout the construction of the algorithm a cat model was used for testing that is pictured in figure \ref{fig:cat_model} 
together with it's interpolated surface (the isosurface was generated with marching cubes). 
The smoothness of the interpolant can be assessed visually.

<div id="fig:cat_model">
![](./source/figures/cat_raw.png){width=50%}
![](./source/figures/cat_cubes_isosurf.png){width=50%}

An isosurface extracted via marching cubes of an interpolated cat model. a)input mesh, b)interpolated mesh.
</div>

<!--\begin{figure}[!h]-->
<!--\caption{}-->
<!--\label{fig:cat_model}-->
<!--\end{figure}-->

An intersection through the cat surface is shown in [@fig:cat_isolines]. The isolines show that the surface 
is generally well behaved with the isolines being mostly parallel. 
Deviations can occur in areas of high curvature of the original mesh (the feet) and where other parts of the model 
are in proximity (this is no issue in this case).

For models with very close proximity of parts (in relation to the spacing of the original mesh) the slope around zero
given by equation \eqref{eq:offsites} should be adapted.


![An 2d section through the interpolant of the cat model with 7 isolines around 0.](./source/figures/cat_isolines.png){#fig:cat_isolines}

## Smoothing
The resulting isosurfaces of the topology optimization generally had rough surfaces with seemingly random small 
surface features like bumbs and dents. These features are deemed unphysical but would be preserved in an interpolation. 
They would also be agressively refined since the normals are irregular. 

To circumvent this, a mesh smoothing method was employed prior to the interpolation to smooth the isosurface mesh.
Since the often used Laplace smoothing diminishes volume I opted for Taubin smoothing as described in [@taubin_curve_1995].

The smoothing is very similar to the vertex-smoothing introduced above. For a vertex $v_i$ and neighbors $v_j$, the position
of the vertex is shifted with a weighed average of the neigbors positions:
$$\Delta v_i = \sum_{j \in \mathcal{N}_i} w_{ij} (v_j - v_i)$$
where the weights $w_{ij}$ are just set as the inverse number of neighbors $w_{ij}=1/|\mathcal{N}_i|$. The shift is then added partially to the original vertex.
$$v_i' = v_i + \lambda \Delta v_i \qquad 0<\lambda<1$$

For Taubin smoothing a second smoothing step is introduced with a negative $\lambda$ i.e. a roughening.
The coefficient for this is denoted $\mu$ with the restriction that $0< \lambda < -\mu$.
In [@taubin_curve_1995] Taubin shows that repeated iteration of these two step act as a lowpass filter and limit the shrinkage of the model.

For the application I used values of $\lambda = 0.40$, $\mu=-0.50$ and ran 40 smoothing iterations.
The smoothing effect of this is displayed in [@fig:dragon].


![The mesh smoothing method applied to a dragon test model](./source/figures/dragon_smoothing.png){#fig:dragon} 


## Projection step

Inserting a new vertex in an edge split and smoothing a vertex requires a projection of a (mid-)point onto the surface.
For sufficiently small distances to the surface this projection can be assumed to be orthogonal since the gradient has no components
in the tangent plane to the isosurface
and the tangent planes are mostly parallel. This is seen in [@fig:cat_isolines].
However this no requirement since consecutive vertex smoothing will adjust the positions of the vertices on the surface.

![Fast convergence of the gradient descent onto the surface for a steplength of 1.](./source/figures/projection_steps.png){#fig:projection} 

The convergence of this projection was generally very fast and stayed within 5 iterations for all test cases to give an interpolant value of $1e^{-4}$.
The convergence is depicted in [@fig:projection].


## Remeshing 

After the smoothed mesh is interpolated the remeshing begins.

Generally, points on the boundary are not included in the remeshing procedure as the coplanarity of points on the boundary 
could not be preserved. Also those points present an interface that should be fixed. If a reforming of the boundary was needed a seperate 2d 
interpolant could be constructed.

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
$$\sigma_{default} = \frac{\text{size}_x(B_m) + \text{size}_y(B_m) +\text{size}_z(B_m)}{10}$$
The value 10 was obtained heuristically but depending on the model proportions and desired refinement,
values as low as 5 or as high as 15 might be used.

The effect of different $\sigma$ are shown in [@fig:sigma_values].


<div id="fig:sigma_values">
![$\sigma=20$](./source/figures/fox_nose_sigma=20.png){width=50%}
![$\sigma=28$](./source/figures/fox_nose_sigma=28.png){width=50%}\
![$\sigma=36$](./source/figures/fox_nose_sigma=36.png){width=50%}
![$\sigma=50$](./source/figures/fox_nose_sigma=50.png){width=50%}

Greater values of $\sigma$ yield a refinement of curved surfaces. However, due to small variation in normals irregularities can occur. Notice also
that some thin strip triangles can be seen in (d).
</div>



## Implementation details

The programming language Python was used to build a datastructure for the mesh (that is named Trimesh in the code) and implement 
the remeshing operations from [@sec:remeshing_ops] with it.
This datastructure is an undirected graph made up of points with associated pointnormals and references to their neighbors. Additionally each point
stores references to the edges and triangles it takes part in.

Also in this structure are lists of edge and triangle objects that each hold references to their points and to each other. A triangle object has labels A,B,C for its points and a,b,c for its edges where the lower letter edge is located opposite to the respective capital letter Point.

Also, the order of points in a triangle not only determines the normal vector but is used in finding 
triangles left and right to an edge (looking from the outside).
Therefor the correctness of these information is of fundamental importance.

The richness^[All relations are stored directly and are not deduced on the fly] of this datastructure
has the benefit that the remeshing operations could be written in a relatively compact form.
The code for this datastructure and the remeshing algorithm can be found on the accompanying DVD or, should it be approved by the supervisors on github under
[this link](https://github.com/TimBurg/rbf_remesh).

To then optimize the performance of this datastructure it was ported to the C-language with the cython transpiler where additional datatypes were added.

However, performance was not a consideration from the beginning. And it was discovered that 
unstructured graphs of relatively large python objects have a bad cache performance.
Adding to this, for large input meshes, the evaluation of the interpolant takes a lot of time since the distance to each 
center needs to be computed. And for vertex smoothing this needs to be done multiple times for all vertices in the mesh.
That is to say, the topology optimization meshes that were remeshed in the following section took
several hours to remesh even though smaller meshes of only a few thousand vertices could be remeshed in acceptable times from around 5 to 10 minutes.

I will reconsider this issue in the outlook section and give recommendations on how to improve this.

For the implementation the following third party libraries were used:

* numpy (array package for python)
* numpy-stl (stl mesh reader)
* glumpy (openGL wrapper)
* scipy (for sparse matrix linalg)
* cython (Python to C transpiler)

<!--As mentioned in [@sec:edge_flip] a too large angle condition for the 6d-angles on the opposing points of a to-be-flipped edge can lead to-->
<!--very few flips being done at all.-->
<!--For why this is consider the triangle depicted in [@fig:tri_strip]. The triangle angle $\beta$ at the point B is calculated with the following forumla.-->
<!--Let $A^{6d}$ be the vector $(\text{A}, \sigma \text{n}_\text{A})$ and analogously for B and C. Then-->
<!--$$\beta = \text{arccos}\Big( \frac{(A-B, C-B)_{3d} + \sigma^2 (n_A - n_B, n_C - n_B )}{\lVert A^{6d} - B^{6d} \rVert_{6d} \lVert C^{6d} - B^{6d}\rVert_{6d}}\Big)$$-->

<!--Take a look at the scalar product after $\sigma^2$. For a n angle of $\pi/2$ this term would need to become zero. This will can only happen if-->
<!--$n_A = n_B \text{ or } n_C = n_B$ or $n_A - n_B \perp n_C - n_B$ which-->

<!--![A thin strip triangle on a curved surface](./source/figures/triangle_strip.svg){#fig:tri_strip width=50%}-->


