#BaiTap1_Nhom1
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()

ax = fig.add_subplot(111, projection= '3d')

x = [0, 0, 5]

y = [0, 5, 0]

z = [5, 0, 0]

vertices = [list(zip(x,y,z))]

poly3D = Poly3DCollection(vertices, alpha = 0.8)

ax.add_collection3d(poly3D)

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(0,5)

ax.plot([0,1,2],[0,0,0],[0,0,0])
ax.plot([0,0,0],[0,1,2],[0,0,0])
ax.plot([0,0,0],[0,0,0],[0,1,2])
ax.plot(x,y,z)
plt.show()