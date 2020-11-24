import scrapy 
from scrapy.crawler import CrawlerProcess

class movieCrawler(scrapy.Spider):
    name = "movieCrawler"
   

    def start_requests(self):
       url ="https://en.wikipedia.org/wiki/%22Hello,_World!%22_program"
       yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        title = response.xpath("//*[@id='mw-content-text']/div[1]/p[1]/text()[2]").extract_first()
        #print(str(title))
        with open("SinglePageScrape.txt","w") as f:
            f.write(title)
           #f.write("Scraper 1 didnt get any info from link. Issue is not with code but with site permissions or xpath")
        f.close()


process = CrawlerProcess()
process.crawl(movieCrawler)
process.start()

