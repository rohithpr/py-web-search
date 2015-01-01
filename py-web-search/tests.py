from bs4 import BeautifulSoup
from bing import Bing
import unittest

EXPECTED_RESULT_1 = [{'link': 'http://en.wikipedia.org/wiki/Hello_world_program', 'link_info': 'A " Hello, world !" program is a computer program that outputs " Hello, World !" (or some variant thereof) on a display device. Because it is typically one of the ...', 'link_text': '" Hello, world !" program - Wikipedia, the free encyclopedia', 'additional_links': {'History': 'http://en.wikipedia.org/wiki/Hello_world_program#History', 'Variations': 'http://en.wikipedia.org/wiki/Hello_world_program#Variations', 'Purpose': 'http://en.wikipedia.org/wiki/Hello_world_program#Purpose'}}, 
                     {'link': 'https://www.hello-world.com/', 'link_info': 'Main index for hello-world : links to login and all of the languages', 'link_text': 'Total immersion, Serious fun! with Hello-World !', 'additional_links': {}}, 
                     {'link': 'http://www.helloworld.com/', 'link_info': 'Wayman joins senior leadership team. Meet Chris, Chief Client Officer, and learn about this new role at HelloWorld .', 'link_text': 'HelloWorld Inc - Official Site', 'additional_links': {}}, 
                     {'link': 'http://www.helloworldchennai.com/', 'link_info': 'A leading chain of mobile stores in Chennai , Hello World , founded in 1999, caters to all cellular needs of todays informed buyer.', 'link_text': 'Hello World', 'additional_links': {}}, 
                     {'link': 'http://en.wikipedia.org/wiki/List_of_Hello_world_program_examples', 'link_info': 'The Hello world program is a simple computer program that prints (or displays) the string " Hello, world !" or some variant thereof. It is typically one of ...', 'link_text': 'List of Hello world program examples - Wikipedia, the free ...', 'additional_links': {}}, 
                     {'link': 'http://www.youtube.com/watch?v=al2DFQEZl4M', 'link_info': '05-11-2010 · Music video by Lady Antebellum performing Hello World on You Tube.', 'link_text': 'Lady Antebellum - Hello World - YouTube', 'additional_links': {}}, 
                     {'link': 'http://www.gnu.org/fun/jokes/helloworld.html', 'link_info': 'Hello World ! How the way people code “ Hello World ” varies depending on their age and job: High School/Jr. High 10 PRINT " HELLO WORLD " 20 END', 'link_text': 'Hello World ! - GNU Project - Free Software Foundation (FSF)', 'additional_links': {}}, 
                     {'link': 'http://msdn.microsoft.com/en-us/library/ms765388(v=vs.85).aspx', 'link_info': 'The following example shows a simple but complete XML document transformed by an XSLT style sheet. The source XML document, hello .xml, contains a " Hello, World !"', 'link_text': 'Hello, World ! (XSLT)', 'additional_links': {}}, 
                     {'link': 'http://asp.net-tutorials.com/basics/hello-world/', 'link_info': 'In almost every programming tutorial you will find the classic " Hello, world !" example, and who am I to break such a fine tradition? Let me show you how you can say ...', 'link_text': 'Hello, world ! - The complete ASP.NET Tutorial', 'additional_links': {}}, 
                     {'link': 'http://www.helloworldchennai.com/branches.asp', 'link_info': 'HELLO WORLD . Basement Shop #2, Gokul Arcade, #2, Sardar Patel Road, Adyar, Chennai - 20 Ph: 044 - 24425573 / 42115215', 'link_text': 'Hello World', 'additional_links': {}}]

class BingTest(unittest.TestCase):

    def test_scrape_search_result(self):
        with open('ipbing') as fp:
            test_result_1 = Bing.scrape_search_result(BeautifulSoup(fp))
            self.assertEqual(EXPECTED_RESULT_1, test_result_1)

if __name__ == '__main__':
    unittest.main()