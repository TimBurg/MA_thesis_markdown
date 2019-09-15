import numpy as np
import matplotlib.pyplot as plt
from math import exp

def default_weights( x):
    x4=-(x**4)
    return (1+x4)*exp(x4)

def laplace_weights( x):
    return min(1-x, x)

plotting_range=np.linspace(0,2, 100)

fix,axes=plt.subplots(1,2, sharey=True, figsize=[5, 2.5])

axes[0].axhline(xmax=2, color='k', linestyle='-')
axes[1].axhline(xmax=2, color='k', linestyle='-')

axes[0].set_title('laplace weights')
axes[1].set_title('used weights')
axes[0].set_xlabel('d')
axes[1].set_xlabel('d')

plot1=axes[0].plot(plotting_range, np.array([laplace_weights(x) for x in plotting_range]))
plot2=axes[1].plot(plotting_range, np.array([default_weights(x) for x in plotting_range]))

# plot1.axis['xzero'].set_axisline_style("-|>")
# plot2.axis['xzero'].set_axisline_style("-|>")

plt.savefig('../weight_funcs.png', dpi=90, pad_inches=0.0)

