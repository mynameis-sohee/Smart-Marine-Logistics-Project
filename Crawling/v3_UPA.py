# 필요한 라이브러리 import
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

# 크롬 드라이버 통한 접속
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("C:/Modules/chromedriver.exe")
driver.implicitly_wait(3)

# 웹사이트 접속
driver.get('https://www.upa.or.kr/safe/pub/main/index.do')
driver.implicitly_wait(3)



# 울산본항 데이터 수집
table = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[1]/ol')
ul = table.find_elements_by_tag_name("li")

save_dict_1={}
for i in ul:
    save_dict_1['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), i.text[:6])] = i.text



# 온산항 데이터 수집
btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[2]/button')
btn.click()

table = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[2]/ol')
ul = table.find_elements_by_tag_name("li")

save_dict_2={}
for i in ul:
    save_dict_2['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), i.text[:6])] = i.text




# 울산신항 데이터 수집
btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[3]/button')
btn.click()

table = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[3]/ol')
ul = table.find_elements_by_tag_name("li")

save_dict_3={}
for i in ul:
    save_dict_3['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), i.text[:6])] = i.text




# 미포항 데이터 수집
btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[4]/button')
btn.click()

table = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[4]/ol')
ul = table.find_elements_by_tag_name("li")

save_dict_4={}
for i in ul:
    save_dict_4['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), i.text[:6])] = i.text


# 출력 - {'key값':'선석 당 데이터 (3개의 columns이 한 개의 데이터로 집계)}
print(save_dict_1)
print(save_dict_2)
print(save_dict_3)
print(save_dict_4)