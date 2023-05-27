import numpy as np

def swap(a: np.array, b: np.array):
    tmp = b
    b = a
    a = tmp

class Simulation:
    def __init__(self, row=100, col=100, dt=0.001):
        self.dt = dt
        self.row = row
        self.col = col
        self.data = np.zeros((row, col)) # data to display
        pass

    def Update():
        pass

    def Handle(event, row=0, col=0):
        pass

class Fluid(Simulation):
    def __init__(self, row=100, col=100, dt=0.001):
        super().__init__(row, col, dt)
        shape = (row, col)
        self.density = np.zeros(shape)
        self.density_prev = np.zeros(shape)
        self.velocityX = np.zeros(shape)
        self.velocityX_prev = np.zeros(shape)
        self.velocityY = np.zeros(shape)
        self.velocityY_prev = np.zeros(shape)
        self.data = self.density # set the data for displaying purposes
        pass

    def set_bnd(self, b, x: np.array):
        N = self.row - 2
        for i in range(1, N + 1):
            x[0][i]     = -1 * x[1][i] if b == 1 else x[1][i]
            x[N + 1][i] = -1 * x[N][i] if b == 1 else x[N][i]
            x[i][0]     = -1 * x[i][1] if b == 2 else x[i][1]
            x[i][N + 1] = -1 * x[i][N] if b == 2 else x[i][N]
        x[0][0]     = 0.5 * (x[1][0] + x[0][1])
        x[0][N + 1] = 0.5 * (x[1][N + 1] + x[0][N])
        x[N + 1][0] = 0.5 * (x[N][0] + x[N + 1][1])
        x[N + 1][N + 1] = 0.5 * (x[N][N + 1] + x[N + 1][N])


    def diffuse(self,b , x: np.array, x0: np.array):
        N = self.row - 2
        k = 20
        a = self.dt * N * N
        for _ in range(k):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    x[i][j] = (x0[i][j] + a * (x[i - 1][j] + x[i + 1][j] + x[i][j - 1] + x[i][j + 1]) / (1 + 4 * a))
            self.set_bnd(b, x)
        pass

    def advect(self, b, d: np.array, d0: np.array, u: np.array, v: np.array):
        N = self.row - 2
        dt0 = self.dt * self.row
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                x = i - dt0 * u[i][j]
                y = j - dt0 * v[i][j]
                if x < 0.5:
                    x = 0.5
                elif x > N + 0.5:
                    x = N + 0.5
                if y < 0.5:
                    y = 0.5
                elif y > N + 0.5:
                    y = N + 0.5
                i0 = int(x)
                i1 = i0 + 1
                j0 = int(y)
                j1 = j0 + 1
                s1 = x - i0
                s0 = 1 - s1
                t1 = y - j0
                t0 = 1 - t1
                d[i][j] = s0 * (t0 * d0[i0][j0] + t1 * d0[i0][j1]) + s1 * (t0 * d0[i1][j0] + t1 * d0[i1][j1])
        self.set_bnd(b, d)
        pass

    def densityUpdate(self):
        # update density grid
        # swap(self.density_prev, self.density)
        # self.diffuse(0, self.density, self.density_prev)
        # swap(self.density_prev, self.density)
        # self.advect(0, self.density, self.density_prev, self.velocityX, self.velocityY)
        self.diffuse(0, self.density_prev, self.density)
        self.advect(0, self.density, self.density_prev, self.velocityX, self.velocityY)
        pass

    def project(self, u: np.array, v: np.array, p: np.array, div: np.array):
        N = self.row - 2
        h = 1 / N
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                div[i][j] = -0.5 * h * (u[i + 1][j] - u[i - 1][j] + v[i][j + 1] - v[i][j - 1])
                p[i][j] = 0
        self.set_bnd(0, div)
        self.set_bnd(0, p)

        for _ in range(20):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    p[i][j] = (div[i][j] + p[i - 1][j] + p[i + 1][j] + p[i][j - 1] + p[i][j + 1]) / 4
            self.set_bnd(0, p)
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                u[i][j] -= 0.5 * (p[i + 1][j] - p[i - 1][j]) / h
                v[i][j] -= 0.5 * (p[i][j + 1] - p[i][j - 1]) / h
        
        self.set_bnd(1, u)
        self.set_bnd(2, v)
        pass

    def velocityUpdate(self):
        # update velocity grid
        self.diffuse(1, self.velocityX_prev, self.velocityX)
        self.diffuse(1, self.velocityY_prev, self.velocityY)
        self.project(self.velocityX_prev, self.velocityY_prev, self.velocityX, self.velocityY)
        self.advect(1, self.velocityX, self.velocityX_prev, self.velocityX_prev, self.velocityY_prev)
        self.advect(2, self.velocityY, self.velocityY_prev, self.velocityX_prev, self.velocityY_prev)
        self.project(self.velocityX, self.velocityY, self.velocityX_prev, self.velocityY_prev)
        pass

    def Update(self):
        self.densityUpdate()
        self.velocityUpdate()

    def Handle(event, row=0, col=0):
        # handle fluid states based on event type and mouse position
        pass