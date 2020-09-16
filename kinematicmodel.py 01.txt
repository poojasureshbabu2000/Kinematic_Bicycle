class Bicycle(Bicycle):
    def step(self, v, w):
        # ==================================
        #  Implement kinematic model here
        # ==================================
        self.xc = self.xc + v * np.cos(self.theta + self.beta) * self.sample_time
        self.yc = self.yc + v * np.sin(self.theta + self.beta) * self.sample_time
        self.theta = self.theta + ((v * np.cos(self.beta) * np.tan(self.delta)/self.L)) * self.sample_time
        self.delta = w * self.sample_time + self.delta
        self.beta = np.arctan((self.lr / self.L) * np.tan(self.delta))

        pass