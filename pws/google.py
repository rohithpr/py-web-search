from bs4 import BeautifulSoup
import re
import requests
from html.parser import HTMLParser

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
def generate_url(query, num, start):
    """(str, str, str) -> str
    A url in the required format is generated.
    """
    query = '+'.join(query.split())
    url = 'https://www.google.com/search?q=' + query + '&num=' + num + '&start=' + start
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
    def search(query, num=10, start=0):
        url = generate_url(query, str(num), str(start))
        soup = BeautifulSoup(requests.get(url).text)
        # print(soup.prettify())
        results = Google.scrape_search_result(soup)

        temp = {'results' : results,
                'url' : url,
                'num' : num,
                'start' : start,
                'search_engine': 'google',
        }
        return temp

    @staticmethod
    def scrape_search_result(soup):
        number_of_results = try_cast_int(soup.find('div', attrs = {'id' : 'resultStats'}).string)
        raw_results = soup.find_all('li', attrs = {'class' : 'g'})
        results = []
        
        for result in raw_results:
            link = result.find('a').get('href')[7:]

            raw_link_text = result.find('a')
            link_text = strip_tags(str(raw_link_text))
            
            raw_link_info = result.find('span', attrs = {'class' : 'st'})
            # print(raw_link_info, '\n\n\n')
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