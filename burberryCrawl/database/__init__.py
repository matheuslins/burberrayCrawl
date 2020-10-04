from elasticsearch import Elasticsearch

from burberryCrawl.settings import ES_HOST


def config_client():
    return Elasticsearch(hosts=ES_HOST, timeout=25)
