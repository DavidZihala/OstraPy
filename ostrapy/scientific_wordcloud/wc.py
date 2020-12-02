"""
usage:
python wc.py output_name Your Name
"""



#!/usr/bin/python
import sys
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import os
import numpy as np
from Bio import Entrez, Medline

name = ' '.join(sys.argv[2:])
print(name)
outfile = sys.argv[1]


text = ""

MAX_COUNT = 100
TERM = name

Entrez.email = 'zihaladavid@gmail.com'  # put your mail here
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(h)
ids = result['IdList']
h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
records = Medline.parse(h)

for paper in records:
    try:
        if paper['AB']:
            text = text + ' ' + paper['AB']
    except:
        pass


def create_wordcloud(text):
    mask = np.array(Image.open('cloud.png'))
    stopwords = set(STOPWORDS)
    stopwords.add('one')
    stopwords.add('two')
    stopwords.add('three')

    wc = WordCloud(background_color="white", mask=mask,
                   max_words=100, stopwords=stopwords)

    wc.generate(text)

    wc.to_file(outfile)


create_wordcloud(text)
