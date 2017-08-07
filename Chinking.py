#Chinking  - Getting something out which we don't need. Chink something from the Chunk 

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
            
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""   
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked) #output is complex, doesn't make sense to humans 
            
            #getting in proper format
            
            chunked.draw() #This gives a tree
            
           #Makes a lot of mistake with Names but overall very good  
         
        
    except Exception as e :
        print(str(e))
        
        
content_process()
