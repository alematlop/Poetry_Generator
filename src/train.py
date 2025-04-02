from keras.src.utils import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, Dropout
import numpy as np
from preprocess import tokenize_text
import tensorflow as tf

NUMBER_OF_POEMS = 100
NUMBER_OF_EPOCHS = 30

data = np.load("../data/processed/poems.npy")
data = data[0:NUMBER_OF_POEMS]
tokenizer, sequences = tokenize_text(data)

X, y = [], []

for seq in sequences:
    for i in range(1, len(seq)):
        X.append(seq[:i])
        y.append(seq[i])

max_len = max([len(seq) for seq in X])
X = pad_sequences(X, maxlen=max_len, padding='pre')
y = np.array(y)

model = Sequential([
    Embedding(input_dim = len(tokenizer.word_index) + 1, output_dim=100, input_length = max_len),
    LSTM(150, return_sequences = True),
    Dropout(0.2),
    LSTM(100),
    Dense(len(tokenizer.word_index) + 1, activation = 'softmax')
])

optimizer = tf.keras.optimizers.Adam(0.001)

model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer = optimizer,
              metrics = ['accuracy']
              )
model.fit(X, y, epochs = NUMBER_OF_EPOCHS, verbose=1)
model.save("../models/lstm_poetry.h5")