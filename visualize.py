import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

DATA_SET = [
    {
        'name' : 'blue',
        'X' : None,
        'GM': None,
        'mask' : 2
    },
    {
        'name' : 'not_barrel_blue',
        'X' : None,
        'GM': None,
        'mask': 1

    },

    {

        'name' : 'not_blue',
        'X' : None,
        'GM': None,
        'mask': 0
    }
]


for index in range(len(DATA_SET)):
    filename = '%s.txt'%(DATA_SET[index]['name'])
    x,y,z = [],[],[]
    for line in open(filename, 'r'):
        x.append(int(line.split(' ')[0]))
        y.append(int(line.split(' ')[1]))
        z.append(int(line.split(' ')[2]))
    ax.scatter(x[:],y[:],z[:])


plt.show()

