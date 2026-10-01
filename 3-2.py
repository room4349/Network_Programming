def min_max(nums):
    return min(nums), max(nums)

num = list(map(int, input ("정수들을 입력하세요 (공백으로 구분): ").split()))

result = min_max(num)

print(f"최솟값: {result[0]}, 최댓값: {result[1]}")
