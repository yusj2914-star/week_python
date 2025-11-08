# numpy 모듈
# 수치해석용 파이썬 파일
# 각종 행렬이나 배열 연산을 위해서 사용하는 모듈


# numpy를 사용하는 이유
# 1. C언어를 기반으로 작성된 파이썬 파일이어서 고속 연산 지원
# 2. 배열 연산
# 3. scikit-learn, tensorflow, pytorch는 배열을 기대함


# numpy로 곱하기 2하기
import numpy as np


# 리스트를 배열로 바꾸기
ar = np.array([1, 2, 3, 4])


print(ar)
print(ar * 2)
