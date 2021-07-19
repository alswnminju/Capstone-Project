from django.db import models

class Parkmoa(models.Model):

    Num = models.TextField(null=True)
    District = models.TextField(null=True)
    Park_division = models.TextField(null=True)
    Park_name = models.TextField(null=True)
    Road_address = models.TextField(null=True)
    Parcel_address = models.TextField(null=True)
    Park_overview = models.TextField(null=True)
    Park_area = models.TextField(null=True)
    Main_facility = models.TextField(null=True)
    Sporting_goods = models.TextField(null=True)
    Guidemap = models.TextField(null=True)
    Direction = models.TextField(null=True)
    Use_notes = models.TextField(null=True)
    Image = models.TextField(null=True)
    Park_number = models.TextField(null=True)
    Latitude = models.TextField(null=True)
    Longitude = models.TextField(null=True)
    Shortcut = models.TextField(null=True)
    Grade = models.TextField(null=True)
    Keyword = models.TextField(null=True)   

    def indexing(self):
        obj = ParmoaIndex(meta={'id': self.id },
                        Num = self.Num,
                          District = self.District,
                          Park_division = self.Park_division,
                          Park_name = self.Park_name,
                          Road_address = self.Road_address,
                          Parcel_address = self.Parcel_address,
                          Park_overview = self.Park_overview,
                          Park_area = self.Park_area,
                          Main_facility = self.Main_facility,
                          Sporting_goods = self.Sporting_goods,
                          Guidemap = self.Guidemap,
                          Direction = self.Direction,
                          Use_notes = self.Use_notes,
                          Image = self.Image,
                          Park_number = self.Park_number,
                          Latitude = self.Latitude,
                          Longitude = self.Longitude,
                          Shortcut = self.Shortcut,
                          Grade = self.Grade,
                          Keyword = self.Keyword)
        obj.save()
        return obj.to_dict(include_meta=True)
