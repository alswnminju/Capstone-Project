from elasticsearch_dsl import Document, Text

class ParkmoaIndex(Document):
    Num = Text()
    District = Text()
    Park_division = Text()
    Park_name = Text()
    Road_address = Text()
    Parcel_address = Text()
    Park_overview = Text()
    Park_area = Text()
    Main_facility = Text()
    Sporting_goods = Text()
    Guidemap = Text()
    Direction = Text()
    Use_notes = Text()
    Image = Text()
    Park_number = Text()
    Latitude = Text()
    Longitude = Text()
    Shortcut = Text()
    Grade = Text()
    Keyword = Text()

    class Index:
        name = 'parkmoa'
