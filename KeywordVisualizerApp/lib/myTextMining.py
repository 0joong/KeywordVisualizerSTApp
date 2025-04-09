from collections import Counter

def load_corpus_from_csv(corpus_file, col_name):
    import pandas as pd
    data_df = pd.read_csv(corpus_file)
    result_list = list(data_df[col_name])
    return result_list


def tokenize_korean_corpus(corpus_list, tokenizer, tags, stopwords):
    
    text_pos_list = [] 
    for text in corpus_list:
        text_pos = tokenizer.pos(text)
        text_pos_list.extend(text_pos)
    token_list = [token for token, tag in text_pos_list if tag in tags and token not in stopwords]
    return token_list


def analyze_word_freq(corpus_list, tokenzier, tags, stopwords):
    token_list = tokenize_korean_corpus(corpus_list, tokenzier, tags, stopwords)
    counter = Counter(token_list)
    return counter


def visualize_barchart(counter, title, xlable, ylable):
    # 데이터 준비
    most_common = counter.most_common(20)
    word_list = [word for word, count in most_common]
    count_list = [count for word, count in most_common]
    
    # 한글 폰트 설정하기
    from matplotlib import font_manager, rc
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)


    # 수평 막대그래프
    import matplotlib.pyplot as plt
    plt.barh(word_list[::-1], count_list[::-1])
    # 그래프 정보 추가 
    plt.title(title)
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    import streamlit as st
    st.pyplot()
    # 화면에 출력
    plt.show()


def visualize_wordcloud(counter):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # 한글 폰트 path 지정
    font_path = "c:/Windows/fonts/malgun.ttf"

    # WordCloud 객체 생성
    wordcloud = WordCloud(font_path
                        ,width=600
                        ,height=400
                        ,max_words=50
                        ,background_color='ivory')
    
    # 전체 텍스트로 워드클라우드 시각화
    wordcloud = wordcloud.generate_from_frequencies(counter)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    import streamlit as st
    st.pyplot() 

def visualize_barchart_web(counter, title, xlable, ylable, max_words=20):
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    import streamlit as st

    # 데이터 준비
    most_common = counter.most_common(max_words)
    word_list = [word for word, count in most_common]
    count_list = [count for word, count in most_common]

    # 한글 폰트 설정
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    # 🔧 안전한 figure 객체 생성
    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])
    ax.set_title(title)
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylable)

    # ✅ Streamlit에 렌더링
    st.pyplot(fig)


def visualize_wordcloud_web(counter, max_words=50):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import streamlit as st

    font_path = "c:/Windows/Fonts/malgun.ttf"

    # WordCloud 객체 생성
    wordcloud = WordCloud(
        font_path=font_path,
        width=600,
        height=400,
        max_words=max_words,
        background_color='ivory'
    ).generate_from_frequencies(counter)

    # 🔧 안전한 figure 객체 생성
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    # ✅ Streamlit에 렌더링
    st.pyplot(fig)
