import matplotlib.pylab as plt
import numpy as np

#Almacena los datos de signal.dat y signalSuma.dat. La columna 1 es el tiempo y la columna 2 es la señal f(t).
data1 = np.genfromtxt("signal.dat", delimiter='')
t=data1[:,0]
f=data1[:,1]

data2 = np.genfromtxt("signalSuma.dat", delimiter='')
t2=data2[:,0]
f2=data2[:,1]

#Gráficas de las señales
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(t,f,'orange')
plt.title('Signal')
plt.xlabel('time(t)')
plt.ylabel('f(t)')

ax2 = fig.add_subplot(222)
ax2.plot(t2,f2,'orange')
plt.title('Signal Suma')
plt.xlabel('time(t)')
plt.show()

#Metodo de Fourier
def fourier(y,N):
    n = len(y)
    F = np.zeros(N, dtype=np.complex)
    for k in range (0,N):
        t = np.arange(0, n)
        F[k] = np.sum(y*np.exp(-2j*np.pi*t*(k/n)))
    return F

#Datos de signal.dat
N=len(t)
fou=fourier(f,N)
dt=t[1]-t[0]
freq=np.fft.fftfreq(N, dt)
##Grafica de la transformada de Fourier de signal.dat
fig = plt.figure()
t1 = fig.add_subplot(221)
t1.plot(freq,fou)
plt.title('Transformada Signal')
plt.xlabel('Frecuencias')
plt.ylabel('Fourier')

#Datos de signalSuma.dat
N2=len(t2)
fou2=fourier(f2,N2)
dt2=t2[1]-t2[0]
freq2=np.fft.fftfreq(N2, dt2)
##Grafica de la transformada de Fourier de signalSuma.dat
t2 = fig.add_subplot(222)
t2.plot(freq2,fou2)
plt.title('Transformada Signal Suma')
plt.xlabel('Frecuencias')
plt.show()
