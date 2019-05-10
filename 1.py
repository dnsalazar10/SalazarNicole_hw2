import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("edificio.txt")

t=data[0]
v=data[1]


plt.plot(t,v)
plt.savefig("data.pdf")
