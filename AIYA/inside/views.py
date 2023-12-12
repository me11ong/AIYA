from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import pandas as pd

# Create your views here.
def inside(request):
    data=pd.read_csv('./inside/ICW0W2000034.csv',encoding='utf-8')
    data=data[-23:]
    
    return render(request,'./inside/inside.html',{"data":data})

def inside_forecast(request):
    data=pd.read_csv('./inside/ICW0W2000034.csv',encoding='utf-8')
    data=data[-23:]
    
    return render(request,'./inside/inside_forecast.html',{"data":data})