def deco_add(func):
    def wrapper(a, b):
        return f"{a} + {b} = {func(a, b)}"
    return wrapper

@deco_add
def add(a, b):
    return a + b


print(add(2, 4))  # 2 + 4 = 6 출력
