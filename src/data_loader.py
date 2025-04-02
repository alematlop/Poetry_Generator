import numpy as np
import re
import string

def clean_text(text):

    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = " ".join([word for word in text.split()])

    return text


arr = []
c = 0
with open("../data/raw/poetry_foundation_data.txt", encoding="utf-8") as file:
    for line in file:
        if line[0] == '"' and c == 0:
            c = 1
            poem = ""
            continue

        if line[0] == "<" and c == 1:
            c = 0
            arr.append(clean_text(poem))

        if c == 1:
            poem += line

np.save("../data/processed/poems", arr)

