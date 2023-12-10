import requests 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from lxml import etree 
 
def get_running(url):
    #산책, 달리기
    res=requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    dom = etree.HTML(str(soup))
    index_data=dom.xpath('/html/body/div[1]/div[6]/div/div/div[2]/div[2]/div[3]/a[2]/div[4]')[0]
    
    return(index_data.text)

def get_cycle(url):
    #자전
    res=requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    dom = etree.HTML(str(soup))
    index_data=dom.xpath('/html/body/div[1]/div[6]/div/div/div[2]/div[2]/div[3]/a[4]/div[4]')[0]
    
    return(index_data.text)


def get_hiking(url):
    #등산
    res=requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    dom = etree.HTML(str(soup))
    index_data=dom.xpath('/html/body/div[1]/div[6]/div/div/div[2]/div[2]/div[3]/a[7]/div[4]')[0]
    
    return(index_data.text)


def get_drive(url):
    #운전
    res=requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    dom = etree.HTML(str(soup))
    index_data=dom.xpath('/html/body/div[1]/div[6]/div/div/div[4]/div[2]/div[3]/a[2]/div[4]')[0]
    
    return(index_data.text)

