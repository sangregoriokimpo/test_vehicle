#q=0.04375, r=5.625
#q=0.0375, r=5.25
#q=1.0, r=0.5

class KalmanFilter:
    def __init__(self, q=0.7, r=2.0):
        self.q = q  # process noise
        self.r = r  # measurement noise
        self.x = 0.0  # estimated angle
        self.p = 1.0  # error covariance

    def update(self, measurement):
        # Predict
        self.p += self.q

        # Kalman Gain
        k = self.p / (self.p + self.r)

        # Update estimate
        self.x += k * (measurement - self.x)

        # Update error covariance
        self.p *= (1 - k)

        return self.x
