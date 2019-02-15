

'''

After using get_words.
Imports the wave word chunks from all_chunks as a numpy arrays, according to numberOfFiles,
stores as 'soundData' variable for pre-processing and feature extraction.

'''
import numpy as np
from scipy.io.wavfile import read
from matplotlib import pyplot as plt
import scipy.io.wavfile
from pydub import AudioSegment
import os


rateList = []
dataList = []
soundData = []


outFileWav = [] # wav file chunks
outFileMp3 = [] # mp3 file chunks


def getNumberOfFiles(path = './LL_chunks'):
    list = os.listdir(path)  # dir is your directory path
    number_files = len(list)

    # print ("Number of Files found in all_chunks:", number_files-1)

    return number_files



def getNumberOfSentences(path = './LL-sentences'):

    list = os.listdir(path)  # dir is your directory path
    number_files = len(list)

    # print ("Number of sentences found in sentences directory:", number_files - 1)

    return number_files


def convertToMp3(numberOfFilesHere): # run only after you get all the wav chunks in all_chunks

    outFile, outFileMp = nameAll(numberOfFilesHere)
    for i in range(numberOfFilesHere):
        AudioSegment.from_wav(outFile[i]).export(outFileMp[i], format="mp3")


def importAll(numberOfFilesHere):

    print("assigning names of samples")
    outFile, outFileMpthree = nameAll(numberOfFilesHere)

    for i in range(numberOfFilesHere-1):

        # get names of all the samples in the form of "outfile"

        rate, data = scipy.io.wavfile.read(outFile[i])
        rateList.append(rate)
        dataList.append(rate)
        soundData.append(np.absolute(data))  # diode full wave rectification is done here
    return soundData


def nameAll(numberOfFilesHere): # gets list of file names for wav and mp3 to export later

    for i in range(numberOfFilesHere-1):
        outFileWav.append("./LL_chunks/chunk{0}.wav".format(i))
        print(outFileWav[i])

    for i in range(numberOfFilesHere-1):
        outFileMp3.append("./mp3_chunks/chunk{0}.mp3".format(i))


    print("done naming all samples...")

    return outFileWav, outFileMp3




def plotAllMaxFour(soundData, numberOfFilesHere): # for max 4 plots

    print("plotting all the samples")
    for i in range(numberOfFilesHere-1):

        plt.subplot(221+i)
        plt.plot(soundData[i])

    plt.show()
    print("done plotting samples...")


def plotAll(soundDataHere, numberOfFilesHere):

    print("plotting all the samples")
    for i in range(numberOfFilesHere-1):
        plt.plot(soundDataHere[i])
        plt.show()


    print("done plotting samples...")




if __name__ == '__main__':

    print getNumberOfSentences('./train-data')
    # numberOfFiles = getNumberOfFiles()

    # soundData = importAll(numberOfFiles) # function to import all the chunks

    # plotAll(soundData, numberOfFiles)

    # convertToMp3()





