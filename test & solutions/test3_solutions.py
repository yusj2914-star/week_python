# 딕셔너리 관련 예제용 데이터
student_scores = {"철수": 85, "영희": 92, "민수": 76, "지혜": 88}
customer_purchases = {"고객A": 5, "고객B": 12, "고객C": 7, "고객D": 3}
missing_counts = {"sensor1": 0, "sensor2": 5, "sensor3": 0, "sensor4": 12}
class_counts = {"class1": 120, "class2": 80, "class3": 100}
model_scores = {"model_A": 0.88, "model_B": 0.93, "model_C": 0.85}


# 집합 관련 예제용 데이터
features_A = {"age", "height", "weight", "blood_type"}
features_B = {"height", "weight", "salary", "education"}
all_features = {"age", "height", "weight", "salary", "education", "blood_type"}
drop_features = {"salary", "blood_type"}
train_ids = {1, 2, 3, 4, 5}  # 인덱스(행)
test_ids = {4, 5, 6, 7}
new_features = {"gender", "income"}

# 조건문 관련 예제용 데이터
num_samples = 950  # 실제 데이터의 개수
missing_ratio = 0.28  # 결측값 비율
unique_values = 45  # 고유값 개수
variance = 0.0  # 분산
class_ratio = {"positive": 950, "negative": 50}  # 클래스 비율
train_size = 800  # 훈련용 샘플 개수
test_size = 900  # 테스트 데이터 개수
outliers = 60  # 이상치 데이터 개수
total_samples = 1000  # 총 데이터의 개수
text_column = ["abc", "hello!", "data123", "clean_text"]  # 문자열 컬럼(열)
expected_features = 5  # 요구 피처 개수
input_features = 4  # 입력 피처 개수
train_mean, test_mean = 50.0, 70.5  # 학습 데이터의 평균, 테스트 데이터의 평균

# 딕셔너리 (5문제)

# 1. 학생 데이터셋에서 {이름: 점수} 형태의 딕셔너리가 있다. 평균 점수를 계산하고, "영희"의 점수를 출력하시오.
student_scores = {"철수": 85, "영희": 92, "민수": 76, "지혜": 88}

a = list(student_scores.values())

b = a[0] + a[1] + a[2] + a[3] 

print(b/len(a))

print(student_scores["영희"])

# 2. 고객별 구매 횟수를 저장한 딕셔너리에서 구매 횟수가 가장 많은 고객의 이름을 찾으시오.
customer_purchases = {"고객A": 5, "고객B": 12, "고객C": 7, "고객D": 3}

max_name = None
max_num = None

for name, num in customer_purchases.items():
    if max_num == None:
        max_name = name
        max_num = num
    elif num > max_num:
        max_name = name
        max_num = num
    else:
        print(max_num)
        print(max_name)
        break
# 답

print(max(customer_purchases, key=customer_purchases.get))


# 3. 센서별 결측값 개수를 {센서명: 결측값 개수}로 저장했을 때, 결측값이 0개인 센서를 모두 출력하시오.
missing_counts = {"sensor1": 0, "sensor2": 5, "sensor3": 0, "sensor4": 12}

zero_sensors = [sensor for sensor, count in missing_counts.items() if count == 0]

print("결측값이 없는 센서:", zero_sensors)

# 답
missing = [] # 빈 리스트를 생성하는 것을 요긴하게 사용!

for k, v in missing_counts.items():
    if v == 0:
        missing.append(k)
print(missing)


# 4. 각 클래스별 데이터 개수를 {클래스명: 개수} 형태로 저장했을 때, 총 샘플 수를 계산하시오.
class_counts = {"class1": 120, "class2": 80, "class3": 100}

a = list(class_counts.items())
print(len(a))

# 답

hap = 0
for v in class_counts.values():
    hap = hap + v
print(hap)

# 답2

print(sum(class_counts.values()))

# 5. 실험 결과에서 모델별 성능 점수를 {모델명: 점수}로 저장했을 때, 성능이 가장 높은 모델명을 출력하시오.
model_scores = {"model_A": 0.88, "model_B": 0.93, "model_C": 0.85}

max_model = None
max_score = None

for model, scores in model_scores.items():
    if max_model == None:
        max_model = model
        max_score = scores
    elif max_score < scores:
        max_score = scores
        max_model = model
    else:
        print(max_model)
        break
# 답
max_score = 0
max_model = ""
for k, v in model_scores.items():
    if v > max_score:
        max_model = k
        max_score = v
print(max_model)
        
# 답2

print(max(model_scores, key=model_scores.get))

# 집합 (5문제)

# 1. 데이터셋 A의 피처 목록과 데이터셋 B의 피처 목록이 있다. 두 데이터셋에 공통으로 존재하는 피처를 출력하시오.
features_A = {"age", "height", "weight", "blood_type"}
features_B = {"height", "weight", "salary", "education"}

print(features_A & features_B)

# 또다른 답

print(features_A.intersection(features_B))

# 2. 전체 피처 집합에서 분석에 필요 없는 피처 집합을 제거한 후, 남은 피처 집합을 출력하시오.
all_features = {"age", "height", "weight", "salary", "education", "blood_type"}
drop_features = {"salary", "blood_type"}

print(all_features.difference(drop_features))

# 또다른 답

print(all_features - drop_features)


