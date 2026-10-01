x = 10


def first_test():
    x = 20
    print(x)


first_test()
print(x)


def second_test():
    print(x)


second_test()
print(x)


def outer():
    x = 20

    def inner():
        x = 30
        print("A:", x)

    inner()
    print("B:", x)


outer()
print("C:", x)


def third_test():
    global x
    print(x)
    x = 20


third_test()
print(x)
