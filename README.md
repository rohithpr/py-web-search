# py-web-search

A Python module to fetch and parse results from different search engines.

### Table of Contents

* [Support](#search-engines-supported)
* [Installation](#installation)
* [Usage](#usage)
* [Todo](#todo)

## Search engines supported

* Google
* Bing

## Installation

Needs Python3.

## Usage

```python
    from google.search import Google
    print (Google.search('hello world', 5, 2))

    # from bing.search import Bing
    # print (Bing.search('hello world', 5, 2))
```
Prints 5 results from the the third result onwards (ignores the first 2) in the following format.

```
    {
        'url': '...',
        'num': 5,
        'start': 2,
        'search_engine': 'google',
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

## Todo

* Other search engines
* Images etc.