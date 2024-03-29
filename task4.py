'''Условие задачи "Самое длинное слово":
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному менеджменту.
Так как Гоша хочет спланировать день заранее, ему необходимо оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в нём ищется
самое длинное слово. Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.
'''

'''Формат ввода:
В первом элементе кортежа дана длина текста L.

Во втором элементе кортежа записан текст, состоящий из строчных латинских букв и пробелов.
Слово — последовательность букв, не разделённых пробелами.
'''

'''Формат вывода:
В первой строке выведите самое длинное слово.
Во второй строке выведите его длину. Если подходящих слов несколько, выведите то, которое встречается раньше.
'''

# Пример ввода -> вывода:
inputs = [
    ('19', 'i love segment tree'),   # -> segment, 7
    ('21', 'frog jumps from river')  # -> jumps, 5
]

# тут ваше решение:
def len_words(line: str) -> str:
    arr = line.split()
    max_length = len(arr)
    if max_length == 1:
        return ''.join(arr)
    current_word = arr[0]
    for i in range(1, max_length):
        if len(arr[i]) > len(current_word):
            current_word = arr[i]
    return current_word


def read() -> str:
    _ = input()
    line = input().strip()
    return line


def result(result: str) -> None:
    print(result)
    print(len(result))


result(len_words(read()))