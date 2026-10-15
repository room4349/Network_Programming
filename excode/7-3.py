numbers = [1, 2, 2, 5, 3, 4, 3, 5, 1, 6]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
