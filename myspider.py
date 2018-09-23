import scrapy

class BlogSpider(scrapy.Spider):
    name = 'newsSpider'
    start_urls = ['https://toyotanews.pressroom.toyota.com/toyota/releases/']

    def parse(self, response):
        lines = response.css('#leftContentArea').extract()[0]
        Articles = response.css('div.remainingArticles').extract()
        headlines = response.css('h2.headline a::text').extract()
        names = []
        #print(Articles)
        #print(lines)
        for headline in headlines:
            names.append(headline)
        next_page = response.css('.tekpagination a::attr(href)').extract()
        if len(next_page) == 2:
            next_page = next_page[1]
        else:
            next_page = next_page[0]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        print(names)