import numpy
import pylab

V, C3, C2, T = numpy.loadtxt("C:\\Users\\Utente Microsoft\\Documents\\Laurea_Magistrale\\LabIF\\Esperienza1\\DatiLabIntFond\Preliminare\\Efficienza.txt", unpack = True)

dC3 = numpy.sqrt(C3)
dC2 = numpy.sqrt(C2)
Err = numpy.sqrt((dC3/C3)**2+(dC2/C2)**2)*(C3/C2)
dV = 0.007*V

media = ((C3/C2).sum())/len(C3)
print(media)
pylab.errorbar(V,C3/C2, Err, dV, color = 'blue', fmt = '.')
pylab.grid(color = 'gray', linestyle = 'dotted')
pylab.xlabel("$V_{al, 2}$ [V]")
pylab.ylabel("Efficienza")
pylab.minorticks_on()
pylab.show()