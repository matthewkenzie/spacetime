import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from python.image import draw_image
from python.plot import *

os.system('mkdir -p plots/lightcone')

xmin = -1
xmax =  5
ymin = -1
ymax =  5

beta = 0.5
gamma = (1-beta**2)**(-0.5)

fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_sim_lines(ax=ax, grad=0, which='both', start=0, lw=1, ls='--', c='0.5')

p = (2,2)
d = 2.4

ax.axline( p, slope=1, lw=1, c='r', ls=':' )
ax.axline( p, slope=-1, lw=1, c='r', ls=':' )
ax.plot( [p[0]-d,p[0],p[0]+d], [p[1]-d,p[1],p[1]+d], 'r-', lw=1 )
ax.plot( [p[0]+d,p[0],p[0]-d], [p[1]-d,p[1],p[1]+d], 'r-', lw=1 )
patchf = mpatches.Ellipse( (p[0], p[0]+d), 2*d, 0.2, ec='r', fc='none', lw=1 )
patchp = mpatches.Ellipse( (p[0], p[0]-d), 2*d, 0.2, ec='r', fc='none', lw=1 )
ax.add_patch(patchf)
ax.add_patch(patchp)
ax.text(p[0], p[0]+d+0.22, 'FUTURE', c='r', va='bottom', ha='center', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})
ax.text(p[0], p[0]-d-0.22, 'PAST', c='r', va='top', ha='center', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})

ax.plot(2,2,'ko')
ax.text(2.2,2,"P", va='center')

fig.savefig('plots/lightcone/L_1.pdf')

fig, ax = plt.subplots(figsize=(4,4))
ax.axis('off')

draw_coord_axes(ax=ax, xrng=(xmin, xmax), yrng=(ymin, ymax))
draw_sim_lines(ax=ax, grad=0, which='both', start=0, lw=1, ls='--', c='0.5')

p = (2,2)
d = 2.4

undefR = mpatches.Polygon( [ p, (xmax,ymin), (xmax,ymax) ], closed=True, fill=True, ec='none', fc='0.8', alpha=0.8 )
undefL = mpatches.Polygon( [ p, (xmin,ymin), (xmin,ymax) ], closed=True, fill=True, ec='none', fc='0.8', alpha=0.8 )
ax.add_patch(undefR)
ax.add_patch(undefL)
ax.text(4,p[0], "Undefined", c='k', ha='center', va='center', bbox={'fc':'0.85', 'alpha': 1, 'ec': 'none'} )
ax.text(0,p[0], "Undefined", c='k', ha='center', va='center', bbox={'fc':'0.85', 'alpha': 1, 'ec': 'none'} )

ax.axline( p, slope=1, lw=1, c='r', ls=':' )
ax.axline( p, slope=-1, lw=1, c='r', ls=':' )
ax.plot( [p[0]-d,p[0],p[0]+d], [p[1]-d,p[1],p[1]+d], 'r-', lw=1 )
ax.plot( [p[0]+d,p[0],p[0]-d], [p[1]-d,p[1],p[1]+d], 'r-', lw=1 )
patchf = mpatches.Ellipse( (p[0], p[0]+d), 2*d, 0.2, ec='r', fc='none', lw=1 )
patchp = mpatches.Ellipse( (p[0], p[0]-d), 2*d, 0.2, ec='r', fc='none', lw=1 )
ax.add_patch(patchf)
ax.add_patch(patchp)
ax.text(p[0], p[0]+d+0.22, 'FUTURE', c='r', va='bottom', ha='center', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})
ax.text(p[0], p[0]-d-0.22, 'PAST', c='r', va='top', ha='center', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})

fig.savefig('plots/lightcone/L_2.pdf')

ax.plot(2,2,'ko')
ax.text(2.2,2,"P", va='center')

ax.plot(3,4,'go')
ax.text(3.2,4,"Q", va='center', c='g', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})

ax.plot(1.8,0.5,'go')
ax.text(2,0.5,"R", va='center', c='g', bbox={'fc':'w', 'alpha': 0.8, 'ec':'none'})

ax.plot(4,3.2,'bo')
ax.text(4.2,3.2,"S", va='center', c='b')

ax.plot(4,0.5,'bo')
ax.text(4.2,0.5,"T", va='center', c='b')

fig.savefig('plots/lightcone/L_3.pdf')
plt.show()
