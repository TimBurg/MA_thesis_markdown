
# Theoretical backgrounds

First I present the theory for the topology optimization that was used. 
This includes a brief recapitulation of linear elasticity and compliance minimization and then a short 
derivation of the optimality conditions and the discretizations that are applied to iterate towards them numerically.
After that the extration of the isosurface, the radial basis function based surface interpolation and the remeshing operations are introduced.

## Linear elasticity

### The equations of static elasticity
Mathematical elasticity can be considered a branch of continuum dynamics whose research reaches as far back as the late 16th century.
I only give a short outline of the stepstones to linear elasticity that are mostly based on  
the book mathematical elasticity by Ciarlet which is a comprehensive standard piece on the topic.

Continuum dynamics deals with a body occupying a lipschitz-continuous reference configuration $\overline{\Omega}\subset \mathbb{R}^3$ under rest which is deformed to a
configuration $\Omega \subset \mathbb{R}^3$ by applied forces.
The deformation is described by an injective mapping $\varphi$ via a displacement field $u:\overline{\Omega} \mapsto \Omega$:
$$\varphi:\overline{\Omega} \mapsto \Omega \qquad \varphi=id+u$$
For the static case treated here, the deformation is time independent.
The deformation and displacement mappings are required to be two times continuously differentiable but this reqirement can be relaxed in the variational formulation of the equations. 
I denote the coordinates in the reference configuration with $x$ and and those in the deformed configuration with $x^\varphi = \varphi(x)$. 
In engineering textbooks those coordinates are sometimes referred to as Lagrange- and Euler-coordinates respectively.

The elasticity theory is then build on the following two contributions from Cauchy of which the second is fundamental to continuum dynamics:

1. Axiom of force balance:

   Given volume- and surface-force-densities as $f^\varphi$ and $g^\varphi$  in the deformed configuration then for every subset
   $A^\varphi \subset \Omega$ the following equality holds:
   $$\int_{A^\varphi} f^\varphi(x^\varphi) dx^\varphi + \int_{\partial A^\varphi} t^\varphi(x^\varphi,n^\varphi)da^\varphi = 0$$
   Here, $dx^\varphi$ and $da^\varphi$ are the volume and surface elements in the deformed configuration, $n^\varphi$ is the surface-unit-normal and $t^\varphi$ is the Cauchy stress vectorfield defined as:
   $$t^\varphi:\Omega \times \mathbb{S}_1 \mapsto \mathbb{R}^3 \quad where \quad \mathbb{S}_1 := \{v \in \mathbb{R}^3\:|\: \lVert v \rVert = 1 \}$$
   Note that the Cauchy stress vector $t^\varphi$ depends on the given volume $A$ only through the normal vector at a surface point and
   that any surface-force dictated on part of $\partial A \cap \partial\Omega$ must be dispersed through 
   the remaining part of $\partial A$.

2. Stress Tensor theorem:

   Assuming that $f^\varphi$ is continuous and 
   ${t^\varphi \in \textrm{C}^1(\Omega) \cap \textrm{C}(\mathbb{S}_1)}$,
   then $t^\varphi$ is linear w.r.t. 
   to the surface normal i.e.:
   \begin{subequations}\label{eq:equilibrium}
   \begin{align}
   t^\varphi (x^\varphi, n) &= T^\varphi (x^\varphi)n \qquad \forall x^\varphi \in \Omega, \! &\forall n \in \mathbb{S}_1\\
   &\text{and additionally} \nonumber\\
     -\text{div}^\varphi T^\varphi (x^\varphi) &= f^\varphi   &\forall x^\varphi \in \Omega \label{eq:divT} \\
     T^\varphi (x^\varphi) &= T^\varphi (x^\varphi)^T         &\forall x^\varphi \in \Omega \\
     T^\varphi (x^\varphi) n^\varphi &= g^\varphi(x^\varphi)  &\forall x^\varphi \in \Gamma_g^\varphi
   \end{align}\end{subequations}
   where $\Gamma_g^\varphi$ is the part of $\partial \Omega$ where the boundary condition $g$ is prescribed 
   and $\text{div}T = \partial_j T_{ij}, e_i$
   [See @philippe_ciarlet_mathematical_1990 p.63-65 for the proof].

Notice that the formulation above uses the stress tensor in the deformed configuration where it is symmetric.
The pullback of the tensor onto the reference configuration is achieved with the Piola-transformation after which it needs 
to be symmetrized again. This then yields the so-called first and second Piola-Kirchhoff-Stress-Tensors of 
which the latter is denoted with $\Sigma$.
A change in the force densities due to the deformation is often ignored. Such forces are then called dead loads
[see @philippe_ciarlet_mathematical_1990 chapter 2.7].

The equilibrium equations for them are omitted here for brevity but the second Piola-Kirchhoff-Stress is the stress tensor to be determined in the next chapter.

Another thing that is important is that the boundary condition can and will only be prescribed on a part of the boundary.

### Stess, strain and the equations of equilibrium in the linear case
So far the theory is valid for all continuums but there are also nine unknown functions, 
namely the three components of the deformation and the six components of the stress tensor.
However, several simplifications can be made in the case of isotropic and homogeneous media that lead to a remarkably simple form of the tensor.

To this end the (right-) Chauchy (Green) strain tensor $C$ and its difference from unity $E$ is introduced.
I will refer to $E$ simply as the strain tensor.
They describe the first order change in local length-scale under a deformation and are defined via the 
Fréchet derivative of the mapping $\varphi\mathrm{,} \: \nabla \varphi$:

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
2. Material-Frame Indifference (invariance under changes of coordinates)
3. Isotropy of the material
4. Rivlin-Ericksen representation theorem for matrices
5. Homogeneity of the material

