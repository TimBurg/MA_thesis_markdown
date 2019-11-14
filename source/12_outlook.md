
# Problems, outlook and future work

As already stated in the algorithm section, the performance of the remeshing algorithm posed to be a major drawback for larger meshes.
The easiest way to influence this is not to interpolate the input mesh but rather approximate the mesh with fewer functions.
This would also provide a superior smoothing than the Taubin smoothing used here and would allow to use a dense interpolation matrix.
In [@carr_reconstruction_2001-1] this approach was realized with a greedy algorithm that starts with few interpolation centers and
iteratively includes more centers into the quasi-interpolant where the error to the original mesh is largest.
They can fit detailed meshes with small erros with 80.000 centers.
As a comparison, the bridge mesh was interpolated with over 10 million centers.

Another improvement can be made by evaluating radial basis functions iteratively via the Fast Multipole method [see @buhmann_radial_2003, chap. 7.3].

As the pliant remeshing relies on local mesh modifications that include deleting, manipulating and adding entities,
an optimised datastructure can give a good performance benefit. With smaller data sizes and by reusing the memory of 
deleted objects, less fragmentation can be achieved which gives a better cache performance. 
An approach to this that I would recommend is to utilize an unrolled linked list with points, edges and triangles 
stored side-by side rather than using individual datastructures. 

Also the vertices could be stored in a on-demand resized array to then utilize a vectorized(parallelised) version of the vertex smoothing.
This would be ideally implemented in a statically typed programming language like C/C++ or the more modern Julia.

The surface interpolation with the local Wendland radial basis functions has worked well and was only dependent on choosing
a fitting $\varepsilon$. The projection onto that surface was robust and converged fast.


Another possibility to generate an adaptive mesh without relying on the higher dimensional embedding is to use the interpolants values as an indicator for
accuracy of meshpoints. This is possible because close to the surface the interpolant has the shape of the signed distance function.
Using quadrature points on triangles/edges the volume/area under the surface defined by the approximant/interpolant and the mesh entity could be calculated.
