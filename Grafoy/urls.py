from django.urls import path
from . import views 

app_name = 'Home'

urlpatterns=[
    #Todas las extenciones que requiera. es un render
    path('',views.home, name='Home'),

    path('tabla/',views.tabla,name='tabla')
]