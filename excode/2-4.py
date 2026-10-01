number = int(input("1에서 100 사이의 정수를 입력하세요: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number}은 3과 5의 배수입니다")
elif number % 3 == 0:
    print(f"{number}은 3의 배수입니다")
elif number % 5 == 0:
    print(f"{number}은 5의 배수입니다")
else:
    print(f"{number}은 3과 5의 배수가 아닙니다")
