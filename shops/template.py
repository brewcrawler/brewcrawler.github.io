import requests
from bs4 import BeautifulSoup


MALT_URL = [""]
HOP_URL = [""]
YEAST_URL = [""]
SHOP = ""

page = None
soup = None

malt_list = []
hop_list = []
yeast_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}


def process_malts(soup):
    #TODO
    pass

def process_hops(soup):
    #TODO
    pass

def process_yeasts(soup):
    #TODO
    pass

def crawl_malts():
    for malt_page in MALT_URL:
        page = requests.get(malt_page, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #TODO
        process_malts(soup)
    return malt_list

def crawl_hops():
    for hop_page in HOP_URL:
        page = requests.get(hop_page, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #TODO
        process_hops(soup)
    return hop_list

def crawl_yeasts():
    for yeast_page in YEAST_URL:
        page = requests.get(yeast_page, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #TODO
        process_yeasts(soup)
    return yeast_list

if __name__ == "__main__":
    pass

    