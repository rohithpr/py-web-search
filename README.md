# py-web-search

A Python module to fetch and parse results from different search engines.

### Table of Contents

* [Usage](#usage)
* [Features](#features)

## Usage

```python
    from google.search import Google
    print (Google.search('hello world', 5, 2))
```
Returns 5 results from the the third result onwards (ignores the first two).

## Features


### Currently implemented

* Google search (text)

### Todo

* Other search engines
* Images etc.