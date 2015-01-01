from bs4 import BeautifulSoup
import re
import requests
from html.parser import HTMLParser
from time import sleep

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

# http://www.bing.com/search?q=hello+world&first=9
def generate_url(query, first):
    """(str, str) -> str
    A url in the required format is generated.
    """
    query = '+'.join(query.split())
    url = 'http://www.bing.com/search?q=' + query + '&first=' + first
    print (url)
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


class Bing:
    @staticmethod
    def search(query, num=10, start=0):
        results = []
        while len(results) < num:
            # sleep(1)
            url = generate_url(query, str(start))
            soup = BeautifulSoup(requests.get(url).text)
            new_results = Bing.scrape_search_result(soup)
            results += new_results
            start += len(new_results)
        results = results[:num]

        temp = {'results' : results,
                'url' : url,
                'num' : num,
                'start' : start,
                'search_engine' : 'bing',
        }
        return temp

    @staticmethod
    def scrape_search_result(soup):
        number_of_results = try_cast_int(soup.find('span', attrs = {'class' : 'sb_count'}).string)
        raw_results = soup.find_all('li', attrs = {'class' : 'b_algo'})
        results = []

        for result in raw_results:
            link = result.find('a').get('href')

            raw_link_text = result.find('a')
            link_text = strip_tags(str(raw_link_text))

            additional_links = dict()

            raw_link_info = result.find('div', attrs = {'class' : 'b_caption'})
            description = raw_link_info.find('div', attrs = {'class' : 'b_snippet'})
            if description is None:
                link_info = strip_tags(str(raw_link_info.find('p')))
            else:
                link_info = strip_tags(str(description))
                for a_link in raw_link_info.find_all('a'):
                    additional_links[strip_tags(str(a_link))] = a_link.get('href')

            temp = { 'link' : link,
                     'link_text' : link_text,
                     'link_info' : link_info,
                     'additional_links' : additional_links,
            }
            results.append(temp)

        return results