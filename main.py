# 각 파일별 클래스 호출
from ml_prep.scaler import Datasclaer 
from ml_prep.cleaner import TextCleaner
from ml_prep import stats

# stats 파일은 파일 자체를 호출하여 함수들을 실행

data = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]

# 클래스 객체화
scaler = Datasclaer()

normalized = scaler.fit_transform(data)

print("=== Normalized Data ===")
print(normalized)


summary = stats.summary(data)
print("=== Data Summary ===")
print(summary)

texts = ["Hello!!!", "Machine-Learning??", "Python123"]

cleaner = TextCleaner()

cleaned = cleaner.clean_corpus(texts)
print("=== Cleaned Texts ===")
print(cleaned)


