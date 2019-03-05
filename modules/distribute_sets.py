'''
takes final numpydata sets and labels as inputs and distrubutes them into 2 sets, test and train
input data is already shuffled, and matched with the corresponding shuffled label before distribution
'''
import math
from get_mfcc import *

train= 0.8
test = 0.2
dev = 0


def distribute(data, labels):

    print("distributing data to test and train arrays...")

    split = math.floor(len(data)*train);
    print split




if __name__ == '__main__':

    data, labels = getFinalNormalizedMfcc()
    print data
    print labels
