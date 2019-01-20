from import_words import importAll, plotAll
import numpy as np



numberOfFiles = 4  #for now plotAll can only plot 4 subplots

betaForExponentialAverage = 0.98 # use b = 0 to mirror the original data


def reduceDensity(soundDataHere):

    cleanSoundData = []

    for i in range(numberOfFiles):

        k = 0
        bufferForCleaning = []

        for j in range(0, soundDataHere[i].size-1, 300):

            bufferForCleaning.insert(k, soundDataHere[i][j])
            k += 1

        cleanSoundData.append(np.absolute(bufferForCleaning))

    return cleanSoundData



def weightedAverage(soundDataHere, beta): # as beta increases, oscillations decrease

    # newData[i] = beta*newData[i-1] + (1-beta)*soundData[i]

    print("Finding the weighted exponential average...")

    newSoundData = []

    for i in range(numberOfFiles):

        bufferHere = []

        for j in range(0, soundDataHere[i].size - 1, 1):

            if j == 0:
                bufferHere.append(0)
            else:
                biasCorrection = 1/(1-pow(beta, j))
                bufferHere.append(beta*bufferHere[j-1] + (1-beta)*soundDataHere[i][j] * biasCorrection)

        newSoundData.append(np.absolute(bufferHere))

        print("done finding the exponential average...")

    return newSoundData




# MAIN

soundData = importAll(numberOfFiles)
soundData = reduceDensity(soundData)
soundData = weightedAverage(soundData, betaForExponentialAverage)

plotAll(soundData, numberOfFiles)







