# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі.
# Завдання 2
# Для класів із першого завдання перевизначте магічні
# методи int (повертає площу) та str (повертає інформацію
# про фігуру).
import math

class Shape:
    
    def area():
        pass

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width
    
    def area(self):
        return self._length * self._width
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}, Length: {self._length}, Width: {self._width}'

    def __int__(self):
        return int(self.area())

class Circle(Shape):
    def __init__(self, radius) -> None:
        self._radius = radius
    
    def area(self):
        return math.pi * (self._radius**2)
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}, Radius: {self._radius}'

    def __int__(self):
        return int(self.area())
    
class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self._base = base
        self._height = height
    
    def area(self):
        return 0.5 * self._base * self._height
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}, Base: {self._base}, Height: {self._height}'

    def __int__(self):
        return int(self.area())
    
class Trapezoid(Shape):
    def __init__(self, base_a, base_b, height) -> None:
        self._base_a = base_a
        self._base_b = base_b
        self._height = height
    
    def area(self):
        return 0.5 * (self._base_a + self._base_b) * self._height
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}, Base A: {self._base_a}, Base B: {self._base_b}, Height: {self._height}'

    def __int__(self):
        return int(self.area())

rectangle = Rectangle(10, 10)
circle = Circle(10)
triangle = Triangle(10, 10)
trapezoid = Trapezoid(10,10,10)

print(rectangle)
print(int(rectangle))

print(circle)
print(int(circle))

print(triangle)
print(int(triangle))

print(trapezoid)
print(int(trapezoid))