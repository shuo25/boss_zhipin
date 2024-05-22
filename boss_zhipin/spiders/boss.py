import scrapy
from boss_zhipin.items import BossZhipinItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/']

    def parse(self, response):
        jobs = response.xpath('//div[@class="job-primary"]')
        for job in jobs:
            item = BossZhipinItem()
            item['title'] = job.xpath('.//span[@class="job-name"]/a/text()').get()
            item['company'] = job.xpath('.//div[@class="company-text"]/h3/a/text()').get()
            item['location'] = job.xpath('.//span[@class="job-area"]/text()').get()
            item['salary'] = job.xpath('.//span[@class="red"]/text()').get()
            item['link'] = job.xpath('.//span[@class="job-name"]/a/@href').get()
            print(item)
            yield item