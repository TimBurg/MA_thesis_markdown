
# Theoretical backgrounds

## Linear elasticity

### The equations of static elasticity
Mathematical elasticity can be considered a branch of continuum dynamics whose research reaches as far back as the late 16th century.
I only give a short outline of the stepstones to linear elasticity and refer mostly to  
the book mathematical elasticity by Ciarlet which is a comprehensive standard piece on the topic.

Continuum dynamics deals with a body occupying a lipschitz-continuous reference configuration $\overline{\Omega}\subset \mathbb{R}^3$ under rest which is deformed to a
configuration $\Omega \subset \mathbb{R}^3$ by applied forces.
The deformation is then described by an injective mapping $\varphi$ which contains a displacement field $u:\overline{\Omega} \mapsto \Omega$:
$$\varphi:\overline{\Omega} \mapsto \Omega \qquad \varphi=id+u$$
For the static case treated here, the deformation is time independant.
The deformation and displacement mappings are required to be two times continuously differentiable but this reqirement can be relaxed in the variational formulation of the equations. 
I denote the coordinates in the reference configuration with $x$ and and those in the deformed configuration with $x^\varphi = \varphi(x)$. 
In engineering Textbooks those coordinates are sometimes referred to as Lagrange- and Euler-coordinates respectively.

The elasticity theory is then build on the follwowing two contibutions from Cauchy of which the second is fundamental to continuum dynamics:

1. Axiom of force balance:

   Given volume- and surface-force-densities as $f^\varphi$ and $g^\varphi$  in the deformed configuration then for every subset
   $A^\varphi \subset \Omega$ the following equality holds:
   $$\int_{A^\varphi} f^\varphi(x^\varphi) dx^\varphi + \int_{\partial A^\varphi} t^\varphi(x^\varphi,n^\varphi)da^\varphi = 0$$
   Here, $dx^\varphi$ and $da^\varphi$ are the volume and surface elements in the deformed configuration, $n^\varphi$ is the surface-unit-normal and $t^\varphi$ is the cauchy stress vectorfield:
   $$t^\varphi:\Omega \times \mathbb{S}_1 \mapsto \mathbb{R}^3 \quad where \quad \mathbb{S}_1 := \{v \in \mathbb{R}^3\:|\: \lVert v \rVert = 1 \}$$
   Note cauchy stress vector $t^\varphi$ depends on the given Volume $A$ only through the normal vector at a surface point and
   that any surface-force dictated on part of $\partial A \cap \partial\Omega$ must be dispersed through 
   the remaining part of $\partial A$.

2. Stress Tensor theorem:

   Assuming that $f^\varphi$ is continuous and 
   ${t^\varphi \in \textrm{C}^1(\Omega) \cap \textrm{C}(\mathbb{S}_1)}$,
   then $t^\varphi$ is linear w.r.t. 
   to the second argument ie.:
   \begin{subequations}\label{eq:equilibrium}
   \begin{align}
   t^\varphi (x^\varphi, n) &= T^\varphi (x^\varphi)n \qquad \forall x^\varphi \in \Omega, \! &\forall n \in \mathbb{S}_1\\
   &\text{and} \nonumber\\
     -\text{div}^\varphi T^\varphi (x^\varphi) &= f^\varphi   &\forall x^\varphi \in \Omega \label{eq:divT} \\
     T^\varphi (x^\varphi) &= T^\varphi (x^\varphi)^T         &\forall x^\varphi \in \Omega \\
     T^\varphi (x^\varphi) n^\varphi &= g^\varphi(x^\varphi)  &\forall x^\varphi \in \Gamma^\varphi 
   \end{align}\end{subequations}
   where $\Gamma^\varphi$ is the part of $\partial \Omega$ where the boundary condition $g$ is prescribed 
   and $\text{div}T = \partial_j T_{ij}, e_i$
   [See @philippe_ciarlet_mathematical_1990 p.63-65 for the proof]  

