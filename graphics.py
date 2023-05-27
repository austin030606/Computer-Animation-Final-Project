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
                self.sim.Handle(event, mousePos, self.cellSize)
        return True
        pass

    def updateSimulation(self):
        # update the simulation
        self.sim.Update()

    def updateFrame(self):
        # update frame output
        # clear frame then draw each box using the value in sim.data

        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw the current frame
        for row in range(self.sim.row):
            for col in range(self.sim.col):
                if self.sim.data[row][col] > 0:
                    # define each cell's area
                    colored_cell_area = pygame.Rect(col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize)

                    # define cell intensity based on density value in sim.data
                    cell_intensity = self.sim.data[row][col]
                    cell_intensity = min(255, cell_intensity)
                    color_intensity = (cell_intensity, cell_intensity, cell_intensity)

                    # Draw using cell's area and intensity
                    pygame.draw.rect(self.screen, color_intensity, colored_cell_area)

        # Update the screen
        pygame.display.flip()
        # Update 1 frame per second
        self.clock.tick(1)