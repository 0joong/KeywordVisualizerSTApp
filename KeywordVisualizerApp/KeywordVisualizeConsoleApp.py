import lib.naverNewsCrawler as nnc
import lib.myTextMining as tm
from collections import Counter 
from konlpy.tag import Okt

keyword = input("검색어 : ").strip()
nnc.naverNewsAPICraw(keyword)
crawedList =  tm.load_corpus_from_csv(f"./data/{keyword}_naver_news.csv", "description")

tags = ['Noun', 'Adjective', 'Verb']
stopwords = ['가', '나']
tokenizer = Okt()

tokenList = tm.tokenize_korean_corpus(crawedList, tokenizer, tags, stopwords)

counter = tm.analyze_word_freq(crawedList, tokenizer, tags, stopwords)

tm.visualize_barchart(counter, "분석 결과", "빈도수", "키워드")

tm.visualize_wordcloud(counter)