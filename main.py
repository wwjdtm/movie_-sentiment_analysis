from idlelib import browser
from webbrowser import Chrome
from selenium import webdriver
from pandas import Series, DataFrame
from konlpy.tag import Okt
import json
import os
from pprint import pprint
import time
from bs4 import BeautifulSoup


base_url = 'https://movie.naver.com/movie/bi/mi/point.nhn?code=38899'
browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
browser.get(base_url)

browser.switch_to.frame(browser.find_element_by_id('pointAfterListIframe'))

naver_movie = DataFrame({'star_score':[], 'review':[]})

for page in range(0,3):
    time.sleep(1)
    html0 = browser.page_source
    html1 = BeautifulSoup(html0,'html.parser')
    html2 = html1.find('div',{'class':'ifr_area basic_ifr'})
    review0 = html2.find('div',{'class':'score_result'}).find_all('li')

    for i in range(len(review0)):
        star_score = review0[i].find('div', {'class': 'star_score'}).find('em').text  # 별점
        review = review0[i].find('div', {'class': 'score_reple'}).find('p').text.replace("\n","").replace("\t","")  # 댓글

        insert_data = DataFrame({'star_score': [star_score],
                                    'review': [review]})
        naver_movie = naver_movie.append(insert_data)

        # 다음페이지로 넘어가기
    if page == 0:
        browser.find_elements_by_xpath('//*[@class = "paging"]/div/a')[10].click()
    else:
        browser.find_elements_by_xpath('//*[@class = "paging"]/div/a')[11].click()

naver_movie.index = range(len(naver_movie))
print(type(naver_movie))
print(naver_movie)
naver_movie['star_score'] = naver_movie['star_score'].astype('float32')
star_score_ls = naver_movie['star_score'].tolist()

print(star_score_ls)







