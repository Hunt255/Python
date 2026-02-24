# 15.1. Клас Прямокутник
#
# Створіть клас «Прямокутник», у якого необхідно реалізувати два поля (ширина та висота) та кілька обов'язкових методів:
# Метод порівняння прямокутників за площею.
# Метод складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).
# Методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
# У класі можуть бути створені додаткові (допоміжні методи)
# Декілька уточнень:
# Методи складання, множення, поділу тощо. обов'язково маємо повертати новий екземпляр класу Прямокутник!
# Для множення, додавання, порівняння, обов'язково потрібно перевизначати "магічні" методи. Для множення є вбудований метод mul
# Коли в результаті мат. дій створюєте новий екземпляр класу Прямокутник, то у цього екземпляру, перемноження сторін,
# має давати необхідну площу. Це теж важливо. Тобто, якщо Ви до прямокутника, у якого площа дорівнює 8, додаєте інший
# прямокутник з площею 18, необходимо створити новий прямокутник, площа якого дорівнює 26. Площа це довжина, помноженна
# на висоту. Значить необхідно підібрати сторони вновь створенного прямокутника таким чином, щоб вони давали необхідну площу!


# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             new_area = self.get_square() + other.get_square()
#             return Rectangle(1, new_area)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_area = self.get_square() * n
#             return Rectangle(1, new_area)
#         return NotImplemented
#
#     def __str__(self):
#         return f"Rectangle({self.width}, {self.height})"
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8
# assert r2.get_square() == 18
#
# r3 = r1 + r2
# assert r3.get_square() == 26
#
# r4 = r1 * 4
# assert r4.get_square() == 32
#
# assert Rectangle(3, 6) == Rectangle(2, 9)


# 15.2. Клас «Правильний дріб»
#
# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання
# та множення для екземплярів цього класу.


# class Fraction:
#     def __init__(self, a, b):
#         if b == 0:
#             raise ValueError("Denominator cannot be zero")
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def __add__(self, other):
#         return Fraction(
#             self.a * other.b + other.a * self.b,
#             self.b * other.b
#         )
#
#     def __sub__(self, other):
#         return Fraction(
#             self.a * other.b - other.a * self.b,
#             self.b * other.b
#         )
#
#     def __eq__(self, other):
#         return self.a * other.b == other.a * self.b
#
#     def __gt__(self, other):
#         return self.a * other.b > other.a * self.b
#
#     def __lt__(self, other):
#         return self.a * other.b < other.a * self.b
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')