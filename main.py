class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        return self.a + self.b + self.c


class Parallelogram:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimetr(self):
        return 2 * (self.a + self.b)



