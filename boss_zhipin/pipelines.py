from elasticsearch import Elasticsearch

class ElasticsearchPipeline:

    def __init__(self, es_server, es_port, es_index, es_type, es_uniq_key):
        self.es_server = es_server
        self.es_port = es_port
        self.es_index = es_index
        self.es_type = es_type
        self.es_uniq_key = es_uniq_key
        self.es = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_server=crawler.settings.get('ELASTICSEARCH_SERVER'),
            es_port=crawler.settings.get('ELASTICSEARCH_PORT'),
            es_index=crawler.settings.get('ELASTICSEARCH_INDEX'),
            es_type=crawler.settings.get('ELASTICSEARCH_TYPE'),
            es_uniq_key=crawler.settings.get('ELASTICSEARCH_UNIQ_KEY')
        )

    def open_spider(self, spider):
        self.es = Elasticsearch([{'host': self.es_server, 'port': self.es_port}])

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        doc = dict(item)
        self.es.index(index=self.es_index, doc_type=self.es_type, id=doc[self.es_uniq_key], body=doc)
        return item