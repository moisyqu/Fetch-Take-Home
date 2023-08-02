#%%
from scipy import spatial
import pandas as pd
import numpy as np
import os

import re
from nltk.corpus import stopwords

#%%
word2vec = {}
with open (os.path.join("glove.42B.300d/glove.42B.%sd.txt" % 300), encoding="utf8")as f:
    for line in f:
        values=line.split()
        word=values[0]
        vec = np.asarray(values[1:], dtype="float32")
        word2vec[word] =vec   
#%%

data = pd.read_csv('data/offer_retailer.csv', encoding="latin-1")
offers = data['OFFER'].values

#%%

REPLACE_BY_SPACE_RE = re.compile('[(){}\[\]\|$@,;.%:-]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
        text: a string
        
        return: modified string
    """
    text = str(text).lower() # lowercase text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    text = REPLACE_BY_SPACE_RE.sub('', text) # replace bad characters
    return text.split()
#%%
def get_vector(s):
    clean_val =  clean_text(s)
    temp=[]
    for elt in clean_val:
        try:
            temp.append(word2vec[elt])
        except:
            temp.append(np.array([1 for i in range(300)]))
    return np.sum(np.array(temp), axis=0)

#%%
embedding = []
for offer in offers:
    embedding.append(get_vector(offer))
embedding = np.array(embedding)

#%%
np.save('embedding.npy',embedding)

#%%

emb = np.load('embedding.npy')

#query = "Shrimp at walmart"
query = input("Enter search querry:")

def search (query,n):
    result = {}
    for i in range(len(emb)):
        result[i]= round((1 - spatial.distance.cosine(get_vector(query),emb[i]))*100,2)
        
    sorted_result = sorted(result.items(),reverse=True, key=lambda x:x[1])[:n]
    
    for elt in sorted_result:
        print(offers[elt[0]]," ",elt[1],"%")


sorted_result = search(query,5)

# %%
