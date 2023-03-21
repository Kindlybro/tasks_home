

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError as e:
    print(f'{e} - Делить на ноль нельзя')
except ValueError as e:
    print(f'{e} - Неправильный формат входных данных')
except Exception as e:
    print(f'{e} - Непредвиденная ошибка')
finally:
    print('Как-то так')