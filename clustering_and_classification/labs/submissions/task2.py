# WRITE YOUR CODE HERE
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer

def process_and_save_tfidf():
    tfidf_transformer = TfidfTransformer()

    # tfidf for train dataset
    X_train = np.load('data/bow_train.npy')
    x_train_tfidf = tfidf_transformer.fit_transform(X_train).toarray()
    np.save('data/tfidf_train.npy', x_train_tfidf)

    # tfidf for test dataset 
    X_test = np.load('data/bow_test.npy')
    x_test_tfidf = tfidf_transformer.transform(X_test).toarray()
    np.save('data/tfidf_test.npy', x_test_tfidf)

    # display dimension for each of them
    print("TF-IDF train shape: " + str(x_train_tfidf.shape[0]) + " x " + str(x_train_tfidf.shape[1]))
    print("TF-IDF test shape: " + str(x_test_tfidf.shape[0]) + " x " + str(x_test_tfidf.shape[1]))
