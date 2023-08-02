#%%
import pandas as pd
from txtai.embeddings import Embeddings


#%%

def main():
    data = pd.read_csv('../data/offer_retailer.csv', encoding="latin-1")

    offers = data['OFFER'].values

    # Create embeddings index with content enabled. The default behavior is to only store indexed vectors.
    embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})

    # Create an index for the list of text
    embeddings.index([(uid, text, None) for uid, text in enumerate(offers)])
    
    embeddings.save("models/vol_index_")

# %%

if __name__ == '__main__':
    main()
