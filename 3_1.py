words = {'zero': 'ноль',
           'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять', }


def num_translate(word):
    return words.get(word)


print(num_translate(input('Введите число на английском (в нижнем регистре): ')))