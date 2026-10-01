first = int(input("첫 번째 정수를 입력하세요: "))
second = int(input("두 번째 정수를 입력하세요: "))

print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} x {second} = {first * second}")
print(f"{first} / {second} = {first / second}")

first, second = map(int, input("정수 두 개를 입력하세요: ").split())

print("{} + {} = {}".format(first, second, first + second))
print("{} - {} = {}".format(first, second, first - second))
print("{} x {} = {}".format(first, second, first * second))
print("{} / {} = {}".format(first, second, first / second))
