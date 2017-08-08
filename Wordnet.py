#Wordnet - biggest corpora in nltk; Can look up to words, synonyms, defination, content 

from nltk.corpus import wordnet
syn = wordnet.synsets("program")
print(syn)

print(syn[0].name()) # returns the synset
print(syn[0].lemmas()[0].name()) #just the name of the word
print(syn[0].definition())
print(syn[0].examples())

syns = []
ants = []

for syn in wordnet.synsets("program"):
    for l in syn.lemmas():
        syns.append(l.name())
        if l.antonyms():
            ants.append(l.antonyms()[0].name())
            
            
print(set(syns))
print(set(ants))

#Similarity Checks:

w1 = wordnet.synset("Ship.n.01")
w2 = wordnet.synset("Dog.n.01")
print(w1.wup_similarity(w2)) # gives a percentage of similarity 

# Can be used for checking cheating in exams
# Can be used to find out similar articles 
# Can be used for suggestion tools 

#Output :
[Synset('plan.n.01'), Synset('program.n.02'), Synset('broadcast.n.02'), Synset('platform.n.02'), Synset('program.n.05'), Synset('course_of_study.n.01'), Synset('program.n.07'), Synset('program.n.08'), Synset('program.v.01'), Synset('program.v.02')]
plan.n.01
plan
