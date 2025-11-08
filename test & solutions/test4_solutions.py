numbers = [5, 12, 7, 20, 3, 15]
scores = [88, 92, 76, 81, 95]
names = ["철수", "영희", "민수", "지혜"]
reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"]
features = ["age", "height", "weight", "blood_type", "salary"]
datasets = [{"id": 1, "missing": 0}, {"id": 2, "missing": 3}, {"id": 3, "missing": 0}]
train_data = [10, 12, 11, 13, 9, 12]
test_data = [20, 21, 19, 18, 22]
outliers = [1, 500, 2, 3, 450, 4]

# For 반복문 문제 (10문제)

# numbers = [5, 12, 7, 20, 3, 15] 리스트의 모든 원소에 2를 곱해 출력하는 코드를 작성하시오.
numbers = [5, 12, 7, 20, 3, 15]
for num in numbers:
    print(num*2)

# 답
result = [] 
for num in numbers:
    result.append(num*2)
print(result)

# 답 2 (numpy)
import numpy as np

ar = np.array(numbers)

print(ar)


# scores = [88, 92, 76, 81, 95] 리스트에서 80점 이상인 점수만 출력하는 코드를 작성하시오.
# 답
scores = [88, 92, 76, 81, 95]
for num in scores:
    if num >= 80:
        print(num)

    
# names = ["철수", "영희", "민수", "지혜"] 리스트의 원소를 인덱스와 함께 출력하는 코드를 작성하시오.
names = ["철수", "영희", "민수", "지혜"]
num = 0
for fac_index in names:
    print(fac_index, num)
    num = num + 1

# 답

for num, name in enumerate(names):
    print(num, name)

# 답

for i in range(len(names)):
    print(i, names[i])

# reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"] 리스트에서 **클리닝이 필요한 리뷰(알파벳+숫자 이외 문자가 포함된 항목)**를 출력하는 코드를 작성하시오.
reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"]

for review in reviews:
    if review.find("!") != -1:
        print(review)
    elif review.find("@") != -1:
        print(review)
    elif review.find("#") != -1:
        print(review)
    else:
        pass

# 답

for review in reviews:
    if not review.isalnum():
        print(f"\"{review}\"는 클리닝이 필요함")



# features = ["age", "height", "weight", "blood_type", "salary"] 리스트에서 길이가 5 이상인 피처 이름만 출력하는 코드를 작성하시오.
features = ["age", "height", "weight", "blood_type", "salary"]

for feature in features:
    if len(feature) >= 5:
        print(feature)
    
# datasets = [{"id": 1, "missing": 0}, {"id": 2, "missing": 3}, {"id": 3, "missing": 0}] 리스트에서 결측값이 존재하는 데이터셋을 출력하시오.
datasets = [{"id": 1, "missing": 0}, {"id": 2, "missing": 3}, {"id": 3, "missing": 0}]

for data in datasets:
    if data["missing"] != 0:
        print(data)
    
# train_data = [10, 12, 11, 13, 9, 12] 와 test_data = [20, 21, 19, 18, 22] 의 평균 차이를 for문을 활용하여 출력하시오.
train_data = [10, 12, 11, 13, 9, 12] 
test_data = [20, 21, 19, 18, 22]
''''
for i in range(len(train_data)):
    a = (train_data[i])/len(train_data)
for j in range(len(test_data)):
    b = (test_data[j])/len(test_data)

print(abs(a-b))
'''
# 답 
sum_train_data = 0

for i in train_data:
    sum_train_data = sum_train_data + i

average_train_data = sum_train_data/len(train_data)

sum_test_data = 0

for i in test_data:
    sum_test_data = sum_test_data + i

average_test_data = sum_test_data/len(test_data)

print(abs(average_test_data - average_train_data))

# outliers = [1, 500, 2, 3, 450, 4] 리스트에서 값이 100 이상인 항목을 "이상치"로 출력하시오.

for a in outliers:
    if a >= 100:
        print(f"\"{a}\"는 이상치이다.")

# 또다른 답
def over(x):
    return x >= 100

print(list(filter(over, outliers))) # over 라는 함수로 outliers를 filter해주고 list화 한것을 print 하라.


# scores = [88, 92, 76, 81, 95] 리스트의 점수를 기준으로 A(90점 이상), B(80점 이상), C(그 외) 등급을 매겨 출력하시오.

for b in scores:
    if b >= 90:
        print(f"{b}는 A(90점 이상)")
    elif b < 90 and b >= 80:
        print(f"{b}는 B(80점 이상)")
    else:
        print(f"{b}는 그 외")

