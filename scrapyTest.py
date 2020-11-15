import scrapy

class Spider(scrapy.Spider):
    name = "Newegg"

    def start_requests(self):
        urls = [
            'https://www.newegg.ca/core-i7-9th-gen-intel-core-i7-9700k/p/N82E16819117958',
            'https://www.newegg.ca/amd-ryzen-5-5600x/p/N82E16819113666',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log(f'Saved File {filename}')