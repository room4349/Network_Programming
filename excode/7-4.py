# 연습 7-4: 리스트 컴프리헨션
words = ["tiger", "lion", "elephant", "cat", "horse"]
long_words = [word for word in words if len(word) >= 5]

print(long_words)
