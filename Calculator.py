def Addition(a, b):
    s = a + b
    return print(f'\nОтвет: {s}\n')

def Subtraction(a, b):
    s = a - b
    return print(f'\nОтвет: {s}\n')

def Multiplication(a, b):
    s = a * b
    return print(f'\nОтвет: {s}\n')

def Divition(a, b):
    if b == 0:
        return print('\nНа ноль делить нельзя!\n')
    s = a / b
    return print(f'\nОтвет: {s}\n')
    
def numbers(num): #Проверка, является сторка числом.
    n = 0 
    for i in num:
        if i not in ('-1234567890'):
            n += 1

    if n == 0:
        return False
    else:
        return True

def EnterVar(n): #Вводим число
    while True:
        var = input(f'Введите число № {n}: ')
        if var =='' or numbers(var):
            print('Ошибка при вводе данных! Повторите попытку!') 
        else:
            False
            return float(var)
    
while True:
    print('Выбирете действие:\n\n 1)Сложение\n 2)Вычитание\n 3)Умножение\n 4)Деление\n 5)Выход\n')
    value = input('Ваш выбор: ')
    
    if value == '1':
        var1 = EnterVar(1)
        var2 = EnterVar(2)
        Addition(var1, var2)
    elif value == '2':
        var1 = EnterVar(1)
        var2 = EnterVar(2)
        Subtraction(var1, var2)
    elif value == '3':
        var1 = EnterVar(1)
        var2 = EnterVar(2)
        Multiplication(var1, var2)
    elif value == '4':
        var1 = EnterVar(1)
        var2 = EnterVar(2)
        Divition(var1, var2)
    elif value == '5':
        quit()
    else:
        print('Допущена ошибка! Повторите попытку!\n')
