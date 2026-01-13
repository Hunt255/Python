# 5.1. Ім'я змінної
# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

# import string
# import keyword
#
#
# input_name = input("Enter a name: ")
#
# if input_name[0].isdigit():
#     print(False)
#     exit()
#
# if input_name in keyword.kwlist:
#     print(False)
#     exit()
#
# if any(ch.isupper() for ch in input_name):
#     print(False)
#     exit()
#
# if input_name.count("_") > 1:
#     print(False)
#     exit()
#
# allowed_punctuation = string.punctuation.replace("_", "")
#
# for ch in input_name:
#     if ch in allowed_punctuation or ch == " ":
#         print(False)
#         exit()
#
# print(True)


# 5.2. Модифікувати калькулятор
# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

# print("Operations available:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
#
# while True:
#     choice = input("Select a number operation (1/2/3/4): ")
#
#     if choice in ('1', '2', '3', '4'):
#        num1 = float(input("Enter first number: "))
#        num2 = float(input("Enter second number: "))
#
#        if choice == '1':
#            print("Result:", num1 + num2)
#        elif choice == '2':
#            print("Result:", num1 - num2)
#        elif choice == '3':
#            print("Result:", num1 * num2)
#        elif choice == '4':
#            if num2 == 0:
#                print("Division by 0 is impossible")
#            else:
#                print("Result:", num1 / num2)
#     else:
#        print("Operation wrong")
#     exit_or_no = input("Enter 'y' if you want to continue: ")
#     if exit_or_no == 'y':
#         continue
#     else:
#         break


# 5.3. hashtag
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string
import keyword


input_name = input("Enter a name: ")