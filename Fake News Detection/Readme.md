### Fake News Detection

This project provides a detailed analysis and a machine learning model for the detection of fake news. The process is broken down into several key steps: data preprocessing, exploratory data analysis, and model building.

### Key Features

- **Data Preprocessing**: The project combines true and fake news datasets, cleans the text data by converting it to lowercase and removing common stop words, and creates new features like text length.

- **Exploratory Data Analysis (EDA)**: Visualizations are used to understand the characteristics of the data. This includes analyzing the distribution of subjects for both true and fake news, examining the relationship between news sentiment and text length, and plotting the most frequently occurring words and phrases (trigrams).

- **Machine Learning Model**: A `Pipeline` is used to build a classification model that can distinguish between true and fake news. This model uses  `CountVectorizer` and `TfidfTransformer` for text feature extraction and a `Multinomial Naive Bayes` classifier for prediction. The model achieves an accuracy of approximately **95.4%**.
