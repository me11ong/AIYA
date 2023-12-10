from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def inside(request):
    
    return render(request,'./inside/inside.html')