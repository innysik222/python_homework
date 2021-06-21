import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,250)
k=1
k2=3
plt.plot(x, np.cos(k*x), x, np.cos(k2*x))
plt.show()