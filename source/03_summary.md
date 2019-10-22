# Abstract {.unnumbered}

<!-- This is the abstract -->

In this work I implement and extend a triangular mesh remeshing approach by [@dassi_novel_2016] that facilitates a surface interpolation by Radial Basis Fuctions (RBFs). 

While serving a representation of the surface for remeshing this interpolation also allows to obtain a normalvector to the surface
which is used in a higher-dimensional embedding sheme to yield a curvature adapted mesh ie. 
smaller triangle-sizes where the curvature is larger.

Some fundamental issued with the approach are presented and discussed.

As an application,
I wrote a remeshing-program that incorporates the algorithm with some corrections 
to remesh isosurfaces that I obtained from phase-field topology optimization calculations.

The topology optimizations were calculated with a software library pdelib custom to the Weierstrass-Institute.

Both the calculation and the remeshing were conducted on the Weierstraß-servers.


\pagenumbering{roman}
\setcounter{page}{1}
