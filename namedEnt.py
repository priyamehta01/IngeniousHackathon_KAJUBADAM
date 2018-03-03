# -*- coding: utf-8 -*-
"""
One of the most major forms of chunking in natural language processing is called 
"Named Entity Recognition." The idea is to have the machine immediately be able to pull 
out "entities" like people, places, things, locations, monetary figures, and more.
"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")

sample_text = "Lincoln was smart. Bush was great. Martin Luther King and United States. Linclon was big. Nelson Mandela is from Africa"

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            namedEnt = nltk.ne_chunk(tagged)
                                    
            print(namedEnt[0][0])
            
        
    except Exception as e:
        print(str(e))
        
        
    
    
process_content()