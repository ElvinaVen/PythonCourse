try:
    # a,b = input('Введите 2 числа:').split()
    # a,b = int(a), int(b)
    # result = a / b
    a = float(input("a = "))
    b = float(input("b = "))
    c = a / b
except ValueError:
    print('на вход принимаются только числа')
except ZeroDivisionError:
    print('второе значение не может быть равно нулю')
else:
    print(c)
finally:
    print('вычисление завершено')