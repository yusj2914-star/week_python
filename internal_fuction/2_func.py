# 모든 값에 2를 곱한 값을 출력하는 코드
def two_times(l):
    # 곱한 값을 담을 빈 리스트 생성
    result = []
    # for 반복문을 사용하여 리스트 요소 하나씩 가져오기
    for i in l:
        # 2를 곱한 값을 result 리스트에 담아주기
        result.append(i * 2)
    return result


print(two_times([1, 2, 3, 4]))


# 매번 값을 곱하기 위해 함수를 복잡하게 만들어야 함
# 곱하기 코드로 함수를 만들고 map() 함수 사용
def two_times(x):
    return x * 2


print(list(map(two_times, [1, 2, 3, 4])))
