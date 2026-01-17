# 6.1. Діапазон букв
# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

# import string
#
# letters = string.ascii_letters
#
# range_letter = input("Enter letters range in format (a-c): ")
#
# if len(range_letter) == 3:
#     first_letter, second_letter = range_letter.split("-")
#
#     if first_letter.isalpha() and second_letter.isalpha():
#         start = letters.index(first_letter)
#         end = letters.index(second_letter)
#
#         if start > end:
#             start, end = end, start
#
#         print(letters[start:end + 1])

# 6.2. Конвертер із числа в дату
# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями
# при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну
# кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)

# num = int(input("Enter a number from 1 to 8640000 : "))

# v1
#
# if 0 < num < 8640000:
#     days = num // 86400
#     hours = (num % 86400) // 3600
#     minutes = ((num % 86400) % 3600) // 60
#     seconds = ((num % 86400) % 3600) % 60
#
#     if days == 1:
#         day_word = "день"
#     elif 2 <= days <= 4:
#         day_word = "дні"
#     else:
#         day_word = "днів"
#
#     print(f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
# else:
#     print("The number is out of range!")

# v2
# if 0 < num < 8640000:
#     days, rem = divmod(num, 86400)
#     hours, rem = divmod(rem, 3600)
#     minutes, seconds = divmod(rem, 60)
#
#     if days == 1:
#         day_word = "день"
#     elif 2 <= days <= 4:
#         day_word = "дні"
#     else:
#         day_word = "днів"
#
#     print(f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
# else:
#     print("The number is out of range!")


# 6.3. Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.


# num = int(input("Enter a number: "))
#
# while num > 9:
#     s = 1
#     for element in str(num):
#         s *= int(element)
#     num = s
#
# print(num)