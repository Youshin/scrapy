import scrapy
from scrapy.contrib.exporter import CsvItemExporter

names = []

class NewsSpider(scrapy.Spider):
    name = 'newsSpider'
    download_delay = 0.1
    start_urls = ['https://toyotanews.pressroom.toyota.com/toyota/releases/']
    title = scrapy.Field()
    date = scrapy.Field()
    context = scrapy.Field()

    def parse_news(self, response): # parse news page
        Main = response.css('#contentMain') # find content
        # print(Main)

        title = Main.css('h1::text').extract()[0]  # find title
        date = Main.css('.rel-dt::text').extract()[0] # find date the news published
        contents = Main.css('div:not([class])::text').extract() # find all contents
        context = ""
        for i in contents:  # add as 1 string
            context = context + "\n" + i.strip() 
        yield { # add to field
            "title":title,
            "date":date,
            "context": context.encode('utf-8'), 
        }
        
    def parse(self, response):  # parse the news lists
        articles = response.css('h2.headline a::attr(href)').extract() # find links to news page
        # print(articles)
        for i in articles: # go parse the news page
            i = response.urljoin(i)
            yield scrapy.Request(i, callback=self.parse_news)
        
        next_page = response.css('.tekpagination a::attr(href)').extract() # find next
        indicator = response.css('a.pagenavlinks::text').extract() # find next as string
        #print(indicator)
        if len(next_page) == 2: # if back and next both exist
            next_page = next_page[1] # 1 is next
            indicator = indicator[1] #
        elif len(next_page) == 1: # when only back or next exists
            next_page = next_page[0] # 0 is next
            indicator = indicator[0]

        if next_page is not None and indicator == "Next >>": # go to next if it is next
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)