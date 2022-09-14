import re, string, pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def wordopt(news):
    news = news.lower()
    news = re.sub('\[.*?\]', '', news)
    news = re.sub("\\W"," ",news) 
    news = re.sub('https?://\S+|www\.\S+', '', news)
    news = re.sub('<.*?>+', '', news)
    news = re.sub('[%s]' % re.escape(string.punctuation), '', news)
    news = re.sub('\n', '', news)
    news = re.sub('\w*\d\w*', '', news)    
    return news

def process(news):
    news = [wordopt(news)]
    vectorization = pickle.load(open('models/vectorization.pkl', 'rb'))
    news = vectorization.transform(news)
    LR = pickle.load(open('models/logistic.pkl', 'rb'))
    DT = pickle.load(open('models/tree.pkl', 'rb'))
    GBC = pickle.load(open('models/gradient.pkl', 'rb'))
    RFC = pickle.load(open('models/forest.pkl', 'rb'))
    model_names = ['Logistic Regression', 'Decision Tree Classifier', 'Gradient Boost Classifier', 'Random Forest Classifier']
    models = [LR, DT, GBC, RFC]
    results = []
    for name, model in zip(model_names, models):
        result = {
            'name': name,
            'result': model.predict(news)[0]
        }
        results.append(result)
    
    return results