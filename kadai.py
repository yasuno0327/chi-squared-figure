import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import math

def chiSquare(x):
    a = 2**(-5/2)
    b = 4/(3*math.pi**0.5)
    c = x**(3/2)
    d = np.exp(-x/2)
    result = a * b * c * d
    print(x, c, d, result)
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]
results = []

for n in data:
    results.append(chiSquare(n))
    
plt.scatter(data, results)
plt.plot(data, results)
plt.show()
