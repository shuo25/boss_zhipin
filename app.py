from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

app = Flask(__name__)

# 配置Elasticsearch连接
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}], headers={'Accept': 'application/json'})

# 配置Elasticsearch索引
INDEX_NAME = 'boss_zhipin'

@app.route('/search', methods=['GET'])
def search():
    # 获取查询参数
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    # 创建查询
    s = Search(using=es, index=INDEX_NAME).query('multi_match', query=query, fields=['title', 'company', 'location', 'salary'])

    # 执行查询
    response = s.execute()

    # 构造结果
    results = []
    for hit in response:
        results.append({
            'title': hit.title,
            'company': hit.company,
            'location': hit.location,
            'salary': hit.salary,
            'link': hit.link,
        })

    return jsonify(results)

@app.route('/all', methods=['GET'])
def get_all():
    # 创建查询：获取所有文档
    s = Search(using=es, index=INDEX_NAME).query('match_all')

    # 执行查询
    response = s.execute()

    # 构造结果
    results = []
    for hit in response:
        results.append({
            'title': hit.title,
            'company': hit.company,
            'location': hit.location,
            'salary': hit.salary,
            'link': hit.link,
        })

    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)
