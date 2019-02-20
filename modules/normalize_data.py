'''
Not yet Fully implemented.
Standardizes the data, to mean 0 and unit variance distribution.

'''

import numpy as np
from import_words import importAll, plotAll, nameAll, getNumberOfFiles

def normalizeSoundData(soundDataHere, numberOfFilesHere): # takes numpy array and normalizes it

    print("normalizing the sound data, for {} files".format(numberOfFilesHere))

    for i in range(numberOfFilesHere):
        print("normalizing the sound data, for {}st chunk".format(i))
        mean = np.mean(soundDataHere[i])
        std = np.std(soundDataHere[i])
        soundDataHere[i] = (soundDataHere[i] - mean) / std
        plotAll(soundDataHere, numberOfFilesHere)
        print("done")


if __name__ == '__main__':
    numberOfFiles = getNumberOfFiles() # gets the number of files according to the LL_chunks dir
    print(numberOfFiles)
    soundData = importAll(numberOfFiles)
    normalizeSoundData(soundData, numberOfFiles)




