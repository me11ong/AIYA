from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import users
from django.http import HttpResponse
import pandas as pd
from django.contrib import messages
import re

# Create your views here.
def sign_up(request):
    data=pd.read_csv('./sign_up/Seoul.csv',encoding='utf-8')
    dictionary={
        'gu' : list(dict.fromkeys(data["gu"].drop_duplicates()))
    }
    if request.method == "GET":
        return render(request,'./sign_up/sign_up.html',dictionary)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        city = request.POST.get('city')
        gu = request.POST.get('gu')
        dong = request.POST.get('dong')

        if not username or not password or not re_password or not city or not gu or not dong:
            messages.error(request, "모든 정보를 입력해주세요.")
            return redirect('sign_up:sign_up')  # 회원가입 페이지로 리디렉션

        if not re.match("^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]+$", username):
            messages.error(request, "아이디를 영어와 숫자의 조합으로 입력해주세요.")
            return redirect('sign_up:sign_up')  # 회원가입 페이지로 리디렉션
        
        if password != re_password:
            messages.error(request, "비밀번호가 다릅니다. 다시 입력해주세요.")
            return redirect('sign_up:sign_up')  # 회원가입 페이지로 리디렉션
        
        user_info = users(
            username= username,
            password= password,
            city=city,  
            gu=gu,      
            dong=dong 
        )

        user_info.save()

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            #messages.success(request, "회원가입이 완료되었습니다.")
            return redirect('Home_page')
        
        return render(request, './sign_up/sign_up.html',dictionary)