class KalmanFilter(object):

    def __init__(self, processNoise=1, measurementNoise=1, stateVector=1,
                 controlVector=0, measurementVector=1):
        self.processNoise = processNoise
        self.measurementNoise = measurementNoise
        self.stateVector = stateVector
        self.controlVector = controlVector
        self.measurementVector = measurementVector
        self.covariance = None
        self.estimate = None

    def filter(self, measurement, control=1):
        if (self.estimate is None):
            self.estimate = (1 / self.measurementVector) * measurement
            self.covariance = (1 / self.measurementVector) * self.measurementNoise * (1 / self.measurementVector)
        else:
            # Calculate the Kalman predictions
            predictedMeasurement = (self.stateVector * self.estimate) + (self.controlVector * control)
            predictedCovariance = ((self.stateVector * self.covariance) * self.stateVector) + self.processNoise

            # Calculate Kalman gain
            kalmanGain = predictedCovariance * self.measurementVector * (1 / ((self.measurementVector * predictedCovariance * self.measurementVector) + self.measurementNoise))

            # Set Kalman Filter Variables (Correction)
            self.estimate = predictedMeasurement + kalmanGain * (measurement - (self.measurementVector * predictedMeasurement))
            self.covariance = predictedCovariance - (kalmanGain * self.measurementVector * predictedCovariance)
        return self.estimate

    def lastMeasurement(self):
        return self.estimate

    def setMeasurementNoise(self, noise):
        self.measurementNoise = noise

    def setProcessNoise(self, noise):
        self.processNoise = noise
