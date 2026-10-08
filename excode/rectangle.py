import figure


class Rectangle(figure.Polygon):
    """square rectangle class"""

    def __init__(self):
        super().__init__(4)

    def getArea(self):
        return self.sideLen * self.sideLen


if __name__ == "__main__":
    r = Rectangle()
    print(r.getShape())

    sideLen = float(input("Enter side length : "))
    r.setSideLen(sideLen)
    print(r.getArea())
