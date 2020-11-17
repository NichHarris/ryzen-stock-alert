from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

## This code will individually seperate each link to products in the catalogue
## TODO: Add keyword detection
## TODO: Port over properly to 3080scraper.py


def urllib_get(url):
    request = Request(url, headers={'User-Agent': 'Chrome/35.0.1916.47'})
    page = urlopen(request, timeout=30)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def main():
    url = "https://microbytes.com/catalogsearch/result/?cat=0&q=rtx+2080"
    while True:
        html = urllib_get(url)
        keyword = "Add to Cart"
        index = html.upper().find(keyword.upper())
        soup = BeautifulSoup(html, 'html.parser')
        
        if index != -1:
            for link in soup.find_all("a", class_="product-image", href=True):
                print(link['href'])
        elif index == -1:
            for link in soup.find_all("a", class_="product-image", href=True):
                print(link['href'])
            
if __name__ == '__main__':
    main()