Details on these steps can again be found in [@philippe_ciarlet_mathematical_1990 chapter 3].
After following these steps, $\Sigma$ takes on the following form:
$$\Sigma(C) = \lambda (\mathrm{tr}E)I + 2\mu E + o(\lVert E \rVert)$$

Here, $\lambda$ and $\mu$ are the Lamé coefficients of the material and $I$ is the identity tensor.
In the linear theory that is used as the basis for the topology optimization, the strain $E$ is replaced with 
its linearized version $\varepsilon$: 
$$\varepsilon = \frac{1}{2}( \nabla u^T + \nabla u )$$

this yields the following even simpler form of the tensor which is referred to as $\sigma$:

$$\sigma = \lambda ( \nabla u) I + \mu \left(\nabla u + \nabla u^T \right)$$
The more prominent form of which is called Hooks-law and written with the so-called stiffness tensor that is unfortunately also named $C$ in the literature:
\begin{equation} \sigma = C : \varepsilon \qquad \text{or} \qquad \sigma = C \varepsilon \label{eq:stiffness}\end{equation}

Here, the second form is written in vector notation for the components of the tensors and
the following tensoroperation for rank 2 tensors  is introduced that will be used in the coming sections:
$$G:V :=  \sum_{i,j} G_{ij} V_{ij}$$

### Variational formulation
For finite-element simulations and reduced smoothness requirements of the displacement, a variational formulation of the equilibrium equations \eqref{eq:equilibrium} must be formulated.

For this we first define the space $$
H^1_D = \{\theta \in H^1(\Omega, \mathbb{R}^3) \mid \theta=0 \text{ on } \Gamma_D=\partial \bar{\Omega} - \Gamma_g \}\, ,$$
to exclude the boundary on $\Gamma_D$ from contributing its force terms.

Multiplying equation \eqref{eq:divT} with a test function $\theta$ from this space on both sides and integrating 
yields ($\cdot$ denotes the scalar product):
$$\int_{\Omega^\varphi} \text{div}^\varphi T^\varphi \cdot \theta^\varphi \: dx^\varphi = -\int_{\Omega^\varphi} f^\varphi \cdot
\theta^\varphi \: dx^\varphi + \int_{\Gamma_g^\varphi} g^\varphi \cdot \theta^\varphi \: da^\varphi \, ,$$
which has to hold for all test functions $\theta \in H^1_D$.

Using the Greens-formula for Tensor fields:
$$\int_{\bar{\Omega}} \text{div} H \cdot \theta \  dx = - \int_{\bar{\Omega}} H:\nabla \theta \ dx + \int_\Gamma Hn\cdot \theta \ da $$
and applying the pullback to the reference configuration with the second Piola-Kirchhoff-Stress-tensor then gives:

$$\int_{\bar{\Omega}} \nabla \varphi \Sigma : \nabla \theta \: dx = \int_{\bar{\Omega}} f 
\cdot \theta \: dx + \int_\Gamma g \cdot \theta \: da \qquad \forall \theta \in H^1_D$$

For All vector fields $\theta: \bar{\Omega} \mapsto \mathbb{R}^3$ from $H^1_D$.
This is also called the 'principle of virtual work' (in the reference configuration).

For very small strains the deformation gradient in front of $\Sigma$ can be dropped since the 
diplacement gradient multiplied with the stress-tensor is of second order in $\nabla u$. [see @braess_finite_2013 p.280] 

Furthermore, since the product of a symmetric tensor with an antisymmetric one is zero, we split $\nabla \theta$ into:
$\left[ \frac{1}{2}(\nabla \theta + \nabla \theta^T) + \frac{1}{2}  (\nabla \theta - \nabla \theta^T)\right]$

And thus we write the equilibrium equation in the variational form as:
\begin{equation}
\int_{\bar{\Omega}} \sigma \frac{1}{2}(\nabla \theta + \nabla \theta^T) = \int_{\bar{\Omega}} \sigma \varepsilon(\theta) =
\int_{\bar{\Omega}} f \cdot \theta dx + \int_\Gamma g \cdot \theta da  \quad \forall \theta \in H^1_D \label{eq:equi_variational}
\end{equation}


For the following sections I denote this as the following shorthand notation using the inner product 
and the stiffness tensor from \eqref{eq:stiffness}:
$\langle A,B \rangle_C = \int_{\bar{\Omega}} A: CB$ :

\begin{equation}\langle \varepsilon(u), \varepsilon(\theta)\rangle_{C(\varphi)} = \int_{\bar{\Omega}} f \cdot \theta \: dx + 
\int_\Gamma g \cdot \theta \: da =: F(\theta) \qquad \forall \theta \in H^1_D \label{eq:compliance}\end{equation}

Notice that I sneaked a dependence of the stiffness tensor on a parameter $\varphi$ into the equation that will be made concrete in the following chapter.
The well posedness of this weak formulation is proved using the Lax-Milgram Lemma and Korns Inequality in [@blank_relating_2014 Theorem 3.1]

For an actual deformation rather than a virtual one, the functional $F$ in \eqref{eq:compliance} represents the compliance of the structure.
This compliance is what is to be optimized in the following section. 

## Topology optimization

The topology optimization procedure used in this work is a direct implementation of the works of [@blank_relating_2014].
As a result of this I frequently refer to this paper and those relating to it and only strive to give a compact summary of the steps.
A phase field based topology optimization was first introduced by [@bourdin_design-dependent_2003]. It has has similarities to the 
SIMP-method[^1]
introduced by Bendsøe over a decade earlier (see [@bendsoe_topology_2004] for a reference thereof).

![Example of a topology optimised structure in 2D. source:[@ebeling-rump_topology_2019]](./source/figures/ebeling_2d_bridge.png)


The term topology optimization was coined in the context of optimizing mechanical structures.
It is not bound to a certain implementation but to the requirement that a structure under load may change its topology under the optimization procedure.
For this the facility of nucleation of holes in a previously filled material is generally needed.

