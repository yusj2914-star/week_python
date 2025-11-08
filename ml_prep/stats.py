# 3. stats.py
# - calculate_mean(data): 각 열의 평균값 계산
# - calculate_variance(data): 각 열의 분산 계산
# - summary(data): 평균, 분산을 모두 딕셔너리로 반환
# [[12, 25, 37], [15, 27, 39], [16, 30, 45]]
# [14.3, 27.3, 40.3]
# zip -> sum - > len (for)
def calculator_mean(data): 
    means = [sum(col) / len(col) for col in zip(*data)]
    return means

# 분산 계산 함수 생성
# means 를 값에서 모두 빼주고 제곱하고 나눠주자
# [[12, 25, 37], [15, 27, 39], [16, 30, 45]]

def calculate_variance(data):
    means = calculator_mean(data)
    varicance = []

    for i, value in enumerate(zip(*data)):
        # 12, 15, 16 -> 25, 27, 30 ...
        # 0, [12, 15, 16]
        # var = [sum((12 - means[0]) ** 2) for x in value)]
        var = sum((x - means[i]) ** 2 for x in value) / len(value)
        varicance.append(var)

    return varicance

# 함수들을 호출하여 딕셔너리로 전달하는 함수 생성
# 이 파일의 대장
def summary(data):
    return {
"mean": calculator_mean(data), 
"variance": calculate_variance(data)
    }
    