Notice that the forumulation above uses the stress tensor in the deformed configuration.
The pullback of the tensor onto the reference configuration is achieved with the piola-transform after which it needs 
to be symmetrized again. This then yields the so-called first and second Piola-Kirchhoff-Stress-Tensors denoted with $\Sigma$.
The densities in the  pullback of the forces is often ignored. These are then called dead loads
[see @philippe_ciarlet_mathematical_1990 chapter 2.7].

They are omitted here for brevity but the second Piola-Kirchhoff-Stress is the stress tensor to be determined in the next chapter.

### Stess, strain and the equations of equilibrium in the linear case
So far the theory is valid for all continuums but there are also nine unknown functions, namely the three components of the deformation and the six components of the stress tensor tensor.
Luckily, several simplifictaions can be made in case of isotropic and homogeneous media that lead to a remarkably simple form of the tensor.

To this end the chauchy strain tensor $C$ and its difference from unity $E$ is introduced.
They describes the first order local change in length-scale under a deformation and are via the 
fréchet derivative of the mapping $\varphi\mathrm{,} \: \nabla \varphi$:

$$\nabla \varphi = \begin{pmatrix}
			\partial_1 u_1 & \partial_2 u_1 &  \partial_3 u_1 \\
			\partial_1 u_2 & \partial_2 u_2 &  \partial_3 u_2 \\
			\partial_1 u_3 & \partial_2 u_3 &  \partial_3 u_3 \\
			\end{pmatrix}
			$$

$$C=\nabla \varphi^T \nabla \varphi = I + \nabla u^T + \nabla u + \nabla u^T \nabla u = I + 2 E  $$
Viewed in a different light, the deformed state can be considered a manifold with $C$ as the metric-tensor.

The simplification of the second Piola-Kichhoff-Stress-tensor follows these steps:

1. The stress tensor can only depend on $\varphi$ through its derivative $\nabla \varphi$ (Elasticity) 
2. Material-Frame Indifference
3. Isotropy
4. Rivlin-Ericksen representation theorem
5. Homogeneity

Details on these steps can again be found in [@philippe_ciarlet_mathematical_1990 chapter 3].
After following these steps, $\Sigma$ takes on the following form:
$$\Sigma(C) = \lambda (\mathrm{tr}E)I + 2\mu E + o(\lVert E \rVert)$$

Here, $\lambda$ and $\mu$ are the lamé coefficients of the material.
In the linear theory that is used as the basis for the topology optimization, the strain $E$ is replaced with 
the linearized version $\varepsilon$: 
$$\varepsilon = \frac{1}{2} \nabla u^T + \nabla u$$

this yields the following even simpler form of the tensor which is referred to as $\sigma$:

$$\sigma = \lambda ( \nabla u) I + \mu \left(\nabla u + \nabla u^T \right)$$
The more prominent form however is called Hooks-law and written with the so-called stiffness tensor $c$:
\begin{equation} \sigma = c : \varepsilon \qquad \text{or} \qquad \sigma = c \varepsilon \end{equation}
Where the last form is written in vector form for the components of the tensors.

### Variational formulation
For finite-element simulations and reduced smoothness requirements of the displacement, a variatonal formulation of the equilibrium equations \ref{eq:equilibrium} must be formulated.
To simplify the writing, the following tensoroperation for rank 2 tensors  is introduced:
$$G:V :=  \sum_{i,j} G_{ij} V_{ij}$$

Multiplying equation \ref{eq:divT} with a test function $\theta$ on both sides and integrating yields:
$$\int_{\Omega^\varphi} \text{div}^\varphi T^\varphi \cdot \theta^\varphi dx^\varphi = -\int_{\Omega^\varphi} f^\varphi
\theta^\varphi dx^\varphi + \int_{\Gamma^\varphi} g^\varphi \theta^\varphi$$

Using the Greens-formula for Tensor fields:
$$\int_{\bar{\Omega}} \text{div} H \cdot \theta dx = - \int_{\bar{\Omega}} H:\nabla \theta dx + \int_\Gamma Hn\cdot \theta da $$
and applying the pullback to the reference configuration with the second Piola-Kirchhoff-Stress-tensor then gives:

