import matplotlib.pylab as plt
import numpy as np

#### Punto 1 ####
#Almacena los datos de signal.dat y signalSuma.dat. La columna 1 es el tiempo y la columna 2 es la señal f(t).
data1 = np.genfromtxt("signal.dat", delimiter='')
t=data1[:,0]
f=data1[:,1]

data2 = np.genfromtxt("signalSuma.dat", delimiter='')
t2=data2[:,0]
f2=data2[:,1]

#### Punto 2 ####
#Gráficas de las señales
fig = plt.figure()
x1 = fig.add_subplot(221)
x1.plot(t,f,'g')
plt.title('Signal')
plt.xlabel('time(t)')
plt.ylabel('f(t)')

x2 = fig.add_subplot(222)
x2.plot(t,f2,'g')
plt.title('Signal Suma')
plt.xlabel('time(t)')


#### Punto 3 ####
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

#### Punto 4 ####
#Grafica de la transformada de Fourier de signal.dat
fig = plt.figure()
t1 = fig.add_subplot(221)
t1.plot(freq,fou)
plt.title('Transformada Signal')
plt.xlabel('Frecuencias')
plt.ylabel('Fourier')

#Datos de signalSuma.dat
##Grafica de la transformada de Fourier de signalSuma.dat
t2 = fig.add_subplot(222)
fou2=fourier(f2,N)
t2.plot(freq,fou2)
plt.title('Transformada Signal Suma')
plt.xlabel('Frecuencias')

##Suma de transformadas
plt.figure()
plt.plot(freq,fou,"orange")
plt.title('Suma de transformadas')
plt.xlabel('Frecuencias')
plt.ylabel('Fourier')
plt.plot(freq,fou2,'blue')
plt.title('Transformada Signal Suma')
plt.xlabel('Frecuencias')

#Tres frecuencias principales de su señal.
def freq_max(FR,FR2):
    freq_max=[]
    F_max=[]
    for i in range(6):
        index=list(FR).index(max(FR2))
        if freq[index]>0:
            F_max.append(FR[index])
            freq_max.append(freq[index])
        FR2[index]=0

    print("Las frecuencias principales de la señal son:",freq_max)

#Frecuencia signal.dat
FR=np.sqrt(np.real(fou)**2+np.imag(fou)**2)
FR2=FR
freq_max(FR,FR2)
#Frecuencia signalSuma.dat
FR2=np.sqrt(np.real(fou2)**2+np.imag(fou2)**2)
FR4=FR2
freq_max(FR2,FR4)

#Filtro pasa bajos que le permita filtrar el ruido de la senial del punto 1
def pasa_bajos(T,freq,corte):
    filtro=np.copy(T)
    for i in range(len(T)):
        if abs(freq[i])>corte:
            filtro[i]=0
    return filtro

F3=pasa_bajos(fou,freq,400)
inversa=np.fft.ifft(F3)

F4=pasa_bajos(fou2,freq,400)
inversa2=np.fft.ifft(F4)

#Grafica de la señal inicial y la señal filtrada de signal.dat
fig = plt.figure()
s1 = fig.add_subplot(221)
s1.plot(t,f,'g')
s1.plot(t,inversa,'m')
plt.xlabel('time(t)')
plt.ylabel('f(t)')

#Grafica de la señal inicial y la señal filtrada de signalSuma.dat
s2 = fig.add_subplot(222)
s2.plot(t,f2,'g', label="Señal inicial")
s2.plot(t,inversa2,'m', label="Señal filtrada")
plt.xlabel('time(t)')
plt.legend()
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


#### Punto 5 ####
# Plot de la señal signal.dat
Frequency = 450
plt.subplot(221)
plt.plot(t,f)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Signal')

# Plot de la señal signalSuma.dat
plt.subplot(222)
plt.plot(t,f2)
plt.xlabel('Sample')
plt.title('Signal Suma')

# Plot del spectrograma
plt.subplot(223)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(f, Fs=Frequency)
plt.xlabel('Time(t)')
plt.ylabel('Frequency')

# Plot del spectrograma
plt.subplot(224)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(f2, Fs=Frequency)
plt.xlabel('Time(t)')


#### Punto 6 ####
#Almacena los datos de un temblor real
temblor = np.genfromtxt("temblor.txt")
x=np.linspace(0,90001, 90001)
y=temblor[:]

#### Punto 7 ####
#Grafica la señal de un temblor real en función del tiempo
plt.figure()
plt.plot(x,y)
plt.xlabel('time(t)')
plt.ylabel('f(t)')
plt.title('Temblor')
plt.plot(range(12))


N3=len(x)
fou3=np.fft.fft(y)
dt3=x[1]-x[0]
freq3=np.fft.fftfreq(N3, dt3)

#### Punto 8 ####
#Plot de transformada de Fourier del temblor
plt.plot(freq3,fou3)
plt.title('Transformada')
plt.xlabel('Frecuencias')
plt.ylabel('Fourier')


Frequency = 0.05

# Plot de la señal signalSuma.dat
plt.subplot(211)
plt.plot(x,y)
plt.ylabel('Amplitud')
plt.title('Temblor')

#### Punto 9 ####
# Plot del spectrograma
plt.subplot(212)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(y, Fs=Frequency)
plt.xlabel('Time(t)')
plt.ylabel('Frequency')
plt.show()
