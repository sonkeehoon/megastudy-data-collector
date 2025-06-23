'''

메가스터디의 수능/모의고사 역대 정답률과 난이도를 크롤링해서 수집해주는 코드입니다
- 링크 : https://www.megastudy.net/Entinfo/correctRate/main.asp?SubMainType=I&mOne=ipsi&mTwo=588
- 수집 기준 : 고3 시험
- 시행 연도 : 2016년부터 현재까지의 데이터

문제번호, 정답, 난이도, 배점, 정답률, 선지별 선택비율 등을 csv파일로 저장해줍니다

[사용한 라이브러리]
- megastudy_utils (사용자 정의 유틸리티)
- selenium (webdriver, By, Options)
- pandas

'''

from megastudy_utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

DELAY = 0.5
headers = ['번호', '정답', '난이도', '배점', '정답률', '선지1', '선지2', '선지3', '선지4', '선지5', '시험과목', '시험일', '시험구분']

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

data = pd.DataFrame(columns= headers)
data = data.astype({
    '번호' : 'int', '정답' : 'int', '난이도' : 'str', '배점' : 'int', '정답률' : 'str',
    '선지1' : 'str', '선지2' : 'str', '선지3' : 'str', '선지4' : 'str', '선지5' : 'str',
    '시험과목' : 'str', '시험일': 'str', '시험구분': 'str'
})

url = 'https://www.megastudy.net/Entinfo/correctRate/main.asp?SubMainType=I&mOne=ipsi&mTwo=588'
driver = webdriver.Chrome(options = chrome_options)
driver.get(url)
time.sleep(DELAY)

count = len(driver.find_element(By.ID, "examNmArea").find_elements(By.TAG_NAME, "li"))
print(count)

for i in range(count):
    time.sleep(DELAY)
    
    exam_area = driver.find_element(By.ID, "examNmArea")        # 매번 최신 DOM 추출
    lis = exam_area.find_elements(By.TAG_NAME, "li")            # li 목록 추출
    
    li = lis[i]
    text = li.text
    
    li.click()           # li 클릭
    time.sleep(DELAY)    # 로드 대기 (필요하면 변경)
    
    print(f"클릭 대상: {text}")
    
    
    math_button = driver.find_element(By.LINK_TEXT, "수학")
    math_button.click()

    time.sleep(DELAY)
    menu_div = driver.find_element(
        By.CLASS_NAME, 
        "searchSection--secondMenu")

    num_buttons = len(menu_div.find_elements(By.TAG_NAME, "a"))

    for j in range(num_buttons):
        time.sleep(DELAY)  # 페이지가 바뀔 시간을 줌

        # 클릭 시마다 새로 menu_div와 buttons를 다시 찾음
        menu_div = driver.find_element(By.CLASS_NAME, 
                                    "searchSection--secondMenu")
        buttons = menu_div.find_elements(By.TAG_NAME, "a")

        test_type = buttons[j].text
        print(f"클릭 중: {test_type}")

        buttons[j].click()
        time.sleep(DELAY)
        
        tbl_data = pd.DataFrame(extract_table_data(driver), columns = headers[:-3])
        tbl_data['시험과목'] = test_type
        tbl_data['시험일'], tbl_data['시험구분'] = text.split()[0], text.split()[1]
        print(tbl_data)
        
        data = pd.concat([data, tbl_data], ignore_index = True)
        
save_to_csv(data, '수학시험_데이터')
