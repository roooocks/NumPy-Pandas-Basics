import numpy as np

array01 = np.random.random((4, 2))
print(array01)

# shape는 모양(지금은 (4, 2) 출력), dtype은 들어간 값의 타입, ndim은 차원, size는 원소 개수
print(array01.shape, array01.dtype, array01.ndim, array01.size)

# 01의 전치 행렬을 의미한다. 2행 4열로 출력된다.
print(array01.T)