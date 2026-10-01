def calc(*numbers, op):
    if op == "+":
        result = 0
        for number in numbers:
            result += number
        return result

    if op == "*":
        result = 1
        for number in numbers:
            result *= number
        return result

    raise ValueError("연산자는 + 또는 *만 사용할 수 있습니다")


print(calc(1, 1, 4, op="+"))
print(calc(1, 2, op="*"))
