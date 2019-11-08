import numpy
import pylab

#LOAD DATA
V1, Delta_t1, N1 = numpy.loadtxt('PlateauPMT1-3F.txt', unpack = True)
dN1 = numpy.sqrt(N1)
dV1 = 0.007*V1

V2, Delta_t2, N2 = numpy.loadtxt('PlateauPMT3-1F.txt', unpack = True)
dN2 = numpy.sqrt(N2)
dV2 = 0.007*V2

#Grafico
pylab.subplot(121)
pylab.errorbar(V1, N1, dN1,dV1, color = 'blue', label = 'PMT1', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al}$ [mV]")
pylab.ylabel("Coincidenze")
pylab.minorticks_on()
pylab.title("PMT3 fisso, varia PMT1", color = "blue")
pylab.subplot(122)
pylab.errorbar(V2, N2, dN2,dV2, color = 'red', label = 'PMT2', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al}$ [mV]")
pylab.ylabel("Coincidenze")
pylab.minorticks_on()
pylab.title("PMT 1 fisso, varia PMT3", color = "red")
pylab.show()