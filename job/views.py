from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    
    return render(request ,'job/jobs.html',{'job_list' : job_list})


def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    
    return render(request ,'job/job_detail.html',{'job_detail' : job_detail})