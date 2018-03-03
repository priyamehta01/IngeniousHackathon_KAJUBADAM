# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:27:35 2018

@author: Admin
"""

import nltk
from nltk.tag import StanfordNERTagger


st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/usr/share/stanford-ner/stanford-ner.jar',
					   encoding='utf-8')
text = """Lincoln was smart. Bush was great. Martin Luther King and United States. Linclon was big. Nelson Mandela is from Africa"""

for sent in nltk.sent_tokenize(text):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
        if tag[1]=='PERSON': 
            print(tag)
