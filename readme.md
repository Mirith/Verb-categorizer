**Last updated August 24, 2017** by [Mirith](https://github.com/Mirith)

# Overview

This project is a natural-language processing exercise done in Python (this is in Python 3)  to analyze the verbs of a document.  In this case, the corpus used is [CapitolWords from textacy](http://textacy.readthedocs.io/en/latest/api_reference.html#module-textacy.doc).  [spaCy](https://spacy.io/docs/api/) is used to process the corpus and examine/compare the tags of words.  Phrasal verbs are categorized as being prepositional or particle.  Verbs are also categorized based on transitivity.  Those two tasks are done in two separate files.  

# Usage

You will need [spaCy](https://spacy.io/docs/usage/) and python installed to run the program yourself.  As of right now, the programs run quite slowly.  Hopefully this will be remedied in further updates.  

# Files 

## phrasal verbs.py

Analyzes the CapitolWords corpus using tags from spaCy to determine whether phrasal verbs are particle or prepositional phrasal verbs.  Also prints out the results.  

## transitivity.py

Collects all the verbs from the CapitolWords corpus and determines their transitivity using spaCy's tags.  Also prints out verbs and how often they occur as each transitivity by percentage, ie VERB:  -- 100 occurences/Intransitive: 10% of the time/Transitive: 50% of the time/Ditransitive: 40% of the time.



