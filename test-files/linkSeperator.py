from bs4 import BeautifulSoup
import json
import time
from urllib.request import urlopen, Request

## This code will individually seperate each link to products in the catalogue
## TODO: Add keyword detection
## TODO: Port over properly to 3080scraper.py

with open('sites3080.json', 'r') as f:
    sites = json.load(f)


def urllib_get(url):
    request = Request(url, headers={'User-Agent': 'Chrome/35.0.1916.47'})
    page = urlopen(request, timeout=30)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def main():
    # url = "https://microbytes.com/catalogsearch/result/?cat=6&q=intel+core"
    while True:
        for site in sites:
            print("\tChecking {} ...".format(site.get('name')))
            if site.get('enabled'):
                try:
                    html = urllib_get(site.get('url'))
                except Exception as e:
                        print("\tConnection Failed...")
                        print("\tSkipping")
                        continue
                
                keyword = "Add to Cart"
                index = html.upper().find(keyword.upper())
                soup = BeautifulSoup(html, 'html.parser')
        
                for link in soup.find_all("a", class_="product-image", href=True):
                    tag = link['href']
                    try:
                        html = urllib_get(tag)
                    except Exception as e:
                        print("\tConnection Failed...")
                        print("\tSkipping")
                        continue
                
                    index = html.upper().find(keyword.upper())
                    if index != -1:
                        print(link['href'])
                    elif index == -1:
                        continue
            time.sleep(1)
            
            
if __name__ == '__main__':
    main()