The method used throughout this work which accomplishes this is based on minimizing a functional with gradient based optimization.
The functional is constructed from a compliance term and a regularization term for the  phasefield.
In effect, compliance minimization maximizes the stiffness of the structure while a mass- or volume constraint formulated via the phase field controls where material is placed in the domain. 

The use of a phase-function description allows to incorporate a computationally cheap perimeter regularization via an additional term in the optimization functional.
This is needed since the compliance minimization in itself is not well posed and allows high variation in 
the microstructure of a part that cannot be manufactured and is not numerically stable.
This can manifest itself as a checkerboard like pattern in the phasefield.

[^1]:Solid Isotropic Material with Penalization

### Compliance minimization

Compliance is a very common goal function for topology optimization and defined as in equation \eqref{eq:compliance}:
$$F(u) = \int_{\bar{\Omega}} f \cdot u + \int_\Gamma g \cdot u $$

Here, $u$ is the displacement solution of the mechanical system in the left-hand side of equation \eqref{eq:compliance}

However, it is still open at this time how the compliance depends on the structure of the part.
This dependence is actually encoded in the Stiffness-tensor $C$ of the mechanical system that will be constructed from the 
phase field after it is defined in the next section.

### The phase-field description and regularization energy

For the modeling of structures either a level set method or a phase field description is viable.
In case of the phase-field a continuous function is chosen 
that here can take on values in the range from 0 to 1 where 0 represents the void and 1 the material:
$$ 0 \leq \varphi \leq 1$$

A penalty term is then added to the optimization to force the phasefield to condensate to either 0 or 1 depending on a forcing term from the compliance minimization.
Consequently an interface between the two phases forms whose change is subject to the resulting Allen-Cahn type equation which can drive the interface in
the direction of its normal. This falls into the category of advancing-front algorithms. For details see [@barles_front_1993]
or [@blank_phase-field_2010].
For an understanding of the convergence of the induced dynamics I consider the optimality conditions of the system.


Since integrating the phase field over a region gives the volume, a volume constraint
is imposed by requiring the integral to be equal to a parameter $m$ which then
dictates how much of the design domain is allowed to be material:
$$\int_\Omega \varphi \: dx = m \cdot \text{vol}(\Omega)$$

Bear in mind that values in the intermediate range of $\varphi$ distort this relationship.
However, since they only occur in the interfacial region that will be forced to occupy a neglible portion of the domain, this is can be neglected.

For the reading convenience I stipulate the requirements on $\varphi$ in the following space:
$$\mathcal{G}^m = \big\{\varphi \in H^1(\Omega, \mathbb{R})) \quad \big| \quad 0\leq \varphi \leq 1 \quad \text{and} \quad \int_\Omega \varphi dx = m \cdot \text{vol}(\Omega) \big\}$$
These requirements are later taken care of by terms from the Karush-Kuhn-Tucker theory, namely the complementary slackness and a Lagrange multiplier.

As stated, an additional term has to be added to the compliance functional as to enforce a condensation of the phasefield and 
regularize the occurence of jumps. The term used is due to [@takezawa_shape_2010] and is called the Ginzburg-Landau Energy:

$$ E^\varepsilon = \int_\Omega \frac{\varepsilon}{2} |\nabla \varphi|^2 + \frac{1}{\varepsilon} \Psi(\varphi) dx $$

The potential $\Psi(\varphi)$ serves as the condensation potential that forces the phase field to either 0 or 1.
Here, an obstacle potential is used while for the analysis, a differentiable double-well potential is considered:
$$\Psi_\text{dw}(\varphi) = \frac{1}{4} (\varphi^2 - \varphi)^2$$

$$\Psi_\text{obs} = \begin{cases} (1-\varphi)\varphi,  \quad \text{if}\ \varphi \in [0,1]\\
			           \infty \quad \text{else}
\end{cases}$$
The two potentials are displayed in figure \ref{fig:potentials}

![The two potentials in the Ginzburg-Landau energy term \label{fig:potentials}](source/figures/double_well.png){width=70%}

### Interpolation of the stiffness tensor and gravitational force
Using this phasefield, an interpolating stiffness tensor can be constructed.
The stiffness tensor in the void is modeled by a very soft material $C_\text{void}$.
For the interpolation in the interfacial region towards the material tensor $C_\text{mat}$ a linear interpolation with a superimposed 
transition function $t(\varphi) = \varphi^3$ is used:
$$C(\varphi) = C_\text{mat} t(\varphi) + C_{void} (1- t(\varphi)) $$

Also, the force $f$ occuring in the mechanical system can now be made concrete.
Namely the phase-field acts as a direct scaling factor for the mass density $\rho_{\text{mat}}$ and excludes the void from contributing any forces:

$$f = \varphi \cdot \rho_\text{mat} \cdot G_z \quad \text{with} \  G_z=9.81 \cdot [0, 0, 1]^T \: "N"$$

$$F(u, \varphi) = \int_{\bar{\Omega}} \varphi \cdot \rho_\text{mat} \cdot G_z \cdot  u + \int_{\Gamma_g} g \cdot u $$

### The optimal control problem
I now state the first order necessary optimality conditions for a minimum which are given by the Karush-Kuhn-Tucker theory.  

As indicdated before, the goal is to minimize the functional made up of the compliance and the Ginzburg-Landau term:
$$ \text{min}\ J(u, \varphi) := \gamma E(\varphi) + F(u, \varphi) \quad \text{with} \ \varphi \in \mathcal{G}^m \text{ and } u\ 
\text{ fulfills eq }\eqref{eq:compliance}$$ 
Here $\gamma$ is a parameter that controls the influence of the regularization term and it's will value will determine the fineness of 
the obtained structure.

