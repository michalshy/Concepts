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

n_steps = 20
_data = []
def create_dataset(dataset):
    data = []
    temp = []
    for j in reversed(range(n_steps)):
        a = dataset[len(dataset) - j - 1]
        temp.append(a)
    data.append(temp)
    return np.array(data)

df = pd.read_csv(r'agv.pkl', low_memory=False)
# df = pd.read_csv(r'chosen.csv', low_memory=False)
df = df[['X-coordinate', 'Y-coordinate', 'Heading', 'Current segment']]

df['X-coordinate'] = pd.to_numeric(df['X-coordinate'], errors='coerce')
df['Y-coordinate'] = pd.to_numeric(df['Y-coordinate'], errors='coerce')
df['Heading'] = pd.to_numeric(df['Heading'], errors='coerce')
df['Current segment'] = pd.to_numeric(df['Current segment'], errors='coerce')

df['Next segment'] = df['Current segment'].shift(-1, fill_value=0.0)
df = df.dropna()

_scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[['X-coordinate', 'Y-coordinate', 'Heading', 'Current segment', 'Next segment']] = _scaler.fit_transform(df[['X-coordinate', 'Y-coordinate', 'Heading', 'Current segment', 'Next segment']])
to_drive = df_scaled.values.tolist()
for i in range(15000):
    _data.append(to_drive[i])
dataNP = np.array(_data)
plt.scatter(dataNP[:, 0], dataNP[:, 1])
plt.show()