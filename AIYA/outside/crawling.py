import requests 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
def get_pm25_index(html):
    
    soup=BeautifulSoup(html,"html.parser")

    pm25 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantPM2_5"})
    pm25_state=pm25.find('div',attrs={"class":"category"})
    pm25_state= pm25_state.text
    if pm25_state =='완벽함':
        pm25_state ='매우 좋음'
    pm25_data=pm25.find('div', attrs={"class":"column desktop-left"})
    pm25_val=pm25_data.find('div', attrs={"class":"pollutant-concentration"})
    pm25_score=pm25_data.find('div', attrs={"class":"pollutant-index"})
    pm25_val=pm25_val.text.split(" ")[0]+"µg/m³"
    
    return pm25_val,pm25_state,pm25_score.text

def get_pm10_index(html):
    
    soup=BeautifulSoup(html,"html.parser")


    pm10 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantPM10"})
    pm10_state=pm10.find('div',attrs={"class":"category"})
    pm10_state= pm10_state.text
    if pm10_state =='완벽함':
        pm10_state ='매우 좋음'
    pm10_data=pm10.find('div', attrs={"class":"column desktop-left"})
    pm10_val=pm10_data.find('div', attrs={"class":"pollutant-concentration"})
    pm10_score=pm10_data.find('div', attrs={"class":"pollutant-index"})
    pm10_val=pm10_val.text.split(" ")[0]+"µg/m³"
    
    return pm10_val,pm10_state,pm10_score.text

def get_no2_index(html):
    
    soup=BeautifulSoup(html,"html.parser")


    no2 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantNO2"})
    
    no2_state=no2.find('div',attrs={"class":"category"})
    no2_state= no2_state.text
    if no2_state =='완벽함':
        no2_state ='매우 좋음'
    no2_data=no2.find('div', attrs={"class":"column desktop-left"})
    no2_val=no2_data.find('div', attrs={"class":"pollutant-concentration"})
    no2_score=no2_data.find('div', attrs={"class":"pollutant-index"})
    no2_val=no2_val.text.split(" ")[0]+"µg/m³"
    
    return no2_val,no2_state,no2_score.text

def get_so2_index(html):
    
    soup=BeautifulSoup(html,"html.parser")


    so2 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantSO2"})
    
    so2_state=so2.find('div',attrs={"class":"category"})
    so2_state= so2_state.text
    if so2_state =='완벽함':
        so2_state ='매우 좋음'
    so2_data=so2.find('div', attrs={"class":"column desktop-left"})
    so2_val=so2_data.find('div', attrs={"class":"pollutant-concentration"})
    so2_score=so2_data.find('div', attrs={"class":"pollutant-index"})
    so2_val=so2_val.text.split(" ")[0]+"µg/m³"

    return so2_val,so2_state,so2_score.text

def get_o3_index(html):
    
    soup=BeautifulSoup(html,"html.parser")


    o3 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantO3"})
    
    o3_state=o3.find('div',attrs={"class":"category"})
    o3_state= o3_state.text
    if o3_state =='완벽함':
        o3_state ='매우 좋음'
    o3_data=o3.find('div', attrs={"class":"column desktop-left"})
    o3_val=o3_data.find('div', attrs={"class":"pollutant-concentration"})
    o3_score=o3_data.find('div', attrs={"class":"pollutant-index"})
    o3_val=o3_val.text.split(" ")[0]+"µg/m³"

    return o3_val,o3_state,o3_score.text

def get_co_index(html):
    
    soup=BeautifulSoup(html,"html.parser")


    pm10 = soup.find('div', attrs={"class":"air-quality-pollutant new-colors", "data-qa" : "airQualityPollutantCO"})
    pm10_state=pm10.find('div',attrs={"class":"category"})
    pm10_state= pm10_state.text
    if pm10_state =='완벽함':
        pm10_state ='매우 좋음'
    pm10_data=pm10.find('div', attrs={"class":"column desktop-left"})
    pm10_val=pm10_data.find('div', attrs={"class":"pollutant-concentration"})
    pm10_score=pm10_data.find('div', attrs={"class":"pollutant-index"})
    pm10_val=pm10_val.text.split(" ")[0]+"µg/m³"
    
    return pm10_val,pm10_state,pm10_score.text

def get_AQI_index(html):
    soup=BeautifulSoup(html,"html.parser")

    AQI = soup.find('div', attrs={"class": "aq-number-wrapper"})
    AQI_data = AQI.find('div', attrs={"class": "aq-number-container"})
    AQI_val = AQI_data.find('div', attrs={"class": "aq-number"})
    AQI_value = AQI_val.text.strip()
    
    return AQI_value

def get_AQI_state(html):
    soup=BeautifulSoup(html,"html.parser")

    AQI = soup.find('div', attrs={"class": "content-wrapper"})
    AQI_data = AQI.find('div', attrs={"class": "air-quality-data-wrapper"})
    AQI_state = AQI_data.find('p', attrs={"class": "category-text"})
    
    if AQI_state.text== "완벽함":
        return '매우좋음','대기질이 대부분의 사람들에게 적합합니다. 일상적인 야외 활동을 하기에 좋습니다.'
    
    elif AQI_state.text== "보통":
        return '보통','대기질이 대부분의 사람들에게 대체로 적합합니다. 그러나 장시간 노출될 경우 민감군은 경미하거나 중간 수준의 관련 증상을 보일 수 있습니다.'
    
    elif AQI_state.text== "나쁨":
        return "나쁨",'대기 오염이 심각한 상태이며 민감군에 유해합니다. 호흡 곤란이나 목 자극과 같은 증상이 발생할 경우 야외 활동 시간을 줄이시기 바랍니다.'
    
    elif AQI_state.text== "건강에 해로움":
        return "건강에 해로움",'민감군에 즉각적인 영향을 미칠 수 있으며 건강한 사람들도 장시간 노출될 경우 호흡 곤란이나 목 자극 같은 증세를 보일 수 있습니다. 야외 활동을 제한하시기 바랍니다.'
    
    elif AQI_state.text== "건강에 매우 해로움":
        return "건강에 매우 해로움","민감군은 즉각적인 영향을 받을 수 있기 때문에 야외 활동을 피해야 합니다. 건강한 사람들도 호흡 곤란이나 목 자극 같은 증세를 보일 수 있습니다. 실내 활동을 하거나 야외 활동의 시간을 조정하시기 바랍니다."
    
    else:
        return "위험","건강 상태에 관계없이 모든 사람이 단 몇 분이라도 공기에 노출될 경우 심각한 영향을 받을 수 있습니다. 야외 활동을 피하시기 바랍니다."