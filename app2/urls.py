from app2.views import *
from django.urls import path
app_name='venkey'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('deepu/',deepu,name='deepu'),
    path('sample/',sample,name='sample'),
]