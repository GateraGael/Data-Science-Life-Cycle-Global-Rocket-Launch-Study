from scraper import Scraper
import pandas as pd
from bs4 import BeautifulSoup


class WikiTablesSraper(Scraper):

    def __init__(self, url, parser, table=False):
        Scraper.__init__(self, url, parser)

        self.html_class = 'wikitable'
        self.soup_obj = BeautifulSoup(self.website_url, self.parser)

        if table:
            self.Table = str(table)

        self.all_html_tables = self.soup_obj.find(self.Table, {"class":self.html_class})
        self.table_count = len(self.all_html_tables)
    
    def html_table_pd_dataframe(self, wiki_table_obj, table_index):
        df = pd.read_html(str(wiki_table_obj))
        print(df[table_index])


test_url = "https://en.wikipedia.org/wiki/Broglio_Space_Center"
scrape_object = WikiTablesSraper(test_url, "lxml", 'table')
WikiTablesSraper.html_table_pd_dataframe(scrape_object, WikiTablesSraper(test_url, "lxml", 'table').all_html_tables, 0)

