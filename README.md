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
    from pws.google import Google
    from pws.bing import Bing

    print(Google.search('hello world', 1))
    print(Bing.search('hello world', 1))
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