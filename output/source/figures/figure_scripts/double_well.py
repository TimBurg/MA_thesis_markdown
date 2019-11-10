import numpy as np
import matplotlib.pyplot as plt
from math import exp

def double_well(x):
    return 1/4*(x**2 - x)**2

def obstacle(x):
    return (1-x)*x

plotting_range_dw=np.linspace(-.5, 1.5, 100)
plotting_range_obs=np.linspace(0., 1., 100)

fix,axes=plt.subplots(1,2, sharey=False, figsize=[10, 5])

# axes[0].axhline(xmax=2, color='k', linestyle='-')
# axes[1].axhline(xmax=2, color='k', linestyle='-')

axes[0].set_title('double well potential')
axes[1].set_title('obstacle potential')
# axes[0].set_xlabel('d')
# axes[1].set_xlabel('d')

plot1=axes[0].plot(plotting_range_dw, np.array([double_well(x) for x in plotting_range_dw]))
plot2=axes[1].plot(plotting_range_obs, np.array([obstacle(x) for x in plotting_range_obs]))

axes[0].set_ylim(0, 0.1)

axes[1].vlines([0,1], ymin=0, ymax=.5, colors='C0')
axes[1].set_ylim(0, .5 )


# plot1.axis['xzero'].set_axisline_style("-|>")
# plot2.axis['xzero'].set_axisline_style("-|>")

plt.savefig('../double_well.png', dpi=90, pad_inches=0.0)

