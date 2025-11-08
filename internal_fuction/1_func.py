# 양수만 출력하는 코드
def positive(l):
    # 양수만 담을 빈 리스트 생성
    result = []
    # for 반복문을 사용하여 리스트 요소 하나씩 가져오기
    for i in l:
        # 양수인지 판별하여 양수이면 result 리스트에 담아주기
        if i > 0:
            result.append(i)
    return result


print(positive([-1, 3, -5, 6, 2, -3]))


# 매번 조건에 맞는 값을 찾기 위해 함수를 복잡하게 만들어야 함
# 양수만 판별하는 코드로 함수를 만들고 filter() 함수 사용
def positive(x):
    return x > 0


print(list(filter(positive, [-1, 3, -5, 6, 2, -3])))
