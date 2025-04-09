import urllib.request
import json

def searchNaverNews(keyword, start, display):
    client_id = "nKly6IUEZyUQuuI2Cuj0"
    client_secret = "qocZFrBFfJ"
    
    # 한글 검색어 안전하게 변환
    # encText = urllib.parse.quote("인공지능")
    encText = urllib.parse.quote(keyword)
    
    # url + query 생성
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과

    # request message 구성
    new_url = url + f"start={start}&display={display}"
    request = urllib.request.Request(new_url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    resultJSON = None

    try:
        # request -> response 받아오기
        response = urllib.request.urlopen(request)
            
        # 받아온 데이터가 정상인지 확인
        rescode = response.getcode()
        if(rescode==200):
            # 정상이면 데이터 읽어오기
            response_body = response.read()
            # 한글이 있으면 utf-8 decoding
            resultJSON = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    except Exception as e:
        print("Error :", new_url)
        
    return resultJSON

# JSON의 list를 dataframe으로 변환하여 csv 파일로 저장
def saveSearchResult_CSV(json_list, filename):
    import pandas as pd
    data_df = pd.DataFrame(json_list)
    data_df.to_csv(filename)
    print(filename, "SAVED")

#응답데이터를 리스트에 저장 (검색 결과는 json의 'items'에 들어 있음)
def setNewsSearchResult(resultAll, resultJSON):
    for result in resultJSON['items']:
        resultAll.append(result)


resultAll = []


# 첫 검색 API 호출
def naverNewsAPICraw(keyword):
    resultAll = []
    start = 1
    display = 10
    resultJSON = searchNaverNews(keyword, start, display)

    while (resultJSON != None) and (resultJSON['display'] > 0):
        # 응답데이터 정리하여 리스트 저장
        setNewsSearchResult(resultAll, resultJSON)

    
        # 다음 검색 API 호출을 위한 파라미터 조정
        start += resultJSON['display']

        # API 호출
        resultJSON = searchNaverNews(keyword, start, display)
        
        # API 호출 성공 여부 출력
        if resultJSON != None:
            print(keyword, start, " : Search Request Success")
        else:
            print(keyword, start, " : Error")
        

    # 리스트를 csv 파일로 저장
    filename = f"./data/{keyword}_naver_news.csv"
    saveSearchResult_CSV(resultAll, filename)