# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 21:15:49 2018

@author: VISHWA
"""

import requests
from google import search
from bs4 import BeautifulSoup

try:
    from google import search
except ImportError: 
    print("No module named 'google' found")

# to search
query = "Narendra Modi inshorts"


k=0
i=0
news = []
newsDictionary = {
        'success': True,
        #'category': category,
        'data': []
    }

def getNews(url, i):
    
   
    try:
        htmlBody = requests.get(url)
    except requests.exceptions.RequestException as e:
        newsDictionary['success'] = False
        newsDictionary['errorMessage'] = str(e.message)
        return newsDictionary

    soup = BeautifulSoup(htmlBody.text, 'lxml')
    newsCards = soup.find_all(class_='news-card')
    if not newsCards:
        newsDictionary['success'] = False
        #newsDictionary['errorMessage'] = 'Invalid Category'
        return newsDictionary

    for card in newsCards:
        try:
            title = card.find(class_='news-card-title').find('a').text
        except AttributeError:
            title = None

#        try:
#            imageUrl = card.find(
#                class_='news-card-image')['style'].split("'")[1]
#        except AttributeError:
#            imageUrl = None

        try:
            url = ('https://www.inshorts.com' + card.find(class_='news-card-title')
                   .find('a').get('href'))
        except AttributeError:
            url = None

        try:
            content = card.find(class_='news-card-content').find('div').text
        except AttributeError:
            content = None

        try:
            author = card.find(class_='author').text
        except AttributeError:
            author = None

        try:
            date = card.find(clas='date').text
        except AttributeError:
            date = None

        try:
            time = card.find(class_='time').text
        except AttributeError:
            time = None

        try:
            readMoreUrl = card.find(class_='read-more').find('a').get('href')
        except AttributeError:
            readMoreUrl = None

        newsObject = {
              i: title,
             'content': content,
             'date': date,
             'time': time
        }
        newsDictionary['data'].append(newsObject)
    
    #print(newsDictionary['data'])
        
    return newsDictionary

#newsss = getNews('Narendra Modi')
    
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        newsss = getNews(j, i)
        i=i+1
    
print(newsss['data'])

   # print(j)