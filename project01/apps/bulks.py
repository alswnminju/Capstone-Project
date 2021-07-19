from elasticsearch_dsl import connections
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from . import models
from apps.utils import ParkmoaIndex

connections.create_connection(hosts=['https://team-parkmoa.kb.ap-northeast-2.aws.elastic-cloud.com:9243'])


def bulk_indexing():
    es = Elasticsearch(cloud_id ="team-parkMoa:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjkyNDMkNjc2ODhhNjFmOTZiNDNjNTlkZWFiNDUwMzUwMmQ2YTckZGM4Y2EyMTg4N2FlNDM1Nzg2OTkxMTI2YmZmNzJmZTY=",
                       http_auth=("elastic","IaPpgyeCkU38iytPPHn4jQny"))
    bulk(client=es, actions=(b.indexing() for b in models.Parkmoa.objects.all().iterator()))


def search():
    s = Search().query("match",image="http://parks.seoul.go.kr/file/info/view.do?fIdx=1741")
    response = s.execute()
    return response
#    for hit in s:
 #       print(hit.image)
        
