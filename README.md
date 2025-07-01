# Megastudy Data Collector

Megastudy의 **수능·모의고사 역대 정답률과 난이도**를 크롤링하여 수집해주는 도구입니다.

---

## 📝 개요
Megastudy 웹사이트로부터 **고3 시험** 기준 `2016년 ~ 현재`까지의 데이터를 크롤링하여 저장합니다.

### 수집되는 데이터 예시
- 문제번호
- 정답
- 난이도
- 배점
- 정답률
- 선지별 선택 비율 등

---

## 🔗 대상 링크
[Megastudy 정답률 페이지](https://www.megastudy.net/Entinfo/correctRate/main.asp?SubMainType=I&mOne=ipsi&mTwo=588)

---

## 🛠️ 개발 환경
- `Python 3.9.13`
- `OS: Windows`
## 📦 사용된 라이브러리
- `utils` (사용자 정의 유틸리티 모듈)
- `selenium` (`webdriver`, `By`, `Options` 등)
- `pandas`

---

## 📁 파일 구조
```
megastudy-data-collector/
├─ **crawler.py**        # 크롤러 메인 파일
├─ utils.py              # 유틸리티 함수 모음
├─ README.md             # 프로젝트 문서
├─ CHANGELOG.md          # 변경사항
├─ 수학시험_데이터.csv    # 크롤링 된 결과 데이터
```

## 🚀 설치 및 실행 방법

### 1️⃣ 저장소 클론
```bash
git clone https://github.com/sonkeehoon/megastudy-data-collector.git
cd megastudy-data-collector
```

### 2️⃣ 필요 라이브러리 설치 (설치 안돼있는 경우)
```bash
pip install selenium pandas
```

### 3️⃣ 크롤러 실행
```bash
python crawler.py
```

> 본 프로젝트는 Python 3.9.13 환경에서 개발되었으며, 웹 크롤링 및 데이터 처리 작업에 사용됩니다.