$$\int_{\bar{\Omega}} \nabla \varphi : \Sigma \nabla \theta dx = \int_{\bar{\Omega}} f \cdot \theta dx + \int_\Gamma g \cdot \theta da $$

For All sufficiently regular vector fields $\theta: \bar{\Omega} \mapsto \mathbb{R}^3$.
This is also called the 'principle of virtual work' (in the reference configuration).

For very small strains the deformation gradient in front of $\Sigma$ can be dropped since the 
diplacement gradient multiplied with the stress-tensor is of second order in $\nabla u$. [see @braess_finite_2013 p.280] 

Furthermore, since the product of a symmetric tensor with an antisymmetric one is zero, we split $\nabla \theta$ into:
$\left[ \frac{1}{2}(\nabla \theta + \nabla \theta^T) + \frac{1}{2}  (\nabla \theta - \nabla \theta^T)\right]$

And thus we write the equation in the following form:
\begin{equation}
\int_{\bar{\Omega}} \sigma \frac{1}{2}(\nabla \theta + \nabla \theta^T) = \int_{\bar{\Omega}} \sigma \varepsilon(\theta) =
\int_{\bar{\Omega}} f \cdot \theta dx + \int_\Gamma g \cdot \theta da \end{equation}


For the following sections we write this as the following shorthand notation using the inner product 
$\langle A,B \rangle_C = \int_{\bar{\Omega}} A: CB$ :

\begin{equation}\langle \varepsilon(u) \varepsilon(\theta)\rangle_{C(\varphi)} = \int_{\bar{\Omega}} f \cdot \theta + \int_\Gamma g \cdot \theta =: F(\theta)\label{eq:compliance}\end{equation}

For an actual deformation rather than a virtual one, the functional $F$ is called the compliance of the structure.
This compliance is what is to be optimized in the following section. 

## Topology optimization

The topology optimization procedure used in this work is a direct implementation the works of ... 
As a result of this I frequently refer to these papers. 
Topology optimization is a relativly new technique and was first 

The term topology optimization was coined in the context of optimizing mechanical structures.
It is not bound to a certain implementation but to the requirement that a structure under load that is optimized via a certain functional may change its topology under that optimization.
This is generally understood in the sense as to allow the nucleation of holes in a previously filled material rather than forming new 
strucutres in the void.

The method used throuout this work that accomplishes this uses the compliance minimization functional with a phase field description of the structure.
In effect, compliance minimization maximizes the stiffness of the structure under a mass- or volume constraint while the phase field describes where material is placed in the domain. 

The use of a phase-function description allows to incorporate a computationally cheap perimeter regularization via an additional term in the optimization functional.
This is needed since the compliance minimization in itself is not well posed and allows high variaton in the microstructure of a part that cannot be manufactured and is not numerically stable.

### Compliance minimization

Compliance is a very common goal function for topology optimization and defined as in equation \ref{eq:compliance}:
$$F(u) = \int_{\bar{\Omega}} f \cdot u + \int_\Gamma g \cdot u $$

Here, $u$ is the displacement solution of the mechanical system in the left-hand side of equation \ref{eq:compliance}

However, it is still open at this time how the compliance depends on the structure of the part.
This dependence is actually encoded in the Stiffness-tensor $c$ of the mechanical system that will be constructed from the 
phase field after this has been rigorously defined.

### The phase-field description and regularization energy

For the modeling of structures either a level set method or a phase field description is viable.
In case of the phase-field a continuous function is chosen 
that here can take on values in the range from 0 to 1 where 0 represents the void and 1 the material:
$$ 0 < \varphi < 1$$

A penalty term is then added to the optimization to force the phasefield to condensate to either 0 or 1 depending on a forcing term from the compliance minimization.
Consequently an interface forms that can expand or retract and this falls into the category of advancing front algorithms. For details see [@barles_front_1993].
The resulting equation driving the interface is an Allan-Cahn Equation as discussed in [@blank_phase-field_2010].
However, for the general understanding the optimality conditions are of more avail.


Firstly, since integrating a value of 1 over a region, a volume constraint is easily added with a parameter $m$ that dictates how much of the design domain is to be void:
$$\int_\Omega \varphi dx = m \cdot \text{vol}(\Omega)$$

