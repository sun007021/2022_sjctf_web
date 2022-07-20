# parser.py
import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#chrome_options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
# 로그인할 유저정보
LOGIN_INFO = {
    'username': 'ssguser',
    'password': 'ssg@very#str0ng%pw!8213'
}
latest_num = 0

# Session 생성, with 구문 안에서 유지
while True:
    time.sleep(10)
    with requests.Session() as s:
        first_page = s.get('http://101.101.217.175:8213/users/login/')
        html = first_page.text
        soup = bs(html, 'html.parser')
        csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'}) # input태그 중에서 name이 csrfmiddlewaretoken가져옴
        print(csrf['value']) # 위에서 찾은 태그의 value를 가져옴

        # LOGIN_INFO에 csrf값을 추가
        LOGIN_INFO = {**LOGIN_INFO, **{'csrfmiddlewaretoken': csrf['value']}}
        try:
            # 로그인
            login_req = s.post('http://101.101.217.175:8213/users/login/', data=LOGIN_INFO)
            print(login_req.status_code)
            dic=s.cookies.get_dict()
            driver.get('http://101.101.217.175:8213/')
            for cookie, value in dic.items():
                 driver.add_cookie({
                    'name': cookie,
                    'value': value,
                 })
        except:
            continue
        while True:
            try:
                req = s.get('http://101.101.217.175:8213/board/commonboard/')
                html2 = req.text
                soup2 = bs(html2, 'html.parser')
                posts = soup2.find("tr", {"class":"list1"})
                post_num = posts.find("td", {"class":"num"}).text
                print(post_num)
                #새로운 글인지 확인
                if post_num != latest_num:
                    latest_num = post_num
                    print(latest_num)
                    link = 'http://101.101.217.175:8213/board/commonboard/'+post_num
                    driver.get(link)
                time.sleep(15)
            except:
                break
