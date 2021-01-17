import scrapy 

class QuoteSpider(scrapy.Spider):
    name = 'quotes' #name of the spider 
    start_urls = [
        'https://quotes.toscrape.com/'
    ] #urls to scrape 

    def parse(self, response):  #method - with the reponse of the source code of the quotes of the text
        title = response.css('title::text').extract() #retrvie the title tage of the element 
        yield {'titletext': title}  #creating a dictornary to store the title from the response, key and a value 

