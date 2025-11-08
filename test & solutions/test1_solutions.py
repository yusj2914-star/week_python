review = "이 제품 정말 좋아요 가격도 착하고 배송도 빨라요"

print(review.split())

review1 = " 배송이 늦었지만 제품은 만족합니다 "

print(review1.strip())
print(len(review1.strip()))

review2 = "배송이/빠르고/품질도/좋습니다"

words = review2.split("/")
print(words)

print(" ".join(words))

review3 = "별로였어요., 별로였어요., 별로였어요."

print(review3.replace("별로였어요.","만족스러워요."))

review4 = "빠름! 친절! 만족!"

words1 = review4.split("!")
print(words1)

words1[1] = words1[1].strip()
words1[2] = words1[2].strip()
del words1[3] 

print(words1)

review5 = "제품이좋아요"

print(" ".join(review5))

review6 = "배송 빠름 품질 만족 재구매 의사 있음"

words2 = review6.split(" ")
print(words2[0])
print(words2[-1])

review7 = "*****"

print(len(review7))

review8 = "배송 빠름 품질 만족"

words3 = review8.split(" ")

print(",".join(words3))

# perch_data.append([45.0, 13.0, 8.0])
# print(perch_data)

# perch_data.insert(0,[7.0, 1.5, 1.0])

# del perch_data[-3]
# perch_data.remove([19.0, 5.64, 3.05])

# pop은 꺼내서 제거
# print(perch_data.pop(-1))
# pirnt(perch_data)

# print(perch_data.pop(9))

# print(len(perch_data))
# perch_data.append(50.0, 14.0, 9.0)
# print(len(perch_data))

# mid_index = len(perch.data) // 2
# perch_data.insert(mid_index, [20.0, 6.0, 3.0])
# print(perch_data.pop(mid_index))

# first_five = perch_data[:5]
# print(first_five.pop(-1))
# print(first_five)

# perch_data.append([45.5, 13.2, 8.1])
# perch_data.append([46.0, 13.5, 8.3])

# first_data = perch_data.pop(0)
# perch_data.append(first_data)