Notice that values in the intermediate range of $\varphi$ contribute a lesser volume. 
However, these values, as they only occur in the interfacial region, will be forced to occupy a small portion of the domain.

We explicitly stipulate the requirements on $\varphi$ in the following space:
$$\mathcal{G}^m = \big\{\varphi \in H^1(\Omega, \mathbb{R})) \quad \big| \quad 0\leq \varphi \leq 1 \quad \text{and} \quad \int_\Omega \varphi dx = m \cdot \text{vol}(\Omega) \big\}$$

As stated, an additional term has to be added to the compliance functional as to force condensation of the phasefield and 
regularize the occurence of jumps. The term used is due to [@takezawa_shape_2010]:

$$ E^\varepsilon = \int_\Omega \frac{\varepsilon}{2} |\nabla \varphi|^2 + \frac{1}{\varepsilon} \Psi(\varphi) dx $$

The potential $\Psi(\varphi)$ serves as the condensation potential that forces the phase field to either 0 or 1.
Here, an obstacle potential is used while for the analysis, a differentiable double-well potential is employed:
$$\Psi_\text{dw}(\varphi) = \frac{1}{4} (\varphi^2 - \varphi)^2$$

$$\Psi_\text{obs} = \begin{cases} (1-\varphi)\varphi,  \quad \text{if}\ \varphi \in [0,1]\\
			           \infty \quad \text{else}
\end{cases}$$
The two potentials are displayed in figure \ref{fig:potentials}

![The two potentials in the Ginzburg-Landau energy term \label{fig:potentials}](source/figures/double_well.png){width=70%}

### Interpolation of the stiffness tensor
The stiffness tensor in the void is modeled by a very soft material $C_\text{void}$.
For the interpolation in the interfacial region towards the material tensor $C_\text{mat}$ a linear interpolation with a superimposed 
transition function $t(\varphi) = \varphi^3$ is used:
$$C(\varphi) = C_\text{mat} t(\varphi) + C_{void} (1- t(\varphi)) $$

### Isosurface extraction
Since the Finite-Element-Mesh is providing a 3D-tesselation of the domain, which in this case consists of tetrahedra, the generation of an isosurface is handled as in the marching-tetrahedra algorithm. 
Tetrahedra, as opposed to cubes, can only have 3 distinct cases of edge intersections that differ in terms of their makeup of triangular faces. No intersections, intersection at 3 edges(1 triangle) and intersection at 4 edges (2 triangles). See figure \ref{fig:isocuttetraeder} for an illustration.

For the edge intersections, a linear interpolation of the values between two vertices is used. 
The intersections are then found via simple line intersections comparable to the section of the x-axis for a line.
If 3 intersections are found one triangle is generated with the vertices of the intersections and if 4 intersections are found 2 triangles are generated.
Susequently the ordering of the vertices is checked so that looking from the outside, the vertices are ordered counterclockwise in accordance with the stl-specification. For this, the function values at the tetrahedra-nodes are considered to find a point that is inside (has a value greater than 0)
This is especially important since the orientation is used in the remeshing procedure and can only be correctly determined at this step.

![In the case of a 3D-Tetrahedra tesselation only 3 distinct cases can appear a)intersection
at three edges(left) or b)intersection at 4 edges(right) or c)no intersections(not displayed)\label{fig:isocuttetraeder}](source/figures/tetrahedrons.svg){width=80%}

## Radial-basis-function theory

### RBF Interpolation

Interpolation can be viewed as a special kind of approximation in which, for an approximant $S$ to some function $F$,
it is demanded that the interpolant reproduces the original functions values at special points $x_i$ ie.:
\begin{equation}S(x_i) = F(x_i) \quad \forall i\in \Xi \label{eq:interpolation_condition} \end{equation}
Where $\Xi$ is some finite (possibly scattered) dataset in $\mathbb{R}^N$ (multivariate) ie. a set $(\xi, f_\xi) \in \mathbb{R}^N \times \mathbb{R}$.
The functions considered here are scalar valued. A construction of vector-valued interpolants from scalar-valued conmponent-ones ist straightforward.

