from django.shortcuts import render
from time import strftime, gmtime

def time(request):
    time_d={
        'time': strftime('%I:%M %p', gmtime()),
        'date': strftime('%A %B %d'),
    }

    return render(request,'time.html', time_d)
