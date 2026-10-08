from abc import ABC, abstractmethod
import math


# 6-3에서는 Polygon의 getArea()를 추상 메쏘드로 정의한다.
class Polygon(ABC):
    shapes = {3: 'triangle', 4: 'rectangle', 5: 'pentagon'}

    def __init__(self, numSide):
        self.sideNumber = numSide
        self.sideLen = 0

    def setSideLen(self, sideLen):
        self.sideLen = float(sideLen)

    def getShape(self):
        return Polygon.shapes[self.sideNumber]

    @abstractmethod
    def getArea(self):
        pass


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def getArea(self):
        return math.sqrt(3) / 4 * self.sideLen ** 2


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def getArea(self):
        return self.sideLen * self.sideLen


# getArea()를 구현하지 않은 자식 클래스
class Pentagon(Polygon):
    def __init__(self):
        super().__init__(5)


if __name__ == "__main__":
    triangle = Triangle()
    triangle.setSideLen(300)
    print(f'{triangle.getShape()} area: {triangle.getArea()}')

    rectangle = Rectangle()
    rectangle.setSideLen(10)
    print(f'{rectangle.getShape()} area: {rectangle.getArea()}')

    try:
        pentagon = Pentagon()
    except TypeError as error:
        print(f'Pentagon 객체 생성 실패: {error}')
