from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

today = date.today()
# Create your views here.


def home(request):
    context = {
        "todays_date": today
    }
    return render(request, 'hello.html', context)



    
                    
