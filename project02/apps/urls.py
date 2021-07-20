from django.urls import path
from .views import ParkmoaSearchView

urlpatterns = [path('',ParkmoaSearchView.as_view(), name='ParkmoasSerceView')]
