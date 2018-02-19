import numpy as np
import matplotlib.pyplot as plt
import abc

# Under what conditions do the two oscillators phase lock if the periods are different,
# there is a strength factor epsilon, and g is the same for both oscillators?
# What is the value of g(phi) when the two phase lock?

phaseDiff = .5
periodB = .8
strengthFactor = 1

class Neuron(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __init__(self, phase = 0, phi = 0, period = 1):
        self.phase = phase
        self.phi = phi
        self.period = period
    def phaseStep(self, delta):
        self.phase = np.mod(self.phase + delta, self.period)
        self.phi = self.phase / self.period
    def updatePhase(self):
        self.phi = self.phi + phaseResponseCurve(self.phi)
        self.phase = self.phi * self.period
    def fires(self, delta):
        return(self.phase + delta > self.period or self.phase - delta < 0)

class NeuronA(Neuron):
    #here, can write a different potential function for A
    pass

class NeuronB(Neuron):
    def __init__ (self, phase = phaseDiff, period = periodB):
        self.phase = phase
        self.period = period
    #here, can write a different potential function for A


# --------------------------------------- #

# can change g, the phase response curve
def phaseResponseCurve(p):
    return(strengthFactor * np.power(p, 2)*(1-p))


if __name__ == "__main__":
    a = NeuronA()
    b = NeuronB()

    # can change time steps and number of time units
    steps = 1000
    time = 4

    delta = time / steps
    timeSteps = np.arange(0, time, delta)
    aVals = np.zeros(np.shape(timeSteps))
    bVals = np.zeros(np.shape(timeSteps))


    for i in range(len(timeSteps)):
        a.phaseStep(delta)
        b.phaseStep(delta)
        if b.fires(delta):
            a.updatePhase()
        if a.fires(delta):
            b.updatePhase()
        aVals[i] = a.phi
        bVals[i] = b.phi

    plt.figure()
    plt.plot(timeSteps, aVals, 'c.', timeSteps, bVals, 'k')
    plt.xlabel(r'$time$')
    plt.ylabel(r'$potential$')
    plt.show()
