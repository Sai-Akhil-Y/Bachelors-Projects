### **Description**

This project addresses the challenge of metaphor detection in natural language processing (NLP). It aims to build a deep learning model that can distinguish between metaphorical and non-metaphorical sentences. The approach leverages transfer learning by using pre-trained language models to generate contextualized word embeddings, which are then used to train a neural network classifier.

---
### **Project Goal**

The primary goal is to create a model that can classify a given sentence as either 'literal' or 'non-literal' (metaphorical). The project analyzes existing models and then develops and deploys a new model with improved efficiency.

---
### **Proposed Architecture**

The system's architecture involves several key modules:

- **Preprocessing**: This phase involves data wrangling steps like removing null values and duplicates, converting text to lowercase, tokenizing sentences, and lemmatizing tokens.

- **Contextualized Word Embeddings**: Sentences are prepared by adding `[CLS]` and `[PAD]` tokens and then fed into a pre-trained NLP model like BERT or ERNIE 2.0 to generate contextualized word embeddings.

- **Classification**: The generated embeddings are used to train a neural network classifier. The project specifically evaluates and compares the performance of a Dense Neural Network (DNN), Long Short-Term Memory (LSTM), and a Bidirectional Long Short-Term Memory (Bi-LSTM) network. Bi-LSTMs were found to be the most effective, as they capture long-range relationships between words.


---
### **Software/Tools**

The project utilizes several Python libraries and tools:

- **Jupyter Notebook/Google Colab**: Used for creating and sharing documents with live code.
- **Pandas, NumPy**: For processing and extracting features from data.
- **Keras, PyTorch**: Open-source libraries for deep learning applications.
- **Scikit-learn**: For dataset modifications and model evaluation.
- **Natural Language Toolkit (NLTK)**: A suite of libraries for symbolic and statistical NLP in English.

---
### **Datasets**

The model's performance was evaluated using two datasets:

1. **TroFi Dataset**: Consists of sentences with 50 different verbs and a total of 3,737 samples. This dataset helps evaluate the model's performance on a smaller variety of verbs.
2. **VUA Dataset**: Contains 17,380 sentences with 2,063 unique verbs. This dataset is used to assess the model's performance with a larger variety of verbs.