<!------->
<!--title: "Curvature based remeshing for phase field based topology optimization"-->
<!--subtitle: "Thesis as required for the attainment of the degree Master of Science" -->
<!--author: Tim Burg-->
<!--date: "2019-10-20"-->
<!--subject: ""-->
<!--keywords: [Markdown, Example]-->
<!--lang: "en"-->
<!--bibliography: ./bibliography/tot.bib-->
<!--...-->

\pagenumbering{arabic}
# Introduction & Overview 


Triangular meshes are the most prominent representation of 3D surfaces in computer graphics and the go-to format for computer-aided-design. 
Aside from the topological aspects of the described surfaces or non-manifold errors (which are an issue of their own in remeshing and additive manufacturing),
these meshes, being piecewise linear, can only approximate curved surfaces. 
Often such approximations 
are inefficient in terms of their required data storage because the grid is isotropic and uses about the same number of datapoints 
in areas of high curvature variation as in flat areas.
This problem arises for example when the datapoints are obtained from some form of measurement data (e.g.laser scanners) or are 
constructed from local algorithms like marching cubes or marching tetrahedra.

One such case which is the one treated here concerns the extraction of an isosurface-mesh of a scalar-valued function defined on a finite-element mesh.
The isovalue-intersections may cut the Finite-element-simplices close to corners and edges resulting in very small and possibly distorted ie. non-equilateral triangles.
Variance of the surface is not accounted for in the usual isosurface algorithms and hence a mesh that is 
as dense as the FE-mesh is extracted.
Subsequently various remeshing techniques may be used to yield an adaptive mesh.
The method used for this in this work is a pliant remeshing algorithm with local mesh modification.

The application of which the FE-mesh stems from is a topology optimization using the phase-field method.
Topology optimization is a form of optimization of mechanical structures that can nucleate and adapt
holes in the material where low stress is encountered and add material in high stress regions.

Often a certain minimum stiffness or maximum give in a structure is required for it to perform its target application.
Topology optimization can then yield designs that need less material or give better 
stiffness and hence a better performing part for the same material.

The phase-field is integral in this method and distinguishes material from void but has a continuous range from 0 to 1 where 0 is void and 1 is material. 
Usually then the isosurface to the value 0.5 is used to determine the boundary of the solid-body.

## common approaches for remeshing
There are different approaches for remeshing a given triangular mesh that each involve some form 
of interpolation or approximation to find new vertices for the mesh or generate a whole new mesh altogether. 
Oftentimes the original piecewise-linear complex ie. the original mesh is used to find the new vertices which
is linear interpolation. For applications where a smooth output mesh is desired this is not suitable and 
more intricate interpolation schemes need to be used.
However, all Interpolation schemes do respect the original mesh in the sense that the vertices are still points on the surface.
This is not the case if the original mesh is approximated ie. fitted with a functional description.


## Radial basis function surface interpolation
For remeshing a surface one has to have a representation that can be queried for new on-surface points.
Here implicit surface descriptions, ie. $F(x)=0$ for an interpolating space-function $F: D\to\mathbb{R}$ where $D$ is the data space have proven to be practical.
Radial-basis-functions interpolation falls into that catergory and it is, besides polynomial-interpolation,
among the most widely used interpolation-scheme nowadays.
Radial-basis-functions are especially suited for multivariate data because the dimensionality of the data
is only incorporated through the vectornorm of the associated space and as such is especially easy to implement.

To see this, consider the simplest case where the interpolant is given as a sum over basis funtions centered at the data points $i$:
$$F(x) = \sum_i \alpha_i \varphi(\lVert x-x_i\rVert)$$


### Higher dimensional embedding for curvature adaption
The RBF-interpolant can be easily differentiated analytically to obtain the gradient formula. 
This gradient, standing perpendicular on the 0-level-set describes the curvature of the mesh and is used
for curvature adaptive remeshing. 
This is accomplished with an extension that incorporates the gradient in a 6d formulation: $(x,y,z, \sigma n_x, \sigma n_y, \sigma n_z)$
The 6d norm is then used in the 
remeshing process. This essentially gives longer edges where normals are different and induces a refinement.

Final thoughts on the reliability of this method can be found in the conclusive statement.
