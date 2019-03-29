from modules.get_words import startRecording, storeWavFile, checkChunk
from pydub import AudioSegment
from pydub.silence import split_on_silence
from modules.get_mfcc import absoluteFilePaths
import subprocess
from modules.get_mfcc import librosaMfcc
from modules.keras_test import loadandpredict
from modules.normalize_data import normalizeSoundData

class stutteranalyser():

    # paths to on disk data

    path = './temp/test.wav'
    pathforchunks = './tempchunks'

    pathtomodeljson = './modules/models/average9.json'
    pathtomodelh5 = './modules/models/average9.h5'

    frames = [] # contains the sounddata to inspect

    pausedurations = []

    wordcount = 0
    sentencecount = 0
    totalsilence = 0
    totalduration = 0
    llcount = 0
    nonllcount = 0
    llratio = 0

    instancename = ""


    def __init__(self, name = 'defaultname', duration = 10):

        # print ("init running")
        self.instancename = name
        self.totalduration = duration



    def getSound(self):

        frames = startRecording()
        storeWavFile(frames, self.path)

        line = AudioSegment.from_wav(self.path)

        audio_chunks = split_on_silence(line, min_silence_len=60, silence_thresh=-60)  # isolation of words is done here


        for i, chunk in enumerate(audio_chunks):  # audio_chunks is a python list

            if (checkChunk(chunk,i, 50, 3000) or i == 0):  #
                continue

            out_file = "./tempchunks/chunk{}.wav".format(i)
            # print ("exporting", out_file)
            chunk.export(out_file, format="wav")

        # print("Total number of words:", i + 1)

        self.wordcount = i + 1

    def predict(self):

        # print ("Importing Averages Mfccs...")
        data = librosaMfcc(self.pathforchunks)
        data = normalizeSoundData(data)
        # print data
        # print ("Done importing")


        classes = loadandpredict(self.pathtomodeljson, self.pathtomodelh5, data)

        return classes



    def __del__(self):

        print ("killing object '{}'".format(self.instancename))

        # subprocess.call("./empty_temp.sh")

        print ("emptied chunks from temp")


    def printinfo(self):
        print ("printing statistics of uttered speech:")



    def saveinfo(self):
        print ("saving info of object")

    def statistics(self):

        print ("building statistics on last 10 seconds...")
        classes = self.predict()
        self.wordcount = float(len(classes))
        self.llcount = float(len([classes[i] for i in range(len(classes)) if(classes[i,0] < classes[i,1])]))
        # self.nonllcount = self.wordcount - self.llcount
        self.llratio = self.llcount/self.wordcount

        print("{}% fluency in your speech".format(self.llratio*100))






if __name__ == '__main__':

    sentence = stutteranalyser("test")
    # sentence.getSound()
    sentence.statistics()
