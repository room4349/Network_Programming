first = [1, 0, 1]
second = [1, 1, 2]

total = sum(first[index] * second[index] for index in range(3))
print(f"{first} * {second} = {total}")
