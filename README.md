爬取boss直聘
===============

基于 Python3 的boss直聘官网的 Scarpy 爬虫。

### 使用方法
-------
命令行启动
启动Elasticsearch
直接前往[Elasticsearch官网](https://www.elastic.co/cn/downloads/elasticsearch)下载

    # 安装依赖
    pip install --no-cache-dir -r requirements.txt
    # 启动收集程序
    scrapy crawl boss
    # 定时收集程序
    python schedule_crawl.py
    # 启动查询数据接口服务
    python app.py
    
docker启动

    # 容器编排启动
    docker-compose up -d
    # 容器编排停止
    docker-compose stop
    # 容器编排日志
    docker-compose logs
完成上述步骤后可以在接口地址中查询搜索数据
https://ko93u1zz7k.apifox.cn/api-176694270