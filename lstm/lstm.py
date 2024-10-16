import tensorflow as tf
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, InputLayer
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv('csvData.csv')
df = df[df["Automatic Mode active"] == True]
#TO TEST
df.index = df['Timestamp']
print(df)
df = df[df["Current segment"] == 10.0]
#UPPER TO TEST
df = df[["Battery cell voltage", "X-coordinate", "Y-coordinate", "Going to ID", "Current segment"]]
print(df)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

sequenceLen = 10
nimFeatures = len(df.columns)

# Create sequences and corresponding labels
sequences = []
labels = []
for i in range(len(scaled_data) - sequenceLen):
    seq = scaled_data[i:i+sequenceLen]
    label = scaled_data[i+sequenceLen]  # '_tempm' column index
    sequences.append(seq)
    labels.append(label)

# Convert to numpy arrays
sequences = np.array(sequences)
labels = np.array(labels)

# Split into train and test sets
train_size = int(0.8 * len(sequences))
train_x, test_x = sequences[:train_size], sequences[train_size:]
train_y, test_y = labels[:train_size], labels[train_size:]

print("Train X shape:", train_x.shape)
print("Train Y shape:", train_y.shape)
print("Test X shape:", test_x.shape)
print("Test Y shape:", test_y.shape)

# Create the LSTM model
model = Sequential()

# Add LSTM layers with dropout
model.add(InputLayer(batch_input_shape=(1, train_x.shape[1], train_x.shape[2])))
model.add(LSTM(units=128, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=64, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=32, return_sequences=False))
model.add(Dropout(0.2))

# Add a dense output layer
model.add(Dense(units=5))

model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()

# Define callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('./model/best/model.keras', monitor='val_loss', save_best_only=True)

# # Train the model
# history = model.fit(
#     train_x, train_y,
#     epochs=100,
#     batch_size=64,
#     validation_split=0.2,  # Use part of the training data as validation
#     callbacks=[early_stopping, model_checkpoint]
# )

best_model = tf.keras.models.load_model('C:/Users/Michin/Desktop/Zajawki/projekty/Concepts/lstm/model/best/model.keras')
test_loss = best_model.evaluate(test_x, test_y)
print("Test Loss:", test_loss)

predictions = best_model.predict(test_x)

# Calculate evaluation metrics
mae = mean_absolute_error(test_y, predictions)
mse = mean_squared_error(test_y, predictions)
rmse = np.sqrt(mse)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

# y_true values
test_y_copies = np.repeat(test_y.reshape(-1, 1), test_x.shape[-1], axis=-1)
print(test_y_copies)
true_temp = scaler.inverse_transform(test_y_copies)[:,4]


# predicted values
prediction = best_model.predict(test_x)
print(prediction)
prediction_copies = np.repeat(prediction, 1, axis=-1)
predicted_temp = scaler.inverse_transform(prediction_copies)[:,4]
print(predicted_temp)