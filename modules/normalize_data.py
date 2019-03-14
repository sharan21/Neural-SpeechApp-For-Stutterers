'''
Not yet Fully implemented.
Standardizes the data, to mean 0 and unit variance distribution.

'''

from import_words import *
import math

def normalizeSoundData(soundDataHere): # takes numpy array and normalizes it

    print("normalizing the sound data, for {} files".format(len(soundDataHere)))

    for i in range(len(soundDataHere)):
        print("normalizing the sound data, for {}st chunk".format(i))
        mean = np.mean(soundDataHere[i])
        std = np.std(soundDataHere[i])
        soundDataHere[i] = (soundDataHere[i] - mean) / std
        print("done")

def assertZeroMean(soundDataHere):
    for sound in soundDataHere:
        # print(np.mean(sound))
        if np.mean(sound) > 0.01:
            return False
    return True


def assertUnitVariance(soundDataHere):
    for sound in soundDataHere:
        print(np.std(sound))
        if math.floor(np.std(sound)) != 1 or math.ceil(np.std(sound)) != 1:
            return False
    return True


if __name__ == '__main__':


    soundData, labels = importAllFromDir('../LL_chunks')

    normalizeSoundData(soundData)
    plotAll(soundData)










