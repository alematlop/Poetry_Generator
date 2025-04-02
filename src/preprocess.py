from tensorflow.keras.preprocessing.text import Tokenizer

def tokenize_text(poems):

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(poems)
    sequences = tokenizer.texts_to_sequences(poems)

    return tokenizer, sequences