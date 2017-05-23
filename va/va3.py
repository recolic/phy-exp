import numpy
import sys
from quickmap import GetMap as draw

dat=numpy.loadtxt(sys.argv[1], delimiter=' ')
Uraw,Iraw=dat[:,0],dat[:,1]
U=[utrue/100*5 for utrue in Uraw]
I=[itrue/150*15 for itrue in Iraw]
# 1V 15mA. Edit it to adjust Ammeter/Voltmeter range.
draw(I,U)
