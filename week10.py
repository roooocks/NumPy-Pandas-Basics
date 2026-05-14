import numpy as np
import pandas as pd
import seaborn as sns

# 1. Subset Variables - columns(열)
# 수업 시간에 연습은 안했다. 원하는 열 출력
# df = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df)

# print(df[['국', '수']]) # 국, 수의 열만 출력한다.
# print(df['국']) # or df.국 / 하나만 하면 열의 이름은 나오지 않는다.
# print(df.filter(regex='국')) # 컬럼 혹은 인덱스 이름 필터용이다. 다만 인덱스는 axis=0 혹은 axis='index' 필요



# 2. Logic in Python(and pandas)
# 수업 시간에 연습은 안했다. 각종 비교식의 함수 버전 소개
# df = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df)

# print(df['수'] >= 5) # 비교 연산자
# print(df[(df['국'] + df['영']) > 10])
# print(df[df['화'] == 3]) # equals (==)
# print(df[df['영'] != 4]) # not equals (!=)
# print(df['수'].isin([3, 5, 9])) # isin (그룹 포함 여부)
# print(df[df['국'].isin([1, 7])], '\n')

# 여기서부턴 결측치 확인 (isnull, notnull)
# df2 = df.copy()
# df2.loc[2, '영'] = None # 결측값 생성
# print(df2)
# print(df2.isnull()) # 결측값 여부 확인
# print(df2.notnull()) # 결측값이 아닌 데이터만 True
# print(df2.dropna(), '\n') # 결측값이 있는 행 제거

# 여기서부턴 논리 연산 (and / or / not)
# print(df[(df['국'] >= 6) & (df['수'] >= 5)]) # 국 >= 6 AND 수 >= 5
# print(df[(df['국'] == 1) | (df['화'] == 1)]) # 국 == 1 OR 화 == 1
# print(df[~(df['국'] >= 6)]) # NOT 조건 (국이 6 이상이 아닌 행)



# 3. 1번의 filter에 사용하는 regex(정규 표현식)
#   - regex (Regular Expressions) Examples
#   - 그냥 쓰면(axis=1) 컬럼을 찾게 된다. 인덱스는 axis=0을 써야한다.
#   - 만약 정규화 안쓰고 다르게 쓸거면 items(정확한 이름 선택), like(문자열 포함)이 존재한다.
# df_dict = pd.DataFrame({'국': ["1", "6", "7"], '영': ["2", "4", "8"], '수': ["3", "5", "9"], '화': ["10", "3", "1"]}, index=[1, 2, 3])
# print(df_dict)

# print(df_dict.iat[0, 1])
# df_dict.iat[0, 1] = "23"
# print(df_dict.filter(regex='[1-2]$', axis=0))



# 4. Group Data
# df = pd.DataFrame({
#     '국': [2, 6, 7], # 1, 6, 7
#     '영': [2, 4, 8],
#     '수': [3, 5, 9],
#     '화': [3, 10, 1] # 10, 3, 1
# }, index=[1, 2, 3])

# print("=== 원본 데이터 ===")
# print(df, '\n')

# print(df.groupby(by="국")['영'].mean()) # SQL의 GROUP BY column과 같다.
# print(df.groupby(level="ind")) # 위와 같으나 인덱스 기준으로 그룹화. 때문에 계층형 인덱스(MultiIndex)일 때만 의미있다.

# print(df.groupby('화').size()) # 컬럼 '화' 기준 행 개수 계산
# print(df.groupby('화').agg('mean')) # 컬럼 '화' 기준 각 컬럼의 평균 계산
# print(df.groupby('화').agg(['sum', 'mean'])) # 중복도 가능으로 한 컬럼 아래 sum, mean 컬럼이 생기고 거기에 맞게 값이 생긴다.

# print(df['국'].shift(1)) # 1 칸 아래로 이동 (이전 값 보기)
# print(df['국'].shift(-1)) # -1 칸 위로 이동 (다음 값 보기)

# rank는 기본적으로 낮은 숫자가 1등 (오름차순, ascending=True)
# print(df['화'].rank(method='dense')) # 동점이어도 순위를 건너뛰지 않음
# print(df['화'].rank(method='min')) # 동점이면 가장 작은 순위 부여
# print(df['화'].rank(pct=True)) # 백분율 순위(내 순위 / 전체 개수). 여기서 나오는 값이 작으면 1등. 1.0에 가까울 수록 큰 백분율이 된다.
# print(df['화'].rank(method='first')) # 먼저 나온 순서대로 순위 부여 (동일 값도 순서대로 순위를 매긴다.)

