import scrapy
from boss_zhipin.items import BossZhipinItem
from faker import Faker

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/']

    def parse(self, response):
        # jobs = response.xpath('//div[@class="job-primary"]')
        # for job in jobs:
        #     item = BossZhipinItem()
        #     item['title'] = job.xpath('.//span[@class="job-name"]/a/text()').get()
        #     item['company'] = job.xpath('.//div[@class="company-text"]/h3/a/text()').get()
        #     item['location'] = job.xpath('.//span[@class="job-area"]/text()').get()
        #     item['salary'] = job.xpath('.//span[@class="red"]/text()').get()
        #     item['link'] = job.xpath('.//span[@class="job-name"]/a/@href').get()
        #     print(item)
        #     yield item

        fake = Faker()
        for _ in range(10):  # 生成10个虚假的职位信息
            item = BossZhipinItem()
            item['title'] = fake.job()
            item['company'] = fake.company()
            item['location'] = fake.city()
            item['salary'] = str(fake.random_int(min=1000, max=10000))
            item['link'] = fake.url()
            print(item)
            yield item