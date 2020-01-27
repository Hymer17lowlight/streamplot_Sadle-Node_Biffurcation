import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as anim

fig, ax = plt.subplots(2, 2)

ax[0][0].set_xlim(right=6, left=-6)
ax[0][0].set_ylim(top=6, bottom=-6)
ax[1][0].set_xlim(right=6, left=-6)
ax[1][0].set_ylim(top=6, bottom=-6)
ax[1][0].set_xlabel('Saddle-Node(2)')

Y, X = np.mgrid[-6:6:10j,
                -6:6:10j]


def getuv(X, Y):
    U = -X*X
    V = -Y
    return U, V


def plotuv(X, Y, i, m=0, n=0):
    U = i -X*X
    V = -Y
    ax[m][n].streamplot(X, Y, U, V,
                  color='b')


X1, Y1 = np.mgrid[-6:6:15j,
                -6:6:15j]

def plot1uv(X, Y, X1, Y1):
    U, V = getuv(X, Y)
    U1, V1 = getuv(X1, Y1)

    ax[1][0].streamplot(X, Y, U, V,
                     color='b')

    ax[1][0].quiver(X1, Y1, U1, V1,
              color = 'k')

fig.set_figwidth(8)
fig.set_figheight(8)

def redrawing(i):
    ax[0][0].clear()
    plotuv(X, Y, -2+0.04*i)

plot1uv(X, Y, X1, Y1)
plotuv(X, Y, -2, m=0, n=1)
plotuv(X, Y, 3, m=1, n=1)

a = anim.FuncAnimation(fig, redrawing, frames=100, repeat=True)

a.save('Saddle-Node.html')

plt.show()