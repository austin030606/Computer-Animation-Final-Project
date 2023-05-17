import numpy as np

class Simulation:
    def __init__(self, row=100, col=100):
        self.row = row
        self.col = col
        self.data = np.zeros((row, col)) # data to display
        pass

    def Update():
        pass

    def Handle(event, row=0, col=0):
        pass

class Fluid(Simulation):
    def __init__(self, row=100, col=100):
        super().__init__(row, col)
        shape = (row, col)
        self.density = np.zeros(shape)
        self.velocity = np.zeros(shape)
        self.data = self.density # set the data for displaying purposes
        pass

    def densityUpdate(self):
        # update density grid
        pass

    def velocityUpdate(self):
        # update velocity grid
        pass

    def Update(self):
        self.densityUpdate()
        self.velocityUpdate()

    def Handle(event, row=0, col=0):
        # handle fluid states based on event type and mouse position
        pass