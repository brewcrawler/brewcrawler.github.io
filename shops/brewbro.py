import requests
from bs4 import BeautifulSoup


MALT_URL = ["https://www.brewbro.hu/malatak/osszes-malata"]
HOP_URL = ["https://www.brewbro.hu/komlok/osszes-komlo"]
YEAST_URL = ["https://www.brewbro.hu/elesztok/osszes-eleszto"]
SHOP = "Brewbro"

page = None
soup = None

malt_list = []
hop_list = []
yeast_list = []

def process_malts(soup):
    malts = soup.find_all("div", class_="product-snapshot list_div_item")
    for malt in malts:
            name = malt.find('div', class_='snapshot-list-item list_prouctname').text.replace("\n", "")
            price = malt.find('div', class_='snapshot-list-item list_unitprice').text.replace("\n", "").replace("    ", "")
            if malt.find('td', class_='param-value featured-param featured-malata_ebc'):
                ebc = malt.find('td', class_='param-value featured-param featured-malata_ebc').text.replace("\n", "").replace("EBC: ", "")
            else:
                ebc = ""

            temp = {
                "type" : "malt",
                "name" : name,
                "price" : price,
                "ebc" : ebc,
                "shop": SHOP
            }
            malt_list.append(temp)

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

def process_yeasts(soup):
    yeasts = soup.find_all("div", class_="product-snapshot list_div_item")
    for yeast in yeasts:
            name = yeast.find('div', class_='snapshot-list-item list_prouctname').text.replace("\n", "")
            price = yeast.find('div', class_='snapshot-list-item list_prouctprice').text.replace("\n", "").replace("    ", "")

            temp = {
                "type" : "yeast",
                "name" : name,
                "price" : price,
                "shop": SHOP
            }
            yeast_list.append(temp)

def crawl_malts():
    for malt_page in MALT_URL:
        page = requests.get(malt_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        multiple_pages = soup.find_all("a", class_="pagination-link")
        page_list = []
        for mp in multiple_pages:
            page_list.append(mp["href"])
        page_list=list(dict.fromkeys(page_list))
        process_malts(soup)
        for other_page in page_list:
            page = requests.get(other_page)
            soup = BeautifulSoup(page.content, 'html.parser')
            process_malts(soup)
    return malt_list

def crawl_hops():
    for hop_page in HOP_URL:
        page = requests.get(hop_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        multiple_pages = soup.find_all("a", class_="pagination-link")
        page_list = []
        for mp in multiple_pages:
            page_list.append(mp["href"])
        page_list=list(dict.fromkeys(page_list))
        process_hops(soup)
        for other_page in page_list:
            page = requests.get(other_page)
            soup = BeautifulSoup(page.content, 'html.parser')
            process_hops(soup)
    return hop_list

def crawl_yeasts():
    for yeast_page in YEAST_URL:
        page = requests.get(yeast_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        multiple_pages = soup.find_all("a", class_="pagination-link")
        page_list = []
        for mp in multiple_pages:
            page_list.append(mp["href"])
        page_list=list(dict.fromkeys(page_list))
        process_yeasts(soup)
        for other_page in page_list:
            page = requests.get(other_page)
            soup = BeautifulSoup(page.content, 'html.parser')
            process_yeasts(soup)
    return yeast_list

if __name__ == "__main__":
    #crawl_malts()
    #crawl_hops()
    #crawl_yeasts()
    #dump_to_json("malt", malt_list)
    #dump_to_json("hop", hop_list)
    #main()
    #print(yeast_list)
    pass
    