import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubble_sort

# Load the data from the CSV file
data = load_data('data/activity.csv')

# Extract the 'PowerOriginal' column from the data
#sort
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)
sorted_power_W = sorted_power_W[::-1]

#time_s = np.linspace(0, 1805, len(sorted_power_W))
time_min = np.linspace(0, 1805 / 60, len(sorted_power_W))

# create a plot and store in figure/
plt.plot(time_min, sorted_power_W)
plt.xlabel('time / min')
plt.ylabel('power / W')
plt.grid()
plt.title('Power Curve')
plt.savefig('figures/power_curve.png')
plt.show()