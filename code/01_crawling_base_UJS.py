from selenium import webdriver as wb
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.action_chains import ActionChains

# 마우스를 menu 요소 중앙으로 이동한 뒤 hidden_submenu 요소를 클릭하는 것을 실행


import re
import random
import time
import pandas as pd


def scroll():
    try:
        # 페이지 내 스크롤 높이 받아오기
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            # 임의의 페이지 로딩 시간 설정
            # PC환경에 따라 로딩시간 최적화를 통해 scraping 시간 단축 가능
            pause_time = random.uniform(0.,0.7)
            # 페이지 최하단까지 스크롤
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # 페이지 로딩 대기
            time.sleep(pause_time)
            # 무한 스크롤 동작을 위해 살짝 위로 스크롤(i.e., 페이지를 위로 올렸다가 내리는 제스쳐)
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight-50)")
            time.sleep(pause_time)
            # 페이지 내 스크롤 높이 새롭게 받아오기
            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
            # 스크롤을 완료한 경우(더이상 페이지 높이 변화가 없는 경우)
            if new_page_height == last_page_height:
                print("스크롤 완료")
                break

            # 스크롤 완료하지 않은 경우, 최하단까지 스크롤
            else:
                last_page_height = new_page_height

    except Exception as e:
        print("에러 발생: ", e)


# f-string
options = Options()
key_count = 0
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument('User-Agent=' + user_agent)
options.add_argument('lang=ko_KR')

# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

driver = wb.Chrome(options=options)

options.add_argument('--start-maximized')

search_list = ['고양시']
for list in search_list:
    base_url = 'https://map.naver.com/p/search/{} 음식점'.format(list)
    driver = wb.Chrome(options=options)

    try:
        driver.get(base_url)
        time.sleep(2)
    except:
        print('drivet.get')
        exit(1)
    iframe_element = driver.find_element(By.ID, "searchIframe")
    driver.switch_to.frame(iframe_element)
    time.sleep(0.5)
    res_list = driver.find_elements(By.CLASS_NAME,'UEzoS')


    reviews = []
    res_names=[]


    for list in res_list:   #식당명 가져와서 리뷰 가져오는 부분

        res_name = list.find_element(By.CLASS_NAME,'TYaxT').text
        res_names.append(res_name)    #음식점명 저장
        sample = list.find_element(By.CLASS_NAME, 'tzwk0')
        driver.execute_script("arguments[0].click();", sample)
        time.sleep(2)

        driver.switch_to.default_content()
        iframe_element = driver.find_element(By.ID, "entryIframe")
        driver.switch_to.frame(iframe_element)

        time.sleep(2)
        review_links  = driver.find_elements(By.CLASS_NAME, 'tpj9w')
        for link in review_links:
            if link.text == '리뷰':
                driver.execute_script("arguments[0].click();", link)

        time.sleep(2)
        #아래로 스크롤 후 더보기 클릭 가장 밑으로 내려간후에
        num=0
        for i in range(100):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(0.2)

            try:
                sample = driver.find_element(By.CLASS_NAME,'fvwqf')
                driver.execute_script("arguments[0].click();", sample)
            except:
                num+=1
                if num == 10:
                    break
                continue

        review_class = driver.find_elements(By.CLASS_NAME,'xHaT3')
        text = ' '

        for r_view in review_class:

            try:

                sample = r_view.find_element(By.CLASS_NAME,'rvCSr')

            except:

                text = text + ' ' + r_view.find_element(By.CLASS_NAME, 'zPfVt').text
                continue

            driver.execute_script("arguments[0].click();", sample)

            time.sleep(0.2)
            text = text + ' ' + r_view.find_element(By.CLASS_NAME, 'zPfVt').text


        reviews.append(text)
        # xHaT3(리뷰클래스)찾아서 더보기가 있으면 더보기 클릭 없으면 리뷰에 있는 텍스트 가져오기
        # zPfVt(리뷰)
        # rvCSr(리뷰더보기)

        driver.switch_to.default_content()
        iframe_element = driver.find_element(By.ID, "searchIframe")
        driver.switch_to.frame(iframe_element)
        print(res_names,reviews)
        time.sleep(0.2)




        # time.sleep(2)
        # sample =
        # driver.execute_script("arguments[0].click();", sample)
        # time.sleep(2)
        # scroll()






    #
    #
    # scroll()
    # movies=driver.find_elements(By.CLASS_NAME,"MovieItem")
    # print(len(movies))
    #
    # title_list=[]
    # href_list=[]
    # element_list=[]
    #
    #
    # time.sleep(2)
    #
    # for movie in movies: #영화리스트를 가져와서 해당 리스트의 영화제목  및 리뷰를 가져올 링크를 저장.
    #
    #     item = movie.find_element(By.TAG_NAME,'a')
    #     title = item.get_attribute('title')
    #     href  = item.get_attribute('href') + '/reviews'
    #     title_list.append(title)
    #     href_list.append(href)
    # df = pd.DataFrame({'titles':title_list,'href':href_list})
    # df.to_csv('./data/movie_href_data.csv',index=False)
    #
    # #