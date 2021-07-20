# redefining elasticsearch instance and adding query to filter/fetch data.

from elasticsearch_dsl import Q

class ElasticSearchService:

    """
    make elasticsearch instance using dovument_class_name
    holds query_list, size and search_instance.
    query_list : list of query/keyword, on which parkmoa will filter
    size: length of fitered result
    """

    def _init_(self, document_class_name, query, size):
        self.query = query
        self.size = size
        self.search_instance = document_class_name.search()

    
    # filter parkmoa_db using query from given query list
    def run_query_list(self):
        # to filter using each query/keyword
        # define elasticsearch query, where Park_division field must match with given query/keyword
        q = Q('bool', must=[Q('match', Park_division=self.query)])

        # adding elasticsearch query
        # sort filtered result based on _score
        # result's length star from 0 to self.size
        # q is getting add with elasticsearch instance using .query()
        # .sort() is used for sorting the elasticsearch's result data
        # [0:self.size] is if self.size = 5, show the top 5 records which start from 0 till 4 index
        search_with_query = self.search_instance.query(q).sort('_score')[0:self.size]

        # execute elastic query
        response = search_with_query.execute()
        result = response.to_dict()['hits']['hits']

        return result
