# ✨ LSTM Poetry Generator

## 📌 Project Overview
This project implements a **text generation model** using **LSTMs** to generate poetry. It trains on a dataset of poems and produces new poetry based on a given seed text.

## 📂 Project Structure
```
LSTM-Poetry-Generator/
│── data/                      # Poetry dataset storage
│   ├── raw/                   # Saved raw data
│   ├── processed/             # Saved processed data
│── src/                        
│   ├── data_loader.py         # Loads poetry dataset
│   ├── preprocess.py          # Tokenization & text processing
│   ├── train.py               # LSTM model training
│   ├── generate.py            # Poetry generation
│── models/                    # Saved LSTM model
│── README.md                  # Project documentation
│── requirements.txt           # Dependencies
```

## 🛠️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/alematlop/Poetry-Generator.git
   cd Poetry-Generator
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Run
1. **Train the Model**
   ```bash
   python src/train.py
   ```
2. **Generate Poetry**
   ```bash
   python src/generate.py
   ```

## 📊 Model Details
- **Model Type:** LSTM-based Recurrent Neural Network
- **Training Data:** Poetry Foundation Poems
- **Training Process:** Next-word prediction using a word-level tokenizer
- **Input:** Seed text
- **Output:** AI-generated poem

## 📈 Example Output
**Input:**
```text
Once upon a time
```

**Generated Output:**
```text
Once upon a time
A whisper in the night
Shadows dance in silver light
Dreams take flight so bright
```

## 🎯 Future Enhancements
- Train on a larger dataset for better results
- Use pre-trained embeddings (GloVe, Word2Vec)
- Implement character-level LSTM for richer generation

## 📝 License
This project is open-source and available under the MIT License.

---
Made with ❤️ by Alexandros Matinopoulos-Lopez (https://github.com/alematlop)

