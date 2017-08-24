# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:25:12 2017

@author: Mirith

Info: finding whether verbs are phrasal or prepositional

"""

# for nlp and dataset
import spacy
import textacy

cw = textacy.corpora.CapitolWords()
nlp = spacy.load('en')

# list of unique phrasal verbs
uniqueVerbs = set([])
# sets for particle or prepositional verbs
particleVerbs = set([])
prepositionalVerbs = set([])

# goes through records 
# will take about 30-40 minutes to complete bc nested for loops... 
for record in cw.records():
    
    # gets text of record
    text = record["text"]
    # processes the text of the record
    processed = nlp(text)
    
    # goes through processed text's tokens
    for token in processed:
        # adds to dictionary if phrasal verb as marked by dependency relationship
        if ((token.dep_ == "prep") or (token.dep_ == "prt")) and (token.head.pos_ == "VERB"):
            # adds tokens to dictionary verb:particle
            phrasal = token.head.lemma_ + " " + token.lemma_
            # adds the verbs as lemmas to a set for unique phrasal verbs
            uniqueVerbs |= set([phrasal])
            
            # adds to different sets based on adjacencies
            # as lemmas
            # if adjacent, to prepositionalVerbs
            # if not adjacent, to particleVerbs
            if ((token.i + 1 == token.head.i) or (token.i - 1 == token.head.i)):
                 prep = token.head.lemma_ + " " + token.lemma_
                 # adds the verbs as lemmas to a set for prepositional phrasal verbs
                 prepositionalVerbs |= set([prep])
            else:
                 part = token.head.lemma_ + " " + token.lemma_
                 # adds the verbs as lemmas to a set for particle phrasal verbs
                 particleVerbs |= set([part])
                 
for thing in particleVerbs:
    print(thing)
for thing in prepositionalVerbs:
    print(thing)