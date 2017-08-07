from nltk.corpus import stopwords
example_sentence = "This is an example  showing off some stop words filteration"

#what are the stop words defined in nltk stopwords?
print(stop_words)

#what can we do with it?

words = word_tokenize(example_sentence)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print(filtered_sentence)

#putting the above work in one line :

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
