import scrapy

class BlogSpider(scrapy.Spider):
    name = 'newsSpider'
    start_urls = ['https://toyotanews.pressroom.toyota.com/toyota/releases/']

    def parse(self, response):
        lines = response.css('#leftContentArea').extract()[0]
        Articles = response.css('div.remainingArticles').extract()
        headlines = response.css('h2.headline a::text').extract()

        #print(Articles)
        #print(lines)
        for headline in headlines:
            print(headline)
        
        # next_page = response.css('.tekpagination a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)