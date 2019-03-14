from keras.models import Sequential
from keras.layers import Dense
from distribute_sets import *
from keras.utils import to_categorical
from keras import optimizers
from keras.models import model_from_json



def makemodel():

    print ("Making model")
    model = Sequential()
    model.add(Dense(units=20, activation='relu', input_dim=20))
    model.add(Dense(units=50, activation='relu'))
    model.add(Dense(units=30, activation='relu'))
    model.add(Dense(units=10, activation='relu'))
    model.add(Dense(activation='softmax', output_dim=2))

    adam = optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.004)

    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    return model


def trainmodel():
    print ("Training model")

    trainedmodel = makemodel()
    trainedmodel.fit(x_train, y_train, epochs=300, batch_size=16)

    print ("Saving model")

    model_json = trainedmodel.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    trainedmodel.save_weights("model.h5")
    print("Saved model to disk")

    return trainedmodel


def testmodel():
    print ("Testing model")

    trainedmodel = trainmodel()
    score, acc = trainedmodel.evaluate(x_test, y_test, batch_size=16)
    print ("Scores for Test set: {}".format(score))
    print ("Accuracy for Test set: {}".format(acc))


def predict(model):

    classes = model.predict(x_test, batch_size=16)


def loadandpredict(pathtojson, pathtoh5, data):

    print("using model: {}".format(pathtojson))

    # load json and create model
    json_file = open(pathtojson, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    #load weights into new model

    loaded_model.load_weights(pathtoh5)
    print("Loaded model from disk")


    loaded_model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print ("compiled the loaded model with cat. cross entropy with adam optim...")

    classes = loaded_model.predict(data)

    print ("done predicting, printing")

    for instance in classes:
        print instance




# model.train_on_batch(x_batch, y_batch)


if __name__ == '__main__':

    print("hello")

    data, labels = getFinalNormalizedMfcc()
    print data.shape
    print type(data)
    print labels.shape
    print type(labels)

    x_train, y_train, x_test, y_test = distribute(data, labels)
    print x_train.shape
    print y_train.shape
    print x_test.shape
    print y_test.shape

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    makemodel()

    trainmodel()

    # testmodel()




