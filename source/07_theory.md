
# Theoretical backgrounds

## Topology optimization via the phase-field method

### The equations of linear elasticity

### Compliane minimization

### Phase-field formulation and advancing-front algorithms

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
$$(-1)^l g^l(t) \ge 0 \forall l \in \mathbb{N} \forall t>0$$
Then it can be shown that the interpolation matrix is always positive definite.
The proof relies on the Bernstein representation theorem for monotone functions. [see @buhmann_radial_nodate pp. 11-14 for the case of multiquadratics ]
A weaker reeqirement is that only one of the derivatives must be completely monotone.
This then leads to the concept of conditonally positive definiteness of a function in which polynomial is added to the interpolant. 

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
$\sqrt{1+r^2}$	    multiquadratics	             pd 
$1/\sqrt{1+r^2}$    inverse multiquadratics          pd 
$r^3$               polyharmonic spline	            cpd

Table: RBF functions with global support

function                         name                     definiteness 
-----------------                ------------------------ -------------
$(1-r)_+^4(4r+1)$                $\varphi_{3,1}(r)$           pd
$(1-r)_+^6(35r^2+18r+3)$         $\varphi_{3,2}(r)$           pd
$(1-r)_+^8(32r^3+25r^2+8r+1)$    $\varphi_{3,3}(r)$           pd

Table: Local RBF functions introduced by Wendland [@wendland_piecewise_1995]

## Remeshing operations

## Higher dimensional embedding 
