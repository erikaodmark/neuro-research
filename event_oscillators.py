import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

phaseDiff = .5
strengthFactor = 1

def phaseResponseCurve(p):
    return(strengthFactor * np.power(p, 2)*(1-p))

def F(p):
    return(1 - p + phaseResponseCurve(1 - p))

if __name__ == "__main__":
    phaseA = 0
    phaseB = phaseDiff
    periodA = 1
    periodB = .8
    time = 0
    eventsA = np.zeros((1, 2))
    eventsB = np.zeros((1, 2))

    eventsA[0, :] = [0, phaseA]
    eventsB[0, :] = [0, phaseB]
    phaseA = 1

    signals = PriorityQueue()

    for i in range(1,10):
        if phaseA == 1:
            eventsB = np.vstack([eventsB, [time, phaseB]])
            phaseB = F(F(phaseB))
            eventsB = np.vstack([eventsB, [time, phaseB]])
            eventsA = np.vstack([eventsA, [time, phaseA]])
            phaseA = 0
            eventsA = np.vstack([eventsA, [time, phaseA]])
        if phaseB == 1:
            eventsA = np.vstack([eventsA, [time, phaseA]])
            phaseA = F(F(phaseA))
            eventsA = np.vstack([eventsA, [time, phaseA]])
            eventsB = np.vstack([eventsB, [time, phaseB]])
            phaseB = 0
            eventsB = np.vstack([eventsB, [time, phaseB]])

        timeUntilA = (1 - phaseA) * periodA
        timeUntilB = (1 - phaseB) * periodB
        if np.minimum(timeUntilA, timeUntilB) == timeUntilA:
            phaseA = 1
            phaseB += np.mod(timeUntilA/periodB, 1)
            time += timeUntilA
        else:
            phaseB = 1
            phaseA = np.mod(timeUntilB/periodA, 1)
            time += timeUntilB

    plt.figure()
    plt.plot(eventsA[:, 0], eventsA[:, 1], 'k', eventsB[:, 0], eventsB[:, 1], 'c')
    plt.xlabel(r'$time$')
    plt.ylabel(r'$potential$')
    plt.show()
