'''

Imports processed features and exports as CSV data to train-data, to feed into NN
'''


import numpy as np
from import_words import *
from clean_data import *
from get_mfcc import *
from distribute_sets import *


EXPORTDIR = './train-data'


def nameCSV():
    if getNumberOfSentences('./train-data') == 0:
        return "bunch0"
    else:
        return "bunch" + str(getNumberOfSentences('./train-data')+1)



def exportMFCC(data, labels = []):

    print("exporting MFC features as CSV")
    print

    path = '../csvdata'
    pathl = '../csvlabels'
    # path = nameCSV()
    headerlist = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

    np.savetxt(path, data, delimiter=",", header=headerlist)
    np.savetxt(pathl, labels, delimiter=",")

    # print("done exporting to", EXPORTDIR)



if __name__ == '__main__':


    data, labels = getFinalNormalizedMfcc() #data is imported, normalized and shuffled.


    exportMFCC(data,labels)
    '''
    numberOfFiles = getNumberOfFiles()
    soundData = importAll(numberOfFiles)
    cleanedSoundData = reduceDensity(soundData)
    cleanedSoundData = weightedAverage(soundData)

    cleanedSoundData = trimChunks(soundData)

    exportMFCC(cleanedSoundData)
    '''









