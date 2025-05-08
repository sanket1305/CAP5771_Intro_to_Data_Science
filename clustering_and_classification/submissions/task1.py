# WRITE YOUR CODE HERE
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer

def process_and_save_bow():
    # ftech dataset from train and test subsets
    newsgroups_train = fetch_20newsgroups(subset='train', data_home="/tmp")
    newsgroups_test = fetch_20newsgroups(subset='test', data_home="/tmp")

    # the result contains 2 imp attributes... data and target
    # data contains the actual news article
    # label contains the category for the news article

    '''
    Here's a list of the 20 newsgroup categories (targets) in the dataset:

    1] alt.atheism
    2] comp.graphics
    3] comp.os.ms-windows.misc
    4] comp.sys.ibm.pc.hardware
    5] comp.sys.mac.hardware
    6] comp.windows.x
    7] misc.forsale
    8] rec.autos
    9] rec.motorcycles
    10] rec.sport.baseball
    11] rec.sport.hockey
    12] sci.crypt
    13] sci.electronics
    14] sci.med
    15] sci.space
    16] soc.religion.christian
    17] talk.politics.guns
    18] talk.politics.mideast
    19] talk.politics.misc
    20] talk.religion.misc
    '''

    print("Training set size:", len(newsgroups_train.data))
    print("Test set size:", len(newsgroups_test.data))

    # limiting features to 1000 due to compute constraints
    vectorizer = CountVectorizer(max_features=1000)
    X_train = vectorizer.fit_transform(newsgroups_train.data).toarray()
    print("BoW train shape: " + str(X_train.shape[0]) + " x " + str(X_train.shape[1]))
    np.save('data/bow_train.npy', X_train)

    # as we have already fit out train data, now we are just going to transform on our test data
    X_test = vectorizer.transform(newsgroups_test.data).toarray()
    print("BoW test shape: " + str(X_test.shape[0]) + " x " + str(X_test.shape[1]))
    np.save('data/bow_test.npy', X_test)

    print("Train labels shape: " + str(len(newsgroups_train.target)) + " x 1")
    np.save('data/train_labels.npy', newsgroups_train.target)
    print("Test labels shape: " + str(len(newsgroups_test.target)) + " x 1")
    np.save('data/test_labels.npy', newsgroups_test.target)
