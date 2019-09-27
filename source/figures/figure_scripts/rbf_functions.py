from math import sqrt
import numpy as np

def MQ( r,  c) :
    return np.sqrt((r)**2 + c)

# def  MQ_deriv( r,  c) :
    # return r/sqrt((r)**2+c)

def inverse_MQ( r,  c) :
    return 1/np.sqrt((r)**2 + c)

# def  inverse_MQ_deriv( r,  c) :
    # return -r/sqrt((r**2+c)**3)

def Wendland_C2(r,   phi) :
    return np.maximum(1-(r/phi),0.)**4*(4*(r/phi)+1)

# def  Wendland_C2_deriv( r,  phi) :
    # return max(1-(r/phi),0)**3*(-r/phi)*20

import matplotlib.pyplot as plt

plotting_range=np.linspace(0, 2, 100)

fig, ax = plt.subplots(1,1, figsize=(8,4))

ax.set_xlabel('r')
ax.plot(plotting_range, MQ(plotting_range, 1.), label='Multiquadratics')
ax.plot(plotting_range, inverse_MQ(plotting_range, 1.), label='Inverse multiquadratics')
ax.plot(plotting_range, Wendland_C2(plotting_range, 1.), label='Wendland C2')

plt.legend(loc='upper left')
# plt.show()

plt.savefig('../rbf_functions.png', dpi=90, pad_inches=0.0)

