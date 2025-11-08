student_scores = {"철수": 85, "영희": 92, "민수": 76, "지혜": 88}
customer_purchases = {"고객A": 5, "고객B": 12, "고객C": 7, "고객D": 3}
missing_counts = {"sensor1": 0, "sensor2": 5, "sensor3": 0, "sensor4": 12}
class_counts = {"class1": 120, "class2": 80, "class3": 100}
model_scores = {"model_A": 0.88, "model_B": 0.93, "model_C": 0.85}

print(max(customer_purchases, key=customer_purchases.get()))