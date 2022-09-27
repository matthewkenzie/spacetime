import numpy as np

def draw_coord_axes(xrng=(-5,5), yrng=(-5,5), ax=None, color="k", xlab="$x$", ylab="$ct$"):
    ax = ax or plt.gca()
    ax.plot( xrng, (0,0), c=color, ls='-', lw=1.5 )
    ax.plot( (0,0), yrng, c=color, ls='-', lw=1.5 )
    ax.plot(1, 0, ">", c=color, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^", c=color, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.text(1, -0.07, xlab, transform=ax.get_yaxis_transform(), c=color, ha='right', va='top', fontsize=14)
    ax.text(-0.07, 1, ylab, transform=ax.get_xaxis_transform(), c=color, ha='right', va='top', fontsize=14)
    ax.set_xlim(xrng)
    ax.set_ylim(yrng)

def draw_boost_axes(beta, origin=(0,0), ax=None, color='b', xlab="$x'$", ylab="$ct'$", arrows=True, which='both'):
    ax = ax or plt.gca()
    if which=='both' or which=='x':
        ax.axline( origin, slope=beta,   c=color, lw=1.5 )
    if which=='both' or which=='y':
        ax.axline( origin, slope=1/beta, c=color, lw=1.5 )
    #ep1 = ( ax.get_xlim()[1], ax.get_xlim()[1]*beta )
    #ep2 = ( ax.get_ylim()[1]/beta, ax.get_ylim()[1] )
    #ax.plot( *ep1, c='k', marker=(3,0,np.arctan(beta)), clip_on=False )
    angle = np.degrees(np.arctan(beta))
    rott = 270 + angle
    rotx = 360 - angle
    # arrows
    xax = ( ax.get_xlim()[1], origin[1]+beta*(ax.get_xlim()[1]-origin[0]) )
    yax = ( origin[0]+beta*(ax.get_ylim()[1]-origin[1]), ax.get_ylim()[1] )
    xrot = angle
    yrot = 90-angle if beta>0 else 180+90-angle
    xdiff = ax.get_xlim()[1] - ax.get_xlim()[0]
    ydiff = ax.get_ylim()[1] - ax.get_ylim()[0]
    if arrows:
        if which=='both' or which=='x':
            ax.plot( xax[0], xax[1], c=color, ms=8, marker=(3,0,rott), clip_on=False )
            ax.text( xax[0], xax[1]-0.05*ydiff, xlab, c=color, ha='right', va='top', fontsize=14, rotation=xrot)

        if which=='both' or which=='y':
            ax.plot( yax[0], yax[1], c=color, ms=8, marker=(3,0,rotx), clip_on=False )
            ax.text( yax[0]-0.01*xdiff, yax[1]+0.03*ydiff, ylab, c=color, ha='right', va='top', fontsize=14, rotation=yrot)

def draw_light_cone( ax=None, orig=(0,0) ):
    ax.axline( orig, slope=1, lw=1, c='r' )
    ax.axline( orig, slope=-1, lw=1, c='r' )

def draw_sim_lines(ax=None, steps=1, grad=1, which='both', start=None, stop=None, skip_zero=True, **kwargs):
    xsims = ( which=='x' or which=='both' )
    ysims = ( which=='y' or which=='both' )

    if ysims:
        for i in np.arange(*ax.get_ylim(), steps):
            if skip_zero and i==0:
                continue
            if start is not None and i<start:
                continue
            if stop is not None and i>stop:
                continue
            ax.axline( (0,i), slope=grad, **kwargs )

    if xsims:
        for i in np.arange(*ax.get_xlim(), steps):
            if i==0:
                continue
            if start is not None and i<start:
                continue
            if stop is not None and i>stop:
                continue
            if grad==0:
                ax.axvline( i, **kwargs )
            else:
                ax.axline( (i,0), slope=1/grad, **kwargs )


