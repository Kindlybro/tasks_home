'''Условие задачи "Палиндром":
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
'''

'''Формат ввода:
В единственной строке записана фраза или слово. Буквы могут быть только латинские.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
'''

'''Формат вывода:
Выведите «True», если фраза является палиндромом, и «False», если не является.
'''

# Пример ввода -> вывода:
inputs = [
    'A man, a plan, a canal: Panama',  # -> True
    'zo',                              # -> False
    '10001',                           # -> True
    '123'                              # -> False
]

# тут ваше решение:
def palindrom(line: str) -> bool:
    line_1 = (''.join(c for c in line if c.isalnum())).lower()
    line_2 = line_1[::-1]
    if line_1 == line_2:
        return True
    return False

print(palindrom(input().strip()))