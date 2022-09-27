import os
import numpy as np
import matplotlib.pyplot as plt
from python.image import draw_image
from python.plot import *

os.system('mkdir -p plots/spacetime')

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
draw_light_cone(ax=ax)

fig.savefig('plots/spacetime/S_1.pdf')

# S' on S
draw_boost_axes(ax=ax, beta=beta)

fig.savefig('plots/spacetime/S_2.pdf')

draw_sim_lines(ax=ax, grad=0, which='y', lw=1, ls='--', c='0.5')
fig.savefig('plots/spacetime/S_3.pdf')

draw_sim_lines(ax=ax, grad=beta, which='y', lw=1, ls='--', c='b')
fig.savefig('plots/spacetime/S_4.pdf')

ax.plot( 0, 1, 'ko' )
fig.savefig('plots/spacetime/S_5.pdf')
ax.plot( 0, 2, 'ko' )
fig.savefig('plots/spacetime/S_6.pdf')
ax.plot( 0, 3, 'ko' )
fig.savefig('plots/spacetime/S_7.pdf')

pts = [ (0,1), (0,2), (0,3) ]
i=8
for x, y in pts:
    y = gamma**2 * y
    x = y*beta
    ax.plot( x, y, 'bP' )
    fig.savefig(f'plots/spacetime/S_{i}.pdf')
    i+=1

# frame S'
fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

draw_coord_axes(ax=ax, xrng=(-xmax, -xmin), yrng=(ymin, ymax), color='b', xlab="$x'$", ylab="$ct'$")
draw_light_cone(ax=ax)

fig.savefig('plots/spacetime/S_11.pdf')

# S' on S
draw_boost_axes(ax=ax, beta=-beta, color='k', xlab="$x$", ylab="$ct$")

fig.savefig('plots/spacetime/S_12.pdf')

