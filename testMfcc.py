from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt


(rate,sig) = wav.read("output.wav")


mfcc_feat = mfcc(sig,rate,nfft=512)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

feat = fbank_feat[1:3,:]
print(mfcc_feat.shape)
plt.plot(mfcc_feat)
plt.show()