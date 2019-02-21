
'''

takes a wav file as input and outputs its 13 co-efficient MFCC.
Only implemented for single path, single MFCC extraction and does not automatically work on whole directory.
'''


import numpy
import scipy.io.wavfile
from scipy.fftpack import dct
import matplotlib.pyplot as plt
from dtw import dtw
import librosa.display
from numpy.linalg import norm

pre_emphasis = 0.97
frame_size = 0.025
frame_stride = 0.01
NFFT = 512
nfilt = 40
num_ceps = 12
cep_lifter = 22 # 0 for no filter
nonllpath = './LL_chunks/chunk0.wav'
llpath = './nonLL_chunks/chunk0.wav'


def librosaMFCC(nonllpath, llpath):
    print ('Calculating both the MFCC')
    y1, sr1 = librosa.load(nonllpath)
    y2, sr2 = librosa.load(llpath)

    mfcc1 = librosa.feature.mfcc(y1, sr1)
    mfcc2 = librosa.feature.mfcc(y2, sr2)

    return mfcc1, mfcc2

def plotMfcc(mfcc1, mfcc2):

    plt.subplot(1, 2, 1)
    librosa.display.specshow(mfcc1)
    plt.subplot(1, 2, 2)
    librosa.display.specshow(mfcc2)
    plt.show()



def computeDistace(mfcc1, mfcc2):

    print("Finding DTW between the 2 mfccs")
    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    print 'Normalized distance between the two sounds:', dist
    plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
    plt.plot(path[0], path[1], 'w')
    plt.xlim((-0.5, cost.shape[0] - 0.5))
    plt.ylim((-0.5, cost.shape[1] - 0.5))
    plt.show()


if __name__ == '__main__':

    nonllmfcc, llmfcc = librosaMFCC(nonllpath, llpath)
    plotMfcc(nonllmfcc, llmfcc)
    computeDistace(nonllmfcc, llmfcc)

