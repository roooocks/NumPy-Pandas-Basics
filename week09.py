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

df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
print(df_dict)
# df_new = df_dict.iloc[1:3] # 원본의 컬럼에서 두번째와 세번째만 가져온다. ([1:]도 가능)
df_new = df_dict.iloc[1:3, 2:4]
print(df_new)