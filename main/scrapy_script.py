

import scrapy


class ResearchPaperSpider(scrapy.Spider):
    name = 'research_paper_spider'
    
    # Set the URLs to scrape
    start_urls = [
        'https://dl.acm.org/doi/abs/10.1145/2505057'
        # Add more URLs here
    ]
    
    def parse(self, response):
        # Extract the abstract, title, and URL
        abstract = response.css('abstract::text').get()
        title = response.css('h1::text').get()
        url = response.url
        
        # Print or store the extracted information as desired
        print("Title:", title)
        print("Abstract:", abstract)
        print("URL:", url)
        print("--------------------------------------")


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(ResearchPaperSpider)
process.start()
