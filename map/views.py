from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib import messages
from map.forms import FilesForm 
from map.baseClass import JsonChart 
from map.models import Configh
from map.map import uri
import json
from openpyxl import load_workbook

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
  
  return render(request , 'map/dashbord.html')


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
            except : 
               messages.success(request , 'فرت فایل مناسب نیست لظفا یک فایل اکسل آپلود کنید ' ,'success')
               return redirect('addData')
            value = [] 
            for cell in sh['A'] : 
               if cell.value != None: 
                  value.append(cell.value) 
            
            d1 = []
            for cell in sh['C'] : 
               if cell.value != None: 
                  d1.append(cell.value) 

            d2 = [] 
            for cell in sh['D'] : 
               if cell.value != None: 
                 d2.append(cell.value)
     
            chart.setConfighChart({
               'data' : d1 ,
               'borderColor' : 'rgba(215,0,164,0.60)',
                'backgroundColor' : 'rgba(215,0,164,0.60)'
                                   
                                   } , 1)
            chart.setConfighChart({'data' : d2 ,'borderColor' : 'rgba(0,500,200,0.60)'
                                   
                                   } , 2)
            chart.setLabel(value)             
            
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return redirect('dashbord')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilesForm()
    return render(request, "map/addData.html", {"form": form})





