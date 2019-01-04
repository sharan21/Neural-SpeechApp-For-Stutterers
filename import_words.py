
import numpy as np
from scipy.io.wavfile import read
from matplotlib import pyplot as plt
import scipy.io.wavfile
from pydub import AudioSegment


rateList = []
dataList = []
soundData = []
outFile = [] #array of all the names of the chunk files
outFileMpthree = []
numberOfFiles = 4

def convertToMpthree():
    outFile, outFileMp = nameAll(numberOfFiles)
    for i in range(numberOfFiles):
        AudioSegment.from_wav(outFile[i]).export(outFileMp[i], format="mp3")


def importAll(numberOfFilesHere):

    print("assigning names of samples")
    outFile, outFileMpthree = nameAll(numberOfFilesHere)

    for i in range(numberOfFiles):

        # get names of all the samples in the form of "outfile"

        rate, data = scipy.io.wavfile.read(outFile[i])
        rateList.append(rate)
        dataList.append(rate)
        soundData.append(np.absolute(data))  # diode full wave rectification is done here
    return soundData


def nameAll(numberOfFilesHere):
    for i in range(numberOfFilesHere):
        outFile.append("./all_chunks/chunk{0}.wav".format(i))
        print(outFile[i])

    for i in range(numberOfFiles):
        outFileMpthree.append("./new_chunks/chunkmp{0}.mp3".format(i))


    print("done naming all samples...")

    return outFile, outFileMpthree


def singleSampleTest():

    rate, data = scipy.io.wavfile.read("./all_chunks/chunk5.wav")
    soundData.append(np.absolute(data))
    plt.plot(soundData[0])
    plt.show()



def plotAll(soundData, numberOfFilesHere):

    print("plotting all the samples")
    for i in range(numberOfFilesHere):

        plt.subplot(221+i)
        plt.plot(soundData[i])

    plt.show()
    print("done plotting samples...")


soundData = importAll(numberOfFiles) # function to import all the chunks

#plotAll(soundData, numberOfFiles)

#convertToMpthree()    TO CONVERT SAMPLES FROM WAV->MP3





