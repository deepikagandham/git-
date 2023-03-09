from app1.views import*
from django.urls import path 
app_name='deepu'
urlpatterns=[  
    path('dhoni/',dhoni,name='dhoni'),
    path('sample/',sample,name='sample'),
    path('sample1/',sample1,name='sample1'),
]