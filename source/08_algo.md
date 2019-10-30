
# Algorithm description and implemenation details

## interpolation 
The vertices of the extracted isosurface are the principal points for the interpolation.

As stated in [@sec:surface_interpol], additionally, the off-surface values both in the positive as well as the negative direction are 
incorporated into the interpolation. These are calculated via the original meshes vertices $v$ and triangle normals $n_T$ as follows:

$$ \vec{v_{\text{off}}} = \vec{v} \pm \varepsilon \frac{\vec{n_v}}{\lVert \vec{n_v} \rVert} $$

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
around the border of the surface.
As an illustration take a look at [@fig:centroid_normalprobe]

![Interpolant values along the normal direction sampled at the triangle centroids](./source/figures/centroid_normalprobe.png){#fig:centroid_normalprobe}






The interpolation matrix \ref{eq:interpolation_matrix} is then constructed as a sparse matrix with a scale factor $c$ as explained in
[@sec:rbf_interpol] and the system \ref{eq:interpolation_system} is subsequently solved for the coefficients.

 
![](./source/figures/cat_raw.png){width=50%}
![](./source/figures/cat_cubes_isosurf.png){width=50%}
\begin{figure}[!h]
\caption{An isosurface extracted via marching cubes of an interpolated cat model}
\end{figure}

## Smoothing
The resulting isosurfaces of the topology optimization generally had rough surfaces with seemingly random small 
surface features like bumbs dents. Since an interpolation rather than a fit were used, these features would be preserved and result
in small refinement for those features.

To circumvent this, a mesh smoothing method was employed to smooth the isosruface mesh.
Since the often used laplace smoothing diminishes volume I opted for taubin smoothing as described in [@taubin_curve_1995].

The smoothing is very similar to the introduced vertex-smoothing above. For a vertex $v_i$ and neighbors $v_j$, the position
of the vertex is shifted with a weighed average of the neigbors positions:
$$\Delta v_i = \sum_{j \in \mathcal{N}_i} w_{ij} (v_j - v_i)$$
With $w_{ij}=1/|\mathcal{N}_i|$ as the number of neighbors. The shift is then added partially to the original vertex.
$$v_i' = v_i + \lambda \Delta v_i \qquad 0<\lambda<1$$

For taubin smoothing an analogous second smoothing step is introduced with a negative $\lambda$ ie. an expansion.
The coefficient for this is denoted $\mu$ with the restriction that $0< \lambda < -\mu$.
In [@taubin_curve_1995] taubin shows that this acts as a lowpass filter and prevents shrinkage of the model.

For the application I used values of $\lambda = 0.40$, $\mu=-0.52$ and made 40 smoothing iterations.



## Projection step

Inserting a new vertex in an edge split and smoothing a vertex requires a projection of a midpoint onto the surface.
For sufficiently small distances to the surface this projection is assumed to be orthogonal since the gradient has no components
in the tangent plane to the isosurface.
This is however no requirement since vertex smoothing will take care of adjusting the positions of the vertices on the surface later on.

![Fast convergence of the gradient descent onto the surface for a steplength of 1](./source/figures/projection_steps.png){#fig:projection} 


## Remeshing 

Generally, points on the boundary are not touched since they form a fixed interface to 

The remeshing algorithm is taken from [@dassi_novel_2016]

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



### convergence analysis

