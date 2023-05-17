import pygame
from simulation import *

class Graphics:
    def __init__(self, sim: Simulation, cellSize=5):
        # initialize pygame object and class members
        self.sim = sim
        self.cellSize = cellSize
        pygame.init()
        screenShape = (self.sim.col * self.cellSize, self.sim.row * self.cellSize)
        self.screen = pygame.display.set_mode(screenShape)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('simulation')
        pass

    def Stop(self):
        # stop the pygame object
        pygame.quit()
        pass

    def handleEvents(self) -> bool:
        # handle events
        # return False if the game is supposed to quit
        # otherwise return True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            else:
                mousePos = pygame.mouse.get_pos()
                self.sim.Handle(event, mousePos)
        return True
        pass

    def updateSimulation(self):
        # update the simulation
        self.sim.Update()

    def updateFrame(self):
        # update frame output
        # clear frame then draw each box using the value in sim.data
        pass