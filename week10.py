import numpy as np
import pandas as pd
import seaborn as sns

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
# df = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df)
# print(df.describe())
# print(df.info())

# print(df['국'].value_counts()) # 만약 국을 7 6 7로 바꾸면 국의 7이 2개가 된다.
# print(len(df))
# print(df.shape) # 몇행 몇열?
# print(df['국'].nunique()) # columns 몇개 있음?
# print(df.dtypes) # int64, str 등의 행의 타입이 나온다.

# 데이터의 특정 비율 위치 값 계산 함수
# 기본은 50%이며 0.75(75%), 0.25(25%) 같은 방식으로 수치 조절 가능
# 10 20 30 40 50 <= 기준으로 본다면 0.75는 40, 0.25는 20 출력
# 이상치 탐구에도 많이 쓴다고 한다
# print(df.quantile()) 

# apply 사용 방법 1
# 지금의 방식은 값마다 제곱한 값을 리턴한다.
# def square(x):
#     return x * x
# print(df.apply(square)) # 이걸 고차 함수라고 부른다.

# apply 사용 방법 2
# 람다 방식이다. 일회용 함수라고 보면 된다.
# print(df.apply(lambda n: n * n))



# 7. Handling Missing Data
mpg = sns.load_dataset('mpg')

# print(mpg.describe())
# print(mpg.value_counts('cylinders')) # 기통별 개수
# print(mpg[mpg['horsepower'].isnull()], '\n') # null값인 행들만 출력

# 기통별 마력들의 중앙값을 구해서 결측치를 채운다.
mpg['horsepower'] = mpg['horsepower'].fillna(
    mpg.groupby('cylinders')['horsepower'].transform('median')
)
# print(mpg.info(), '\n')

# print(mpg[mpg['horsepower'].isnull()]) # 이제는 중앙값으로 채웠으므로 Empty DataFrame가 나온다.

# horsepower 컬럼에 일부 결측치 존재
# horsepower는 연비(mpg)와 음의 상관관계를 가지는 중요한 변수
# 수치형 변수라서 mean보다 median이 outlier(이상치)에 덜 민감하다.

# print(mpg.dropna())  # 결측치가 포함된 행 제거
# print(mpg.fillna(value))  # 평균, 중앙값 등으로 결측치 대체 가능

# 현재 결측치 비율이 2% 미만이므로 행 삭제(dropna)만으로도
# 전체 데이터 분석 결과에는 큰 영향이 없을 가능성이 높다.

# 다만 임의의 평균값 대체는 데이터 분포를 왜곡할 수 있으므로 주의가 필요하다.

# 만약 결측치 보존이 중요하다면,
# cylinders(기통 수) 기준으로 그룹화하여 중앙값으로 대체하는 방법이 더 안정적일 수 있다.
# => 같은 특성을 가진 차량끼리 값을 보정하므로 노이즈를 줄일 수 있음


# 이제 연비를 구하기 위한 필요없는 값들을 쳐내보자
# origin, name, model_year => 연비는 수치형으로 맞추기도 해야하고, 연식은 필요가 없다.
# print(mpg.sort_values('mpg', ascending=False)) # 전체 출력

mpg = mpg.drop(columns=['origin', 'name', 'model_year']) # 제조 국가, 차 이름, 연식을 삭제
print(mpg.info()) # 필요하면 fillna 전후로 로그 찍어서 확인해라
print(mpg.head())