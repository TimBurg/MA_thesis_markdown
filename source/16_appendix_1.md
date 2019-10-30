# Appendix 1: Some extra stuff {.unnumbered}

<!-- 
This could be a list of papers by the author for example 
-->

# Non manifold-errors of meshes

Triangluar meshes can have a multitude of minor errors that unfortunately are very much tolerated in cad-programs and 3D-software but can cause issues with 

# Interpolation with conditionally positive definite functions

The interpolation condition is to be modified and the the interpolant takes the following form:
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

