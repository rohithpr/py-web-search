# py-web-search

A Python module to fetch and parse results from different search engines.

### Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)

## Installation

Needs Python3.

## Usage

```python
    from google.search import Google
    print (Google.search('hello world', 5, 2))
```
Returns 5 results from the the third result onwards (ignores the first two) in the following format.

```
    {
        'url': '...',
        'num': 5
        'start': 2,
        'results':
        [
            {
                'link': '...',
                'link_text': '...',
                'link_info': '...',
                'additional_links':
                {
                    linktext: link,
                    ...
                }
        	},
        	...
        ]
    }
```

## Features


### Currently implemented

* Google search (text)

### Todo

* Other search engines
* Images etc.