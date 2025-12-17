#Mark each point with a circle:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 2, 12, 16])

plt.plot(ypoints, marker = 'o')
plt.show()