Interpolants are usually constructed from some function space which in this case is made up of Radial-basis-functions.
Radial-basis-functions are special in that they allow easy interpolation of scattered multivariate data with guaranteed existence and uniqueness results.
In general, different interpolants do behave differently for the space in between the datasites and are distinguished by 
their approximation and or convergence properties for special classes or cases of $F$.
However, when no original function(just the values $F(x_i)$) is given the accuracy of an interpolation can not generally be assessed.
Because this is the case here, determining qualities for the RBF-interpolant are discussed in section ...

Radial-basis-function interpolation constructs the interpolant $S$ as a linear combination of scaled Radial-basis-functions centered at the
datasites:
$$S(x) = \sum_i \alpha_i\varphi(\lVert x-x_i\rVert)$$
The norm denotes the standard euclidian norm which is essential for the convergence results [see @buhmann_radial_nodate p]  
The Radial-basis-functions themselves are functions of the form $\varphi:\mathbb{R}\mapsto\mathbb{R}$

By introducing the interpolation matrix $A$ as:
$$A= \varphi(\lVert x_i - x_j\rVert)|_{i,j}$$ 
we can write the interpolation condition \ref{eq:interpolation_condition} as:
$$A\alpha = F$$


### Existence and Uniqueness results
The invertbility of the interpolation matrix has been investigated thoroughly in the 1970's and 1980's.
Key results rely on complete monotonicity of the Radial-Basis-function, ie. the property:
$$(-1)^l g^l(t) \ge 0 \quad \forall l \in \mathbb{N} \quad \forall t>0$$
Then it can be shown that the interpolation matrix is always positive definite.
The proof relies on the Bernstein representation theorem for monotone functions. [see @buhmann_radial_nodate pp. 11-14 for the case of multiquadratics ]
A weaker requirement is that only one of the derivatives must be completely monotone.
This then leads to the concept of conditonally positive definiteness of a function in which a polynomial is added to the interpolant. 

- complete monotonicity yields a positive definite A (result due to Michelli 1986)
- weaker concept: complete monotonicity of some derivative: $(-1)^k \frac{d^k}{dt^k} \varphi(\sqrt{t})$
  - introduces conditionally positive definite functions that use an added polynomial that vanishes on the data sites for interpolation and thus the interpolant is again unique and exists
- called "unisolvence"

### Commonly used Radial basis functions 
It remains for us to recite some of the more often used RBFs and state if they are positive definite or conditionally so.
During the course of writing this thesis it became clear that only local basis functions would be good candidates for a feasible surface interpolation due to the number of vertices common in triangular meshes.

Now commonly used are the Wendland functions [see @wendland_piecewise_1995] which are piecewise polynomial, of minimal degree and positive definite. For the surface interpolation I use the C2 continuous function and it's derivative.

function             name                     definiteness 
-----------------   ------------------------ -------------
$e^{-r^2}$          gaussian                         pd
$\sqrt{r^2 +1}$	    multiquadratics	             pd 
$1/\sqrt{r^2+1}$    inverse multiquadratics          pd 
$r^3$               polyharmonic spline	            cpd

Table: RBF functions with global support

function                         name                     definiteness 
-----------------                ------------------------ -------------
$(1-r)_+^4(4r+1)$                $\varphi_{3,1}(r)$           pd
$(1-r)_+^6(35r^2+18r+3)$         $\varphi_{3,2}(r)$           pd
$(1-r)_+^8(32r^3+25r^2+8r+1)$    $\varphi_{3,3}(r)$           pd

Table: Local RBF functions introduced by Wendland [@wendland_piecewise_1995]

