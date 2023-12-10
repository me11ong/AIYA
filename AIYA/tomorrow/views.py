from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.http import HttpResponse
import pandas as pd
from django.contrib import messages
import re

def tomorrow_A(request):
    
    return render(request, './tomorrow/tomorrow_30s.html')

def tomorrow_B(request):
    
    return render(request, './tomorrow/tomorrow.html')