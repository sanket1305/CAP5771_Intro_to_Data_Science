# WRITE YOUR CODE HERE
import numpy as np

from joblib import dump
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# naive bayes for Bag of Words (BoW)
def train_and_save_nb_bow():
    # get features for train and test dataset
    X_train_bow = np.load('data/bow_train.npy')
    X_test_bow = np.load('data/bow_test.npy')

    # get labels for train and test dataset
    labels_train = np.load('data/train_labels.npy')
    labels_test = np.load('data/test_labels.npy')

    # prepare naive bayes model based on training features and labels
    clf_model = MultinomialNB()
    clf_model.fit(X_train_bow, labels_train)

    # check the accuracy for test dataset
    accuracy = clf_model.score(X_test_bow, labels_test)
    print("BoW Test Accuracy: " + str(round(100*accuracy, 1)) + "%")

    # save the model
    dump(clf_model, 'models/naive_bayes_bow.pkl')

# naive bayes for TF_IDF
def train_and_save_nb_tfidf():
    # get features for train and test dataset
    X_train_tfidf = np.load('data/tfidf_train.npy')
    X_test_tfidf = np.load('data/tfidf_test.npy')

    # get labels for train and test dataset
    labels_train = np.load('data/train_labels.npy')
    labels_test = np.load('data/test_labels.npy')

    # prepare naive bayes model based on training features and labels
    clf_model = MultinomialNB()
    clf_model.fit(X_train_tfidf, labels_train)

    # check the accuracy for test dataset
    accuracy = clf_model.score(X_test_tfidf, labels_test)
    print("TF-IDF Test Accuracy: " + str(round(100*accuracy, 1)) + "%")

    # save the model
    dump(clf_model, 'models/naive_bayes_tfidf.pkl')

train_and_save_nb_bow()
train_and_save_nb_tfidf()