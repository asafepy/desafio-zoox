import requests

from bs4 import BeautifulSoup


class Parser(object):

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        html = self.session.get(url)
        self.content_page = BeautifulSoup(html.content, "html.parser")

    def get_title(self):
        title = self.content_page.find_all("h1", class_="entry-title")
        return title[0].string
        

    def get_description(self):

        description = self.content_page.find_all("div", class_="entry-content")
        
        text_description = ''

        for x in description:
            text_description = text_description + x.find_all('p')[0].text

        return text_description






        