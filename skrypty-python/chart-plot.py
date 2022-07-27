import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


print('you have just closed the chart')
