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

n_steps = 50
steps = 50

def create_dataset(dataset):
    data = []
    temp = []
    for j in reversed(range(n_steps)):
        a = dataset[len(dataset) - j - 1]
        temp.append(a)
    data.append(temp)
    return np.array(data)

_data = []
finData =[]
model: keras.Model = keras.models.load_model(r'fatal.keras')
df = pd.read_csv(r'agv.pkl', low_memory=False)
df = df.head(400)
df = df[df['Speed'] != 0]

# df = pd.read_csv(r'chosen.csv', low_memory=False)
df = df[['X-coordinate', 'Y-coordinate', 'Heading', 'Going to ID', 'Target reached', 'Current segment']]

df['X-coordinate'] = pd.to_numeric(df['X-coordinate'], errors='coerce')
df['Y-coordinate'] = pd.to_numeric(df['Y-coordinate'], errors='coerce')
df['Heading'] = pd.to_numeric(df['Heading'], errors='coerce')
df['Going to ID'] = pd.to_numeric(df['Going to ID'], errors='coerce')
df['Target reached'] = pd.to_numeric(df['Target reached'], errors='coerce')
df['Current segment'] = pd.to_numeric(df['Current segment'], errors='coerce')

df['Next segment'] = df['Current segment'].shift(-1, fill_value=0.0)

_scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[['X-coordinate', 'Y-coordinate', 'Heading', 'Going to ID', 'Target reached', 'Current segment', 'Next segment']] = _scaler.fit_transform(df[['X-coordinate', 'Y-coordinate', 'Heading', 'Going to ID', 'Target reached', 'Current segment', 'Next segment']])
to_drive = df_scaled.values.tolist()
for i in range(len(to_drive)):
    _data.append(to_drive[i])


df.plot(kind = 'scatter', x = 'X-coordinate', y = 'Y-coordinate')
plt.show()
# dataNP = np.array(_data)
# plt.scatter(dataNP[:, 0], dataNP[:, 1])
# plt.show()

# for i in range(5):
#     finData.append(to_drive[i])
# finNp = np.array(finData)
# plt.plot(finNp[:, 0], finNp[:, 1])
# plt.show()

finData.clear()
for i in range(steps):
    finData.append(to_drive[i])
finNp = _scaler.inverse_transform(np.array(finData))
plt.plot(finNp[:, 0], finNp[:, 1])
plt.show()
steps += 1
for i in range(250):
    df2 = pd.DataFrame(finData, columns=['X-coordinate', 'Y-coordinate', 'Heading', 'Going to ID', 'Target reached', 'Current segment', 'Next segment'])
    df2 = df2.values
    toPredict = create_dataset(df2)
    predicted = model.predict(toPredict)
    # finData.append(to_drive[steps])
    finData.append(predicted[0])
    # print(_scaler.inverse_transform(predicted))
    steps += 1
toPlot = _scaler.inverse_transform(finData)

finNp = np.array(toPlot)
plt.plot(finNp[:, 0], finNp[:, 1])
plt.show()

