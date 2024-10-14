import tensorflow as tf
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam

df = pd.read_csv('csvData.csv')
df = df[df["Automatic Mode active"] == True]
#TO TEST
df = df[df["Current segment"] == 10.0]
#UPPER TO TEST
df = df[["Battery cell voltage", "X-coordinate", "Y-coordinate", "Going to ID", "Current segment"]]
print(df)

test_split=round(len(df)*0.20)
df_for_training=df[:-1041]
df_for_testing=df[-1041:]
print(df_for_training.shape)
print(df_for_testing.shape)

scaler = MinMaxScaler(feature_range=(0,1))
df_for_training_scaled = scaler.fit_transform(df_for_training)
df_for_testing_scaled=scaler.transform(df_for_testing)
print(df_for_training_scaled)


def createXY(dataset,n_past):
    dataX = []
    dataY = []
    for i in range(n_past, len(dataset)):
            dataX.append(dataset[i - n_past:i, 0:dataset.shape[1]])
            dataY.append(dataset[i,0:dataset.shape[1]])
    return np.array(dataX),np.array(dataY)
trainX,trainY=createXY(df_for_training_scaled,30)
testX,testY=createXY(df_for_testing_scaled,30)

print("trainX Shape-- ",trainX.shape)
print("trainY Shape-- ",trainY.shape)

model1 = Sequential()
model1.add(InputLayer((5, 5)))
model1.add(LSTM(64))
model1.add(Dense(8, 'relu'))
model1.add(Dense(5, 'linear'))

model1.summary()

cp1 = ModelCheckpoint('model/m.keras', save_best_only=True)
model1.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=0.0001), metrics=[RootMeanSquaredError()])

model1.fit(trainX, trainY, validation_data=(testX, testY), epochs=10, callbacks=[cp1])

from tensorflow.keras.models import load_model
model1 = load_model('model/m.keras')

train_predictions = model1.predict(trainX).flatten()
print(train_predictions)

prediction_copies_array = np.repeat(train_predictions,5, axis=-1)
pred=scaler.inverse_transform(np.reshape(prediction_copies_array,(len(train_predictions),5)))[:,0]
print(pred)

