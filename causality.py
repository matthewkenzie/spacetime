import os
import numpy as np
import matplotlib.pyplot as plt
from python.image import draw_image
from python.plot import *

os.system('mkdir -p plots/causality')

xmin = -1
xmax =  5
ymin = -1
ymax =  5

beta = 0.5
gamma = (1-beta**2)**(-0.5)

# frame S
fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_sim_lines(ax=ax, grad=0, which='both', lw=1, ls='--', c='0.5')
draw_light_cone(ax=ax, orig=(2,2))
ax.plot(2,2,'ko')
ax.text(2.2,2,"P", va='center')

ax.plot(3,4,'ko')
ax.text(3.2,4,"Q", va='center')

fig.savefig('plots/causality/C_1.pdf')

draw_boost_axes(beta=0.6, origin=(2,2), ax=ax, which='x')

for y in np.linspace(3, 5, 3):
    ax.axline( (2,y), slope=0.6, lw=1, ls='--', c='b' )

fig.savefig('plots/causality/C_2.pdf')

fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_sim_lines(ax=ax, grad=0, which='both', lw=1, ls='--', c='0.5')
draw_light_cone(ax=ax, orig=(2,2))
ax.plot(2,2,'ko')
ax.text(2.2,2,"P", va='center')

ax.plot(3.9,4,'ko')
ax.text(3.2,4,"Q", va='center')

fig.savefig('plots/causality/C_3.pdf')
draw_boost_axes(beta=0.95, origin=(2,2), ax=ax, which='x', color='g')

for y in np.linspace(2, 3, 5):
    ax.axline( (2,y), slope=0.95, lw=1, ls='--', c='g' )

fig.savefig('plots/causality/C_4.pdf')


plt.show()
