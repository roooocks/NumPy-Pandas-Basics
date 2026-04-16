import numpy as np

# 1) 넘파이 배열 생성
l1 = [1, 2, 3, 'ㅗㅑㅗㅑ']
array01 = np.array(l1)
print(l1)   
print(array01) # numpy의 list는 [1 2 3]으로 출력된다. ','가 출력되는 것이다.

array02 = np.arange(0, 10, 2) # 0부터 9까지 2스탭으로 출력, 만약 하나만 있다면 자동 0부터 시작
print(array02)

# zeros, ones는 값이 소수로 들어간다.
array03 = np.zeros((2, 3)) # 2행 3열의 모든 원소가 0.으로 들어간다.
print(array03)

array04 = np.ones((2, 3)) # 이건 zeros와 달리 1.로 들어간다.
# array04 = np.ones((2, 3), dtype=int) # 이러면 1로 들어간다.
print(array04)

array05 = np.full((2, 3), 7) # 마지막 부분의 값(int)으로 배열을 채운다.
print(array05)

array06 = np.random.rand(2, 3) # 0~1사이 수라 0.어쩌고로 입력된다. 값은 [0, 1) => 0이상 1미만을 의미
print(array06)

array07 = np.linspace(0, 10, 3) # 0~10 사이를 균등하게 3개로 나누기
print(array07)

# 2) 넘파이 배열 속성
array08 = np.random.random((4, 2))
print(array08)

# shape는 모양(지금은 (4, 2) 출력), dtype은 들어간 값의 타입, ndim은 차원, size는 원소 개수
print(array08.shape, array08.dtype, array08.ndim, array08.size)

# 08의 전치(Transpose) 행렬을 의미한다. 4행 2열이 2행 4열로 출력된다.
print(array08.T)