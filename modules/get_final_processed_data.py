''' Use this when you want to obtain final training data in the form of numpy array and labels to feed into keras
Only run when you have finished recording your dataset using get_words
'''

from import_words import *

def getTrainingData():

    print ("GETTING YOU SHUFFLED PREPROCESSED NUMPY DATA AND LABELS AS 'SOUNDDATA' AND 'LABELS' TO FEED INTO MODEL...")
    print
    print

    # we first obtained a shuffled dataset of both ll and non ll chunks in one array, along with their corresponding labels array

    ll_data, ll_labels = importAllFromDir('../LL_chunks')

    nonll_data, nonll_labels = importAllFromDir('../nonLL_chunks')

    final_data = []
    final_labels = []

    final_data.append(ll_data)
    final_data.append(nonll_data)

    final_labels.append(ll_labels)
    final_labels.append(nonll_labels)

    #shuffling

    shuffle_in_unison_scary(final_data, final_labels)





