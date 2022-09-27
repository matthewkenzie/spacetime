import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import matplotlib.image as mimg
import matplotlib.patches as mpatches

def read_image(fname):
    return mimg.imread(fname)

def draw_image(fname, ax=None, cmap=None, beta=0, extent=[0,1,0,1], transfExtent=False, color='k', wpt=True):

    ax = ax or plt.gca()

    img = mimg.imread(fname)
    im = plt.imshow(img, cmap=cmap,extent=extent, zorder=12)

    skew = np.degrees(np.arctan(beta))
    transf = mtransforms.Affine2D().skew_deg(skew,skew)
    transfData = transf + ax.transData

    im.set_transform(transfData)

    x1, x2, y1, y2 = im.get_extent()
    x = [x1, x2, x2, x1, x1]
    y = [y1, y1, y2, y2, y1]

    ax.plot(x, y, color=color, ls="-",
            transform=transfData,zorder=14)

    if color is not None:
        ax.add_patch( mpatches.Polygon(xy=list(zip(x,y)), fill=True, color=color, alpha=0.2, transform=transfData, zorder=22))

        xpos = x1 if x1>=0 else x2
        ax.plot(xpos,y1, color=color, marker='o', ms=12, transform=transfData,zorder=15)


if __name__ == "__main__":
    fig, ax = plt.subplots()
    draw_image('t0_1.jpeg', ax, beta=0.3)
    plt.show()
