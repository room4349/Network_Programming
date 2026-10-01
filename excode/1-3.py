import math

a = 3
b = 4
c = 5
print("1번:", 1 / (1 + a / b + c))

a = 1
b = 1
c = -6
root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print("2번:", root1, root2)

r = 5
print("3번:", math.pi * r ** 2)

beta = 2.0
g = 3.2
print("4번:", beta * math.exp(-g))

x = 0
mu = 1.5
rho = 2.0
value = math.exp(-((x - mu) ** 2) / (2 * rho ** 2)) / math.sqrt(2 * math.pi * rho)
print("5번:", value)
