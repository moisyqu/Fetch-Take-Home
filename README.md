# Semantic Search Project in Python

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project aims to implement a search engine that can retrieve relevant documents based on the semantic meaning of the user's query for Fetch Data Science Take-Home challenge.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

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

## Usage

The project provides two APIs for semantic search and Web app.



To perform a semantic search from the first, you need to follow these steps:

1. Prepare a collection of documents or articles in a format supported by the search engine (e.g., JSON, CSV).

2. Preprocess the documents (e.g., tokenize, remove stopwords) if required.

3. Create a search index using the provided indexing tools.

4. Query the search index with your user's search input to retrieve relevant documents.

## Examples

Here's a simple example of how to use the semantic search engine:

```python
from semantic_search import SemanticSearch

# Assuming you have a list of documents 'documents' and a user query 'user_query'
documents = [...]  # List of dictionaries containing 'id' and 'content' fields
user_query = "How does photosynthesis work?"

# Create a SemanticSearch instance
search_engine = SemanticSearch(documents)

# Index the documents
search_engine.index_documents()

# Perform the semantic search
results = search_engine.search(user_query)

# Print the search results
for result in results:
    print(result['id'], result['score'])
```

For more detailed examples and use cases, check the [examples](/examples) directory.

## Contributing

We welcome contributions to the Semantic Search Project! If you'd like to add new features, improve existing ones, or fix bugs, please follow the guidelines outlined in [CONTRIBUTING.md](/CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

---

Thank you for your interest in the Semantic Search Project in Python! If you have any questions or suggestions, feel free to create an issue or contact us.

Happy searching!
