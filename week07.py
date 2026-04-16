import numpy as np;
import random

"""
만약 타입이 제각기로 들어간 파이썬 리스트를 array로 넣어 가장 상위 타입인 str로 변환한다.
 - 힘이 쌘 타입 : str > float > int 순이다.
다만 리스트 안에 리스트 구조라면 차원은 1차원으로 바꿔야한다. (inhomogeneous, 1 dimensions)
"""

l2 = list()

for i in range(3):
    l2.append(random.random())
print(l2)

# 파이썬 방식
l3 = []
for i in l2:
    l3.append(i * 10)
print(l3)

# numpy 방식
array03 = np.array(l2)
print(array03 * 10)
print(array03 > 0.5)


# 4) 넘파이 배열 주요 통계함수
array04 = np.arange(1, 11) # 1 ~ 10
print(np.mean(array04))
print(np.median(array04))
print(np.max(array04))
print(np.min(array04))
print(np.var(array04)) # 분산
print(np.std(array04)) # 표준편차