from modules.get_words import startRecording, storeWavFile, checkChunk
from pydub import AudioSegment
from pydub.silence import split_on_silence
from modules.get_mfcc import absoluteFilePaths
import subprocess
from modules.get_mfcc import librosaMfcc
from modules.keras_test import loadandpredict
from modules.normalize_data import normalizeSoundData
from modules.import_words import getNumberOfFiles

def clearlogs():
    print ("clearing logs...")
    f = open("./logs/stats.txt", "w")
    f.write("")

class stutteranalyser():

    def __init__(self, name = 'defaultname', duration = 8):

        # print ("init running")
        self.instancename = name
        self.totalduration = duration
        self.path = './tempsentences/{}.wav'.format(self.instancename)
        self.pathforchunks = './tempchunks'
        self.fileoffset = getNumberOfFiles(self.pathforchunks)

        self.pathtomodeljson = './modules/models/average9.json'
        self.pathtomodelh5 = './modules/models/average9.h5'

        self.frames = []

        self.pausedurations = []

        self.wordcount = 0.0
        self.totalsilence = 0.0
        self.llcount = 0.0
        self.nonllcount = 0
        self.llratio = 0.0
        self.status = False
        self.llscore = 0.0
        self.speed = 0.0

        self.instancename = ""

        self.mfcc = []

    def getSound(self):

        frames = startRecording()
        storeWavFile(frames, self.path)

        line = AudioSegment.from_wav(self.path)

        audio_chunks = split_on_silence(line, min_silence_len=60, silence_thresh=-60)  # isolation of words is done here


        for i, chunk in enumerate(audio_chunks):  # audio_chunks is a python list

            if (checkChunk(chunk,i, 50, 3000) or i == 0):  #
                continue

            out_file = "./tempchunks/chunk{}.wav".format(i+self.fileoffset)
            # print ("exporting", out_file)
            chunk.export(out_file, format="wav")

        # print("Total number of words:", i + 1)

        self.wordcount = i + 1

    def predict(self):

        # print ("Importing Averages Mfccs...")
        data = librosaMfcc(self.pathforchunks)
        data = normalizeSoundData(data)
        # print data

        classes = loadandpredict(self.pathtomodeljson, self.pathtomodelh5, data)

        return classes




    def __del__(self):

        # print ("killing object '{}'".format(self.instancename))

        # subprocess.call("./empty_temp.sh")

        print ("emptied chunks from temp")


    def buildstatistics(self):

        print ("building statistics on last 10 seconds...")

        classes = self.predict()
        self.wordcount = float(len(classes))

        # self.llcount = float(len([classes[i] for i in range(len(classes)) if(classes[i,0] < classes[i,1])]))

        self.llcount = float(len([classes[i] for i in range(len(classes)) if (classes[i, 1] > 0.5)]))

        self.nonllcount = self.wordcount - self.llcount
        self.llratio = self.llcount/self.wordcount
        self.speed = float(self.wordcount)/float(self.totalduration)*60

        self.status= True if self.llratio > 0.5 else False

        print("{}% fluency in your speech".format(self.llratio*100))

    def savestatistics(self):

        print ("saving stats into the disk")

        f = open("./logs/stats.txt", "a")

        # f.write("Name of Instance : '{}' \n".format(self.instancename))
        #
        # f.write("Total number of words: {} \n".format(self.wordcount))
        #
        # f.write("Number of LL words: {} \n ".format(self.llcount))
        #
        # f.write("LL ratio: {} \n".format(self.llratio))
        #
        # f.write("")

        f.write("{} {} {} {} {} {}\n".format(self.instancename, self.wordcount, self.llcount, self.llratio, self.status, self.speed))

if __name__ == '__main__':

    clearlogs()

    i = 0



    while True:

        i = i+1
        sentence = stutteranalyser("sentence{}".format(i))
        sentence.getSound()
        sentence.buildstatistics()
        sentence.savestatistics()

        subprocess.call('./empty_temp.sh')

        #to stop at 10 words
        if(getNumberOfFiles(path = './tempchunks') > 10):
            print("you have finished recording 10 words")
            break

        del sentence

    print("Done!")




