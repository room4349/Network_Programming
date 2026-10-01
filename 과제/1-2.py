"""
x = 10

def outer():
    x = 20
    def inner():
        x = 30
        print("A:", x)
    inner()
    print("B:", x)
outer()
print("C:", x)
"""
x = 10 
def test():
    global x
    print(x) 
    x = 20
test()
print(x)