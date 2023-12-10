from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import pandas as pd
import requests 
from sign_up.models import users
from .crawling import get_pm25_index,get_pm10_index,get_no2_index,get_so2_index,get_o3_index,get_AQI_index,get_AQI_state,get_co_index
from .crawling_health import get_running,get_cycle,get_hiking,get_drive
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Create your views here.
def outside(request):
    data=pd.read_csv('./outside/Seoul.csv',encoding='utf-8')
    dictionary={
        'gu' : list(dict.fromkeys(data["gu"].drop_duplicates()))
    }
    if request.method == "GET":
        print("1")
        return render(request,'./outside/outside.html',dictionary)
        
    elif request.method == "POST":
        
        gu = request.POST.get('gu')
        dong = request.POST.get('dong')
        
        code=int(data.loc[(data['gu']== gu) & (data['dong']== dong)]["code"].iloc[0])
        url="https://www.accuweather.com/ko/kr//{:d}/air-quality-index/{:d}".format(code,code)
        
        print(url)
        
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.headless=True
        
        #chrome_options=webdriver.ChromeOptions()
        #chrome_options.headless=True
        
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=edge_options)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        render(request,'./outside/loading.html')
        
        driver.get(url)
        
        now_url=driver.current_url
        
        driver.find_element(By.XPATH,'//*[@id="view-more-pollutants"]').click()

        html = driver.page_source
        
        pm25_val,pm25_state,pm25_score=get_pm25_index(html)
        pm10_val,pm10_state,pm10_score=get_pm10_index(html)
        no2_val,no2_state,no2_score=get_no2_index(html)
        so2_val,so2_state,so2_score=get_so2_index(html)
        o3_val,o3_state,o3_score=get_o3_index(html)
        co_val,co_state,co_score=get_co_index(html)
        AQI=get_AQI_index(html)
        AQI_state,solution=get_AQI_state(html)
        
        
        url2="https://www.accuweather.com/ko/kr/{:s}/{:d}/health-activities/{:d}".format(now_url.split("/")[5],code,code)
        
        running=get_running(url2)
        cycle=get_cycle(url2)
        hiking=get_hiking(url2)
        drive=get_drive(url2)
        
        center_latitude=float(data[data["dong"]==dong]["lat"])
        center_longitude=float(data[data["dong"]==dong]["lng"])
        
                
        return render(request,'./outside/result.html'
        ,{'gu':gu,'dong':dong, 'pm25_val': pm25_val,'pm10_val': pm10_val,'no2_val': no2_val,'so2_val': so2_val,'o3_val':o3_val,'co_val':co_val,
            'pm25_state':pm25_state,'pm10_state':pm10_state, 'no2_state':no2_state,'so2_state':so2_state,'o3_state':o3_state,'co_state':co_state,
            'pm25_score':pm25_score,'pm10_score':pm10_score, 'no2_score':no2_score,'so2_score':so2_score,'o3_score':o3_score,'co_score':co_score,
            "AQI":AQI,"AQI_state":AQI_state,"solution":solution,
            "running":running,"cycle":cycle,"hiking":hiking,"drive":drive,
            'center_latitude': center_latitude, 'center_longitude': center_longitude})