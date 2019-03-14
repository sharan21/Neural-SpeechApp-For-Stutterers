'''

Cleans the data by reducing it density, and trims each word to constant size
Also implements exponential weighted average to smoothen the data.


'''

from import_words import importAllFromDir, plotAll
import numpy as np
import os


betaForExponentialAverage = 0.99
# use b = 0 to mirror the original data
# as beta increases, oscillations decrease

fixedChunkSize = 200
# each word chunk has a fixed size to feed into the tf graph




def reduceDensity(soundDataHere, densityOfChunk = 100):

    cleanSoundData = []

    for i in range(len(soundDataHere)):

        k = 0
        bufferForCleaning = []

        for j in range(0, len(soundDataHere[i]), densityOfChunk):

            bufferForCleaning.insert(k, soundDataHere[i][j])
            k += 1

        cleanSoundData.append(np.absolute(bufferForCleaning))

    return cleanSoundData



def weightedAverage(soundDataHere, beta = 0.8):

    # newData[i] = beta*newData[i-1] + (1-beta)*soundData[i]

    print("Finding the weighted exponential average...")
    print

    newSoundData = []

    for i in range(len(soundDataHere)):

        bufferHere = []

        for j in range(len(soundDataHere[i])):

            if j == 0:
                bufferHere.append(0)
            else:
                biasCorrection = 1/(1-pow(beta, j))
                bufferHere.append(beta*bufferHere[j-1] + (1-beta)*soundDataHere[i][j] * biasCorrection)

        newSoundData.append(np.absolute(bufferHere))

        print("done finding the exponential average...")

    return newSoundData

def trimChunks(soundData, fixedSize = 200): # trim the chunk to get fixed size

    print("trimming all the chunks...")
    print

    for i in range(len(soundData)):

        diffInSize = len(soundData[i]) - fixedSize

        if len(soundData[i]) % 2 == 0:
            temporaryBuffer = np.split(soundData[i], [diffInSize/2, len(soundData[i])-diffInSize/2])
        else:
            temporaryBuffer = np.split(soundData[i], [diffInSize / 2, len(soundData[i]) - 1 - diffInSize / 2])

        soundData[i] = temporaryBuffer[1] # take the middle slice of the split soundData array


    return soundData

def assertConstantChunkSize(soundData):

    print("asserting that all the chunks are of constant size...")
    print

    size = len(soundData[0])
    status = 1

    for i in range(len(soundData)-1):
        if len(soundData[i]) != len(soundData[i+1]):
            status = 0

    if status == 1:
        print("Done checking...: same size")
    else:
        print("Done checking...: non constant size")


def printChunkSizeDiff(soundData, fixedSize = 200):

    for i in range(len(soundData)):
        diffInSize = fixedSize - soundData[i].size
        print("difference in size for chunk{}: is {}".format(i, diffInSize))


if __name__ == "__main__":

    soundData, labels = importAllFromDir('../LL_chunks')



    soundData = reduceDensity(soundData)

    soundData = weightedAverage(soundData, betaForExponentialAverage)

    trimChunks(soundData, fixedChunkSize)

    assertConstantChunkSize(soundData)

    plotAll(soundData)








