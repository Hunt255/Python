# 7.1. Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.
from idlelib.debugobj import myrepr


# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')



# 7.2.Модифікувати рядок
# На вхід функції correct_sentence передається речення. Необхідно повернути його виправлену копію так,
# щоб воно завжди починалося з великої літери та закінчувалося крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою.
# Вхідні аргументи: string.
# Вихідні аргументи: string.

# def correct_sentence(text):
#     if not text[0].isupper():
#         text = text[0].upper() + text[1:]
#     if not text.endswith("."):
#         text += "."
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')



# 7.3. Пошук підрядка
# Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого
# рядка у рядку для пошуку.
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims".
# Якби нам треба було знайти її перше входження, то тут все просто:
# за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims",
# а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за рахунком.
# Значить індекс другого входження (і у відповідь питання) дорівнює 3.
# Рядок, який потрібно знайти, може складатися з кількох символів.
# Input: Два рядки (String).
# Output: Int or None

# def second_index(text, some_str):
#
#     first_str = text.find(some_str)
#
#     if first_str == -1:
#         return None
#
#     second_str = text.find(some_str, first_str + len(some_str))
#
#     if second_str == -1:
#         return None
#
#     return second_str
#
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# 7.4.Пошук спільних елементів
# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу
# (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

# def common_elements():
#
#     lst1 = list(range(0, 100, 3))
#     lst2 = list(range(0, 100, 5))
#
#     set1 = set(lst1)
#     set2 = set(lst2)
#
#     return set1.intersection(set2)
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


