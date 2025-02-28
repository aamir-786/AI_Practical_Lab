import matplotlib.pyplot as plt
import numpy as np
home_sizes = np.array([120, 150, 200, 250, 300 , 400 , 600])
home_prices = np.array([0.5, 1.0 , 2, 1.3 , 2.0 , 3.0 , 5.0])
plt.plot(home_sizes, home_prices ,'ro')
plt.show()