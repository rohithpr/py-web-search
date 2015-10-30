# py-web-search

[![Latest Version](https://badge.fury.io/py/py-web-search.svg)](http://badge.fury.io/py/py-web-search)[![Join the chat at https://gitter.im/rohithpr/py-web-search](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/rohithpr/py-web-search?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A Python module to fetch and parse results from different search engines.

#### Warning: Do not make queries rapidly! The servers may block you.

### Related project
Use the [search-api](https://github.com/rohithpr/search-api) to get results in JSON format using http requests. (Does not need python)

### Table of Contents

* [Support](#search-engines-supported)
* [Installation](#installation)
* [Usage](#usage)
* [Todo](#todo)
* [Contribution](#contribution)

## Search engines supported

* Google: [news](#news-search), [web](#web-search)
* Bing: [news](#news-search), [web](#web-search)

## Installation

Python3:
Install using pip:
```
    pip install py-web-search
```

Python2: Not available on PyPI at the moment. You can download this repository and set it up manually.

## Usage

#### Web search
```python
    from pws import Google
    from pws import Bing

    print(Google.search('hello world', 5, 2))
    print(Bing.search('hello world', 5, 2))
    
    # Arguments:
    # search(query, num, start, sleep, recent)
    # query: Required. The keyword that will be searched.
    # num: Default 10. The number of results returned.
    # start: Default 0. The number of top results that are to be ignored.
    # sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
    # recent: Default None. The following values are allowed: 'h': hour, 'd': day, 'w': week, 'm': month and 'y': year.(Buggy)
```
Prints 5 results from the the third result onwards (ignores the first 2) in the following format.

```
    {
        'url': '...',
        'expected_num': 5,
        'received_num' : 5, # There will be a difference in case of insufficient results
        'start': 2,
        'search_engine': 'google',
        'total_results': ...,
        'results':
        [
            {
                'link': '...',
                'link_text': '...',
                'link_info': '...',
                'related_queries': [...],
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
    from pws import Bing
    from pws import Google

    print(Bing.search_news('github', 10, 0, True, 'h'))
    print(Google.search_news('github', 10, 0, True, 'd'))
    
    # Arguments:
    # search_news(query, num, start, sleep, recent)
    # query: Required. The keyword that will be searched.
    # num: Default 10. The number of results returned.
    # start: Default 0. The number of top results that are to be ignored.
    # sleep: Default True. If True, the program will wait for a second, when applicable, to avoid overwhelming the servers.
    # recent: Default None. The following values are allowed: 'h': hour, 'd': day, 'w': week, 'm': month and 'y': year.(Buggy)
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
                'additional_links':{}, # Always empty for Bing.
            },
            ...
        ]
    }
```

## Todo

* Other search engines
* Images etc.

## Contribution
Feel free to add any features that you think might be useful.