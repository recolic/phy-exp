import numpy
import matplotlib.pyplot as plt
from matplotlib import rcParams
# Points here!
yrc=[-6.77, -6.78, -6.78, -6.76, -6.73, -6.73, -6.72, -6.70, -6.69, -6.67, -6.60, -6.45, -6.37, -6.20, -5.99, -5.77, -5.45, -5.07, -3.52, -2.87, -2.36, -2.08, -1.77, -1.55, -1.40, -1.26, -0.97, -0.84, -0.64]
xrc=[0.0, 2.0, 4.0, 10.0, 20.0, 22.0, 25.0, 30.0, 33.0, 35.0, 37.0, 38.0, 38.5, 39.0, 39.6, 40.0, 40.5, 41.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 53.0, 55.0, 60.0]
x=xrc
y=[abs(yi) for yi in yrc]

# Draw function map.
rcParams['grid.linestyle']='-'
rcParams['grid.color'] = 'blue'
rcParams['grid.linewidth'] = 0.2
plt.figure(figsize=(8,6)) # Change 8 to yMax here.
plt.scatter(x,y,color="red",label="Sample Point",linewidth=3)
px=numpy.linspace(0,65,1000)
plt.legend()
plt.grid()
plt.show()