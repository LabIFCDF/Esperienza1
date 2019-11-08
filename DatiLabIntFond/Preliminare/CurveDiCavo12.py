import numpy
import pylab

#LOAD DATA
Rit, Delta_t, N = numpy.loadtxt('C:\\Users\\gabri\\Desktop\\DatiLabIntFond\\Preliminare\\CurveDiCavo12.txt', unpack = True)
dN = numpy.sqrt(2*N)

#Grafico

pylab.errorbar(Rit, N, dN, color = 'blue', label = 'PMT1', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$\Delta t_{rit}$ [ns]")
pylab.ylabel("Conteggi")
pylab.minorticks_on()
pylab.title("Curva di cavo 1-2")
pylab.show()