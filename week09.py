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
# df_2dlist = pd.DataFrame(arr2d, columns=['국', '영', '수'], index=[1, 2, 3])
# df_2dlist = pd.DataFrame([[1, 2, 3], [6, 4, 5], [7, 8, 9]], columns=['국', '영', '수'], index=[1, 2, 3])
# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9]}, index=[1, 2, 3])
# print(df_2dlist)
# print(df_dict)


# 03. 메소드 체이닝(Using query 포함)
# ClassName().setName("kim").setAge(30).setJob("doctor")... 방식을 쓰는 경우가 메소드 체이닝이다.
# df_new = pd.melt(df_dict) # 첫번째 방식
# print(df_new)

# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5') # 점수 5 이상만
# print(df_new)

# sort_values가 내림차순이면 열의 이름만 넣으면 되나, 오름차순이면 열의 이름 + ascending=False가 필요하다.
# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5').sort_values('var', ascending=False) # 점수 5 이상을 내림차순 정렬
# print(df_new)

# sort_index()도 존재한다.
# axios로 행/열을 정하고 ascending의 참/거짓으로 index의 오름차순과 내림차순을 정한다.


# 결측치(값) 처리
#   - 아예 날리기
#   - 통계적인 대표값으로 채우기(평균이 대표적)
#   - 결측이 적을 때 결측 행들을 날리는 방식
# df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5').drop(columns=['val']) # 데이터 버리기
# print(df_new)
# drop은 행/열 둘 다 날리기가 가능하다.
#   - .drop('r1'), .drop(['r1', 'r2']) => 행(rows) 삭제
#   - .drop('r1', axis=1), .drop(['r1', 'r2'], axis=1) => 열(columns / axis값 1 / 0이면 행) 삭제
#   - .drop(columns=['A']) => 열 삭제


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
# 원하는 범위 지정 접근(요소 접근)이다.

# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df_dict)

# iloc (index 기준, 앞에 붙은 i가 integer라 숫자만 가능하다.)
# df_new = df_dict.iloc[1:3] # 원본의 컬럼에서 두번째와 세번째 행만 가져온다. ([1:]도 가능)
# df_new = df_dict.iloc[1:3, 2:4] # 원본의 컬럼에서 2~3번째 행만 가져오고 거기서 세번째~네번째 열만 추가로 잘라서 가져온다. 라벨 이름보고 작업하는 놈이다.
# df_new = df_dict.iloc[0:, [1, 3]] # 이거 [0, [1:4:2]]도가 능하다. 다만 이름을 직접 넣는건 안된다.
# print(df_new)

# loc (라벨 기준)
# 라벨 기준이라곤 했지만 첫번째 예제에 있는 ":"는 인덱스를 범위를 뜻한다. 만약 "3:"라면 인덱스 번호 3부터 끝까지란 뜻이 된다.
# df_new = df_dict.loc[3:, '영':'화'] # 이건 영어, 수학, 화학 포함
# df_new = df_dict.loc[df_dict['국'] > 5, ['영', '화']] # 국어 성적 5점 초과인 사람의 '영', '화' 데이터만 출력
# print(df_new)

# 스칼라 값 / 특정 값 하나만 가져오기
# iat (index 기준)
# print(df_dict.iat[1, 2]) # 1열 2행 값 가져오기

# at (라벨 기준)
# 여기까지 오면 라벨 기준에서의 숫자가 뭔지 느낌이 올 것이다.
# 우리가 설정한 index를 최우선으로 잡고 찾는다. 때문에 내가 index 설정을 안했다면 0부터 시작하는게 맞다.
# print(df_dict.at[2, '수'])


# 05. Subsets Observations - rows(행)
# df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9], '화': [10, 3, 1]}, index=[1, 2, 3])
# print(df_dict)

# 중복 제거를 하나 하나는 남긴다. (아마도? 복습할 때 테스트해보자)
# df_dict.drop_duplicates()

# frac는 정수가 아닌 비율 방식이다.
# 보통 "전체 행 개수 * 입력한 수"의 결과만큼 샘플을 뽑는데, 0.5 기준이라면 1.5가 나오므로 1~2개 사이가 나온다. (버전/환경마다 반올림, 버림 다 다름)
# 2행 이상 부터는 출력하는 행의 순서가 "랜덤"이 된다.
# 비율 방식인 부분에서 알 수 있듯이 100만개, 1000만개가 넘어가는 데이터 중 10%, 20% 정도만 뽑고 싶다. 할 때 사용할 수 있다.
# 그렇게 되면 frac는 0.1 혹은 0.2가 된다.
# print(df_dict.sample(frac=0.33))

# print(df_dict.sample(n=2)) # 행 랜덤으로 n개 가져오기
# print(df_dict.nlargest(2, '화')) # 화학 상위 2명 행 추출
# print(df_dict.nsmallest(2, '화')) # 화학 하위 2명 행 추출
# print(df_dict.head(2)) # 1~n 행 가져오기 (기본값 5개)
# print(df_dict.tail(2)) # 마지막에서 n개 행 가져오기 (기본값 5개)