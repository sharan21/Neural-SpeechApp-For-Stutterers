from scipy.fftpack import fft

def convertToFdomain(soundData,numberOfFiles):
    for i in range(numberOfFiles-1):
        for j in range(soundData[i].size - 1):
            soundData[i] = fft(soundData[i])

    print("done with fft...")
    return soundData

