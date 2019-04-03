
'''

takes a wav file as input and outputs its 13 co-efficient MFCC.
Only implemented for single path, single MFCC extraction and does not automatically work on whole directory.
'''

import numpy as np
import os
import librosa.display
from get_spectraldata import *
import matplotlib.pyplot as plt
import dtw
from normalize_data import normalizeSoundData
from import_words import shuffle_in_unison_scary

pre_emphasis = 0.97
frame_size = 0.025
frame_stride = 0.01
NFFT = 512
nfilt = 40
num_ceps = 12
cep_lifter = 22 # 0 for no filter
nonllpath = '../LL_chunks/chunk1.wav'
llpath = '../nonLL_chunks/chunk1.wav'


def librosaMfcc(path):
    list = absoluteFilePaths(path)
    data = []


    for file in list:
        mfcc = average(findMfcc(file))
        # deltah = delta(mfcc)
        #temp = np.concatenate((mfcc, deltah))
        data.append(mfcc)



    return np.array(data)

def plotMfcc(mfcc1, mfcc2):

    plt.subplot(1, 2, 1)
    librosa.display.specshow(mfcc1)
    plt.subplot(1, 2, 2)
    librosa.display.specshow(mfcc2)
    plt.show()



def computeDistace(mfcc1, mfcc2):

    print("Finding DTW between the 2 mfccs")
    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    print ('Normalized distance between the two sounds:', dist)
    plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
    plt.plot(path[0], path[1], 'w')
    plt.xlim((-0.5, cost.shape[0] - 0.5))
    plt.ylim((-0.5, cost.shape[1] - 0.5))
    plt.show()

def padMfcc(mfcc, fixedsize = 30):
    print ("padding mfcc")
    np.transpose(mfcc)
    # mfcc too small
    diff = fixedsize - mfcc.shape[1]
    print (diff)
    for _ in range(diff):
        print ("running")
        np.vstack((mfcc, np.zeros(20)))

    print (mfcc.shape)

def getMfccAverage(): # return average of all mfccs for each word in numpy array

    # first creating the dir list
    pathlist = []

    pathlist.extend(absoluteFilePaths('../LL_chunks'))
    pathlist.extend(absoluteFilePaths('../nonLL_chunks'))

    print ("path list is",pathlist)

    data = []

    for path in pathlist:
        print ("finding mfcc of", path)

        data.append(average(findMfcc(path)))

        # print len(data[-1])

    return np.array(data)

def getndimMfcc(): # return average of all mfccs for each word

    # first creating the dir list
    pathlist = []

    pathlist.extend(absoluteFilePaths('../LL_chunks'))
    pathlist.extend(absoluteFilePaths('../nonLL_chunks'))

    print ("path list is",pathlist)

    data = []

    for path in pathlist:
        print ("finding mfcc of", path)

        data.append(findMfcc(path))
        print len(data[-1])

    return np.array(data)

def getMfccDelta():
    # first creating the dir list
    print ("hello")
    pathlist = []

    pathlist.extend(absoluteFilePaths('../LL_chunks'))
    pathlist.extend(absoluteFilePaths('../nonLL_chunks'))

    print ("path list is", pathlist)

    data = []

    for path in pathlist:
        print ("finding mfcc of", path)
        # mfcc = average((findMfcc(path)))
        deltah = average(delta(findMfcc(path)))
        # temp = np.concatenate((deltah, mfcc))
        print (deltah)
        data.append(deltah)

        print (len(data[-1]))

    return np.array(data)



def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       if ('.DS_Store' in filenames):
        filenames.remove('.DS_Store')
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))



def findMfcc(path):
    y1, sr1 = librosa.load(path)
    mfcc = librosa.feature.mfcc(y1, sr1)
    return mfcc


def average(mfcc):
    # take an n coefficient mfcc for multiple samples and finds its nx1 size average array
    # print ("averaging mfcc")
    ave = []
    for i in range(mfcc.shape[0]):
        ave.append(np.mean(mfcc[i,:]))
    ave_numpy = np.array(ave)
    # print (ave_numpy)

    return ave_numpy

def getFinalNormalizedMfcc(): #shuffling occurs here

    data = getMfccAverage()
    # data = deltaplusmfcc()
    # data = getMfccSum()
    # data = getMfccDelta()
    print (data.size)

    normalizeSoundData(data)


    _, labels = getTrainingData()

    print (labels)

    shuffle_in_unison_scary(data, labels)


    return data, labels


def flatten():
    print("flattening")


def delta(mfcc):
    '''

    :param mfcc: input mfcc 2d array
    :return: first dervative of mfcc 2d array
    '''
    print ("finding the delta")
    return librosa.feature.delta(mfcc)

def sum(mfcc): #over time axis or coloum wise

    data = np.array(mfcc) # if mfcc data is not already in numpy

    return data.sum(axis=1)

def getlabels():
    '''

    :return: gets non shuffled labels as numpy array of size [training samples, 1], 1 for LL 0 for Non LL
    '''


def getMfccSum():
    pathlist = []

    pathlist.extend(absoluteFilePaths('../LL_chunks'))
    pathlist.extend(absoluteFilePaths('../nonLL_chunks'))

    print ("path list is", pathlist)

    data = []

    for path in pathlist:
        print ("finding mfcc of", path)

        data.append(sum(findMfcc(path)))

        print (len(data[-1]))

    return np.array(data)




def getmfccDoubleDelta():
    print






if __name__ == '__main__':

    # nonllmfcc, llmfcc = librosaMFCC(nonllpath, llpath)
    # average(llmfcc)

    # plotMfcc(nonllmfcc, llmfcc)
    # computeDistace(nonllmfcc, llmfcc)


    data, labels = getFinalNormalizedMfcc()
    print (data[1:10, :])
    print (data.size)
    print (type(data))
    # print data[500:,:]

    # deltaplusmfcc()
















