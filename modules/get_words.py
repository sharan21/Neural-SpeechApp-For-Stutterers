import pyaudio
import wave
from pydub import AudioSegment
from pydub.silence import split_on_silence
from import_words import getNumberOfFiles, getNumberOfSentences

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
frames = []
p = pyaudio.PyAudio()
RECORD_SECONDS = 10
minimumWordSize = 450 # if the size of the word is <= this, reject the chunk

fileOffset = getNumberOfFiles() # makes sure that old chunks are not re-written
sentenceOffset = getNumberOfSentences() # makes sure that old sentences are not re-written

WAVE_OUTPUT_FILENAME = "../LL-sentences/output"+str(sentenceOffset)+".wav"
DEFAULT_CHUNKNAME = "../LL_chunks/chunk{}.wav"


def startRecording():

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()


def storeWavFile():
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print("Done recording, stored in output.wav")



def splitWavFileAndStore():

    line = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)

    audio_chunks = split_on_silence(line, min_silence_len=60, silence_thresh=-30)  # isolation of words is done here

    rejectedOffset = 0

    for i, chunk in enumerate(audio_chunks): # audio_chunks is a python list

        if(checkChunk(chunk,i, minimumWordSize)): #
            rejectedOffset = rejectedOffset + 1
            continue

        out_file = DEFAULT_CHUNKNAME.format(i-rejectedOffset+fileOffset)
        print("size of chunk{}: {} ".format(i-rejectedOffset+fileOffset, len(chunk)))
        print ("exporting", out_file)
        chunk.export(out_file, format="wav")
        print("done exporting...")

    print("Total number of files:", i+1)

    return i+1

def checkChunk(chunk, i, minimumWordSize): # check if the chunk is valid or not, according to size of chunk.

    if(len(chunk) <= minimumWordSize):
        print("rejected chunk{}".format(i))

    return len(chunk) <= minimumWordSize

def askUser():

    choice = input("Press 1 for LL sentence input, Press 0 for Non LL sentence input.")
    global RECORD_SECONDS
    RECORD_SECONDS = input("How many seconds do you want to record for")

    if choice == 0:
        print("You are recording Non LL sentences...")
        global WAVE_OUTPUT_FILENAME
        global DEFAULT_CHUNKNAME
        global minimumWordSize
        WAVE_OUTPUT_FILENAME = "../nonLL-sentences/output" + str(getNumberOfFiles("../nonLL_chunks")) + ".wav"
        DEFAULT_CHUNKNAME = "../nonLL_chunks/chunk{}.wav"
        minimumWordSize = 100


    else:
        print("You are recording LL sentences...")




if __name__ == '__main__':

    askUser()
    startRecording()
    storeWavFile()
    splitWavFileAndStore()
    
    
    

