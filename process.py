import scrapy


class TweetPipeline(object):

    def __init__(self):
        self.file = open("tweets.txt", 'w')
        self.tweets_list = []

    def close_spider(self, spider):
        for tweet in self.tweets_list:
            self.file.write(tweet)
        self.file.close()
        spider.logger.info("Wrote %d tweets to file" % len(self.tweets_list))

    def process_item(self, item, spider):
        """
        Process a scraped item and add it to a file
        :param item - dict object containing the tweet text
        :param spider - spider instance that scraped the data
        """
        full_tweet = "BEGIN TWEET"
        tweet = item["text"].strip()
        if tweet != "\n" and len(tweet) != 0:
            full_tweet = full_tweet + " " + tweet
        self.tweets_list.append(full_tweet + " END\n")
        return item
