# Amason spider
import scrapy
class NeweggSpider(scrapy.Spider):
    name = "amazon"
    open('AmazonStatus.txt', 'w').close()

    def start_requests(self):
        urls = [
            'https://www.amazon.ca/DANIPEW-Sepu-ltura-Cotton-Performance-T-Shirt/dp/B08166SLDF',
            'https://www.amazon.ca/AMD-Ryzen-3600-12-thread-processor/dp/B07STGGQ18?ref_=ast_sto_dp',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        myList = []
        product = response.xpath("//*[@class='a-size-medium a-color-price']//text()").get().strip()
        myList = [product]
        if product != 'Currently unavailable.':
            # status = 'Available'
            # for i in range(product):
            #     status += myList[0](i)
            # myList = [status]
            myList[0] = myList[0].strip("CDN$&nbsp;\xa0")
            myList[0] = 'Available ' + myList[0] + "$"
        
        filename = 'AmazonStatus.txt'
        with open(filename, 'a') as f:
            f.write("\nProduct is Currently: " + str(myList))
            ## USE THIS FOR FULL SCRIPT
            #f.write(str(myList))
        self.log(f'Saved File {filename}')
        