# 3. 훈련 데이터셋과 테스트 데이터셋의 ID 집합이 주어졌을 때, 중복된 ID가 있는지 확인하시오.
train_ids = {1, 2, 3, 4, 5}  # 인덱스(행)
test_ids = {4, 5, 6, 7}

print(train_ids & test_ids)

# 4. A 데이터셋에만 존재하는 피처를 출력하시오.
features_A = {"age", "height", "weight", "blood_type"}
features_B = {"height", "weight", "salary", "education"}

print(features_A.difference(features_B))

# 5. 피처 이름 집합에서 새로 수집된 피처 집합을 합쳐 최종 피처 집합을 만드시오.
all_features = {"age", "height", "weight", "salary", "education", "blood_type"}
new_features = {"gender", "income"}

all_features.update(["gender", "income"])

print(all_features)

# 또다른 답

print(all_features | new_features)


# 조건문 관련 예제용 데이터
num_samples = 950  # 실제 데이터의 개수
missing_ratio = 0.28  # 결측값 비율 # 공백
unique_values = 45  # 고유값 개수 # 어떤 데이터인지 가늠이 안가는 데이터
variance = 0.0  # 분산 
class_ratio = {"positive": 950, "negative": 50}  # 클래스 비율
train_size = 800  # 훈련용 샘플 개수
test_size = 900  # 테스트 데이터 개수
outliers = 60  # 이상치 데이터 개수
total_samples = 1000  # 총 데이터의 개수
text_column = ["abc", "hello!", "data123", "clean_text"]  # 문자열 컬럼(열)
expected_features = 5  # 요구 피처 개수
input_features = 4  # 입력 피처 개수
train_mean, test_mean = 50.0, 70.5  # 학습 데이터의 평균, 테스트 데이터의 평균

# 조건문 (10문제)

# 1. 데이터의 개수가 1000개 이상이면 "충분", 아니면 "부족"을 출력하시오.
num_samples = 950

if num_samples > 1000:
    print("충분")
else:
    print("부족")

# 2. 결측값 비율이 30% 이상이면 "제거 고려", 아니면 "사용 가능"을 출력하시오.
missing_ratio = 0.28

if missing_ratio >= 0.3:
    print("제거 고려")
else:
    print("사용 가능")

# 3. 범주형 변수의 고유값 개수가 50개 이상이면 "차원 축소 필요", 아니면 "사용 가능"을 출력하시오.
unique_values = 45

if unique_values >= 50:
    print("차원 축소 필요")
else:
    print("사용 가능")

# 4. 수치형 피처의 분산이 0이면 "제거"를 출력하시오.
variance = 0.0 

if variance == 0:
    print("제거")
else:
    pass
# 5. 클래스 비율이 한쪽으로 90% 이상 치우쳐 있으면 "불균형 데이터", 아니면 "균형 데이터"를 출력하시오.
class_ratio = {"positive": 950, "negative": 50} 

#if (class_ratio.values("positive")/sum(class_ratio.values())) * 100 >= 90:
   # print("불균형 데이터")
#else: print("균형 데이터")

# 답 

total = class_ratio["positive"] + class_ratio["negative"]
total = sum(class_ratio.values())

if class_ratio["positive"] / total >= 0.9 or class_ratio["negative"] / total >= 0.9:
    print("불균형 데이터")
else: print("균형 데이터")

# 6. 샘플 개수가 훈련 데이터보다 테스트 데이터에서 더 많으면 "데이터 분할 오류"를 출력하시오.
train_size = 800
test_size = 900
# train: 80%, test: 20% 가장 이상적
if test_size > train_size:
    print("데이터 분할 오류")

# 7. 이상치 개수가 전체의 5% 이상이면 "이상치 처리 필요", 아니면 "정상"을 출력하시오.
outliers = 60
total_samples = 1000

if outliers/total_samples * 100 >= 5:
    print("이상치 처리 필요")
else:
    print("정상")
# 8. 문자열 컬럼에 특수문자가 있으면 "클리닝 필요", 없으면 "정상"을 출력하시오.
text_column = ["abc", "hello!", "data123", "clean_text"]
'''
c = text_column[0]+text_column[1]+text_column[2]+text_column[3]
 

i = 0
c = text_column[i]

while i <= len(text_column)-1:
    if c.find("!") != -1:
        print("클리닝 필요")
        i = i + 1
    else:
        print("정상")
        i = i + 1
'''
'''
for texts in text_column:
    if texts.find("!") != -1:
        print("클리닝 필요")
    else:
        print("정상")
'''
# 답
for texts in text_column:
    if not texts.isalnum():
        print("클리닝 필요")
    else:
        print("정상")


# 9. 입력된 피처 개수가 모델에서 요구하는 피처 개수와 다르면 "피처 불일치", 같으면 "적합"을 출력하시오.
expected_features = 5
input_features = 4

if expected_features != input_features:
    print("피처 불일치")
else:
    print("적합")

# 10. 학습 데이터의 평균과 테스트 데이터의 평균 차이가 너무 크면 "데이터 분포 불일치", 아니면 "정상"을 출력하시오.
train_mean, test_mean = 50.0, 70.5 

if train_mean - test_mean > 10 or test_mean - train_mean > 10:
    print('데이터 분포 불일치')
else:
    print('정상')

# 답

if abs(train_mean - test_mean) > 10: # 절댓값으로 바꿔주는 함수 사용
    print('데이터 분포 불일치')
else:
    print('정상')