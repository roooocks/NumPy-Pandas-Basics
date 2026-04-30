import numpy as np
import pandas as pd

# 01. numpy 2차원 배열
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# print(arr2d)

# 위의 문제는 "몇번째 배열이 누구 것인가를 기억하지 못한다" 라는 치명적인 문제가 있다.
# 물론 만들면 되는데, 그래도 그거 자체가 귀찮다...


# 02. 2차원 배열 생성
# 1차원: Serise / 2차원: DataFrame(list or dict로 생성)
# df_2dlist = pd.DataFrame(arr2d, columns=['국', '영', '수'], index=[1, 2, 3]) # 이거 1차원이다.
# df_2dlist = pd.DataFrame([[1, 2, 3], [6, 4, 5], [7, 8, 9]], columns=['국', '영', '수'], index=[1, 2, 3])
# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9]}, index=[1, 2, 3])
# print(df_2dlist)
# print(df_dict)


# 03. 메소드 체이닝
# ClassName().setName("kim").setAge(30).setJob("doctor")... 방식을 쓰는 경우가 메소드 체이닝이다.
# df_new = pd.melt(df_dict) # 첫번째 방식

# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5') # 점수 5 이상만
# print(df_new)

# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5').sort_values('var', ascending=False) # 점수 5 이상을 내림차순 정렬
# print(df_new)

# 결측치(값) 처리
#   - 아예 날리기
#   - 통계적인 대표값으로 채우기(평균이 대표적)
#   - 결측이 적을 때 결측 행들을 날리는 방식
# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5').drop() # 데이터 버리기
# print(df_new)


# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '미세먼지': [10, 3, 1]}, index=[1, 2, 3])
# print(df_dict)
# df_new = df_dict.drop(columns=['수', '미세먼지'])
# print(df_new)


# 결측이 적을 때 결측 행들을 날리는 방식의 예시
#  - 강한 양의 상관관계(월급이 높으면 삶의 만족도가 높다.)
#  - 강한 음의 상관관계(미세먼지가 높으면 삶의 만족도가 낮다.)

# 그 외의 Reshaping Data 전부 실습하기
#   - sort에서 볼 수 있는 mpg는 "마일 퍼 겔런"을 뜻한다.
#   - 하지만 우린 없으니깐 미리 만들어둔걸 사용한다.


# 04. Subsets(부분 집합) - rows and columns
# 원하는 범위 지정이다.

# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df_dict)

# iloc (index 기준)
# df_new = df_dict.iloc[1:3] # 원본의 컬럼에서 두번째와 세번째 행만 가져온다. ([1:]도 가능)
# df_new = df_dict.iloc[1:3, 2:4] # 원본의 컬럼에서 2~3번째 행만 가져오고 거기서 세번째~네번째 열만 추가로 잘라서 가져온다. 라벨 이름보고 작업하는 놈이다.
# df_new = df_dict.iloc[0:, [1, 3]] # 이거 [0, [1:4:2]]도가 능하다.
# print(df_new)

# loc (라벨 기준)
# df_new = df_dict.loc[:, '영':'화'] # 이건 영어, 수학, 화학 포함
# df_new = df_dict.loc[df_dict['국'] > 5, ['영', '화']] # 국어 성적 5점 초과인 사람의 '영', '화' 데이터만 출력
# print(df_new)

# 스칼라 값 / 특정 값 하나만 가져오기
# iat (index 기준)
# print(df_dict.iat[1, 2]) # 1열 2행 값 가져오기

# # at (라벨 기준)
# print(df_dict.at[2, '수'])


# 05. Subsets Observations - rows(행)
df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
print(df_dict)

# print(df_dict.sample(frac=0.33)) # 랜덤한 행을 샘플링(%)해서 출력 (0.5면 절반만 / 근데 3행 뿐이라 절반 안되니 0.33 / 이거 이해 안되니 복습)
print(df_dict.sample(n=2)) # 행 랜덤으로 n개 가져오기
# print(df_dict.nlargest(2, '화')) # 화학 상위 2명 행 추출
# print(df_dict.nsmallest(2, '화')) # 화학 하위 2명 행 추출
# print(df_dict.head(2)) # 1~n 행 가져오기
# print(df_dict.tail(2)) # 마지막에서 n개 행 가져오기