
# Problems, outlook and future work

## On the performance issues

As already stated in the algorithm section, the performance of the remeshing algorithm posed to be a major drawback for larger meshes.
The easiest way to influence this is not to interpolate the input mesh but rather approximate the mesh with fewer functions.
This would also provide a superior smoothing than the Taubin smoothing used here and would allow to use a dense interpolation matrix.
In [@carr_reconstruction_2001-1] this approach was realized with a greedy algorithm that starts with few interpolation centers and
iteratively includes more centers into this quasi-interpolant where the error to the original mesh is largest.
They can fit very detailed meshes with small errors with 80.000 centers.
As a comparison, the bridge mesh was interpolated with over 128.000 centers.

Another improvement that sounds promising is to evaluate radial basis functions iteratively via the Fast Multipole method [see @buhmann_radial_2003, chap. 7.3]. How suitable this is for the required amount of centers compared to a parallelization of the distance calculation has to be seen.   

As the pliant remeshing relies on local mesh modifications that include deleting, manipulating and adding entities,
an optimised datastructure can give a good performance benefit. With smaller data sizes and by reusing the memory of 
deleted objects, less fragmentation can be achieved which gives a better cache performance. 
An approach to this that I would recommend is to utilize an unrolled linked list with points, edges and triangles 
stored side-by side rather than using individual datastructures. 

Also the vertices could be stored in an on-demand resized array to then utilize a vectorized(parallelised) version of the vertex smoothing.
This would be ideally implemented in a statically typed programming language like C/C++ or the more modern Julia.

## Conclusion on the conducted surface remeshing

The surface interpolation with the local Wendland radial basis functions has worked well and was only dependent on choosing
a fitting $\varepsilon$. The projection onto that surface was robust and converged fast for all testmodels.


3 Different topology optimization meshes have been remeshed. It was found that a surface interpolation with the local Wendland functions 
is feasible even for a compound model. However, a fitted surface would incorporate a superior smoothing and reduce the computational cost.

Furthermore the utilization of the 6d angles in the edge flips angle condition was related to some anomalies in the remeshing procedure.
The exact nature of these remained unresolved which due to the fact that they only resulted in the later iterations of the remeshing.

For a practicable remeshing a more accurate mesh error may be given by the interpolant value itself rather than its normal.
For this an even closer relationship between the interpolant and the signed distance function may be established.


It was also found that the vertex smoothing weightfunction by [@bossen_pliant_1998] has to be used with a triangle flip check
since the then pushing nature of the smoothing often results in turning/angular momentum.





