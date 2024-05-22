from apscheduler.schedulers.blocking import BlockingScheduler
import os


def start_crawl():
    os.system("scrapy crawl boss")


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(start_crawl, 'interval', hours=1)  # 每隔1小时运行一次爬虫
    print("定时获取任务启动。。。")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass