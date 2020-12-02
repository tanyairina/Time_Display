from django.shortcuts import render
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%b-%d-%Y %I:%M %p", gmtime())      
    }
    return render(request, 'index.html', context)

def time2(request):
    context = {
        "time": strftime("%H:%M:%S %a, %d %b %Y ", gmtime())  
    }
    return render(request, 'index.html', context)

