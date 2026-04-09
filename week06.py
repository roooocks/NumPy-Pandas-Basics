import numpy as np

l1 = [1, 2, 3]
array01 = np.array(l1)
print(l1)   
print(array01) # numpy의 list는 [1 2 3]으로 출력된다. ','가 출력되는 것이다.

array02 = np.arange(0, 10, 2)
print(array02)

# zeros, ones는 값이 소수로 들어간다.
array03 = np.zeros((2, 3)) # 2행 3열의 모든 원소가 0으로 들어간다.
print(array03)

array04 = np.ones((2, 3)) # 이건 zeros와 달리 1로 들어간다.
print(array04)

array05 = np.full((2, 3), 7) # 마지막 부분의 값으로 배열을 채운다.
print(array05)

array06 = np.random.rand(2, 3) # 0~1사이 수라 0.어쩌고로 입력된다.
print(array06)

array07 = np.linspace(0, 10, 3) # 0~10 사이를 균등하게 3개로 나누기
print(array07)
