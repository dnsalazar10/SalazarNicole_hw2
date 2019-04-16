import matplotlib.pylab as plt
import numpy as np

#Almacena los datos de signal.dat y signalSuma.dat. La columna 1 es el tiempo y la columna 2 es la señal f(t).
data1 = np.genfromtxt("signal.dat", delimiter='')
t1=data1[:,0]
f1=data1[:,1]

data2 = np.genfromtxt("signalSuma.dat", delimiter='')
t2=data2[:,0]
f2=data2[:,1]

#Gráficas de las señales
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(t1,f1,'orange')
plt.title('Signal')
plt.xlabel('time(t)')
plt.ylabel('f(t)')

ax2 = fig.add_subplot(222)
ax2.plot(t2,f2,'orange')
plt.title('Signal Suma')
plt.xlabel('time(t)')
plt.show()
