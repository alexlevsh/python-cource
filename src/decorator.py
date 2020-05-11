class Rectangle:
    def __init__(self, a_ret, b_ret):
        self.a_ret = a_ret
        self.b_ret = b_ret

    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.a_ret, self.b_ret)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle(%.1f)" % self.radius

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.a_ret ** 2 + rectangle.b_ret ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)


if __name__ == '__main__':
    main()
