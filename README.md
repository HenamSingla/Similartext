# Similar text
Cluster similar headlines together using cosine similarity on Word2Vec embeddings to group semantically related news.

# Headline Similarity Clustering

This project clusters similar headlines by leveraging cosine similarity computed on Word2Vec embeddings. By tokenizing headlines, removing stopwords, and generating sentence vectors, the tool identifies and groups semantically related headlines together.

## Features

- **Tokenization:**  
  Uses NLTK's RegexpTokenizer to split headlines into tokens.
  
- **Stopword Removal:**  
  Filters out common English stopwords using NLTK's stopwords list.
  
- **Word Embeddings:**  
  Generates word vectors using Gensim's Word2Vec model.
  
- **Sentence Embedding:**  
  Computes sentence vectors by summing individual word vectors.
  
- **Cosine Similarity Calculation:**  
  Calculates pairwise cosine similarity to measure semantic similarity.
  
- **Clustering:**  
  Groups headlines with high similarity scores into clusters.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HenamSingla/Similartext.git
   cd Similartext
