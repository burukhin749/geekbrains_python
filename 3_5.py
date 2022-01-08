# Перекопированное из урока. Не выполняется, и я не понимаю, почему.

from random import choice, randrange

nouns = ['телефон', 'стол', 'стул', 'компьютер', 'дом', 'калькулятор', 'микрофон']
adverbs = ['вчера', 'позавчера', 'утром', 'днём', 'вечером', 'ночью', 'когда-то']
adjectives = ['активный', 'унылый', 'грустный', 'воодушевляющий', 'весёлый', 'игривый', 'жалкий']


def some_jokes(n, repeat=False):
    """
    Функция возвращает случайные шутки, собранные из трёх списков слов

    :param n: количество шуток
    :param repeat: уникальные/неуникальные
    :return список случайных шуток

    """

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = win(no, adv, adj)


while n and len(list_min):
    num = randrange(len(list_min))
    if repeat:
        list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adv.pop(num)}")
    else:
        list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    n -= 1
return list_of_j

print(some_jokes(10, True))
