from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def train_spam_model():
    container_path = "data/spam_emails"
    data = load_files(container_path)

    # split the data and target variables
    X_train, y_train = data.data, data.target
    
    # cretae a pipeline for logistic regression, 
    # add labels for process for quick access later on
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase = True,
            stop_words = "english",
            max_features = 1000
        )),
        ("clf", LogisticRegression(class_weight = "balanced", max_iter = 1000))
    ])

    # train the model
    pipeline.fit(X_train, y_train)
    return pipeline

train_spam_model()