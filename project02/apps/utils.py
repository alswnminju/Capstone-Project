# contains code which are generic

from django.core.management import call_command


# run elasticsearch command to rebuild index
def rebuild_elasticsearch_index():
    call_command('search_index','--rebulid','-f')


#run elasticsearch command to delete index
def delete_elasticsearch_index():
    call_command('search_index','--delete','-f')
