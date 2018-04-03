import numpy as np 
import matplotlib.pyplot as plt 

outfile = open('output_nis.txt', 'r')

lidar_nis = []
radar_nis = []

for line in outfile:
    if 'RADAR' in line:
        words = line.split()
        radar_nis.append(float(words[1]))
    if 'LIDAR' in line:
        words = line.split()
        lidar_nis.append(float(words[1]))

radar_nis.pop(0)
lidar_nis.pop(0)

plt.plot(radar_nis)
plt.plot(np.array([7.8 for i in range(len(radar_nis))]))
plt.show()

plt.plot(lidar_nis)
plt.plot(np.array([5.9 for i in range(len(lidar_nis))]))
plt.show()


