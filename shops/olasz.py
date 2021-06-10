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

def process_malts(soup):
    malts = soup.find_all("tr", class_="productListing-odd")
    for malt in malts:
            #print(malt)
            name = malt.find_all('td', class_='productListing-data')
            print(name)
            #if malt.find('div', class_='productListing-data').find('h3', class_='itemTitle'):
            #    name = malt.find('div', class_='productListing-data').find('h3', class_='itemTitle').find('a')
            #    print(name)
    #        price = malt.find('div', class_='snapshot-list-item list_unitprice').text.replace("\n", "").replace("    ", "")
    #        if malt.find('td', class_='param-value featured-param featured-malata_ebc'):
    #            ebc = malt.find('td', class_='param-value featured-param featured-malata_ebc').text.replace("\n", "").replace("EBC: ", "")
    #        else:
    #            ebc = ""

    #        temp = {
    #            "type" : "malt",
    #            "name" : name,
    #            "price" : price,
    #            "ebc" : ebc,
    #            "shop": SHOP
    #        }
    #        malt_list.append(temp)

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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        page = requests.get(malt_page, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #clear
        #print(soup)
        process_malts(soup)
    return malt_list

def crawl_hops():
    #for hop_page in HOP_URL:
    #    page = requests.get(hop_page)
    #    soup = BeautifulSoup(page.content, 'html.parser')
    #    multiple_pages = soup.find_all("a", class_="pagination-link")
    #    page_list = []
    #    for mp in multiple_pages:
    #        page_list.append(mp["href"])
    #    page_list=list(dict.fromkeys(page_list))
    #    process_hops(soup)
    #    for other_page in page_list:
    #        page = requests.get(other_page)
    #        soup = BeautifulSoup(page.content, 'html.parser')
    #        process_hops(soup)
    return hop_list

def crawl_yeasts():
    
    return yeast_list
    pass

if __name__ == "__main__":
    crawl_malts()
    #crawl_hops()
    #crawl_yeasts()
    #dump_to_json("malt", malt_list)
    #dump_to_json("hop", hop_list)
    pass

    