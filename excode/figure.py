class Polygon:
    shapes = {3: 'triangle', 4: 'rectangle', 5: 'pentagon'}

    def __init__(self, numSide):
        self.sideNumber = numSide
        self.sideLen = 0

    def setSideLen(self, sideLen):
        self.sideLen = float(sideLen)

    def getShape(self):
        return Polygon.shapes[self.sideNumber]

    def getArea(self):
        pass


if __name__ == "__main__":
    print('Shape: {}'.format(Polygon.shapes[5]))

    p = Polygon(4)
    print("number of sides : {}".format(p.sideNumber))
    print("length of side : {}".format(p.sideLen))

    sideLen = float(input("Enter side length : "))
    p.setSideLen(sideLen)
    print("length of side : {}".format(p.sideLen))

    print(p.getShape())
    print(p.getArea())
