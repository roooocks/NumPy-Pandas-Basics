import pandas as pd
import seaborn as sns

# 1. 10주차 일부 복습
mpg = sns.load_dataset('mpg')
# print(mpg['model_year'].value_counts().sort_values(ascending=False))
# print(mpg.sort_values('model_year', ascending=False)) # mpg로 하면 연비가 높은 차량부터 나온다.

# mpg = sns.load_dataset('mpg')
# mpg = mpg.drop(columns=['origin', 'name', 'model_year'])
# print(mpg[mpg['horsepower'].isnull()], '\n')



# 2. exercise 데이터 시트 연습
ex = sns.load_dataset('exercise')

# print(ex.head(10))
# print(ex.info())

# print(ex['kind'].value_counts()) # 3가지 30개
# print(ex['time'].value_counts()) # 3가지 30개
# print(ex['diet'].value_counts()) # 2가지 45개



# 3.



# 4.



# 5. 