import numpy as np
from matplotlib import pyplot as pp
import random 

nSteps = int(input("enter number of steps: "))
nWalkers = 500
allPositions = []

for walker in range(nWalkers):
    x = [0]
    steps = [0]
    for step in range(nSteps):
        x.append(x[-1]+random.randint(-1,1))
        steps.append(step + 1)
        
    #pp.plot(steps,x)
    allPositions.append(x)

allPositions = np.array(allPositions)
mean = np.mean(allPositions, axis=0)
meanSquared = np.mean(allPositions**2, axis=0)

pp.figure()
pp.plot(steps, meanSquared, 'r-', label = '<x^2>')
pp.xlabel('Step Number')
pp.ylabel('Mean Squared of Displacement')    
pp.savefig('manyWalks.png')
