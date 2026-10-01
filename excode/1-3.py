import math

# 1. a = 3, b = 4, c = 5
a = 3
b = 4
c = 5
result1 = 1 / (1 + a / b + c)
print("1번:", result1)

# 2. ax² + bx + c = 0의 두 근 (a = 1, b = 1, c = -6)
a = 1
b = 1
c = -6
root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print("2번:", root1, root2)

# 3. 반지름이 5인 원의 면적
r = 5
area = math.pi * r ** 2
print("3번:", area)

# 4. β = 2.0, g = 3.2일 때 βe^(-g)
beta = 2.0
g = 3.2
result4 = beta * math.exp(-g)
print("4번:", result4)

# 5. x = 0, μ = 1.5, ρ = 2.0일 때 수식의 값
x = 0
mu = 1.5
rho = 2.0
result5 = (1 / math.sqrt(2 * math.pi * rho)) * math.exp(
    -((x - mu) ** 2) / (2 * rho ** 2)
)
print("5번:", result5)