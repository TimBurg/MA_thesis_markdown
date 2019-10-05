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

# Introduction & Overview 


Triangular meshes are the most prominent representation of 3D surfaces in computer graphics and the go-to format for computer-aided-design. 
Aside from the topological aspects of the described surfaces or non-manifold errors that can cause issues with remeshing and additive manufacturing,
These meshes, being piecewise linear, can only approximate curved surfaces and often such approximations may be severely ill-conditioned for computations and inefficient in their surface-description.
This for example the case when the mesh is generated from scattered data.
If this is the case then remeshing techniques can be used to yield a better mesh.

One such case which is the one treated here arises after the extraction of an isosurface-mesh of a scalar-valued function defined on a finite-element mesh.
The isovalue-intersections may cut the Finite-element-simplices close to corners and edges resulting in very small and possibly distorted ie. non-equilateral triangles.

The application considered in this work is a topology optimization with the phase-field method.
Often a certain minimum stiffness or maximum give in a structure is required for it to perform its target application.
Topology optimization then can yield designs that need less material or give better 
stiffness and hence a better performing part for the same material.

The phase-field distinguishes material from void but has a continuous range from 0 to 1 where 0 is void and 1 is material. 
Usually then the isosurface to the value 0.5 is used to determine the boundary of the solid-body.

## common approaches for remeshing
There are different approaches for remeshing a given triangular mesh that each involve some form of interpolation or approximation to find new vertices for the mesh or generate a whole new mesh altogether. Interpolation schemes do, as the name implies respect the original data(here: the mesh) in the sense that the vertices are still points on the surface.


## Radial basis function surface interpolation
For remeshing a surface one has to have a representation that can be queried for new on-surface points.
Here implicit surface descriptions, ie. $F(x)=0$ for an interpolating space-function $F: D\to\mathbb{R}$ where $D$ is the data space have proven to be practical. Radial-basis-functions interpolation falls into that catergory and it is, besides polynomial-interpolation, among the most widely used interpolation-scheme nowadays. Radial-basis-functions are especially suited for multivariate data (read: arbitary dimensions)
as they  only depend on the space-dimensions through the associated vectornorm.
The interpolant is given as a simple sum over basis funtions centered at the data points $i$:
$$F(x) = \sum_i \alpha_i \varphi(\lVert x-x_i\rVert)$$





### Higher dimensional embedding for curvature adaption
The RBF-interpolant can be derived analytically to obtain the gradient. This gradient, standing perpendicular on the 0-level-set describes the curvature of the mesh and used for curvature adaptive remeshing. This is accomplished with something called a higher dimensional embedding. 
The idea is that 


