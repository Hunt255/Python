# 13.1. Група студентів
#
# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об('єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.)
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Нижче наведені заготовки, які необхідно доповнити.

# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}, {self.age} years old"
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f"Student: {self.first_name} {self.last_name}, Record book: {self.record_book}"
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def __str__(self):
#         all_students = ''
#         for student in self.group:
#             all_students += str(student) + "\n"
#
#         return f'Number:{self.number}\n{all_students}'
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!


# 13.2. Клас "Цифровий лічильник"
#
# Створити клас цифрового лічильника. У класі реалізувати методи:
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1.
# Метод можна викликати до тих пір, поки значення досягне максимуму. При досягненні максимуму слід викинути (raise)
# виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1.
# Метод можна викликати до тих пір, поки значення не досягне мінімуму. При досягненні мінімуму потрібно викинути
# (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass

# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.current = current
#
#     def set_current(self, start):
#         if start < self.min_value or start > self.max_value:
#             raise ValueError("Початкове значення поза межами лічильника")
#         self.current = start
#
#     def set_max(self, max_max):
#         if max_max < self.min_value:
#             raise ValueError("Максимум не може бути меншим за мінімум")
#         self.max_value = max_max
#         if self.current > self.max_value:
#             self.current = self.max_value
#
#     def set_min(self, min_min):
#         if min_min > self.max_value:
#             raise ValueError("Мінімум не може бути більшим за максимум")
#         self.min_value = min_min
#         if self.current < self.min_value:
#             self.current = self.min_value
#
#     def step_up(self):
#         if self.current >= self.max_value:
#             raise ValueError("Досягнуто максимуму")
#         self.current += 1
#
#     def step_down(self):
#         if self.current <= self.min_value:
#             raise ValueError("Досягнуто мінімуму")
#         self.current -= 1
#
#     def get_current(self):
#         return self.current
#
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут максимум
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут минимум
# assert counter.get_current() == 7, 'Test4'
