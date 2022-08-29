"""
Identitas:
Nama: Gregory Hope Soegiantoro
Email: gsoegiantoro@gmail.com
"""

# impor numpy
import numpy as np

# impor library plot
from matplotlib import pyplot as plt

# data dasar dan parameter
a = 15
b = 6
c = 100
alpha = np.linspace(-2 * np.pi, 100, num=100)
k = np.linspace(0, 45, num=100)
r = k * (a+np.sin(theta*b+(k/c)))

# koordinat x
x = r * np.cos(theta)

# koordinat y
y = r * np.sin(theta)

# tampilkan
plt.plot(x, y)
plt.title('Rose for Angel')
plt.show()
