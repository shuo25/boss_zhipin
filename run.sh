#!/bin/bash
# 等待Elasticsearch服务启动
echo "Waiting for Elasticsearch to start..."
sleep 15

# 启动定时爬虫任务
python schedule_crawl.py &

# 启动Flask应用
python app.py