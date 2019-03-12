from keras.models import Sequential
from keras.layers import Dense
from distribute_sets import *
from keras.utils import to_categorical



model = Sequential()


model.add(Dense(units=20, activation='relu', input_dim=20))
model.add(Dense(units=30, activation='relu'))
model.add(Dense(activation='softmax', output_dim = 2))


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# import shuffled dataset and labels

data, labels = getFinalNormalizedMfcc()
print data.shape
print type(data)
print labels.shape
print type(labels)

# distribute them to test and train

x_train, y_train, x_test, y_test = distribute(data, labels)
print x_train.shape
print y_train.shape
print x_test.shape
print y_test.shape

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.


model.fit(x_train, y_train, epochs=5, batch_size=20)

# model.train_on_batch(x_batch, y_batch)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

classes = model.predict(x_test, batch_size=128)

