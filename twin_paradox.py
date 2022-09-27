import os
import numpy as np
import matplotlib.pyplot as plt
from python.image import draw_image
from python.plot import *

os.system('mkdir -p plots/twin_paradox')

xmin = -1
xmax =  6
ymin = -1
ymax =  6
imgs = (1,1.3)

beta = 0.5
gamma = (1-beta**2)**(-0.5)

#################################
## Draw S frame and observer O ##
#################################

fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

# S frame
draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_light_cone(ax=ax)
draw_image('image.jpeg', ax=ax, beta=0, extent=[0,imgs[0],0,imgs[1]])

#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara1.pdf')

# S' frame on S
draw_boost_axes(ax=ax, beta=beta)
draw_image('image.jpeg', ax=ax, beta=beta, extent=[0,imgs[0],0,imgs[1]], color='b')

#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara2.pdf')

## now after time T
T = 4
dt = gamma*T
dx = beta * dt
fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')
# S frame
draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_light_cone(ax=ax)
draw_image('image.jpeg', ax=ax, beta=0, extent=[0,imgs[0],T,T+imgs[1]])
# S' frame on S
draw_boost_axes(ax=ax, beta=beta)
draw_image('image.jpeg', ax=ax, beta=beta, extent=[0,imgs[0],T,T+imgs[1]], color='b')
#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara3.pdf')

# Sim lines S
draw_sim_lines(ax=ax, grad=0, which='y', lw=1, ls='--', c='0.5')
#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara4.pdf')

# Sim lines S'
draw_sim_lines(ax=ax, grad=beta, which='y', lw=1, ls='--', c='b')
#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara5.pdf')

#################################
## Draw S' frame and observer O' ##
#################################

fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

# S' frame
draw_coord_axes(ax=ax, xrng=(-xmax,-xmin), yrng=(ymin,ymax), color='b', xlab="$x'$", ylab="$ct'$")
draw_image('image.jpeg', ax=ax, beta=0, extent=[0,imgs[0],T,T+imgs[1]], color='b')
draw_light_cone(ax=ax)

# S frame on S'
draw_boost_axes(ax=ax, beta=-beta, color='k', xlab="$x$", ylab="$ct$")
draw_image('image.jpeg', ax=ax, beta=-beta, extent=[-imgs[0],0,T,T+imgs[1]], color='k')
#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara6.pdf')

# draw sim lines
draw_sim_lines(ax=ax, grad=0, which='y', lw=1, ls='--', c='b')
draw_sim_lines(ax=ax, grad=-beta, which='y', lw=1, ls='--', c='k')

#fig.tight_layout()
fig.savefig('plots/twin_paradox/twpara7.pdf')

########################
## Do the return journey
########################

## now after time T
T = 4
dt = gamma*T
dx = beta * dt
fig, ax = plt.subplots(figsize=(4,20/3))
ax.axis('off')
# S frame
draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, 10))
draw_light_cone(ax=ax)
draw_image('image.jpeg', ax=ax, beta=0, extent=[0,imgs[0],T,T+imgs[1]])
# S' frame on S
draw_boost_axes(ax=ax, beta=beta)
draw_image('image.jpeg', ax=ax, beta=beta, extent=[0,imgs[0],T,T+imgs[1]], color='b')

# Sim lines S
draw_sim_lines(ax=ax, grad=0, which='y', stop=4, lw=1, ls='--', c='0.5')

# Sim lines S'
draw_sim_lines(ax=ax, grad=beta, which='y', stop=3, lw=1, ls='--', c='b')

# Coord S''
draw_boost_axes(ax=ax, beta=-beta, origin=(2,4), color='g',xlab="$x''$", ylab="$ct''$")
draw_sim_lines(ax=ax, grad=-beta, which='y', start=5, lw=1, ls='--', c='g')
fig.savefig('plots/twin_paradox/twpara8.pdf')

draw_image('image.jpeg', ax=ax, beta=-beta, extent=[T+T/3,T+T/3+imgs[0],6.66,6.66+imgs[1]], color='g')
fig.savefig('plots/twin_paradox/twpara9.pdf')

########################
## And back at x=0
########################

## now after time T
T = 8
dt = gamma*T
dx = beta * dt
fig, ax = plt.subplots(figsize=(4,20/3))
ax.axis('off')
# S frame
draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, 10))
draw_light_cone(ax=ax)
draw_image('image.jpeg', ax=ax, beta=0, extent=[0,imgs[0],T,T+imgs[1]])
# S' frame on S
#draw_boost_axes(ax=ax, beta=beta)
draw_boost_axes(ax=ax, beta=beta, xlab="", ylab="", arrows=False)
draw_image('image.jpeg', ax=ax, beta=beta, extent=[0,imgs[0],T,T+imgs[1]], color='b')

# Sim lines S
draw_sim_lines(ax=ax, grad=0, which='y', stop=4, lw=1, ls='--', c='0.5')

# Sim lines S'
draw_sim_lines(ax=ax, grad=beta, which='y', stop=3, lw=1, ls='--', c='b')

# Coord S''
#draw_boost_axes(ax=ax, beta=-beta, origin=(2,4), color='g',xlab="$x''$", ylab="$y''$")
draw_boost_axes(ax=ax, beta=-beta, origin=(2,4), color='g',xlab="", ylab="", arrows=False)
draw_sim_lines(ax=ax, grad=-beta, which='y', start=5, lw=1, ls='--', c='g')

draw_image('image.jpeg', ax=ax, beta=-beta, extent=[5.333,5.333+imgs[0],10.66,10.66+imgs[1]], color='g')
fig.savefig('plots/twin_paradox/twpara10.pdf')
#plt.show()
