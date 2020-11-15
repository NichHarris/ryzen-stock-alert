# Newegg spider
import scrapy
class NeweggSpider(scrapy.Spider):
    name = "newegg"
    open('NeweggStatus.txt', 'w').close()

    def start_requests(self):
        urls = [
            'https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666',
            #'https://www.newegg.ca/amd-ryzen-5-3600x/p/N82E16819113568', test
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        myList = []
        ## Add to Cart Button
        #product = response.xpath("//*[@class='btn btn-message btn-wide']//text()").get().strip() 
        product = response.xpath("//*[@class='product-inventory']//text()").get().strip()
        myList = [product]
        filename = 'NeweggStatus.txt'
        with open(filename, 'a') as f:
            f.write("\nProduct is Currently: " + str(myList))
            ## USE THIS FOR FULL SCRIPT
            # f.write(str(myList))
        self.log(f'Saved File {filename}')
        