To write down the optimality conditions in a concise form, consider the control-to-state operator 
$S(\varphi) = u$ defined implicitly by equation \eqref{eq:compliance}. 
It's directional derivative $S'(\varphi)h = p$ is given by the solution to:

\begin{equation}\langle \varepsilon(p), \varepsilon(\eta)\rangle_{C(\varphi)} =
 \langle \varepsilon(u), \varepsilon(\eta)\rangle_{C'(\varphi)h} - \int_{\bar{\Omega}} h \cdot f \cdot \eta  \quad \forall \eta \in H^1_D
 \label{eq:control_to_state}
 \end{equation}

[see @blank_relating_2014 theorem 3.3]. Here $p$ is also a function from $H^1_D$.

It follows from the definition of the total differential and the chain rule that the reduced functional 
$\widetilde{J}(\varphi)= J(S(\varphi), \varphi)$ is
Fréchet-differentiable with the derivative:
$$\tilde{J}'(\varphi) h = \frac{\partial}{\partial u} J(u,\varphi) p + \frac{\partial}{\partial \varphi} J (u, \varphi) h$$

Since $E(\varphi)$ is independent of $u$, the partial derivative with respect to $u$ is just the right-hand side of the state equation:

$$\frac{\partial}{\partial u} J(u, \varphi) p = F(p,\varphi) $$
Here I have used that the Fréchet derivative of a linear functional in a direction $p$ is the functional applied to that direction.


This is, since $p \in H^1_D$ is an admissible test function in the state equation, equal to the left hand side of the state equation.
Note that if this was not the case, an auxillary state $q \in H^1_D$ could have been introduced which would solve a system sometimes called the adjoint system as to make the following equality hold. 

Now using equation \eqref{eq:control_to_state} with $u$ as a test function this can be written as:

\begin{align}
\frac{\partial}{\partial u} J(u, \varphi) p &= F(p,\varphi)=\langle \varepsilon(u), \varepsilon(p)\rangle_{C(\varphi)} 
&= -\langle \varepsilon(u), \varepsilon(u)\rangle_{C'(\varphi)h} -  \int_{\bar{\Omega}} h \cdot f \cdot u
\end{align}

The calculation of the partial derivative of $J$ with respect to $\varphi$ is straightforward:

$$\frac{\partial}{\partial \varphi}J(u,\varphi) \xi = \gamma \varepsilon \int_\Omega (\nabla \varphi , \nabla \xi) \ dx +
\gamma \int_\Omega \frac{1}{\varepsilon} \Psi'(\varphi) \xi \ dx  + F(u,\xi)$$

Summing up and using $\xi = h$ as the direction in which to 
derive, the reduced functional has the following
directional derivative:
\begin{equation}
\frac{d}{d \varphi} \tilde{J}(\varphi) \xi = 2 \cdot F(u, \xi) + \gamma \int_\Omega \varepsilon \nabla \varphi \nabla \xi +
\frac{1}{\varepsilon} \Psi'(\varphi) \xi \ dx 
 - \langle \varepsilon(u), \varepsilon(u)\rangle_{C'(\varphi)\xi}
\end{equation}

To incorporate the constraints on $\varphi$ we now follow the Karush-Kush-Tucker theory.
For this to work we have to make sure a constraint qualification is satisfied.
Here we consider the slater condition that, for an itermediate density material distribution in the whole domain 
is obviously satisfied. Thus we can assume strong duality and the complentarity follows.

To reconsider, we have the following additional requirements

\begin{align}
\int_\Omega \varphi - m \ dx &= 0 \\
\varphi -1 &\leq 0 \\
-\varphi   &\leq 0 
\end{align}

Introducing lagrange multipliers $\kappa \in \mathbb{R}, \text{ and } \mu_+, \mu_- \in L^2(\Omega)$ the KKT-first order necessary optimality conditions then read:

\begin{align}
\frac{d}{d\varphi} \tilde{J}(\tilde{\varphi}) \omega + \kappa \int_\Omega \omega \ dx + \mu_+ \omega - \mu_- \omega  &= 0 \quad \forall \omega \in H^1_D \label{eq:gradient}\\
\langle \varepsilon(\tilde{u}), \varepsilon(v)\rangle_{C(\varphi)} &= F(\tilde{u}, v)  \quad \forall v \in H^1_D \\
\int_\Omega \tilde{\varphi} - m \ dx &= 0 \label{eq:mass_constraint}\\
\mu_+ \geq 0,& \quad \mu_- \geq 0 \quad \text {a.e. in } \Omega\\
(\mu_+, \tilde{\varphi} -1) &= 0 \quad \text {a.e. in } \Omega \label{eq:complementary1}\\
(\mu_-, -\tilde{\varphi}) &= 0 \quad \text {a.e. in } \Omega \label{eq:complementary2}
\end{align}

Where the last three conditions arise due to complementarity.

### Numerial soution

#### Pseudo time stepping
Suppose for a moment that $\kappa, \mu_+ \text{ and } \mu_-$ were given.
This is reasonable because in the next section, iterates for those functions are given by means of a Primal-Dual Active Set strategy. 
Then we could solve for $\tilde{\varphi}$ in the optimality conditions as follows. Equation \eqref{eq:gradient} 
defines a linear functional on $H^1_D$ which I refer to as $\nabla \mathcal{L} (\omega)$. Using a scalar product this functional can be identified
with a funtion on $L^2$ that we loosely call the gradient. This approach is called a gradient flow. 
Consequently a gradient descent in conjunction with a semi-implicit stepping scheme can be used.

$$\left( \partial_t \varphi, \omega \right) = \nabla \mathcal{L} (\omega)$$

Expanding the functional would give:

\begin{equation}
\begin{split}
\left( \partial_t \varphi, \omega \right) =&  \gamma  \int_\Omega \varepsilon \nabla \varphi \nabla \omega
+ \frac{1}{\varepsilon} \Psi'(\varphi) \omega \: dx + 2 \cdot F(u, \omega) \\
 &- \langle \varepsilon(u), \varepsilon(u)\rangle_{C'(\varphi)\omega} + \kappa \int_\Omega \omega \ dx + \mu_+ \omega - \mu_- \omega  
\end{split} \label{eq:gradflow}
\end{equation}

We start with some initial function $\varphi^k, \ k=0$.
Inserting for $\partial_t \varphi$ its approximation $\frac{\varphi^{k+1}-\varphi^k}{\tau}$ 
and using $\nabla \varphi^{k+1}$ for $\nabla \varphi$ we end up with:

\begin{equation}
\begin{split}
\frac{1}{\tau} \int_\Omega \varphi^{k+1} \omega dx + \gamma \varepsilon \int_\Omega \nabla \varphi^{k+1} \nabla\omega dx =&
\frac{1}{\tau} \int_\Omega \varphi^{k} \omega dx \\
&+ \frac{\gamma}{\varepsilon} \int_\Omega \Psi'(\varphi^k) \omega dx + \langle \varepsilon(u), \varepsilon(u)\rangle_{C'(\varphi^k)\omega} \\
&- 2 \int_\Omega \omega \rho_0 g u dx + \kappa \int_\Omega \omega \ dx + \mu_+ \omega - \mu_- \omega
\end{split}
\label{eq:descent_iteration}
\end{equation}
Where, as before, $u$ solves the mechanical system \eqref{eq:equi_variational}.
This defines an iterative scheme for a descent.

#### Primal-dual active set strategy
As stated the 
A sophisticated method to alleviate the Lagrange multipliers $\mu_+$ and $\mu_-$ from this equation is the Primal-Dual Active Set strategy (PDAS).
The theory to this approach was developed in [@blank_primal-dual_2013].

In essence, PDAS maintains a set of active constraints for every point.  
A constraint is inactive if the corresponding lagrange multiplier is zero and active if $\varphi$ takes on the corresponding bound -
One of which has to hold due to the equations \eqref{eq:complementary1} and \eqref{eq:complementary2}.

These sets are then updated by first solving the so-called primal problem which is \eqref{eq:descent_iteration} without $\mu_\pm$ but 
\eqref{eq:mass_constraint} explicitly cared for.
With the then obtained $\varphi$ and $\kappa$ a dual problem for the $\mu_\pm$ Lagrange multipliers is solved.

More precisely, let $\mu = \mu_+ - \mu_-$ then \eqref{eq:complementary1} and \eqref{eq:complementary2} can be equivalently written as
$$c(\varphi(x) -1) + \mu(x) \geq 0 \quad \text{and} \quad c(- \varphi(x)) + \mu(x) \leq 0$$
respectively for any $c > 0$.

With this the active sets $\mathcal{A}^+ \text{ and } \mathcal{A}^-$ as well as the inactive set $\mathcal{I}$ are defined as:
\begin{equation}
\begin{split}
\mathcal{A}^+ &= \{x\in \Omega \mid c(\varphi(x) -1) + \mu(x) \geq 0 \}\\
\mathcal{A}^- &= \{x \in \Omega \mid c(- \varphi(x)) + \mu(x) \leq 0 \}\\
\mathcal{I}   &= \Omega \setminus (\mathcal{A}^+ \cup \mathcal{A}^-) 
\end{split}
\end{equation}

Starting with a guess of those sets, $\varphi$ is set 1 on $\mathcal{A}^+$ and 0 on $\mathcal{A}^-$.
Consequently the unconstrained iteration step \eqref{eq:descent_iteration} (where $\mu_\pm$ is 0) with \eqref{eq:mass_constraint} explicitly 
accounted for is solved only on the set $\mathcal{I}$.
This is referred to as the primal problem.
Note that due to the definition, $\mathcal{I}$ is synonymous to the interfacial region that takes up a very small portion of the space
thereby making this calculation efficient.

Subsequently the Lagrange multiplier $\mu$ can be updated on $\mathcal{A}^\pm$ with a dual formulation according to [@blank_primal-dual_2013 (PDAS-I)] as follows:
$$\mu = \kappa - \frac{1}{\tau}(\varphi^{k+1} - \varphi^k) + \varepsilon \gamma \Delta \varphi^{k+1} + \frac{\gamma}{\varepsilon} \varphi^{k+1} $$

With this updated $\mu$, the active and inactive sets are recalculated and if no change is detected the descent step is complete.
Otherwise reiterate with the new sets.


### Isosurface extraction
After a calculation has converged, a 0.5 isofurface is used that represents the surface of the part. 

Since the Finite-Element-Mesh is providing a 3D-tesselation of the domain, which in this case consists of tetrahedra, the generation of an isosurface is handled as in the marching-tetrahedra algorithm. 
Tetrahedra, as opposed to cubes, can only have 3 distinct cases of edge intersections that differ in terms of their makeup of triangular faces. No intersections, intersection at 3 edges(1 triangle) and intersection at 4 edges (2 triangles). See figure \ref{fig:isocuttetraeder} for an illustration.

For the edge intersections, a linear interpolation of the values between two vertices is used. 
The intersections are then found via simple line intersections comparable to the section of the x-axis for a line.
If 3 intersections are found one triangle is generated with the vertices of the intersections and if 4 intersections are found 2 triangles are generated.
Susequently the ordering of the vertices is checked so that looking from the outside, 
the vertices are ordered counterclockwise in accordance with the 
stl-specification^[stl is one of the primary file formats for triangular meshes]. 
For this, the function values at the tetrahedra-nodes are considered to find a point that is inside (has a value greater than 0).
This is especially important since the orientation is used in the remeshing procedure and can only be correctly determined at this step.

![In the case of a 3D-Tetrahedra tesselation only 3 distinct cases can appear a)intersection
at three edges(left) or b)intersection at 4 edges(right) or c)no intersections(not displayed)\label{fig:isocuttetraeder}](source/figures/tetrahedrons.svg){width=80%}

