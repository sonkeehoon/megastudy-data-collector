'''

## utils.py

#### `crawler.py`를 보조하는 유틸리티 모듈입니다.

- `save_to_csv`: 데이터를 CSV 파일로 저장
- `extract_table_data`: 크롬 드라이버로 메가스터디 페이지의 표 데이터를 추출

사용 예:

`from utils import *`
`from utils import save_to_csv, extract_table_data`

'''
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def save_to_csv(target: pd.DataFrame, filename: str)-> None:
    '''
    지정된 `Pandas DataFrame` 데이터를 `CSV` 파일로 저장하는 함수
    '''
    target.to_csv(f'{filename}.csv', encoding="utf-8-sig")
    
def extract_table_data(driver: webdriver.Chrome) -> list:
    '''
    메가스터디 페이지에서 표 데이터를 추출하는 함수

    Parameters
    ----------
    driver : `webdriver.Chrome`
        - 크롬 웹드라이버 객체

    Returns
    -------
    list
        - 표 데이터를 `2차원 리스트 형태`로 반환
        - 각 원소는 표의 한 행(row)을 나타냄
    '''
    
    table = driver.find_element(By.CLASS_NAME, "tb_basic")
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []

    for row in rows[2:]:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells]
        if len(row_data) == 6:
            row_data += [""] * 4
        data.append(row_data)
        
    return data
