# 연습 7-1: 문자열과 튜플 슬라이싱
text = "WindowProgramming"

print("문자열 슬라이싱")
print(text[1:4])
print(text[9:])
print(text[2:8:2])
print(text[-1:10:-1])

text_tuple = tuple(text)
print("튜플 슬라이싱")
print(text_tuple[1:4])
print(text_tuple[9:])
print(text_tuple[2:8:2])
print(text_tuple[-1:10:-1])
