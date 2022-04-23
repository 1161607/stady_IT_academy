print('Hello, world!')

# simple calculator

a = float(input('Введите число '))
b = float(input('Введите число '))

what = input('Выберите действие: +, -, /, * ')

if what == '+':
    c = a + b
    print('Результат = ', c)
elif what == '-':
    c = a - b
    print('Результат = ', c)
elif what == '/':
    c = a/b
    print('Результат = ', c)
elif what == '*':
    c = a * b
    print('Результат = ', c)
else:
    print('выбранное неверное действие')