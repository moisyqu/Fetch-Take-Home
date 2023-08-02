# Semantic Search Project in Python

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project aims to implement a search engine that can retrieve relevant documents based of the user's query for Fetch Data Science Take-Home challenge.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Demo](#demo)
- [Next steps](#next_steps)
  
## Overview

Semantic search is an advanced search technique. It focuses on understanding the intent of the search query and retrieving documents that are contextually relevant. This project will implement two solutions building a  search engine along with a web app for a visualization. Documents (offers) will be taken from offer_retailer.csv. 

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/moisyqu/Fetch-Take-Home.git
cd Fetch-Take-Home
```

2. Set up a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Demo

The project provides two APIs for semantic search and a Web app.

### First implementation GLOVE

This implemenation is based on World2Vec using GLOVE.
Each offers from offer_retailer.csv are vectorized and projected onto a 2-dimensional plan. These vectors are trained by ensuring words with similar meanings are physically near each other. The closer the distance is the more similar are the words. Be calculating the distance between two points we can see how similar are the words.
In this case, the user query will be vectorized as well and the distance to each vectorized offers we be calculating. The offers with the smaller distances will be shown.  

1. First download the glove.txt from the drive I shared.

2. Run the script and input your query:
   
```bash
python implementationGlove.py
```

Example: Result for the query = "Shrimp at Walmart":
```bash
Gorton's Air Fried Butterfly Shrimp, at Walmart   66.34 %
Tyson Products, select varieties, spend $15 at Walmart   61.9 %
Butterball, select varieties, spend $10 at Dillons Food Store   61.48 %
Butterball, select varieties, spend $10 at Kroger   59.25 %
```

### Second implementation txtAI

This implemenation used the txtAI API open source. This API use word embedding.

1. Run the script and input your query:
```bash
python implementationTXTAI.py
```

Example: Result for the query = "Shrimp at Walmart":
```bash
Gorton's Air Fried Butterfly Shrimp, at Walmart 80.97 %
AleveXâ¢ at Walmart 74.64 %
Michael Angelo'sÂ® Sauce at Walmart 72.81 %
Arber, at Walmart 70.26 %
```

### Web app

The web application will use txtAI implementation.

1. Run the pre run to setup the model:
   
```bash
python prerun.py
```

2. Run the server:

```bash
python manage.py runserver
```

3. Go to localhost and try a query.
   
## Next steps
   
   1. Only the offers description are used to provide the result, by knowing the company, the tool can do recommendation to similar product.
   2. The glove dictionnary used is a global one, to have better result it's better to create your own vocabulary.
   3. There is not correction on the user query which can drastically reduce the perfomance.

  
---

Thank you for your interest in my response from Fetch Data Science Take-Home challenge. If you have any questions, feel free to contact me at quentin.moisy@gmail.com.
