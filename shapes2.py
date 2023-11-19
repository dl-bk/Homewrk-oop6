# Створіть базовий клас Shape для рисування плоских фігур.
# Визначте методи:
# ■ Show() — виведення на екран інформації про фігуру;
# ■ Save() — збереження фігури у файл;
# ■ Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# ■ Square — квадрат із заданими з координатами лівого
# верхнього кута та довжиною сторони.
# ■ Rectangle — прямокутник із заданими координатами
# верхнього лівого кута та розмірами.

# ■ Circle — коло із заданими координатами центру та радіусом.
# ■ Ellipse — еліпс із заданими координатами верхнього кута
# описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
# фігуру

import pickle

class Shape():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Show(self):
        print(f"\nShape:{self.__class__.__name__}\nCoordinates: ({self.x}, {self.y})")

    def Save(self, filename):
        with open(filename, 'wb') as wfile:
            pickle.dump(self, wfile)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'rb') as rfile:
            return pickle.load(rfile)

class Square(Shape):
    def __init__(self, x, y, side) -> None:
        super().__init__(x, y)
        self._side = side
    
    def Show(self):
        super().Show()
        print(f"Side Length: {self._side}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height
    
    def Show(self):
        super().Show()
        print(f"Width: {self._width}, Height: {self._height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius

    def Show(self):
        super().Show()
        print(f"Radius: {self._radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height
    
    def Show(self):
        super().Show()
        print(f"Width of the circumscribed rectangle: {self._width}, Height of the circumscribed rectangle: {self._height}")


figures = [
    Square(0, 0, 5),
    Rectangle(2, 2, 4, 6),
    Circle(1, 1, 3),
    Ellipse(3, 3, 5, 2)
]

for i, figure in enumerate(figures):
    figure.Save(f'figure_{i}.pkl')

loaded_figures = [Shape.Load(f"figure_{i}.pkl") for i  in range(len(figures))]

for figure in loaded_figures:
    figure.Show()