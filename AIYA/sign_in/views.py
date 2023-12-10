from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def sign_in(request):
    
    return render(request,'./sign_in/sign_in.html')