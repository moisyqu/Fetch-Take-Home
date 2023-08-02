# Import necessary modules
from django.shortcuts import render
from django.db.models import Q
from txtai.embeddings import Embeddings


def default(request):
    return render(request, 'default.html')

def searchQuerry(query,n,embeddings):
    searchs = embeddings.search(query, n)
    tp = []
    for elt in searchs:
        tp.append(elt['text']+" "+str(round(elt['score']*100,2))+"%")
    return tp

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
            results = []
        else:   
            embeddings = Embeddings()
            embeddings.load("models/vol_index_")
            results =searchQuerry(query,4,embeddings)
            
    return render(request, 'search.html', {'query': query, 'results': results})