#Corpora
import nltk

print(nltk.__file__) #to get the location where you have your nltk folder to check nltk data and see different corpora

from nltk.corpus import gutenberg 
from nltk.tokenize import sent_tokenize 

sample = gutenberg.raw("bible-kjv.txt")
tokenize = sent_tokenize(sample)
print(tokenize[10:25])
