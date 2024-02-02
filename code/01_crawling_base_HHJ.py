#선언
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

#변수 선언
options = ChromeOptions()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')
options.add_argument('--blink-setting=imagesEnable=false') #이미지 미로딩
#options.add_argument('headless') #화면 제거

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)

#함수 선언
def restaurant_page_down():
    while(1):
        first_restaurant_list = driver.find_elements(By.CLASS_NAME, 'UEzoS')
        for list in first_restaurant_list:
            print(list.text)
        print(len(first_restaurant_list))
        action.move_to_element(first_restaurant_list[-1]).perform()
        time.sleep(0.5)
        last_restaurant_list = driver.find_elements(By.CLASS_NAME, 'UEzoS')
        print(len(last_restaurant_list))
        if first_restaurant_list == last_restaurant_list:
            return last_restaurant_list
        else:
            print('page down')
            continue
def restaurant_next_page():
    try:
        btn = driver.find_elements(By.CLASS_NAME, 'eUTV2')
        print(btn[1].get_attribute('aria-disabled'))
        if btn[1].get_attribute('aria-disabled') == 'false':
            btn[1].click()
        else:
            print('last page')
            return 0
    except:
        return 1

#리스트
locations = ['교하동', '금촌동', '동패동', '문발동', '서패동', '야당동']

#검색
for location in locations[:1]:
    url = 'https://map.naver.com/p/search/파주시 {} 식당'.format(location)
    driver.get(url)
    time.sleep(3)

    # 프레임 변경
    driver.switch_to.default_content()  # 프레임 초기화
    driver.switch_to.frame('searchIframe')  # 프레임 변경

    restaurant_page_down()

    print(restaurant_next_page())

    time.sleep(3)

    driver.close()