""" 댓글 및 조회수를 selenium 으로 불러와서 crawl.py와 합치려고 했으나 실패 """

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd


# chromedriver는 다운로드 후 경로 지정을 해줘야 한다. (현재는 같은 폴더 )
driver = webdriver.Chrome('./chromedriver/chromedriver')
driver.implicitly_wait(3)

#
base_url = 'https://blog.naver.com/tinyme76/222018371289'
# driver.get(base_url + '&search.menuid=***&search.page=***')
driver.get(base_url)


driver.switch_to_default_content # 상위 프레임으로 전환
driver.switch_to.frame('mainFrame') # cafe_main 프레임으로 전환

html = driver.page_source # 현재 페이지의 주소를 반환 
soup = bs(html, 'html.parser')

# 댓글수와 조회수를 찾는다     
reply_sort = soup.find_all('span', class_='ell')
for re in reply_sort :
    re = re.text
print(reply_sort)
