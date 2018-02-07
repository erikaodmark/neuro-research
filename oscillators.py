import numpy as np
import matplotlib.pyplot as plt
import abc

phaseDiff = .5
periodB = .7

class Neuron(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __init__(self, phase = 0, period = 1):
        self.phase = phase
        self.period = period
    def phaseStep(self, delta):
        self.phase = np.mod(self.phase + delta, self.period)
    def updatePhase(self):
        self.phase += phaseResponseCurve(self.phase)
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
    return(np.power(p, 2)*(1-p))


if __name__ == "__main__":
    a = NeuronA()
    b = NeuronB()

    # can change time steps and number of time units
    steps = 1000
    time = 3

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
        aVals[i] = a.phase
        bVals[i] = b.phase

    plt.figure()
    plt.plot(timeSteps, aVals, 'c', timeSteps, bVals, 'k--')
    plt.xlabel(r'$time$')
    plt.ylabel(r'$potential$')
    plt.show()
