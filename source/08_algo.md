
# Algorithm description and implemenation details

## interpolation 
As stated in section ... first, the off-surface values are calculated via the original meshes vertices and triangle normals as follows:

$$ v_{\text{off}} = v \pm \varepsilon \vec{n_v} $$

where n_v is assembled via the triangles containing $v$ as follows

$$\vec{n_v} = \sum_{T \in \mathcal{N}_T} \frac{1}{\lVert \vec{v} - \vec{\text{cent}} \rVert} \vec{n}_T$$

## remeshing 

## projection step


