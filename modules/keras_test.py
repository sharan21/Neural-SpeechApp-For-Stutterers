from keras.models import Sequential
from keras.layers import Dense
x




model = Sequential()

model.add(Dense(units=20, activation='relu', input_dim=20))
model.add(Dense(units=30, activation='relu'))
model.add(Dense(units=1, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])





# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.


model.fit(x_train, y_train, epochs=5, batch_size=32)

# model.train_on_batch(x_batch, y_batch)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

classes = model.predict(x_test, batch_size=128)