## radial basis function theory

### RBF Interpolation

Interpolation can be viewed as a special kind of approximation in which, for an approximant $S$ to some function $F$,
it is demanded that the interpolant reproduces the original functions values at special points $x_i$ i.e.:
\begin{equation}S(x_i) = F(x_i) \quad \forall x_i \in \Xi \label{eq:interpolation_condition} \end{equation}
Where $\Xi$ is some finite (possibly scattered) set of pairwise distinct points from $\mathbb{R}^d$ (multivariate) ie. a 
set $\{x_i \mid x_i \in \mathbb{R}^d, i=1,..,N, x_i \neq x_j\}$.
The functions considered here are scalar valued multivariate functions but a vector-valued interpolant may be constructed from scalar-valued-component functions.

Interpolants are constructed from some function space which in this case is made up of radial basis functions centered at 
the interpolation centers. This dependence on the centers means that the radial basis function-spaces are individual to each dataset $\Xi$.

Radial basis functions are multivariate functions constructed from univariate functions of the form 
$\phi:[0,\infty)\mapsto\mathbb{R}$ superimposed over the Euclidean norm:
$$\Phi(x) = \phi(\lVert x \rVert_2) \qquad x\in \mathbb{R}^d$$
Special monotonicity properties of those functions lead to unisolvent interpolation (unique solvability) as explained in the next section.
Radial basis functions can also be introduced as general multivariate functions $\Phi:\mathbb{R}^d\mapsto\mathbb{R}$ that then need
to be even: $\Phi(x) = \Phi(-x)$.
The norm usually denotes the standard Euclidean norm which is essential for the convergence results.
Some information about other norms is given in [@wendland_scattered_2005 p.83,84].
In the following $d$ will be 3 as required for the generation of implicit 2-d surfaces.


