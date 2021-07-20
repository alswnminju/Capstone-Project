from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text
from django_elasticsearch_dsl import fields
from .models import Parkmoa


connections.create_connection(hosts=['https://team-parkmoa.kb.ap-northeast-2.aws.elastic-cloud.com:9243'])

# elasticsearch analyzer setup
#html_strip = analyzer('html_strip',
#                      tokenizer = "standard",
#                      filter=["lowercase","stop","snowball"],
#                      char_filter=["html_strip"])


class ParkmoaDocument(Document):

    # The fields of the model you want to be indexed in elasticsearch
    #Num = fields.TextField()
    District = fields.TextField()
    Park_division = fields.TextField()
    Park_name = fields.TextField()
    #Road_address = Text()
    #Parcel_address = Text()
    #Park_overview = Text()
    #Park_area = Text()
    #Main_facility = Text()
    #Sporting_goods = Text()
    #Guidemap = Text()
    #Direction = Text()
    #Use_notes = Text()
    #Image = Text()
    #Park_number = Text()
    #Latitude = Text()
    #Longitude = Text()
    #Shortcut = Text()
    #Grade = Text()
    #Keyword = Text()

    class Index:

        # name of elasticsearch index for Parkmoa model
        name = 'parkmoa'

        #basic setup for elasticsearch
        settings = {"number_of_shards" : 1,
                    "number_of_replicas" : 1}

    class Django:
        model = Parkmoa
