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


# 02. pandas 2차원 배열 생성
# 1차원: Serise / 2차원: DataFrame(list or dict로 생성)
# df_2dlist = pd.DataFrame(arr2d, columns=['국', '영', '수'], index=[1, 2, 3]) # 이거 1차원이다.
df_2dlist = pd.DataFrame([[1, 2, 3], [6, 4, 5], [7, 8, 9]], columns=['국', '영', '수'], index=[1, 2, 3])
df_dict = pd.DataFrame({'국': [1, 6, 7], '영': [2, 4, 8], '수': [3, 5, 9]}, index=[1, 2, 3])
# print(df_2dlist)
print(df_dict)


# 03. pandas 메소드 체이닝
# ClassName().setName("kim").setAge(30).setJob("doctor")... 방식을 쓰는 경우가 메소드 체이닝이다.
# df_new = pd.melt(df_dict) # 첫번째 방식
df_new = pd.melt(df_dict).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 5')
print(df_new)