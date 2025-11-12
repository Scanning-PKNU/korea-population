!pip install requests
import pandas as pd
import requests
# 위키백과 '대한민국의 인구' 페이지
url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
# HTML 테이블 불러오기
tables = pd.read_html(res.text)
print(len(tables))
print(tables[0])