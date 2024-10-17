import tensorflow as tf
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, InputLayer
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv('csvData.csv')
df = df[df["Automatic Mode active"] == True]
#TO TEST
# df.index = df['Timestamp']
# print(df)
df = df[df["Current segment"] == 10.0]
#UPPER TO TEST
df_for_training = df[["Heading", "Battery cell voltage", "X-coordinate", "Y-coordinate"]]
print(df_for_training)

scaler = StandardScaler()
scaler = scaler.fit(df_for_training)
dfScaled = scaler.transform(df_for_training)

trainX = []
trainY = []

n_future = 1
n_past = 15

for i in range(n_past, len(dfScaled) - n_future + 1):
    trainX.append(dfScaled[i - n_past:i, 0:df_for_training.shape[1]])
    trainY.append(dfScaled[i + n_future - 1:i + n_future, 1])

trainX, trainY = np.array(trainX), np.array(trainY)

print('trainX shape == {}.'.format(trainX.shape))
print('trainY shape == {}.'.format(trainY.shape))

model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(trainX.shape[1], trainX.shape[2]), return_sequences=True))
model.add(LSTM(32, activation='relu', return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(trainY.shape[1]))

model.compile(optimizer='adam', loss='mse')
model.summary()


# fit the model
history = model.fit(trainX, trainY, epochs=20, batch_size=16, validation_split=0.1, verbose=1)

plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.legend()
plt.show()

prediction = model.predict(trainX[0:10])

print(prediction)

prediction_copies = np.repeat(prediction, df_for_training.shape[1], axis=-1)
y_pred_future = scaler.inverse_transform(prediction_copies)[:,0]

print(trainX)

print(y_pred_future)