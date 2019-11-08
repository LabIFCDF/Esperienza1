import numpy
import pylab

#LOAD DATA
V1, Delta_t1, N1 = numpy.loadtxt('C:\\Users\\gabri\\Desktop\\DatiLabIntFond\\Preliminare\\PlateauPMT1.txt', unpack = True)
dN1 = numpy.sqrt(N1)
dV1 = 0.007*V1

V2, Delta_t2, N2 = numpy.loadtxt('C:\\Users\\gabri\\Desktop\\DatiLabIntFond\\Preliminare\\PlateauPMT2.txt', unpack = True)
dN2 = numpy.sqrt(N2)
dV2 = 0.007*V2

V3, Delta_t3, N3 = numpy.loadtxt('C:\\Users\\gabri\\Desktop\\DatiLabIntFond\\Preliminare\\PlateauPMT3.txt', unpack = True)
dN3 = numpy.sqrt(N3)
dV3 = 0.007*V3

#Grafico
pylab.subplot(131)
pylab.errorbar(V1, N1, dN1,dV1, color = 'blue', label = 'PMT1', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al}$ [mV]")
pylab.ylabel("Conteggi")
pylab.minorticks_on()
pylab.title("PMT1", color = "blue")
pylab.subplot(132)
pylab.errorbar(V2, N2, dN2,dV2, color = 'red', label = 'PMT2', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al}$ [mV]")
pylab.ylabel("Conteggi")
pylab.minorticks_on()
pylab.title("PMT2", color = "red")
pylab.subplot(133)
pylab.errorbar(V3, N3, dN3,dV3, color = 'green', label = 'PMT2', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al}$ [mV]")
pylab.ylabel("Conteggi")
pylab.minorticks_on()
pylab.title("PMT3", color = "green")
pylab.show()