# print(df['국'].cumsum()) # 누적합 (1: 1, 2: 7(1 + 6), 3: 14(7 + 7))
# print(df['화'].cummax()) # 누적 최대값. 이름이 이상한데, 그냥 컬럼 읽어가면서 가장 큰 값을 갱신한다.
# print(df['화'].cummin()) # 누적 최소값. 위와 같음
# print(df['국'].cumprod()) # 누적곱 (2, 2*6, 2*6*7)



# 5. Combine Data Sets
# df1 = pd.DataFrame({
#     '국': [2, 6, 7],
#     '영': [2, 4, 8]
# }, index=[1, 2, 3])

# df2 = pd.DataFrame({
#     '국': [2, 6, 9],
#     '수': [3, 5, 9]
# }, index=[1, 2, 4])

# print("=== 원본 데이터 ===")
# print(df1)
# print(df2, '\n')

# 병합 결과에 NaN이 포함되면 정수형 컬럼이 실수형(float)으로 변환
# print(pd.merge(df1, df2, on='국', how='inner')) # 공통으로 존재하는 값만 합침
# print(pd.merge(df1, df2, on='국', how='left')) # 왼쪽(df1) 기준 모두 유지. 유지가 안되는건 공통 존재값이 아니라서 그렇다.(NaN)
# print(pd.merge(df1, df2, on='국', how='right')) # 오른쪽(df2) 기준 모두 유지. 유지 못하는건 위와 같다.
# print(pd.merge(df1, df2, on='국', how='outer')) # 모든 값 전부 포함. NaN은 위와 같은 이유

# print(df1.국.isin(df2.국)) # df1 '국' 값이 df2 '국' 안에 있는지 검사 (boolean)
# print(df1[df1.국.isin(df2.국)]) # 위의 값을 기준으로 공통 데이터 조회
# print(df1[~df1.국.isin(df2.국)]) # 위의 값을 기준으로 없는 데이터 조회



# 6. Summarize Data
# df = pd.DataFrame({
#     '국': [2, 6, 7], # 1, 6, 7
#     '영': [2, 4, 8],
#     '수': [3, 5, 9],
#     '화': [3, 10, 1] # 10, 3, 1
# }, index=[1, 2, 3])

# print("=== 원본 데이터 ===")
# print(df, '\n')

# print(df['국'].value_counts()) # 값별 개수 세기. 만약 국을 7 6 7로 바꾸면 국의 7이 2개가 된다.
# print(len(df)) # 행 개수 확인. 여기선 3만 나옴
# print(df.shape) # 몇행 몇열? (3, 4)
# print(df['국'].nunique()) # 고유값 개수. columns 몇개 있음?
# print(df.dtypes) # int64, str 등의 컬럼의 자료형이 나온다.

# describe(표준편차, 분산 등), info(결치값 개수, 행/열 몇개 등)를 많이 쓴다.
# 용어들이 너무 어려워서 길게 설명한다.
# 기초 통계(량) 요약 
# print(df.describe())
#  - count(개수)
#  - mean(평균)
#  - std(표준편차) => 데이터가 평균으로부터 얼마나 멀리 흩어져 있는지(변동성)를 나타내는 지표, 이 값이 클수록 데이터의 격차가 크고 들쭉날쭉
#  - min => 컬럼에서 가장 작은 값
#  - 25%(1사분위수, Q1) => 데이터를 크기순으로 정렬했을 때, 하위 25% 위치에 있는 값 / 예: 100명 중 뒤에서 25등의 성적입니다.
#  - 50%(2사분위수, 중앙값, median) => 위와 같은데 정중앙(50%) 위치에 있는 값 / mean과 다르게 극단적인 값(큰, 작은)에 영향을 받지 않는다.
#  - 75%(3사분위수, Q3) => 위와 같은데 하위 75%(즉, 상위 25%) 위치에 있는 값
#  - max => 컬럼에서 가장 큰 값

# 데이터 구조 확인
# print(df.info())
# - 맨 위
#  - Index: 3 entries, 1 to 3 => 전체 행(Row)의 개수와 인덱스 범위 / 이 수치와 Non-Null Count 비교 시 어떤 컬럼에 결측치가 비어있는지 바로 파악 가능
# - 테이블
#  - Column : 존재하는 컬럼
#  - Non-Null Count : 결측치가 아닌 컬럼 개수
#  - Dtype : 컬럼의 자료형
# - 맨 아래
#  - dtypes : 자료형 요약으로 그냥 자료형의 종류 및 개수 출력
#  - memory usage : 이 데이터프레임이 현재 컴퓨터 메모리(RAM)를 얼마나 차지하고 있는지 보여줍

