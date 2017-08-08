#Naive Bayes 

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:4000]

def find_features(document):
    words = set(doucument)
    features ={}
    for w in word_features:
        feautures[w] = (w in words)
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

training_set = featuresets[:2900]
testing_set = featuresets[2900:]

#posterior  = prior occurences * liklihood /evidence 
 
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("NB accuracy %:" , (nltk.classify.accuracy(classifier, testing_test))*100 )
classifier.show_most_informative_features(20)