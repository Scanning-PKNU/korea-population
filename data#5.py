!pip install requests
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
tables = pd.read_html(res.text)

df = tables[4] 

#sns.set(font="AppleGothic")
sns.set(font="Malgun Gothic")
set_matplotlib_formats("retina")

df_recent = df.tail(10)

plt.figure(figsize=(6, 6))
plt.title("최근 10년간 출생자수 vs 사망자수 비율")
plt.pie(
    [df_recent["출생자수(명)"].sum(), df_recent["사망자수(명)"].sum()],
    labels=["출생자수", "사망자수"],
    autopct="%.1f%%",
    colors=["skyblue", "orange"]
)
plt.show()

plt.figure(figsize=(15, 6))
plt.title("연도별 추계인구 변화")
plt.xticks(rotation=60)
sns.lineplot(data=df, x="연도 (년)", y="추계인구(명)", marker="o", color="green")
plt.show()