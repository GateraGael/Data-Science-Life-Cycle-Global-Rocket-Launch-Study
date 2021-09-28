import requests
import pandas as pd
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, url, parser):
        self.website_url = requests.get(url).text
        self.parser = parser
        pass