import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from preprocess import tokenize_text


def generate_poetry(seed_text, model, tokenizer, max_len=20, num_words=50):

    for _ in range(num_words):
        sequence = tokenizer.texts_to_sequences([seed_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='pre')
        predicted = np.argmax(model.predict(sequence), axis=-1)
        output_word = ""

        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word

    return seed_text

NUMBER_OF_POEMS = 50

model = tf.keras.models.load_model("../models/lstm_poetry.h5")

data = np.load("../data/processed/poems.npy")
data = data[0:NUMBER_OF_POEMS]
tokenizer, _ = tokenize_text(data)

print(generate_poetry("Once upon a time", model, tokenizer))