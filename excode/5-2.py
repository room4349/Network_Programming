def deco2_add(type):
    def decorator(func):
        def wrapper(a, b):
            result = func(a, b)
            if type == "math":
                return f"{a} + {b} = {result}"
            elif type == "word":
                return f"The sum of {a} and {b} is {result}"

        return wrapper

    return decorator


@deco2_add(type="math")
def add(a, b):
    return a + b


print(add(2, 4))  # 2 + 4 = 6 출력


@deco2_add(type="word")
def add(a, b):
    return a + b


print(add(1, 2))  # The sum of 1 and 2 is 3 출력
