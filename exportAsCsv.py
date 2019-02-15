'''

Imports processed features and exports as CSV data to train-data, to feed into NN
'''


import numpy as np
from import_words import *
from clean_data import *


EXPORTDIR = './train-data'


def nameCSV():
    if getNumberOfSentences('./train-data') == 0:
        return "bunch0"
    else:
        return "bunch" + str(getNumberOfSentences('./train-data')+1)



def exportMFCC(soundData):

    print("exporting MFC features as CSV")
    print

    path = nameCSV()

    np.savetxt(path, soundData, delimiter=",")

    print("done exporting to", EXPORTDIR)



if __name__ == '__main__':

    print nameCSV()

    '''
    numberOfFiles = getNumberOfFiles()
    soundData = importAll(numberOfFiles)
    cleanedSoundData = reduceDensity(soundData)
    cleanedSoundData = weightedAverage(soundData)

    cleanedSoundData = trimChunks(soundData)

    exportMFCC(cleanedSoundData)
    '''









