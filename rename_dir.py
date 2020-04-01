import os
import numpy as np

from get_mfcc import absoluteFilePaths

path = '../nonLL_chunks'

def rename(path):

    print("renaming files in {}".format(path))

    list = absoluteFilePaths(path)

    print (list)
    i = 1

    for filename in list:

        os.rename(filename, "/Users/sharan/Desktop/speechApp/nonLL_chunks/chunk{}.wav".format(np.random.uniform(0.0, 5.0)))
        # print ("/Users/sharan/Desktop/speechApp/LL_chunks/chunk{}.wav".format(i))

    list = absoluteFilePaths(path)

    for filename in list:

        os.rename(filename, "/Users/sharan/Desktop/speechApp/nonLL_chunks/chunk{}.wav".format(i))
        # print ("/Users/sharan/Desktop/speechApp/LL_chunks/chunk{}.wav".format(i))
        i = i+1


if __name__ == '__main__':

    rename(path)

