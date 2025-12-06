import numpy as np
from matplotlib import pyplot as pp

v_initial = 1
h = 0.1
m = 70
P = 400
C_d = .9
A = .33
rho = 1.225
n = 2e-5
H = 2
g = 9.8
grade = .05
theta = np.arctan(grade)

def myODE(v):
    return ((P / v) - (.5 * C_d * rho * A * v**2) - (n * A * v/H) - (m * g * np.sin(theta)))/m

def eulerStep(v):
    return v + myODE(v) * h

x = np.arange(0, 200 + h, h)
v = [v_initial]

for i in range(len(x) - 1):
    v.append(eulerStep(v[-1]))

pp.plot(x, v)
pp.xlabel('Time (s)')
pp.ylabel('Velocity (m/s)')
pp.title('Cyclist Velocity vs Time')
pp.grid()
#pp.savefig('bicycle.png')
pp.show()
