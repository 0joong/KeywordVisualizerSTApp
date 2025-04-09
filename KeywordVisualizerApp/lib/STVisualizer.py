import streamlit as st

st.title("영화 리뷰 텍스트 분석")

st.sidebar.header("파일 선택")
uploaded_file = st.sidebar.file_uploader("Drag and drop file here", type="csv")

if uploaded_file is not None:
    st.sidebar.write("파일명:", uploaded_file.name)

column_name = st.sidebar.text_input("데이터가 있는 컬럼명", value="review")
st.sidebar.button("데이터 파일 확인")

st.sidebar.header("설정")

show_freq_graph = st.sidebar.checkbox("빈도수 그래프", value=True)
freq_word_count = st.sidebar.slider("단어 수", min_value=10, max_value=50, value=20)

show_wordcloud = st.sidebar.checkbox("워드클라우드", value=True)
wordcloud_word_count = st.sidebar.slider("단어 수", min_value=20, max_value=500, value=50)

if st.sidebar.button("분석 시작"):
    st.info("분석 중입니다... (워드클라우드와 그래프는 이곳에 표시될 예정입니다.)")