# 또다른 답

for s in scores:
    if s >= 90:
        grade = "A"
    elif s >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"{s} -> {grade} ")

# reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"] 리스트에서 각 리뷰의 문자열 길이를 출력하시오.
reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"]

for len_reviews in reviews:
    print(f"{len_reviews}의 길이는", len(len_reviews))

# While 반복문 문제 (10문제)

# numbers = [5, 12, 7, 20, 3, 15] 리스트의 모든 원소를 while문으로 출력하시오.
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1


# scores = [88, 92, 76, 81, 95] 리스트에서 80점 이상인 점수만 while문으로 출력하시오.
i = 0
while i < len(scores):
    if scores[i] >= 80:
        print(scores[i])
        i = i + 1
    else:
        i = i + 1
        continue

# 또다른 답

while i < len(scores):
    if scores[i] >= 80:
        print(scores[i])
    i = i + 1 # 이게 포인트
# names = ["철수", "영희", "민수", "지혜"] 리스트를 while문을 이용해 거꾸로 출력하시오.

i = 0
while i <= len(names)-1:
    print(names[(len(names)-1)-i])
    i = i + 1

# 또다른 답

num = len(names) - 1
while num >= 0:
    print(names[num])
    num = num - 1

# reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"] 리스트에서 클리닝이 필요한 리뷰를 while문으로 출력하시오.

i = 0
while i <= len(reviews)-1:
    if reviews[i].find("!") != -1:
        print(reviews[i])
    i = i + 1

# 또다른 답
i = 0
while i < len(reviews):
    if not reviews[i].isalnum():
        print(f"{reviews[i]}는 클리닝 필요")
    i = i + 1

# features = ["age", "height", "weight", "blood_type", "salary"] 리스트에서 길이가 5 이상인 피처 이름만 while문으로 출력하시오.
i = 0
while i <= len(features)-1:
    if len(features[i]) >= 5:
        print(features[i])
    i = i + 1

# datasets = [{"id": 1, "missing": 0}, {"id": 2, "missing": 3}, {"id": 3, "missing": 0}] 리스트에서 결측값이 존재하는 데이터셋을 while문으로 출력하시오.
i = 0
while i <= len(datasets)-1:
    if datasets[i]["missing"] != 0:
        print(datasets[i])
    i = i + 1

# train_data = [10, 12, 11, 13, 9, 12] 와 test_data = [20, 21, 19, 18, 22] 의 평균 차이를 while문을 활용하여 출력하시오.
i = 0
sum = 0
while i <= len(train_data)-1:
    sum = sum + train_data[i]
    i = i + 1

average_train_data = sum/len(train_data)

z = 0
sum2 = 0
while z <= len(test_data)-1:
    sum2 = sum2 + test_data[z]
    z = z + 1
average_test_data = sum2/len(test_data)

print(abs(average_test_data - average_train_data))

# outliers = [1, 500, 2, 3, 450, 4] 리스트에서 값이 100 이상인 항목을 while문으로 "이상치"로 출력하시오.
i = 0
while i <= len(outliers)-1:
    if outliers[i] >= 100:
        print(f"{outliers[i]}은 이상치")
    i = i + 1

# scores = [88, 92, 76, 81, 95] 리스트의 점수를 기준으로 A(90점 이상), B(80점 이상), C(그 외) 등급을 while문으로 출력하시오.
i = 0
while i <= len(scores)-1:
    if scores[i] >= 90:
        print(f"{scores[i]}는 A")
        i = i + 1
    elif scores[i] < 90 and scores[i] >= 80:
        print(f"{scores[i]}는 B")
        i = i + 1
    else:
        print(f"{scores[i]}는 그 외")
        i = i + 1
    
# 또다른 답
i = 0
while i <= len(scores)-1:
    if scores[i] >= 90:
        grade = "A"
    elif scores[i] < 90 and scores[i] >= 80:
        grade = "B"
    else:
        grade = "C"
    print(f"{scores[i]} -> {grade}")
    i = i + 1

# reviews = ["좋아요!!!", "별로", "최고최고", "data123", "clean"] 리스트에서 각 리뷰의 문자열 길이를 while문으로 출력하시오.
i = 0
while i <= len(reviews)-1:
    print(len(reviews[i]))
    i = i + 1

# 또다른 답

i = 0
while i <= len(reviews)-1:
    print(f"\"{reviews[i]}\"의 길이는", len(reviews[i]))
    i = i + 1
