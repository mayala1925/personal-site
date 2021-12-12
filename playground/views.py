from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import pandas as pd
today = date.today()
# Create your views here.

df = pd.read_csv("static/predictions/predictions.csv")
pred_html = df.to_html()

def home(request):
    context = {
        "todays_date": today,
        "pred_table": pred_html
    }
    return render(request, 'hello.html', context)


print(pred_html)


    
                    
