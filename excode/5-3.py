def do_operation(func, x, y):
    return func(x, y)


# 1. 일반 함수로 덧셈과 뺄셈 실행
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


result = do_operation(add, 2, 3)
print(result)  # 5

result = do_operation(sub, 2, 3)
print(result)  # -1


# 2. lambda 함수로 덧셈과 뺄셈 실행
add = lambda a, b: a + b
sub = lambda a, b: a - b

result = do_operation(add, 2, 3)
print(result)  # 5

result = do_operation(sub, 2, 3)
print(result)  # -1
