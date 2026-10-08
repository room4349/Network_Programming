class Calc:
    count = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        Calc.count += 1
        self.serial = Calc.count

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def getSerial(self):
        return self.serial


if __name__ == "__main__":
    a = 3
    b = 2
    calc1 = Calc(a, b)
    print(f'{a} + {b} = {calc1.add()}')
    print(f'{a} - {b} = {calc1.sub()}')

    calc2 = Calc(3, 4)
    print(f'{3} + {4} = {calc2.add()}')
    print(f'{3} - {4} = {calc2.sub()}')

    print(f'Serial of calc1: {calc1.getSerial()}')
    print(f'Serial of calc2: {calc2.getSerial()}')
