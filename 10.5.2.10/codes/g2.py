import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('values.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

# Plot the stem plot
plt.stem(n, xn)

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

