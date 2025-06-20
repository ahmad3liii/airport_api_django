from django.urls import path
from . import views
urlpatterns=[
   # path('airportapp/',views.mainpage,name="mainpage"),
    path('airportlist/',views.airport_list,name="airportslist"),
    path('airports/',views.list_airports,name="listairports"),
]