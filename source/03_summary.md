# Abstract {.unnumbered}

<!-- This is the abstract -->

In this work I implement and apply a relatively new triangular mesh remeshing approach by [@dassi_novel_2016] that facilitates a surface interpolation by Radial Basis Fuctions (RBFs).

While serving a representation of the surface for remeshing this interpolation allows to obtain normalvectors to the surface.
These are used in a higher-dimensional embedding sheme to yield a curvature adapted mesh i.e. 
smaller triangle-sizes where the curvature is larger.


As an application,
I wrote a script that incorporates my version of the algorithm
to remesh isosurfaces that I obtained from phase-field topology optimization calculations.

These topology optimizations were calculated on the servers of the Weierstraß Institute with their Finite-Element library pdelib.
To extract the isosurfaces I programmed an stl-export function for this library.


\pagenumbering{roman}
\setcounter{page}{1}
