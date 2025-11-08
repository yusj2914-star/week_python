# 1단계: 패키지 구조 만들기

# 프로젝트 구조를 다음과 같이 설계한다.
# ml_prep/
#     __init__.py
#     scaler.py
#     cleaner.py
#     stats.py
# main.py


# 2단계: 모듈 기능 구현

# 머신러닝 도구에는 크게 2가지가 존재(머신러닝 학습기, 전처리 도구)

# 1. scaler.py
# - DataScaler 클래스 작성
# - fit(data): 각 열의 최소/최대값 계산(데이터 학습)
# - transform(data): min-max scaling 적용 – (value - min) / (max - min)
# - fit_transform(data): fit + transform 실행

# 2. cleaner.py
# - TextCleaner 클래스 작성
# - remove_special(text): 정규식을 이용하여 특수문자 제거 (re.sub)
# - to_lower(text): 소문자로 변환
# - clean_corpus(corpus): 여러 문장 리스트를 받아 전처리 수행

# 3. stats.py
# - calculate_mean(data): 각 열의 평균값 계산
# - calculate_variance(data): 각 열의 분산 계산
# - summary(data): 평균, 분산을 모두 딕셔너리로 반환

# 3단계: main.py 실행 파일 작성

# ml_prep 패키지의 기능을 가져와 다음을 실행한다:
# - 데이터 [ [10, 20, 30], [20, 30, 40], [30, 40, 50] ]를 DataScaler로 정규화
# - 정규화된 데이터를 stats 모듈로 평균/분산을 요약 출력
# - 텍스트 리스트 ["Hello!!!", "Machine-Learning??", "Python123"]를 TextCleaner로 전처리하고 결과 출력

# 출력 예시

# === Normalized Data ===
# [[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [1.0, 1.0, 1.0]]

# === Data Summary ===
# {'mean': [0.5, 0.5, 0.5], 'variance': [0.1666, 0.1666, 0.1666]}

# === Cleaned Texts ===
# ['hello', 'machinelearning', 'python']

