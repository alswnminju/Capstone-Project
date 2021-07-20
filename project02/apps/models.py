from django.db import models


class Parkmoa(models.Model):

    #Num = models.TextField(null=True)
    District = models.TextField(null=True)
    Park_division = models.TextField(null=True)
    Park_name = models.TextField(null=True)
    #Road_address = models.TextField(null=True)
    #Parcel_address = models.TextField(null=True)
    #Park_overview = models.TextField(null=True)
    #Park_area = models.TextField(null=True)
    #Main_facility = models.TextField(null=True)
    #Sporting_goods = models.TextField(null=True)
    #Guidemap = models.TextField(null=True)
   # Direction = models.TextField(null=True)
    #Use_notes = models.TextField(null=True)
    #Image = models.TextField(null=True)
    #Park_number = models.TextField(null=True)
    #Latitude = models.TextField(null=True)
    #Longitude = models.TextField(null=True)
   #Shortcut = models.TextField(null=True)
    #Grade = models.TextField(null=True)
    #Keyword = models.TextField(null=True)

    class Meta:

        # database table name
        db_table = 'parkmoa_db'
        
