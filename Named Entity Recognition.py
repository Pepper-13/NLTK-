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
            
            namedEnt = nltk.ne_chunk(tagged, binary = True) 
            #Giving binary option just classifies everything as named entity and doesn't classify to organisation, money and so on 
            namedEnt.draw()
            
            #Named Entity Types: - Organisation, Person, Location, Date, Time, Money, Percent, Facility, GPE
         
        
    except Exception as e :
        print(str(e))
        
        
content_process()
