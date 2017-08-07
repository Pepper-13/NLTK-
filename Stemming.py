from nltk.stem import PorterStemmer
ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))
    
example_text = "It is important to be pythonly when you are pythoning with python"

words = word_tokenize(example_text)

for w in words:
    print (ps.stem(w))
