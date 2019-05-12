import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("edificio.txt")

t=data[:,0]
u1=data[:,1]
u2=data[:,2]
u3=data[:,3]

plt.title("Sismo en un edificio")
plt.plot(t,u1,label="Piso 1")
plt.plot(t,u2,label="Piso 2")
plt.plot(t,u3,label="Piso 3")
plt.xlabel("tiempo")
plt.ylabel("Amplitud")
plt.legend()
plt.savefig("edificio.pdf")
plt.show()
