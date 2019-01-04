import tensorflow as tf
from tensorflow.contrib.framework.python.ops import audio_ops as contrib_audio

filename = './output.wav'


def parse_wave_tf(filename):
    audio_binary = tf.read_file(filename)
    desired_channels = 1
    wav_decoder = contrib_audio.decode_wav(
        audio_binary,
        desired_channels=desired_channels)
    with tf.Session() as sess:
        sample_rate, audio = sess.run([
            wav_decoder.sample_rate,
            wav_decoder.audio])
        first_sample = audio[0][0] * (1 << 15)
        second_sample = audio[1][0] * (1 << 15)
        print('''
Parsed {filename}
-----------------------------------------------
Channels: {desired_channels}
Sample Rate: {sample_rate}
First Sample: {first_sample}
Second Sample: {second_sample}
Length in Seconds: {length_in_seconds}'''.format(
            filename=filename,
            desired_channels=desired_channels,
            sample_rate=sample_rate,
            first_sample=first_sample,
            second_sample=second_sample,
            length_in_seconds=len(audio) / sample_rate))


parse_wave_tf(filename)