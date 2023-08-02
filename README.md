# Semantic Search Project in Python

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project aims to implement a search engine that can retrieve relevant documents based of the user's query for Fetch Data Science Take-Home challenge.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Demo](#demo)
  
## Overview

Semantic search is an advanced search technique. It focuses on understanding the intent of the search query and retrieving documents that are contextually relevant. This project will implement two solutions building a  search engine along with a web app for a visualization.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/moisyqu/Fetch-Take-Home.git
cd Fetch-Take-Home
```

2. Set up a virtual environment (recommended):

```bash
python3 -m venv venv
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
The querry is vectorized and compared to the database to find similarties.

Run the script and input your querry
```bash
python implementationGlove.py
```

### Second implementation txtAI

This implemenation used the txtAI API

Run the script and input your querry
```bash
python implementationTXTAI.py
```

### Web app

The web application will use txtAI implementation

1. Run the pre run to setup the model
   
```bash
python prerun.py
```

2. Run the server

```bash
python manage.py runserver
```

3. Go to localhost and try a querry

---

Thank you for your interest in my response from Fetch Data Science Take-Home challenge. If you have any questions, feel free to contact me at quentin.moisy@gmail.com.
