class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        area = self.x * self.y
        return print(f'{area}cm')

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)


retangulo1 = Retangulo(5, 8)

retangulo2 = Retangulo(7, 8)

retangulo3 = retangulo1 + retangulo2
retangulo3.get_area()
