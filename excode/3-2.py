def min_max(numbers):
    return min(numbers), max(numbers)


numbers = list(map(int, input("정수들을 입력하세요 (공백으로 구분): ").split()))
minimum, maximum = min_max(numbers)
print(f"최솟값: {minimum}, 최댓값: {maximum}")
