!pip install requests
import pandas as pd
import requests
url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC"
url
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers) 

tables = pd.read_html(res.text)
print(len(tables))

df = tables[4] #tables[0]:지역별 인구밀도 tables[4]:연도별 인구,출생,사망 통계 tables[11] 최신 인구 현황
df.shape

df.head()

df.tail()

import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(font="AppleGothic")
sns.set(font="Malgun Gothic")
from IPython.display import set_matplotlib_formats
set_matplotlib_formats("retina")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.pointplot(data = df, x="연도 (년)", y="추계인구(명)")
plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.lineplot(data = df, x="연도 (년)", y="추계인구(명)")

df

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.pointplot(data = df, x="연도 (년)", y="출생자수(명)")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.lineplot(data = df, x="연도 (년)", y="출생자수(명)")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.pointplot(data = df, x="연도 (년)", y="사망자수(명)")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.lineplot(data = df, x="연도 (년)", y="사망자수(명)")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.lineplot(data = df, x="연도 (년)", y="사망자수(명)")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.pointplot(data = df, x="연도 (년)", y="출생자수(명)")
sns.pointplot(data = df, x="연도 (년)", y="사망자수(명)")

df_pop = df[["연도 (년)", "출생자수(명)", "사망자수(명)"]]
df_pop = df_pop.set_index("연도 (년)")
df_pop.head()

df_pop.plot(figsize=(15, 4))

df_pop[-50:].plot()

df_pop[-50:].plot(figsize=(15, 8))

plt.figure(figsize=(15, 8))
plt.xticks(rotation=60)
sns.pointplot(data=df[-50:], x="연도 (년)", y="출생자수(명)")
sns.pointplot(data=df[-50:], x="연도 (년)", y="사망자수(명)", color="orange")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=60)
sns.barplot(data=df, x="연도 (년)", y="추계인구(명)", palette="Blues")