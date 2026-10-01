number = int(input("1에서 100 사이의 정수를 입력하세요: "))

if number >= 2:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(f"{number}은 소수입니다")