# print(df.memory_usage()) # 메모리 사용량 확인(인덱스별 사용량)
# print(df.dtypes) # 컬럼 자료형 확인
# print(df.sum()) # 컬럼 값 합계
# print(df.count()) # 결측치 제외 개수
# print(df.median()) # 중앙값(잊지 말아라, 주어진 수치 데이터를 작은 수 > 크 수로 나열한 기준이다. / 만약 중앙이 2개라면 "(구한 2개 더하고) / 2" 해줘야 한다.)

# 데이터의 특정 비율 위치 값 계산 함수(사분위수)
# 기본은 50%이며 0.75(75%), 0.25(25%) 같은 방식으로 수치 조절 가능
# 10 20 30 40 50 <= 기준으로 본다면 0.75는 40, 0.25는 20 출력
# 이상치 탐구에도 많이 쓴다고 하며, 여러 비율을 동시에 확인 가능 quantile([0.25, 0.5, 0.75])
# 단, 필요에 따라 가상 값도 쓰는데 "가상의 값 = 시작점 값 + (끝점 값 - 시작점 값) * 남은 비율"이다.
# "남은 비율 = (끝점 비율 - 시작점 비율) / (끝점 비율- 시작점 비율)"
# print(df.quantile())
# print(df.quantile([0.25, 0.5, 0.75]))

# apply는 함수 적용이다. (ex. df.apply(sum) => 이러면 컬럼별로 값을 다 더해서 보여준다.)
# apply 사용 방법 1
# 지금의 방식은 값마다 제곱한 값을 리턴한다.
# def square(x):
#     return x * x
# print(df.apply(square)) # 이걸 고차 함수라고 부른다.

# apply 사용 방법 2
# 람다 방식이다. 일회용 함수라고 보면 된다.
# print(df.apply(lambda n: n * n))

# print(df.min()) # 컬럼별 최소값
# print(df.max()) # 위와 반대
# print(df.mean()) # 컬럼별 평균
# print(df.std()) # 표준편차

# 분산(산포도 / 평균에서 얼마나 멀리 떨어져서 들쭉날쭉하게 흩어져 있는가 / 퍼짐 정도)
# std와 비슷한데, var에 루트를 씌우면 된다. 반대로 std에 제곱하면 var이 된다.
# 값들이 가까워질수록 분산 값이 적고, 멀어질수록 분산 값이 크다.
# print(df.var())


# 7. Handling Missing Data
# 공부
# df = pd.DataFrame({
#     '국': [2, 6, 7], # 1, 6, 7
#     '영': [2, 4, 8],
#     '수': [3, 5, 9],
#     '화': [3, 10, 1] # 10, 3, 1
# }, index=[1, 2, 3])

# print("=== 원본 데이터(결측치 추가) ===")
# df.loc[2, '영'] = None
# print(df, '\n')

# print(df.dropna()) # NaN이 있는 행 제거
# print(df.fillna(0)) # NaN 값을 원하는 값으로 변경(타입 따라감)

# df['영'] = df['영'].fillna(100) # 특정 컬럼만 변경 가능
# print(df)


# 실전
mpg = sns.load_dataset('mpg')

# print(mpg.describe())
# print(mpg.value_counts('cylinders')) # 기통별 개수
# print(mpg[mpg['horsepower'].isnull()], '\n') # null값인 행들만 출력

# 기통별 마력들의 중앙값을 구해서 결측치를 채운다.
# 이때 원본이 가진 단일 요소별로 함수에 대한 값을 채우는 역할을 transform이 해준다. 원본이 아닌 groupby의 축약본을 따르는 agg랑은 또다른 요소
# mpg['horsepower'] = mpg['horsepower'].fillna(
#     mpg.groupby('cylinders')['horsepower'].transform('median')
# )
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
# print(mpg.sort_values('mpg', ascending=False)) # 전체 출력으로 컬럼 확인
# 아니면 info로 확인해도 된다.

# mpg = mpg.drop(columns=['origin', 'name', 'model_year']) # 제조 국가, 차 이름, 연식을 삭제
# print(mpg.info()) # 필요하면 fillna 전후로 로그 찍어서 확인해라
# print(mpg.head()) # 1~5행까지 출력