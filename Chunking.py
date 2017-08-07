#Chunking:
#Group together words thats infering some meaning 
#Familiarity with Regular expressions are required


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
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""  #<NNP>+ gives 1 or more NNPs in one chunk 
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked) #output is complex, doesn't make sense to humans 
            
            #getting in proper format
            
            chunked.draw() #This gives a tree
            
            
         
        
    except Exception as e :
        print(str(e))
        
        
content_process()
