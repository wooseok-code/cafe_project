import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#url & driver.get
url = 'https://map.naver.com/p/search/파주시 음식점'
driver = webdriver.Chrome()
driver.get(url)

#화면 대기
time.sleep(5)

#프레임 변경
driver.switch_to.default_content() #프레임 초기화
driver.switch_to.frame('searchIframe') #프레임 변경

#검색
list_elements = driver.find_elements(By.CLASS_NAME, 'CHC5F')

#출력
for list in list_elements:
    print(list.text)

time.sleep(5)
driver.close()



