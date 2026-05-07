import numpy as np
import pandas as pd

# 1. Subset Variables - columns



# 2. Logic in Python(and pandas)



# 3. 1번의 filter에 사용하는 regex(정규 표현식)
#   - regex (Regular Expressions) Examples
# df_dict = pd.DataFrame({'국': ["1", "6", "7"], '영': ["2", "4", "8"], '수': ["3", "5", "9"], '화': ["10", "3", "1"]}, index=[1, 2, 3])
# print(df_dict)

# print(df_dict.iat[0, 1])
# df_dict.iat[0, 1] = "23"
# print(df_dict.filter(regex='[2-3]$'))


# 4. Group Data



# 5. Combine Data Sets
# df1 = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8]}, index=[1, 2, 3])
# df2 = pd.DataFrame({'국': [9, 6, 17], '수': [3, 5, 9]}, index=[1, 2, 4])

# print(pd.merge(df1, df2, how='left', on='국'))

# '국' 컬럼의 값이 같은 행끼리 병합된다.
# df1과 df2 모두 '국=6'이 존재하므로 df1의 '영=4' 값이 함께 출력된다.
# 병합 결과에 NaN이 포함되면 정수형 컬럼이 실수형(float)으로 변환되므로 4가 4.0으로 표시된다.
# print(pd.merge(df1, df2, how='right', on='국')) # 국의 중간 값을 df2 기준 6과 -1로 순서대로 바꿔보자

# print(pd.merge(df1, df2, how='left', on='국'))



# 6. Summarize Data
# describe(표준편차, 분산 등), info(결치값 개수, 행/열 몇개 등)를 많이 쓴다.
df = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
print(df)
# print(df.describe())
# print(df.info())

# print(df['국'].value_counts()) # 만약 국을 7 6 7로 바꾸면 국의 7이 2개가 된다.
# print(len(df))
# print(df.shape) # 몇행 몇열?
# print(df['국'].nunique()) # columns 몇개 있음?
print(df.dtypes) # int64, str 등의 행의 타입이 나온다.