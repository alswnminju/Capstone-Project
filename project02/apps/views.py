from django.shortcuts import render

import logging
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import elasticsearch
from .models import Parkmoa
from .serializers import ParkmoaSerializer
from .documents import ParkmoaDocument
from .helps import ElasticSearchService
from .utils import rebuild_elasticsearch_index, delete_elasticsearch_index
from rest_framework.response import Response


# get an instance of a logger
logger = logging.getLogger(__name__)


class ParkmoaSearchView(APIView):

    def get(self, request, format=None):
        parkmoas = Parkmoa.objects.all()
        serializers = ParkmoaSerializer(parkmoas, many=True)
        return Response(serializers.data)
        

    # fomat the response with messageg, status, data and send as api response

    def send_response(self, message, status_code, data=None):
        content = {"message": message,
                    "result": data if data is not None else [] }
        return Response(content, status=status_code)


    #handle post request filter the pakrmoa_db data based on given query list with k number
    def post(self, request):
        query = request.data.get('queries',None)
        k = request.data.get('k',None)
        # response = None
        
        if is_empty_or_null(query):
            error_message = "k should be integer and not empty"
            return self.send_response(error_message, status.HTTP_400_BAD_REQUEST)

        try:
            # build elasticsearch index
            rebuild_elasticsearch_index()

            # build search instance using ParkmoaDocument and save query_list and k as instance value
            search_doc = ElasticSearchService(ParkmoaDocument, query, k)

            #run each query using search instance
            result = search_doc.run_query_list()
            response = {'park':result}

            # delete elasticsearch index
            delete_elasticsearch_index()

        except elasticsearch.ConnectionError as connection_error:
            # ConnectionError if elasticsearch sever is down

            logger.debug('ConnectionError: ' + str(connection_error))
            error_message = "Elastic search Connection refused"
            return self.send_response(error_message, status.HTTP_503_SERVICE_UNAVAILABLE)

        except Exception as exception_msg:
            # handle all type of error

            logger.debug('Exception: ' + str(exception_msg))
            error_message = str(exception_msg)
            return self.send_response(error_message, status.HTTP_400_BAD_REQUEST)

        return self.send_response('success', status.HTTP_200_OK, response)
