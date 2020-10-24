from django.shortcuts import render
from .models import Job, Category

# Create your views here.

def job_list(request):
    
    return render(request, 'job/index.html',context)

def job_detail(request, id):
   
    return render(request, 'job/index.html',context)
