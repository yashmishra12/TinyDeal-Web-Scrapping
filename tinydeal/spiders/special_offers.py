import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com/']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        pass
