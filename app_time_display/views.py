from django.shortcuts import render, render
from time import gmtime, strftime


# Create your views here.
def index(request):
    context = {
        "time": strftime("%a %d, %Y %H:%M:%S %p", gmtime())
    }
    return render(request,'app_time_display/index.html', context)