Notably, radial basis functions are special in that they allow easy interpolation of scattered multivariate data of arbitrary dimension with 
guaranteed existence and uniqueness results. 
At the time of writing this is unique to these functions and can not be achieved by for example "classical" polynomial interpolation. 


As for the approximation quality, different interpolants do behave differently for the space in between the data sites and are distinguished by 
their approximation and or convergence properties for special classes of interpolated functions $F$.
However, when no such functions (just the values $F(x_i)$) are given, the accuracy of an interpolation can not generally be assessed.
Because this is the case here, determining qualities for the RBF-interpolant are discussed in [@sec:surf_cond].

The interpolant $S$ is constructed as a linear combination of scaled radial basis functions centered at the
data sites:
$$S(x) = \sum_j^N \alpha_j\phi(\lVert x-x_j\rVert)$$


By introducing the interpolation matrix $\vec{A}$ as:
\begin{equation}A_{ij}= \phi(\lVert x_i - x_j\rVert)|_{i,j} \label{eq:interpolation_matrix}\end{equation}
we can write the interpolation condition \eqref{eq:interpolation_condition} as:
\begin{equation}\vec{A}\alpha = \vec{F} \label{eq:interpolation_system}\end{equation}
Where $\vec{F}$ contains the values $F(x_i)$.

The immediate requirement then is that this system is uniquely solvable which is determined by the invertibility of the interpolation matrix $A$

### Existence and Uniqueness results
The invertbility of the interpolation matrix $A$ for all pairwise distinct combinations of 
centers in $\mathbb{R}^d$ is considered.
This property can be guaranteed for certain radial basis functions which satisfiy a montonicity property.

Definition:
  ~ A continuous function $\Phi:\mathbb{R}^d \mapsto \mathbb{R}$ is called positive \mbox{(semi-)}definite if, for all $N \in \mathbb{N}$ and
    all sets of pairwise distinct points $X=\{x_1, ... ,x_N \} \subseteq \mathbb{R}^d$ and all $\alpha \in \mathbb{R}^N$ the
    following quadratic form is (nonnegative) positive:
    $$\sum_{j=1}^N \sum_{k=1}^N \alpha_j \alpha_k \Phi(x_j - x_k)$$

Analogously, I call the univatiate functions $\phi$ positive (semi-) definite if the induced function $\Phi$ satisfies the definition.

Such induced positive semi definiteness of a function can be shown via a property called complete monotonicity: 
$$(-1)^l g^l(t) \ge 0 \quad \forall l \in \mathbb{N} \quad \forall t>0$$
Where $g^l$ denotes the l-th derivative of a function $g: \mathbb{R} \mapsto \mathbb{R}$.
The prototype of a complete monotone function is the exponential function $e^{-\alpha t}$ for some non negative $\alpha$.

Theorem:
  ~ If $\phi(\sqrt{\cdot})$ is completely monotone on $[0, \infty)$ and not constant, then $\phi$ is positive definite.

The proof requires some theory on measure spaces and generalized fourier transforms and rests on the Bernstein-Widder representation of 
such functions.
Since these are a bit out of scope I refer to [@wendland_scattered_2005 theorem 7.14].

A first formal proof of a positive definite function was completed for the multiquadratics function by [@micchelli_interpolation_1986].
Multiquadratics are not completely monotone but rather one can show that it actually suffices that the first derivative of $\phi$ is 
completely monotone [@buhmann_radial_2003 theorem 2.2].

Complete monotonicity of only some derivative motivates a weaker concept called conditionally positive definiteness and requires an added polynomial for unisolvence.
This is described in the Appendix [@sec:conditional].

### Commonly used Radial basis functions 
I now state some of the more often used RBFs and give some detail on the local functions that were used for the actual implementation.
During the course of writing the interpolation program it became clear that only local basis functions would be good 
candidates for a surface interpolation due to the number of vertices used in most triangular meshes
and the resulting size of a dense interpolation matrix.
But also the conditon number of the interpolation matrix is problematic for large interpolation sets.
To this end the compactly supported basis functions are also much more forgiving. 
I recite some estimates of the condition number in the Appendix.

