import pandas as pd
# 위키백과 '대한민국의 인구' 페이지
url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC"
# URL 출력
print("가져올 주소:", url)
# HTML 테이블 불러오기
tables = pd.read_html(url)
# 몇 개의 테이블이 있는지 확인
print("총 {len(tables)}개의 테이블을 불러왔습니다.")
# 첫 번째 테이블 출력
print("\n[첫 번째 테이블 미리보기]")
print(tables[0].head())