import numpy as np
from import_words import importAll, plotAll, nameAll, getNumberOfFiles

def normalizeSoundData(soundDataHere, numberOfFilesHere): # takes numpy array and normalizes it

    print("normalizing the sound data, for {} files".format(numberOfFilesHere))

    for i in range(numberOfFilesHere):
        print("normalizing the sound data, for {}st chunk".format(i))
        mean = np.mean(soundDataHere[i])



if __name__ == '__main__':
    numberOfFiles = getNumberOfFiles() # gets the number of files according to the all_chunks dir
    soundData = importAll(numberOfFiles)

    normalizeSoundData(soundData, numberOfFiles)




