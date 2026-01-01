#3.1. Найпростіший калькулятор
#Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
#Зробити перевірку на те, що при діленні дільник не дорівнює 0!

print("Operations available:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Select a number operation (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Division by 0 is impossible")
        else:
            print("Result:", num1 / num2)
else:
    print("Operation wrong")