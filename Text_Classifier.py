#Text Classifiers 

#To figure out whether a spam or legitimate kind of email or not , opinion mining, positive or negative 
#Mostly with the two categories - spam or not spam 

import nltk
import random
from nltk.corpus import movie_reviews

#documents  = []
'''for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)),category)'''
        #appends takes exactly one argument so we will write it as one liner 
        
        
documents = [(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
#print(documents[1]) #shows all the words in the movie review of the 1st Indexed document

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
    
#Frequency Distribution of all words

all_words = nltk.FreqDist(all_words)
print(all_words.append.most_common(15)) # Mostly considers stopwords, which can be removed and used again 
print(all_words["happy"]) #Will provide the frequency of "happy" across the entire universe of words

#We can use Naive Bayes and classify as categories of positive and negative words 
