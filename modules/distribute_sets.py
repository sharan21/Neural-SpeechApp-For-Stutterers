'''
takes final numpydata sets and labels as inputs and distrubutes them into 2 sets, test and train
input data is already shuffled, and matched with the corresponding shuffled label before distribution
'''
from get_mfcc import *
import math

train= 0.8
test = 0.2
dev = 0

def distribute(data, labels):

    print("distributing data to test and train arrays...")

    split = int(math.floor(len(data)*train))
    print ("{}:{}".format(split,len(data)-split))


    traindata = data[0:split,:]
    print traindata.shape
    trainlabel = labels[0:int(split),:]
    print trainlabel.shape

    testdata = data[split:len(data), :]
    print testdata.shape
    testlabel = labels[split:len(data), :]
    print testlabel.shape

    return traindata, trainlabel, testdata, testlabel


if __name__ == '__main__':

    data, labels = getFinalNormalizedMfcc()
    xtrain, ytrain, xtest, ytest = distribute(data, labels)


