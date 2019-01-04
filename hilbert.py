import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import hilbert, chirp
from import_words import *


soundData = importAll(numberOfFiles)
numberOfFiles = 10
duration = 3.0
fs = 44100.0
samples = int(fs*duration)
t = np.arange(samples) / fs


def getHilbert(numberOfFiles):

    analytic_signal = hilbert(soundData[1])
    amplitude_envelope = np.abs(analytic_signal)
    instantaneous_phase = np.unwrap(np.angle(analytic_signal))
    instantaneous_frequency = (np.diff(instantaneous_phase) /(2.0 * np.pi) * fs)
    plt.plot(amplitude_envelope)
    plt.show()
    plt.plot(soundData[1])
    plt.show()

def newenv(numberOfFiles):

    print("this is the new env function")
    for i in range(numberOfFiles):
        print(i)

newenv(10)
getHilbert(numberOfFiles)






