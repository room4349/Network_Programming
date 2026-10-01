i = int(input("정수 i를 입력하세요: "))

if i % 3 == 0 and i % 5 == 0:
    print(f"{i}는 3과 5의 공배수입니다.")
elif i % 3 == 0:
    print(f"{i}는 3의 배수입니다.")
elif i % 5 == 0:
    print(f"{i}는 5의 배수입니다.")
else:
    print(f"{i}는 3과 5의 배수가 아닙니다.")