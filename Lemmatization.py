from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("dogs")) #pos is noun by default
print(lemmatizer.lemmatize("better", pos= "a"))
