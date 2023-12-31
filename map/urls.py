from django.contrib import admin
from django.urls import path 
from map import views

urlpatterns = [
    path('' , views.index ,name='index'),
    path('chart' , views.dashbord,name='charts'),
    path('about',views.about , name= 'about'),
    path('poste',views.about , name= 'posts'),
    path('json/' ,views.jsonRe, name= 'json'),
    path('addData' , views.addData , name= 'addData')

]
