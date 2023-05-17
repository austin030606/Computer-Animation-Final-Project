from simulation import *
from graphics import *

# get fluid simulation and perform additional initialization
fluid = Fluid()

# initialize graphics
g = Graphics(fluid)

# animation loop
while g.handleEvents():
    g.updateSimulation()
    g.updateFrame()

# stop the animation
g.Stop()
