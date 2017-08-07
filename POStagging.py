import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunkSentenceTokenizer

train_text = state_union.raw("a.txt")
sample_text = state_union.raw("b.txt") 

custom_sent_tokeniser = PunkSentenceTokenizer(train_text)
tokenized = custom_sent_tokeniser(sample_text)

def content_process():
    try:
        for i in tokenised:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            print(tagged)
        
    except Exception as e :
        print(str(e))
        
        
content_process()

#tuples of words and POS is formed
#POS tagging table needs to be seen to understand acronyms
