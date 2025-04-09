import streamlit as st
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import lib.myTextMining as tm
import lib.naverNewsCrawler as nc
import os

st.title("키워드 기반 텍스트 시각화")

# --- 데이터 소스 선택 ---
data_source = st.radio("데이터 소스를 선택하세요", ("CSV 파일 업로드", "Naver 뉴스 검색"))

# session_state 초기화
if "df" not in st.session_state:
    st.session_state.df = None
if "column_name" not in st.session_state:
    st.session_state.column_name = None

# --- 1. CSV 업로드 ---
if data_source == "CSV 파일 업로드":
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        column_name = st.text_input("분석할 컬럼명", value="description")
        if column_name in df.columns:
            st.session_state.df = df
            st.session_state.column_name = column_name
            st.success(f"'{column_name}' 컬럼에서 텍스트를 분석합니다.")
        else:
            st.error(f"'{column_name}' 컬럼이 CSV에 존재하지 않습니다.")

# --- 2. 뉴스 검색 ---
else:
    keyword = st.text_input("검색어를 입력하세요")
    if keyword and st.button("뉴스 검색 및 수집"):
        st.info(f"🔄 '{keyword}' 뉴스 수집 중...")
        nc.naverNewsAPICraw(keyword)
        csv_path = f"./data/{keyword}_naver_news.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            if "description" in df.columns:
                st.session_state.df = df
                st.session_state.column_name = "description"
                st.success("뉴스 수집 및 데이터 로드 완료!")
            else:
                st.error("컬럼이 존재하지 않습니다.")
        else:
            st.error("뉴스 수집 실패 또는 파일이 존재하지 않습니다.")

# --- 분석 설정 (사이드바) ---
st.sidebar.header("설정")

show_freq_graph = st.sidebar.checkbox("빈도수 그래프", value=True)
freq_word_count = st.sidebar.slider("단어 수", min_value=10, max_value=50, value=20)

show_wordcloud = st.sidebar.checkbox("워드클라우드", value=True)
wordcloud_word_count = st.sidebar.slider("단어 수", min_value=20, max_value=500, value=50)

analyze_button = st.sidebar.button("분석 시작")

# --- 분석 실행 ---
if analyze_button:
    if st.session_state.df is None or st.session_state.column_name is None:
        st.error("분석할 데이터가 없습니다. CSV를 업로드하거나 키워드를 검색하세요.")
    else:
        st.info("텍스트 분석 중입니다...")

        df = st.session_state.df
        column_name = st.session_state.column_name

        corpus_list = list(df[column_name])
        tokenizer = Okt()
        tags = ['Noun', 'Adjective', 'Verb']
        stopwords = ['가', '나']  # 기본 불용어

        token_list = tm.tokenize_korean_corpus(corpus_list, tokenizer, tags, stopwords)
        counter = Counter(token_list)

        if show_freq_graph:
            st.subheader("단어 빈도수")
            top_counter = Counter(dict(counter.most_common(freq_word_count)))
            tm.visualize_barchart(top_counter, "단어 빈도수", "빈도수", "단어")

        if show_wordcloud:
            st.subheader("워드클라우드")
            top_counter = Counter(dict(counter.most_common(wordcloud_word_count)))
            tm.visualize_wordcloud(top_counter)

