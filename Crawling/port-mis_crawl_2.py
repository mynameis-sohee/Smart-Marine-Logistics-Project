from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


# 크롬 드라이버 지정
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("C:/Modules/chromedriver.exe")
driver.implicitly_wait(3)

# url에 접근
driver.get('https://new.portmis.go.kr/portmis/websquare/websquare.jsp?w2xPath=/portmis/w2/main/intro.xml')
driver.implicitly_wait(3)

# 시설조회 접근
btn = driver.find_element_by_id('mf_btnSiteMap')
btn.click()


# 선박입출항
btn = driver.find_element_by_id('mf_tacMain_contents_M0045_body_genMenuLevel1_1_genMenuLevel2_0_genMenuLevel3_1_btnMenuLevel3')
btn.click()

driver.implicitly_wait(10)


# 청(항) 코드 입력 
selected_tag=driver.find_element_by_css_selector('input#mf_tacMain_contents_M1319_body_udc_prtAgCd_cmmCd')
selected_tag.click()

time.sleep(1.5)
driver.implicitly_wait(10)
selected_tag.send_keys('820')

driver.implicitly_wait(10)
btn = driver.find_element_by_id('mf_tacMain_contents_M1319_body_btnSrch_btnSearch')
btn.click()


# 50000개씩 보기 선택
el = driver.find_element_by_id('mf_tacMain_contents_M1319_body_udcGridPageView2_sbxRecordCount_input_0')
for option in el.find_elements_by_tag_name('option'):
    if option.text == '50000개씩 보기':
        option.click()
        break

# 지정한 조건(청코드 820, 50000개씩 조회)으로 검색
driver.implicitly_wait(10)
btn = driver.find_element_by_id('mf_tacMain_contents_M1319_body_btnSrch_btnSearch')
btn.click()

driver.implicitly_wait(10)


# 스크롤 다운
btn = driver.find_element_by_id('mf_tacMain_contents_M1319_body_gridList2_cell_0_0')
btn.click()

save_dict={}
DOWN = '/ue015'
cnt = 0




# 마지막 페이지 테이블 데이터 집계 
def tail_value():
        for i in range(0,15):
            save_value = {}
            try:
                for k in range(0,2):
                    value = soup.select_one('#mf_tacMain_contents_M1319_body_gridList2_cell_{}_{} > nobr'.format(i, k)).text
                    save_value.setdefault('key_{}'.format(k), value)
                # print(save_value)
                save_dict['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), save_value['key_1'])] = save_value
            except AttributeError:
                break


# 데이터 수집
for _ in range(0,30):
    btn.send_keys(Keys.DOWN)
    save_value = {}
    for k in range(0,2):
        # 해당 페이지의 전체 html 소스를 string 형태로 답기 위해 html 저장 + 스크롤 다운한 화면을 동적화
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        value = soup.select_one('#mf_tacMain_contents_M1319_body_gridList2_cell_{}_{} > nobr'.format(0, k)).text
        # 키값이 없으면 키값에 0을 넣고 만약 있으면 키값을 반환
        save_value.setdefault('key_{}'.format(k), value)

    if 'n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), save_value['key_1']) in save_dict:
        cnt += 1

    if cnt > 15:
        tail_value()
        break

    save_dict['n_{}_{}'.format(datetime.datetime.now().strftime("%Y%m%d"), save_value['key_1'])] = save_value
print(save_dict)
