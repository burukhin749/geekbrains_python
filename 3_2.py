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


def num_translate_adv(word):
    if word.istitle():
        return str(words.get(word.lower())).title()
    return words.get(word)


print(num_translate_adv(input('Введите число на английском: ')))
