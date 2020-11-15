# Global spider
import scrapy
import json
with open('sites.json', 'r') as f:
    sites = json.load(f)

class GlobalSpider(scrapy.Spider):
    name = "global"
    open('GlobalStatus.txt', 'w').close()

    def start_requests(self):
        urls = [
            'https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666',
            'https://www.amazon.ca/DANIPEW-Sepu-ltura-Cotton-Performance-T-Shirt/dp/B08166SLDF'
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
        myList = []
        product = " "
        for site in sites:
            if site.get('name') == "Amazon":
                product = response.xpath("//*[@class='a-size-medium a-color-price']//text()").get().strip()
            elif site.get('name') == "Newegg":
                product = response.xpath("//*[@class='product-inventory']//text()").get().strip()
            myList += [product]
        
        filename = 'GlobalStatus.txt'
        with open(filename, 'a') as f:
            f.write("\nProduct is Currently: " + str(myList))
            ## USE THIS FOR FULL SCRIPT
            # f.write(str(myList))
        self.log(f'Saved File {filename}')