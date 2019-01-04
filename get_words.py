import pyaudio
import wave
from pydub import AudioSegment
from pydub.silence import split_on_silence

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
frames = []
p = pyaudio.PyAudio()
RECORD_SECONDS = 10


WAVE_OUTPUT_FILENAME = "output.wav"


def getAudio():

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


getAudio() # get a fresh recording

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(p.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

line = AudioSegment.from_wav("output.wav")
audio_chunks = split_on_silence(line,min_silence_len=100, silence_thresh=-40) #isolation of words is done here

#next step is to name and export all the chunks, into ./all_chunks

for i, chunk in enumerate(audio_chunks):

    out_file = "./all_chunks/chunk{0}.wav".format(i)
    print ("exporting", out_file)
    chunk.export(out_file, format="wav")
    print("done exporting...")
    




    
    
    

