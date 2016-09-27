#coding=utf-8

from bs4 import BeautifulSoup
from time import sleep as wait
import re
import requests

try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser

##################################################
# Copied code
##################################################

class MLStripper(HTMLParser):
    # Code copied from StackOverflow http://stackoverflow.com/a/925630/3664835
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    # Code copied from StackOverflow http://stackoverflow.com/a/925630/3664835
    s = MLStripper()
    s.feed(html)
    return ' '.join(s.get_data().split())

##################################################
# Helpers
##################################################

# https://www.google.com/search?q=hello+world&num=3&start=0
def generate_url(query, num, start, recent, country_code):
    """(str, str, str) -> str
    A url in the required format is generated.
    """
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query + '&num=' + num + '&start=' + start
    if recent in ['h', 'd', 'w', 'm', 'y']:
        url += '&tbs=qdr:' + recent
    if country_code is not None:
        url += '&gl=' + country_code
    return url

# Sortbydate: tbs=sbd:1
# Best:      https://www.google.co.in/search?q=hello+world&tbm=nws#q=hello+world&tbas=0&tbm=nws
# 1 hour:    &tbs=qdr:h
# 1 day:     &tbs=qdr:d
# 1 week:    &tbs=qdr:w
# 1 month:   &tbs=qdr:m
# 1 year:    &tbs=qdr:y
def generate_news_url(query, num, start, recent, country_code):
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query + '&num=' + num + '&start=' + start
    url += '&tbm=nws#q=' + query + '&tbas=0&tbs=sbd:1&tbm=nws'
    if recent in ['h', 'd', 'w', 'm', 'y']:
        url += '&tbs=qdr:' + recent
    if country_code is not None:
        url += '&gl=' + country_code
    return url

def try_cast_int(s):
    """(str) -> int
    All the digits in a given string are concatenated and converted into a single number.
    """
    try:
        temp = re.findall('\d', str(s))
        temp = ''.join(temp)
        return int(temp)
    except:
        return s

##################################################
# Class
##################################################


class Google:
    @staticmethod
    def search(query, num=10, start=0, sleep=True, recent=None, country_code=None):
        if sleep:
            wait(1)
        url = generate_url(query, str(num), str(start), recent, country_code)
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        results = Google.scrape_search_result(soup)
        related_queries = Google.scrape_related(soup)

        raw_total_results = soup.find('div', attrs = {'class' : 'sd'}).string
        total_results = 0
        if raw_total_results is not None:
            for i in raw_total_results:
                try:
                    temp = int(i)
                    total_results = total_results * 10 + temp
                except:
                    continue

        temp = {'results' : results,
                'url' : url,
                'expected_num' : num,
                'received_num' : len(results),
                'start' : start,
                'search_engine': 'google',
                'related_queries' : related_queries,
                'total_results' : total_results,
                'country_code': country_code,
        }
        return temp

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all('div', attrs = {'class' : 'g'})
        results = []
        
        for result in raw_results:
            link = result.find('a').get('href')[7:]

            raw_link_text = result.find('a')
            link_text = strip_tags(str(raw_link_text))
            
            raw_link_info = result.find('span', attrs = {'class' : 'st'})
            link_info = strip_tags(str(raw_link_info))

            additional_links = dict()
            raw_additional_links = result.find('div', attrs = {'class' : 'osl'})
            if raw_additional_links is not None:
                for temp in raw_additional_links.find_all('a'):
                    additional_links[strip_tags(str(temp))] = temp.get('href')[7:]

            temp = { 'link' : link,
                     'link_text' : link_text,
                     'link_info' : link_info,
                     'additional_links' : additional_links,
            }

            results.append(temp)
        return results

    @staticmethod
    def scrape_related(soup):
        related_queries = []
        raw_related = soup.find_all('p', attrs = {'class' : '_Bmc'})
        for related in raw_related:
            related_queries.append(strip_tags(str(related.find('a'))))
        return related_queries

    @staticmethod
    def search_news(query, num=10, start=0,sleep=True, recent=None, country_code=None, proxies=None):
        if sleep:
            wait(1)
        url = generate_news_url(query, str(num), str(start), recent, country_code)
        soup = BeautifulSoup(requests.get(url,proxies).text, "html.parser")
        results = Google.scrape_news_result(soup)

        raw_total_results = soup.find('div', attrs = {'class' : 'sd'}).string
        total_results = 0
        for i in raw_total_results:
            try:
                temp = int(i)
                total_results = total_results * 10 + temp
            except:
                continue

        temp = {'results' : results,
                'url' : url,
                'num' : num,
                'start' : start,
                'search_engine' : 'google',
                'total_results' : total_results,
                'country_code': country_code,
        }
        return temp

    @staticmethod
    def scrape_news_result(soup):
        raw_results = soup.find_all('div', attrs = {'class' : 'g'})
        results = []

        for result in raw_results:
            link = result.find('a').get('href')[7:]

            raw_link_text = result.find('a')
            link_text = strip_tags(str(raw_link_text))

            raw_link_info = result.find('div', attrs = {'class' : 'st'})
            link_info = strip_tags(str(raw_link_info))

            raw_source = result.find('span', attrs = {'class' : 'f'})
            raw_source = strip_tags(str(raw_source)).split(' - ')

            source = raw_source[0]
            time = raw_source[1]

            additional_links = dict()

            # Crazy hack! Fix it. + Buggy!
            try:
                raw_a_links = result.find_all('a')[1:]
                if raw_a_links:
                    raw_source = list(map(strip_tags, list(map(str, result.find_all('span', attrs = {'class' : 'f'})[1:]))))
                    for idx in range(len(raw_a_links)-1):
                        additional_links[strip_tags(str(raw_a_links[idx]))] = (raw_a_links[idx].get('href'), raw_source[idx])
            except:
                pass

            temp = { 'link' : link,
                     'link_text' : link_text,
                     'link_info' : link_info,
                     'additional_links' : additional_links,
                     'source' : source,
                     'time' : time,
            }
            results.append(temp)
        return results
