i = int(input("정수 i를 입력하세요: "))

if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
    print(f"{i}는 윤년입니다.")
else:
    print(f"{i}는 평년입니다.")
    