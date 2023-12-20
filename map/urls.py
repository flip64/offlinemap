from django.contrib import admin
from django.urls import path 
from map import views

urlpatterns = [
    path('' , views.index ,name='index'),
    path('dashbord' , views.dashbord,name='dashbord'),
    path('about',views.about , name= 'about'),
    path('poste',views.about , name= 'posts'),
    path('json/' ,views.jsonRe, name= 'json'),
    path('addData' , views.addData , name= 'addData')

]
