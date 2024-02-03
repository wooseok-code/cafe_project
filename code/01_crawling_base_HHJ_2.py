#선언
import time
import re
import pandas as pd
import datetime
import numpy as np
import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

#함수선언

#검색어
locations = ['교하동', '금촌동', '동패동', '문발동', '서패동', '야당동']

#변수선언
location_num = 0
page_num = 0
restaurant_num = 0

#저장된 데이터 선별 데이터 불러오기
data_paths = glob.glob('../data_naver/naver*HHJ.csv')
print(data_paths)

#저장된 데이터 선별
for location in locations:
    for i in range(6):
        for j in range(50):
            if '../data_naver\\naver_data_{}_{}_{}_HHJ.csv'.format(location, i, j) in data_paths:
                location_num = locations.index(location)
                page_num = i
                restaurant_num = j
            else:
                break
print(location_num, page_num, restaurant_num)