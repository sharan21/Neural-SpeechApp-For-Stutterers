from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from distribute_sets import *
from keras.utils import to_categorical
from keras.models import model_from_json
from keras.callbacks import TensorBoard
from keras import regularizers
from keras import optimizers
log_dir = './logs'

def makemodel():

    print ("Making model")
    model = Sequential()

    # BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,
    #                                 beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros',
    #                                 moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None,
    #                                 beta_constraint=None, gamma_constraint=None)

    model.add(Dense(units=10, activation='relu', input_dim=20))
    model.add(Dense(units=20, activation='relu'))

    # model.add(Dropout(0.5))
    # model.add(Dropout(0.5))

    model.add(Dense(activation='softmax', output_dim=2))

    adam = optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)

    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    return model


def makemodel2():

    print ("Making model")
    model = Sequential()

    BatchNormalization(
        axis=-1, momentum=0.99,
        epsilon=0.001,
        center=True,
        scale=True,
        beta_initializer='zeros',
        gamma_initializer='ones',
        moving_mean_initializer='zeros',
        moving_variance_initializer='ones',
        beta_regularizer=None,
        gamma_regularizer=None,
        beta_constraint=None,
        gamma_constraint=None)

    model.add(Dense(units=20, activation='relu', input_dim=20))
    model.add(Dropout(0.3))
    model.add(Dense(units=80, activation='relu')) (20,80)
    model.add(Dropout(0.3))
    model.add(Dense(units=40, activation='relu')) (80,40)
    model.add(Dropout(0.3))
    model.add(Dense(units=20, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Dense(activation='softmax', output_dim=2))

    adam = optimizers.Nadam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)

    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    return model



def trainmodel(pathtojson, pathtoh5):
    print ("Training model")

    trainedmodel = makemodel2()
    trainedmodel.fit(x_train, y_train, epochs=400, batch_size=16)

    print ("Saving model")

    model_json = trainedmodel.to_json()
    with open(pathtojson, "w") as json_file:
        json_file.write(model_json)
    trainedmodel.save_weights(pathtoh5)
    print("Saved model to disk")

    score, acc = trainedmodel.evaluate(x_test, y_test, batch_size=16)
    print ("Scores for Test set: {}".format(score))
    print ("Accuracy for Test set: {}".format(acc))

    return trainedmodel


def testmodel(pathtojson, pathtoh5, data, labels ):
    print ("Testing model")

    print("using model: {}".format(pathtojson))

    # load json and create model
    json_file = open(pathtojson, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights(pathtoh5)
    print("Loaded model from disk")

    loaded_model.compile(loss='categorical_crossentropy',
                         optimizer='adam',
                         metrics=['accuracy'])
    print(data.shape)

    labels = to_categorical(labels)
    score, acc = loaded_model.evaluate(data, labels, batch_size=16)
    print ("Scores for Test set: {}".format(score))
    print ("Accuracy for Test set: {}".format(acc))


def loadmodel(pathtojson, pathtoh5):

    json_file = open(pathtojson, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights(pathtoh5)

    return loaded_model





def loadandpredict(pathtojson, pathtoh5, data):

    # print("using model: {}".format(pathtojson))

    # load json and create model
    json_file = open(pathtojson, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    #load weights into new model

    loaded_model.load_weights(pathtoh5)
    # print("Loaded model from disk")


    loaded_model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # print ("compiled the loaded model with cat. cross entropy with adam optim...")

    # print ("shape of data {}".format(data.shape))

    classes = loaded_model.predict(data)

    # print ("done predicting, printing")


    for instance in classes:

        print (instance)
        print (parseinstance(instance))

    return classes


# model.train_on_batch(x_batch, y_batch)

def parseinstance(instance):
    return "ll" if instance[1]>instance[0] else "nonll"

def getweightscore(model):
    weightscore = np.identity(20)

    for layer in model.layers:
        print("trying")
        weights = layer.get_weights()  # list of numpy arrays
        if(len(weights)==2):
            print("if")
            weights.pop()
            print(np.shape(weights[0]))
            weightscore = np.dot(weightscore, weights[0])
        else:
            continue


    print("weight score is {}".format(weightscore))

    ranking = [e[0]+e[1] for e in weightscore]
    print("ranking matrix is {}".format(ranking))






    # for layer in model.layers:
    #     print("trying")
    #
    #     weights = layer.get_weights()  # list of numpy arrays
    #     if(len(weights)==2):
    #         print(weights[0])
    #     else:
    #         print("problem")





if __name__ == '__main__':

    print("hello")

    data, labels = getFinalNormalizedMfcc()
    # print data.shape
    # print type(data)
    # print labels.shape
    # print type(labels)

    x_train, y_train, x_test, y_test = distribute(data, labels)
    # print x_train.shape
    # print y_train.shape
    # print x_test.shape
    # print y_test.shape

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    pathtojson = './models/average10.json'
    pathtoh5 = './models/average10.h5'
    #
    #
    # trainmodel(pathtojson, pathtoh5)
    #
    # testmodel(pathtojson, pathtoh5, data, labels)

    # loadandpredict('./model.json','./model.h5',data)

    model = loadmodel(pathtojson, pathtoh5)
    getweightscore(model)

    # print(w)
    # print(len(w))
    # print(type(w))
    # print(w.shape)