Local, piecewise polynomial RBFs are generally dimension dependent in that they are not positive definite 
for $d>d_0$ in $\mathbb{R}^d$ where $d_0$ depends on the function. For this application $d_0 = 3$ is required and 
reflected in the chosen Wendland function.

Now commonly used are the Wendland functions [see @wendland_piecewise_1995] which are of 
minimal degree with respect to the space dimension and smoothness and are positive definite. 
For the surface interpolation I use the twice continuously differentiable function and it's derivative in table [@tbl:local_RBF]

function             name                     definiteness 
-----------------   ------------------------ -------------
$e^{-r^2}$          gaussian                         pd
$\sqrt{r^2 +1}$	    multiquadratics	             pd 
$1/\sqrt{r^2+1}$    inverse multiquadratics          pd 
$r^3$               polyharmonic spline	            cpd

Table: RBF functions with global support

function                         name                     definiteness  smoothness
-----------------                ------------------------ ------------- ----------
$(1-r)_+^2$                      $\phi_{3,0}(r)$           pd           $C^0$
$(1-r)_+^4(4r+1)$                $\phi_{3,1}(r)$           pd           $C^2$
$(1-r)_+^6(35r^2+18r+3)$         $\phi_{3,2}(r)$           pd           $C^4$
$(1-r)_+^8(32r^3+25r^2+8r+1)$    $\phi_{3,3}(r)$           pd           $C^6$

