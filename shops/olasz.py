import requests
from bs4 import BeautifulSoup


MALT_URL = ["https://olaszsped.com/index.php?main_page=index&cPath=2_34&zenid=af55a770d733e764bd56ddd73629cd29"]
HOP_URL = ["https://olaszsped.com/index.php?main_page=index&cPath=2_21&zenid=af55a770d733e764bd56ddd73629cd29"]
YEAST_URL = ["https://olaszsped.com/index.php?main_page=index&cPath=2_19&zenid=af55a770d733e764bd56ddd73629cd29"]
SHOP = "Olasz"

page = None
soup = None

malt_list = []
hop_list = []
yeast_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def process_malts(soup):
    malts = soup.find_all("tr", class_="productListing-odd")
    for malt in malts:
            name = malt.find_all('td', class_='productListing-data')
            print(name)

def process_hops(soup):
    hops = soup.find_all("div", class_="product-snapshot list_div_item")
    for hop in hops:
            name = hop.find('div', class_='snapshot-list-item list_prouctname').text.replace("\n", "")
            price = hop.find('div', class_='snapshot-list-item list_prouctprice')
            if price is None:
                price = hop.find('div', class_='snapshot-list-item list_prouctprice list_productprice_special').find('span', class_='list_special').text.replace("\n", "")
            else:
                price = price.text.replace("\n", "")
            if hop.find('td', class_='param-value featured-param featured-alfa_sav'):
                aa = hop.find('td', class_='param-value featured-param featured-alfa_sav').text.replace("\n", "").replace("ALFA-SAV:", "").replace(" ", "")
            else:
                aa = ""

            temp = {
                "type" : "hop",
                "name" : name,
                "price" : price,
                "aa" : aa,
                "shop": SHOP
            }
            hop_list.append(temp)

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
    return hop_list

def crawl_yeasts():
    
    return yeast_list
    pass

if __name__ == "__main__":
    pass

    