import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.crawler import CrawlerProcess


class TweetSpider(scrapy.Spider):

    name = "tweets"
    start_urls = ["https://mobile.twitter.com/realDonaldTrump"]
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 20,
        'ITEM_PIPELINES': {
          'process.TweetPipeline': 300,
        },
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 3.0,
    }

    def parse(self, response):
        self.logger.info("Starting Parsing of Initial List")
        count = 1
        hxs = HtmlXPathSelector(response)
        for tweet in hxs.select('//div[contains(@class, "timeline")]//table[contains(@class, "tweet")]'):
            yield {
                "text": tweet.select('.//div[contains(@class, "dir-ltr")]/text()').extract_first()
            }

        next_page_url = hxs.select('//div[contains(@class, "w-button-more")]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TweetSpider)
    process.start()
