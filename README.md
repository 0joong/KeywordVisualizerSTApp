# Keyword Text Visualizer

텍스트 데이터를 분석하고 시각화할 수 있는 **Python 기반 텍스트 마이닝 도구**입니다. Naver 뉴스 데이터를 크롤링하거나 CSV 파일을 업로드하여 **단어 빈도수 그래프와 워드클라우드**를 생성할 수 있습니다.

## 프로젝트 구성
project_root/ │ ├── data/ # 크롤링된 뉴스 CSV 저장 경로 │ ├── lib/ # 분석 라이브러리 및 크롤러 코드 │ ├── myTextMining.py # 텍스트 전처리 및 시각화 함수 │ └── naverNewsCrawler.py # 네이버 뉴스 API 크롤러 │ ├── KeywordVisualizeConsoleApp.py # 콘솔 기반 텍스트 분석 도구 ├── KeywordVisualizerSTApp.py # Streamlit 기반 웹 분석 앱 └── STVisualizer.py # 영화 리뷰 데이터 분석용 웹 앱 템플릿
    

---

## 🔧 주요 기능

| 기능 | 설명 |
|------|------|
| **네이버 뉴스 검색** | 키워드 기반 뉴스 수집 (네이버 오픈 API 사용) |
| **CSV 업로드** | 사용자 CSV 파일에서 텍스트 분석 |
| **형태소 분석** | Okt 형태소 분석기를 사용하여 명사, 형용사, 동사 추출 |
| **단어 빈도수 시각화** | 수평 막대 그래프로 주요 키워드 시각화 |
| ☁**워드클라우드 생성** | 빈도 기반 워드클라우드 생성 |
| **Streamlit 인터페이스** | 웹 기반 GUI로 손쉬운 사용 가능 |

---

## 실행 방법

### 1. 콘솔 앱 실행

```bash
python KeywordVisualizeConsoleApp.py