![Comparison of different RBF functions. Note that a convergence to zero is not mandatory.
However, the Wendland functions become zero after r=1](source/figures/rbf_functions.png){#fig:rbf_funcs width=70%}

### Scaling of RBF functions, ambiguities and interpolation properties
The normal RBF functions have a fixed spread as seen in @fig:rbf_funcs.
Since spacing of the interpolation data is not fixed,
a scale needs to be introduced that scales r such that the RBFs
 extend into the space between the datasites. Otherwise the interpolant might just have, in the exteme case, spikes at the sites to attain the required values.
To this end I scale r by $r' = r/c$ with a scale parameter $c$ since that makes the Wendland functions extend to exactly the value of this parameter.

This scaling parameter, in general can be nonuniform over the interpolated values but this comes with uncertainty for the solvability of the interpolation system.

Moreover, it cannot be generally stated which value of a scale parameter is more accurate in an interpolation unless there is a target to which the interpolant can be compared. See @fig:wendland_scales

![Wendland C2 functions for different scaling parameters c. The interpolation values were set to (1,2,1,2,1) at (0,1,2,3,4).
](source/figures/wendland_scale_factors.png){#fig:wendland_scales width=90%}

![Different Radial-Basis-Funtions have different behaviours for off-site values. Multiquadratics grow toward infinity.
Displayed is a 1-2 comb in two dimensions](source/figures/MQ_2D_comb.png){#fig:wendland_scales width=90%}

### surface interpolation
Surface descriptions are either explicit or implicit. Explicit means that the surface is the graph of a function
$F:\Omega\subset\mathbb{R}^2 \mapsto \mathbb{R}^3$ which can be very complicated to construct.
Especially complicated topologies this can usually be only done via 2d-parametric patches of the surface which have their own difficulties for remeshing.
Implicit surfaces on the other hand are defined via a functions level set (usually the zero level) ie. $F(x) = 0$ which is 
easier to construct but is harder to visualise. Usually then for visualization either marching-cubes or raytracing methods are used.

For the surface interpolation with an implicit function this translates to the interpolant being zero at the datasites: $S(x_i) = 0$.
Since the zero function would be a trivial solution to this, off-surface constraints must be given.
This is usually done with points generated from normalvectors to the surface that are given the value of the signed distance function ie. the value of the distance to the surface:

$$ S(\mathbf{x}_i + \epsilon \mathbf{n}_i) = F(\mathbf{x}_i+\epsilon \mathbf{n}_i) = \epsilon  
$${#eq:off_surface_points}
If not available, the normalvectors can be generated from a cotangent plane that is constructed via  a principal component analysis of nearest neighbors. 
This however is a nontrivial problem.
In my case the vectors could be obtained from an average of the normals of the adjacent triangles scaled with the inverse of the corresponding edgelengths:
$$\vec{n} = \sum_{T \in \mathcal{N}_T} \frac{1}{\lVert \vec{n}_T \rVert} \vec{n}_T$$
These offset-points were generated for every vertex of the original mesh and in both directions (on the inside and on the outside) such as to give the interpolant a constant slope of one around the surface.
This is done to have an area of convergence for a simple gradient-descent projection algorithm.



## Remeshing operations
Different approaches exist to remesh a surface. Most fall into one of the following categories:
- triangulate a commpletely new mesh, usually with delauney triangulation and go from there
- incremental triangulation, with new nodes inserted or removed one at a time. 
- local mesh modifications / pliant remeshing 

Additionally most methods utilize some form of vertex-smoothing as this is an straightforward iterative procedure that improves themesh globally and is guaranteed to converge. 

The approach used here falls into the latter category and uses consecutive loops of local mesh modifications of the following kinds:
- Edge collapse
- Edge split
- Edge flip
- Vertex smoothing

Which of the modification is applied depends on an edges length in comparison to a target-edge-length.


### Edge collapse

Edge collapse, as the name suggests removes an edge from the mesh thereby deleting two adjacent triangles and removing one point.
Special conditions have to be checked as there are certain configurations that would result in an illegal triangulation.
See figures @fig:collapse_e2 and \ref{fig:collapse_e1}
To avoid having to project a new midpoint to the surface, the two vertices of the edge are joined at either one of them.

![Edge collapse with the new point at one of the endpoints \label{fig:collapse}](source/figures/edge_collapse.svg){width=100%}

![Illegal edge collapse with more than two common neighbors for the edges endpoints \label{fig:collapse_e2}](source/figures/edge_collapse_error2.svg){#fig:collapse_e2 width=95%}

![Illegal edge collapse with a triangle flip \label{fig:collapse_e1}](source/figures/edge_collapse_error1.svg){width=100%}

### Edge split
The edge split is a straightforward operation as no special cases have to be taken care of. 
A new vertex is put at the surface projected midpoint of the existing edge and 4 new edges as well as 4 new triangles replace the split edge and it's adjacent triangles.

### Edge flip

![Edge flip \label{fig:edge_fip}](source/figures/edge_flip.svg){width=100%}

An edge flip can dramatically increase the aspect ratio of a triangle if the right conditions are met.
Consider the edge in figure \ref{fig:edge_flip}
Such an edge is flippable if:

- The edge does not belong to the boundary of the mesh
- The edge CD does not already belong to the mesh
- $\phi_{ABC} + \phi_{ABD} < \pi \quad \text{and} \quad \phi_{BAC}+ \phi_{BAD} < \pi$  
- The angle between the normals of the triangles is not too big to not cast "ridges"

I do a flip based on the following criteria:


### Vertex smoothing

![Vertex smoothing \label{fig:vertex_smooth}](source/figures/vertex_smoothing.svg){width=70%}

Vertex smoothing finds a new position for a given vertex based on the distance to its neighbors
according to the following formula:
$$\vec{p}' = \vec{p} + \alpha \sum_{j \in \mathcal{N}} f(\lVert\vec{p} - \vec{p}_j \rVert) (\vec{p}-\vec{p}_j)$$

Wherein $\mathcal{N}$ stands for the neighbors, $\alpha$ is a normalization constant and $f$ is a weight function.
Different weights have been investigated in [@bossen_pliant_nodate] where they constructed a well performing weight function.
Given a target edge length $t$ and an actual edge length $l$ a normalized edge length is defined as $d=l/t$ and the weight function reads:
$$f(d) = (1-d^4)\cdot e^{-d^4}$$

This function pushes if $l < t$ and slightly pulls if $t>l$.
The function is plotted in figure \ref{fig:smoothing_weights} versus the frequently used laplace weights.
Additionally, I clipped the movedistance to 80% of the minium of the  adjacent triangles heights.
This is done because moves that exceed this distance are likely to cause unacceptable triangles. 
What unacceptable means is defined in the algorithm section but is basically implemented as triangles with excess tilt versus the surface normal.


![The weight function used compared to the laplace weights \label{fig:smoothing_weights}](source/figures/weight_funcs.png){width=70%}



### Projection of vertices onto the surface

Both in an edge split as well as in vertex smoothing a constructed new vertex must be projected onto the surface.
To this end I use a simple gradient descent with a fixed steplength of one. This is a rather heuristical result
that has proven much better convergence than the exact steplength.
This is most probably due to the fact that around the surface the slope of the function is one by construction.



## Higher dimensional embedding 

The term higher dimensional embedding may sound a bit exaggerated for what is actually done. 
Namely, the pointnormals are included in an edges length calculation as to enlarge the edge when the normals differ.
Thereby, the the enlarged edges are remeshed more finely. 
Formally this reads as follows.
Given a vertex $x$ on the surface, it is concatenated with the surface normal $n$ at this point:

$$\Psi(x) = (x,y,z, \sigma n_x, \sigma n_y, \sigma n_z)^T$$

Here $\sigma$ is a parameter of the embedding and in effect controls how much an edge will be enlarged.
With this new $\Psi$ the edgelength between two points $a$ and $b$ will now be defined as:
$$l_{ab}^{6d}= \lVert \Psi(a) - \Psi(b)\rVert = \sqrt{(\Psi(a)-\Psi(b), \Psi(a)-\Psi(b))}$$

And in the same manner an angle between the points $a,b,c$ is defined via:
$$cos(\theta^{6d}_{abc})= \frac{(\Psi(a)-\Psi(c), \Psi(b)-\Psi(c))_{6d}}{l_{ac}^{6d}l_{bc}^{6d}}$$


