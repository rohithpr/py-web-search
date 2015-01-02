# py-web-search

[![Latest Version](https://pypip.in/version/py-web-search/badge.svg)](https://pypi.python.org/pypi/py-web-search/)

A Python module to fetch and parse results from different search engines.

### Table of Contents

* [Support](#search-engines-supported)
* [Installation](#installation)
* [Usage](#usage)
* [Todo](#todo)

## Search engines supported

* Google: [web](#web-search)
* Bing: [news](#news-search), [web](#web-search)

## Installation

Current release: 0.1.1.3

Needs Python3.
Install using pip:
```
    pip install py-web-search
```

## Usage

#### Web search
```python
    from pws.google import Google
    from pws.bing import Bing

    print(Google.search('hello world', 5, 2))
    print(Bing.search('hello world', 5, 2))
    
    # Arguments:
    # search(query, num, start, sleep, recent)
    # query: Required. The keyword that will be searched.
    # num: Default 10. The number of results returned.
    # start: Default 0. The number of top results that are to be ignored.
    # sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
    # recent: Default True. If True that most recent results are obtained else top results are obtained. (Buggy)
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

#### News search
```python
    from pws.bing import Bing

    print(Bing.search_news('github', 10, 0, True, True))
    
    # Arguments:
    # search(query, num, start, sleep, recent)
    # query: Required. The keyword that will be searched.
    # num: Default 10. The number of results returned.
    # start: Default 0. The number of top results that are to be ignored.
    # sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
    # recent: Default True. If True that most recent results are obtained else top results are obtained. (Buggy)
```
Prints 10 results from the the first result onwards (ignores the first 0) in the following format.

```
    {
        'url': '...',
        'num': 10,
        'start': 0,
        'search_engine': 'bing',
        'results':
        [
            {
                'link': '...',
                'link_text': '...',
                'link_info': '...',
                'source': '...',
                'time': '...',
                'additional_links':{}, # Always empty.
            },
            ...
        ]
    }
```

## Todo

* Other search engines
* Images etc.