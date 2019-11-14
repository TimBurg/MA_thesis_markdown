# Appendix{.unnumbered}

## Non manifold-errors of meshes

Triangluar meshes can have a multitude of minor errors that unfortunately are very much tolerated in cad-programs and 
3D-software but can cause issues with additive manufacturing and algorithms that rely on contiguous surfaces or closed volumes.
Among the common errors are:

- duplicate vertices/edges/triangles
- a surface that is not closed i.e has a boundary
- incoherent triangle normals (flipped triangles)
- self intersection or overlapping triangles

## Interpolation with conditionally positive definite functions {#sec:conditional}

Definition:
  ~ A continuous even function $\Phi:\mathbb{R}^d \mapsto \mathbb{R}$ is conditionally positive (semi) definite
    of order m if and only if for all pairwise distinct $X = {x_1, ... ,x_N } \subset \mathbb{R}^d$ 
    and all $\alpha \in \mathbb{R}^d\setminus\{0\}$ that satisfy 
    $$\sum_j^N \alpha_j p(x_j) = 0 \qquad \forall p\in \Pi_{\mathbb{R}^d}^m$$
    the quadratic form
    $$\sum_{j,k}^N \alpha_j \alpha_k \Phi(x_j - x_k)$$ 
    is (nonnegative) positive.
    Here $\Pi_{\mathbb{R}^d}^m$ is the space of polynomials of maximal order m.
    

Theorem:
  ~ Let a univariate function $\phi \in C[0,\infty) \bigcap C^\infty(0,\infty)$ be given.  
    The mutlivariate function $\Phi$ defined by $\Phi=\phi(\lVert \cdot \rVert^2_2)$ is conditionally positive semi definite
    of order $m\in\mathbb{N}$ on every $\mathbb{R}^d$ if and only if
    $(-1)^m \phi^{(m)}$ is completely monotone on $(0,\infty)$ [@wendland_scattered_2005 theorem 8.19]

The interpolation condition is then to be modified and the the interpolant takes the following form:
$$S(x) = \sum_{j=1}^N \alpha_j \Phi(x - x_j) + \sum_{k=1}^Q \beta_k p_k(x)$$

Where $Q$ is the dimension of the polynomial space and the $p_k$ form a basis.
The interpolation condition is complemented by the the condition:
$$\sum_{j=1}^N \alpha_j p_k(x_j) = 0 \qquad 1\leq k \leq Q$$

The linear interpolation system can then be written in the compact form:
\begin{equation}
\begin{pmatrix}
A_{\Phi} & P \\
P^T & 0 
\end{pmatrix}
\begin{pmatrix}
\alpha \\
\beta 
\end{pmatrix}
=
\begin{pmatrix}
f \\
0 
\end{pmatrix}
\end{equation}

With $P = p_k(k_j) \in \mathbb{R}^{Q \times N}$
This system is solvable if $\Phi$ is conditionally positive definite [@wendland_scattered_2005 theorem 8.21]


# References{.unnumbered}

<div id="refs"></div>

