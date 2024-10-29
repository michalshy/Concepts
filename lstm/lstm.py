from pygame import Surface
import heapq
import queue
import tensorflow as tf
import keras
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import math
from enum import Enum 
import matplotlib.pyplot as plt


def create_dataset(dataset):
    data = []
    temp = []
    for j in range(5):
        a = dataset[len(dataset) - j - 1]
        temp.append(a)
    data.append(temp)
    return np.array(data)

_data = []
_path = []
finData =[]
model: keras.Model = keras.models.load_model(r'jakub.keras')
df = pd.read_csv(r'agv.pkl', low_memory=False)
df = df[['X-coordinate', 'Y-coordinate', 'Heading','Current segment']]
df['X-coordinate'] = pd.to_numeric(df['X-coordinate'], errors='coerce')
df['Y-coordinate'] = pd.to_numeric(df['Y-coordinate'], errors='coerce')
df['Heading'] = pd.to_numeric(df['Heading'], errors='coerce')
df = df.dropna()
df = df[df['Current segment'] == 59.0]
df = df[['X-coordinate', 'Y-coordinate', 'Heading']]
_scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[['X-coordinate', 'Y-coordinate', 'Heading']] = _scaler.fit_transform(df[['X-coordinate', 'Y-coordinate', 'Heading']])
to_drive = df_scaled.values.tolist()
for i in range(len(to_drive)):
    _data.append(to_drive[i])


# df.plot(kind = 'scatter', x = 'X-coordinate', y = 'Y-coordinate')
# plt.show()
# dataNP = np.array(_data)
# plt.scatter(dataNP[:, 0], dataNP[:, 1])
# plt.show()

for i in range(39):
    finData.append(to_drive[131 + i])
finNp = np.array(finData)
plt.plot(finNp[:, 0], finNp[:, 1])
plt.show()

finData.clear()

for i in range(5):
    finData.append(to_drive[131 + i])

for i in range(30):
    df2 = pd.DataFrame(finData, columns=['X-coordinate', 'Y-coordinate', 'Heading'])
    df2 = df2.values
    df2 = df2.astype('float32')
    toPredict = create_dataset(df2)
    predicted = model.predict(toPredict)
    finData.append(predicted[0])

finNp = np.array(finData)
plt.plot(finNp[:, 0], finNp[:, 1])
plt.show()