Table: Local RBF functions introduced by Wendland [@wendland_piecewise_1995]{#tbl:local_RBF}


![Comparison of different RBF functions. Note that multiquadratics are special in their growth to infinity.
The Wendland functions become zero after r=1](source/figures/rbf_functions.png){#fig:rbf_funcs width=100%}

### Scaling of RBF functions, ambiguities and interpolation properties {#sec:rbf_interpol}
The Wendland RBF functions have a fixed support radius of 1 as seen in @fig:rbf_funcs.
Since spacing of the interpolation data is not fixed, a scaling of the radial argument needs to be introduced that scales $r$ such that the RBFs
 extend into the space between the data sites. Otherwise the interpolant might just have, in the exteme case, spikes at the sites to attain the required values.
To this end I scale $r$ with a scale parameter $c > 0$ as $r' = r/c$ since that makes the Wendland functions extend to exactly the value of this scale parameter.


This scaling parameter, in general can be nonuniform over the interpolated values but this comes with uncertainty for the solvability of the interpolation system.

Moreover, it cannot be generally stated which value of a scale parameter is more accurate in an interpolation unless there is a target to which the interpolant can be compared. See @fig:wendland_scales

![Wendland C2 functions for different scaling parameters c. The interpolation values were set to (1,2,1,2,1) at (0,1,2,3,4).
](source/figures/wendland_scale_factors.png){#fig:wendland_scales width=100%}

![Different Radial-Basis-Funtions may have different behaviours for off-site values. Multiquadratics can even grow toward infinity.
Displayed is a 1-2 comb in two dimensions](source/figures/MQ_2D_comb.png){#fig:MQ_2D width=100%}

### surface interpolation {#sec:surface_interpol}
Surface descriptions are either explicit or implicit. Explicit means that the surface is the graph of a function
$F:\Omega\subset\mathbb{R}^2 \mapsto \mathbb{R}$ which can be very difficult to construct.
Especially for complicated topologies, this can usually be only done via 2d-parametric patches of the surface which are difficult to 
match at the boundaries.
Implicit surfaces on the other hand are defined via a functions level set (usually the zero level i.e. $F(x) = 0$) which is 
easier to construct but is harder to visualise. Common methods for visualization include marching-cubes and raytracing methods.

For the surface interpolation with an implicit function this translates to the interpolant being zero at the data sites: $S(x_i) = 0$.
Since the zero function would be a trivial solution to this, off-surface constraints must be given.
This is usually done with points generated from normalvectors to the original surface if such surface exists.
The pointvalues are then assigned the valuea of the signed distance function to the surface:

$$ S(\mathbf{x}_i + \epsilon \mathbf{n}_i) = F(\mathbf{x}_i+\epsilon \mathbf{n}_i) = \epsilon  
$${#eq:off_surface_points}
For a stronger falloff(rise) of the interpolant larger values than $\epsilon$ can be chosen as interpolation values on the right hand side.
If not available, the normalvectors can be generated from a cotangent plane that is constructed via  a principal component analysis of nearest neighbors. 

In my case the vectors could be obtained from an average of the normals of the adjacent triangles scaled with the inverse of the corresponding edgelengths:
$$\vec{n} = \sum_{T \in \mathcal{N}_T} \frac{1}{\lVert \vec{n}_T \rVert} \vec{n}_T$$
These offset-points were generated for every vertex of the original mesh and in both directions (on the inside and on the outside) such as to have
a guaranteed area of convergence of a gradient descent projection.


## Remeshing operations{#sec:remeshing_ops}
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
See figures [@fig:collapse_e2] and [@fig:collapse_e1].
To avoid having to project a new midpoint to the surface, the two vertices of the edge are joined at either one of them.

![Edge collapse with the new point at one of the endpoints](source/figures/edge_collapse.svg){#fig:collapse}

![Illegal edge collapse with more than two common neighbors for the edges endpoints](source/figures/edge_collapse_error2.svg){#fig:collapse_e2 width=95%}

![Illegal edge collapse with a triangle flip](source/figures/edge_collapse_error1.svg){#fig:collapse_e1}

Both cases are easily cared for.
The case of more than two common neighbors can be checked in a graph datastructure
and to check if a triangle was flipped the normal before and after the operation have to be compared.

### Edge split
The edge split is a straightforward operation as no special cases have to be taken care of. 
A new vertex is put at the surface projected midpoint of the existing edge and 4 new edges as well as 4 new triangles replace the split edge and it's adjacent triangles.

The only pitfall than can occur is that the projection of the midpoint with a gradient descent can sometimes project inside another
triangle therefore yielding flipped triangles.
This again need to be checked with a normal-flip check

### Edge flip{#sec:edge_flip}

![Edge flip ](source/figures/edge_flip.svg){#fig:edge_flip}

An edge flip can dramatically increase the aspect ratio of a triangle if the right conditions are met.
Consider the edge in [@fig:edge_flip].
Such an edge is flippable if:

- The edge does not belong to the boundary of the mesh
- The edge CD does not already belong to the mesh
- $\phi_{ABC} + \phi_{ABD} < \pi \quad \text{and} \quad \phi_{BAC}+ \phi_{BAD} < \pi$  
- The angle between the normals of the triangles is not too big to not cast "ridges"

I do a flip according to [@dassi_novel_2016] if the 6d angles of the points opposing the to-be flipped edge $\phi_{BDA} \text{ and } \phi_{ACB}$ together are larger than $\pi$:

$$\phi_{BDA}^{6d} + \phi_{ACB}^{6d} \geq \pi$$

For the definition of those angles see [@sec:HDE].
A value of $\kappa$ near one is problematic in conjunction with the higher dimensional embedding
since the HDE angle seldom takes on values of $\pi/2$ or larger due to the surface-normals
in the 6d-scalar product not being orthogonal. This results in flips not actually taking place.


### Vertex smoothing

![Vertex smoothing \label{fig:vertex_smooth}](source/figures/vertex_smoothing.svg){width=70%}

Vertex smoothing finds a new position for a given vertex based on the distance to its neighbors
according to the following formula:
$$\vec{p}' = \vec{p} + \alpha \sum_{j \in \mathcal{N}} f(\lVert\vec{p} - \vec{p}_j \rVert) (\vec{p}-\vec{p}_j)$$

Wherein $\mathcal{N}$ stands for the neighbors, $\alpha$ is a normalization constant and $f$ is a weight function.
Different weights have been investigated in [@bossen_pliant_1998] where they constructed a well performing weight function.
Given a target edge length $t$ and an actual edge length $l$ a normalized edge length is defined as $d=l/t$ and the weight function reads:
$$f(d) = (1-d^4)\cdot e^{-d^4}$$

This function pushes if $l < t$ and slightly pulls if $t>l$ as opposed to the frequently used Laplace-smoothing which only pulls.
The function is plotted in figure \ref{fig:smoothing_weights} versus Laplace weights.
Additionally, I clipped the movedistance to 80% of the minium of the  adjacent triangles heights.
This is done because moves that exceed this distance are likely to cause triangles that are excessively tilted against the surface yet not flipped. 
These might then cause problems in later operations. 

One of those problems occurs due to the pushing nature of the smoothing that tends to squish larger 
triangles into thin strips when attached short
edges are pushing the vertex into the direction of least resistance. 
Thin strip triangles should then usually be flipped and consequently push back but this can fail due to the requirements 
for the edge flip and consequently yield distorted triangles.


![The weight function used compared to the laplace weights \label{fig:smoothing_weights}](source/figures/weight_funcs.png){width=70%}



### Projection of vertices onto the surface

Both in an edge split as well as in vertex smoothing a constructed new vertex must be projected onto the surface.
To this end I use a simple gradient descent iterations with a fixed steplength of one. This
has proven much faster convergence than the exact steplength.
This is due to the fact that around the surface the slope of the function is one by construction.

The descent algorithm reads as follows

\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoLined
\SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}
\Input{$x_0 \text{ and } eps \text{ and interpolant } f$}
\BlankLine
i=0 \;
\While{$i<$ steplimit}{
    \uIf{i mod 3==0}{
	calculate $\nabla f(x_i)$ \;
	}
    calculate $f(x_i)$ \;
    \uIf{ $f(x_i) <$ eps}{\Return{$x_i$}} 
    stepsize $=\frac{f}{\lVert \nabla f(x_i) \rVert}$ \;
    clip stepsize \;
    $x_{i+1} = x - \text{ stepsize } \cdot \nabla f(x_i)$ \;
}
\caption{Project a vertex $x_0$ onto the surface}
\end{algorithm} 



## Higher dimensional embedding{#sec:HDE} 

The term higher dimensional embedding may sound a bit exaggerated for what is actually done. 
Namely, the pointnormals are included in an edges length calculation as to enlarge the edge when the normals differ.
Thereby, the the enlarged edges are remeshed more finely. 
Formally this reads as follows.
Given a vertex $x$ on the surface, it is concatenated with the surface normal $n$ at this point:

$$\Psi(x) = (x,y,z, \sigma n_x, \sigma n_y, \sigma n_z)^T$$

Here $\sigma$ is a parameter of the embedding and in effect controls how much an edge will be enlarged.
With this new $\Psi$ the edgelength between two points $a$ and $b$ will now be defined with the 6d Euclidean scalar product as:
$$l_{ab}^{6d}= \lVert \Psi(a) - \Psi(b)\rVert_{6d} = \sqrt{(\Psi(a)-\Psi(b), \Psi(a)-\Psi(b))_{6d}}$$

And in the same manner an angle between the points $a,b,c$ is defined via:
$$cos(\theta^{6d}_{abc})= \frac{(\Psi(a)-\Psi(c), \Psi(b)-\Psi(c))_{6d}}{l_{ac}^{6d}l_{bc}^{6d}}$$

These edgelengths are subsequently used as the regulator for the local mesh modifications in the remeshing algorithm.
The 6d angles are therein used in the edge flips.


