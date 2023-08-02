#%%
import pandas as pd
from txtai.embeddings import Embeddings


#%%

data = pd.read_csv('data/offer_retailer.csv', encoding="latin-1")

offers = data['OFFER'].values

# %%
# %%

# Create embeddings index with content enabled. The default behavior is to only store indexed vectors.
embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})

# Create an index for the list of text
embeddings.index([(uid, text, None) for uid, text in enumerate(offers)])
# %%
print()
# %%

def search(query,n):
    searchs = embeddings.search(query, n)
    for elt in searchs:
        print(elt['text'],round(elt['score']*100,2),"%")
    
query= "shrimp from walmart"
search(query,4)
# %%