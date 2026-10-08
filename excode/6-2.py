import math
import figure


class Triangle(figure.Polygon):
    count = 0

    def __init__(self):
        super().__init__(3)
        Triangle.count += 1
        self.serial = Triangle.count

    def getArea(self):
        return math.sqrt(3) / 4 * self.sideLen ** 2

    def getSerial(self):
        return self.serial

    def draw(self):
        import turtle

        for step in range(self.sideNumber):
            turtle.forward(self.sideLen)
            turtle.right(360 / self.sideNumber)


if __name__ == "__main__":
    triangle = Triangle()
    triangle.setSideLen(300)
    print(f'Area: {triangle.getArea()}')
    print(f'Serial: {triangle.getSerial()}')
    triangle.draw()
    input("Press Enter to stop")
