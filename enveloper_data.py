from import_words import *
import numpy as np
from clean_data import reduceDensity

delta = 0.7  # percentage
numberOfFiles = 4
status = 0
newSoundData = []

# RC circuit characteristics

dischargeRate = 0.5 # percentage
exponentialTerm = 0.001
chargeRate = 0
currentCharge = 0


def deltaEnv(delta,numberOfFiles,soundData):

    for i in range(numberOfFiles):  # do for all the audio samples

        for j in range(len(soundData[i])-1):  # each sample is of variable size and is un-clipped

            if soundData[i][j]*delta >= soundData[i][j+1]:  # main envelope condition
                soundData[i][j+1] = soundData[i][j]

    print("done enveloping all the samples")

    return soundData



def rcEnv(dischargeRate, numberOffiles, soundData):  # RC circuit, to envelope the signal
    for i in range(numberOfFiles):
        for j in range(soundData[i].size-1):
            adjDifference = soundData[i][j+1]-soundData[i][j]

            if soundData[i][j] >= soundData[i][j+1]:
                soundData[i][j+1] = soundData[i][j]-dischargeRate*soundData[i][j]
                #dischargeRate += exponentialTerm

            # if soundData[i][j] <= soundData[i][j+1]:
            #     soundData[i][j+1] = soundData[i][j]*1.5



    print("done enveloping the samples according to RC law")
    return soundData

def trimmer(soundData):

    for i in range(numberOfFiles-1):
        threshHold = np.amax(soundData[i]) / 2

        for j in range(soundData[i].size-1):
            if(soundData[i][j]<=threshHold):
                soundData[i][j]=0;

    return soundData



#MAIN FUNCTION

soundData = importAll(numberOfFiles)

