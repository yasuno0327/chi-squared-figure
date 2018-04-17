import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

def chiSquare(x):
    result = 2 ** (-5/2) * (4/(3*math.pi**0.5)) * (x**3/2) * (math.e**(-x/2))
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]
results = []

for n in data:
    results.append(chiSquare(n))
    
plt.scatter(data, results)
plt.plot(data, results)
plt.show()
