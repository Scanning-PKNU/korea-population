import pandas as pd
df = pd.read_csv('Jeonbuk_person_data.csv', encoding="cp949")
df = pd.read_csv('data/GYEONGGI_SUWON_data.csv', encoding="cp949")
print(df.head())
