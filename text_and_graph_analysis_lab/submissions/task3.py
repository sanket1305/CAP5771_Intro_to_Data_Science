import joblib
import json
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_and_index_documents():

    # Open and load the JSON file
    with open("data/qa_data.json", "r") as file:
        data = json.load(file)

    # Access data
    print(len(data))
    vectorizer = TfidfVectorizer(max_features = 1000)

    tfidf_matrix = vectorizer.fit_transform(data)
    vectors = tfidf_matrix.toarray()

    joblib.dump(vectorizer, "output/vectorizer.pkl")
    np.save("output/document_vectors.npy", vectors)

def run_query(query: str, k: int = 5):
    vectorizer = joblib.load("output/vectorizer.pkl")
    vectors = np.load("output/document_vectors.npy")

    query_vector = vectorizer.transform([query])

    cosine_scores = cosine_similarity(query_vector, vectors)[0]
    # print(len(cosine_scores))
    # print(len(cosine_scores[0]))

    # get top k indices
    cosine_scores = cosine_scores.argsort()
    cosine_scores = cosine_scores[::-1] # reverse the array as we want top score first DESC order
    top_k_indices = cosine_scores[:k]
    # print(top_k_indices)

    top_k_scores = cosine_scores[top_k_indices]
    print(top_k_scores)

    # Open and load the JSON file
    with open("data/qa_data.json", "r") as file:
        data = json.load(file)
    
    print(f"Top {k} results for: {query}")
    for idx in top_k_indices:
        print(f"doc_{idx} {data[idx]}")

build_and_index_documents()
run_query("why")