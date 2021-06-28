import urllib.request
from bs4 import BeautifulSoup

url='https://www.google.com'
soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
a_tags = soup.find_all('a')
result_list = []
for i in a_tags:
    result_list.append(i.get_text())
print(result_list)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("C:/Modules/chromedriver.exe")
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://new.portmis.go.kr/portmis/websquare/websquare.jsp?w2xPath=/portmis/w2/main/intro.xml')
driver.implicitly_wait(3)

btn = driver.find_element_by_id('mf_btnSiteMap')
btn.click()

driver.implicitly_wait(10)

btn = driver.find_element_by_id('mf_tacMain_contents_M0045_body_genMenuLevel1_1_genMenuLevel2_1_genMenuLevel3_1_btnMenuLevel3')
btn.click()

driver.implicitly_wait(10)
# 항코드 입력 ㅠㅠ드디어 됐다.
selected_tag=driver.find_element_by_css_selector('input#mf_tacMain_contents_M1554_body_srchPrtAgCd')
selected_tag.click()

time.sleep(1.5)
driver.implicitly_wait(10)
selected_tag.send_keys('820')

driver.implicitly_wait(10)
btn = driver.find_element_by_id('mf_tacMain_contents_M1554_body_udcSearchList_btnSearch')
btn.click()

driver.implicitly_wait(10)

# 50000개씩 보기 선택
el = driver.find_element_by_id('mf_tacMain_contents_M1554_body_udcGridPageView_sbxRecordCount_input_0')
for option in el.find_elements_by_tag_name('option'):
    if option.text == '50000개씩 보기':
        option.click() # select() in earlier versions of webdriver
        break

driver.implicitly_wait(10)
btn = driver.find_element_by_id('mf_tacMain_contents_M1554_body_udcSearchList_btnSearch')
btn.click()

driver.implicitly_wait(10)

btn = driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_0')
btn.click()




stg_list=[{'num':'-1231'}]
DOWN = '/ue015'
for _ in range(0,15):
    num=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_0').text

    if stg_list[-1]['num'] == num:
        btn.send_keys(Keys.DOWN)
        continue

    subnum=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_1').text
    entry_yr=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_2').text
    entry_num=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_3').text
    use_num=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_4').text
    ton=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_5').text
    ship_name=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_6').text
    brch_code=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_7').text
    brch_name=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_8').text
    apfac_code=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_9').text
    apfac_subcode=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_10').text
    apfac_name=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_11').text
    app_from=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_12').text
    app_to=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_13').text
    asfac_code=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_14').text
    acfac_subcode=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_15').text
    asfac_name=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_16').text
    ass_from=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_17').text
    ass_to=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_18').text
    purp=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_19').text

    dataset = {'num':num, 'subnum':subnum, 'entry_yr':entry_yr, 'entry_num':entry_num, 'use_num':use_num, 'ton':ton, 'ship_name':ship_name,
    'brch_code':brch_code, 'brch_name':brch_name, 'apfac_code':apfac_code, 'apfac_subcode':apfac_subcode,'apfac_name':apfac_name, 'app_from':app_from,
     'app_to':app_to, 'asfac_code':asfac_code, 'acfac_subcode':acfac_subcode, 'asfac_name':asfac_name, 'ass_from':ass_from, 'ass_to':ass_to, 'purp':purp}
    
    stg_list.append(dataset)
    btn.send_keys(Keys.DOWN)

print(stg_list)

const mongoose = require('mongoose');
const MONGODB_URI = process.env.MONGODB_URI;


# 순차적으로 리스트안에 저장하는 코드    
# stg_list=[-100]
# DOWN = '/ue015'
# for _ in range(0,15):
#     result=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_0') 
#     if stg_list[-1] == result.text:
#         btn.send_keys(Keys.DOWN)
#         continue
#     stg_list.append(result.text)
#     btn.send_keys(Keys.DOWN)
#     print(stg_list)



# 순차적으로 데이터가 집계되는 방법
# DOWN = '/ue015'
# for _ in range(0,310):
#     result=driver.find_element_by_id('mf_tacMain_contents_M1554_body_grpSrchList_cell_0_0') 
#     print(result.text)
#     btn.send_keys(Keys.DOWN)

# 해당 페이지의 전체 html 소스를 string 형태로 답기 위해 html 저장
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# for i in range(0,10):
#     for k in range(0,10):
#         table = soup.select('#mf_tacMain_contents_M1554_body_grpSrchList_cell_{}_{} > nobr'.format(i, k)).text()
#         print(table)
    