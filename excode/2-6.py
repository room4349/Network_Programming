number = int(input("정수를 입력하세요: "))

if number < 2:
    print("소수가 아닙니다.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("소수가 아닙니다.")
            break
    else:
        print("소수 입니다.")
