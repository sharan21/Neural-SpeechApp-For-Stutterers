''' Use this when you want to obtain final training data in the form of numpy array and labels to feed into keras
Only run when you have finished recording your dataset using get_words
'''

from get_mfcc import *
import numpy as np
from import_words import importAllFromDir


def getTrainingData():

    print ("GETTING YOU SHUFFLED PREPROCESSED NUMPY DATA AND LABELS AS 'SOUNDDATA' AND 'LABELS' TO FEED INTO MODEL...")
    print
    print

    # we first obtained a shuffled dataset of both ll and non ll chunks in one array, along with their corresponding labels array

    ll_data, ll_labels = importAllFromDir('../LL_chunks')

    nonll_data, nonll_labels = importAllFromDir('../nonLL_chunks')

    final_data = []
    final_labels = []

    for data in ll_data:
        final_data.append(data)

    for data in nonll_data:
        final_data.append(data)

    for label in ll_labels:
        final_labels.append(label)

    for label in nonll_labels:
        final_labels.append(label)

    print (len(final_data))
    print (len(final_labels))






    '''

    

    #shuffling

    shuffle_in_unison_scary(final_data, final_labels)

    #processing and cleaning

    reduceDensity(final_data)

    trimChunks(final_data)

    assertConstantChunkSize(final_data)

    weightedAverage(final_data, 0.99)


    trimChunks(final_data)

    assertConstantChunkSize(final_data)

    normalizeSoundData(final_data)

    assertZeroMean(final_data)

    assertUnitVariance(final_data)
    
    '''



    print ("DONE!")


    return final_data, np.array(final_labels)





if __name__ == '__main__':

    data, labels = getTrainingData()











