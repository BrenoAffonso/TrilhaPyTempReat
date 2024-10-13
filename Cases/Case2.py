import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 400)  # 400 points between -3 and 3


ye = np.exp(x)

y3= x/1 + (x**2)/2 + (x**3)/6

y6= x/1 + (x**2)/2 + (x**3)/6 + (x**4)/24 + (x**5)/120 + (x**6)/720

plt.plot(x, ye, label='e^x')
plt.plot(x, y3, label='P3')
plt.plot(x, y6, label='P6')

plt.xlabel('x')
plt.ylabel('Resultado')
plt.title('Gráfico e^x e suas expansões de Taylor 3')


plt.grid(True)


plt.legend()


plt.show()
