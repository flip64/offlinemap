from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib import messages
from map.forms import FilesForm 
from map.baseClass import JsonChart 
from map.models import Configh
from map.map import uri
from openpyxl import load_workbook
from map.PredictH import plot


# Create your views here.
chart = JsonChart()


def index(request): 
  try :  
    file = open('static/img/myplot.png')
  except: 
    uri()
    file = open('static/img/myplot.png')

  
  
  
  context = { 
     'file' : file,
  } 
  return render (request , 'map/index.html' , context)


def about(request):
  return render (request,"map/about.html",{'data':uri})


def dashbord(request): 
  
  return render(request , 'map/dashbord1.html')


def jsonRe(request) : 
      
  return JsonResponse(chart.getJson())


def addData(request) : 
  
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FilesForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
             file = request.FILES['file'] 
             try:
            
              wb = load_workbook(file)
              sh = wb['Sheet1']
              wb.save('static/exels/operation.xlsx')
              plot() 
             except : 
               messages.success(request , 'در آپلود فایل خطایی رخ داده' ,'success')
               return redirect('addData')
             
            
             return redirect('charts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilesForm()
    return render(request, "map/addData.html", {"form": form})





