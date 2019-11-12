
# Problems, outlook and future work

As already stated in the algorithm section, the performance of the remeshing algorithm posed to be a major drawback for larger meshes.
The easiest way to influence this is not to interpolate the input mesh but rather approximate the mesh with fewer functions.
This would also provide a superior smoothing than the Taubin smoothing used here and would allow to use a dense interpolation matrix.
In [@carr_reconstruction_2001-1] this approach was realized with a greedy algorithm that starts with a simple interpolant and
iteratively includes more meshpoints into the interpolation where
a large error is encountered.


As the pliant remeshing relies on local mesh modifications that include deleting, manipulating and adding entities,
an optimised datastructure can give another performance benefit. With smaller data sizes and by reusing the memory of 
deleted objects, less fragmentation can be achieved which gives a better cache performance. 
An approach to this that I would recommend is to utilize an unrolled linked list with points, edges and triangles 
stored side-by side rather than using individual datastructures. 

Also the vertices could be stored in a on-demand resized array to then utilize a vectorized(parallelised) version of the vertex smoothing.



This would be ideally implemented in a statically typed programming language like C/C++ or the more modern Julia.


Datastructures for unstructured graphs are 

The surface interpolation with the local Wendland radial basis functions has worked very well and was only dependent on choosing
a good $\varepsilon$.



Combine interpolation and smoothing into one step with a lower order RBF function that is fitted rather than interpolates.
See Buhmann Chapter 8 or >Reconstruction and Representation of 3D Objects with Radial Basis
Functions paper<

- The unstructured graph datastructure scaled very poorly to larger meshes ie. excessive cache misses yielded a poor performance.
  This is a fundamental problem for pliant remeshing and may be adressed with good datastructures that preserve neighborhood to some degree. 
- fitting with RBFs would have been more appropiate to incorporate the smoothing and reduce the number of RBFs.
  However, projections might not work so well without offset constraints.
- 6d flips work poorly for refinement due to mesh normals being a limited indicator of mesh accuracy -> some long edges remain due to equal normals.
- surface interpolation works well and projections were fast and reliable.

Immediate requirement for a practicable method: faster datastructure and mesh fitting.
