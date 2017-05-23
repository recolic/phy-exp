import numpy
import sys
from quickmap import GetMap as draw

dat=numpy.loadtxt(sys.argv[1], delimiter=' ')
Uraw,Iraw=dat[:,0],dat[:,1]
U=[utrue/100*2.5 for utrue in Uraw]
I=[itrue/150*30 for itrue in Iraw]

draw(I,U,line=True,passO=True)
