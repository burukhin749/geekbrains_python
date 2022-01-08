def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return s_n_sort


print(thesaurus_adv('Антон Иванов', 'Владимир Путин', 'Лиза Чайкина', 'Артём Писаренко',
                    'Людмилла Бабичева', 'Диана Саева', 'Олег Смирнов', 'Анатолий Левицкий',
                    'Григорий Лепс', 'Бритни Спирс', 'Кэтти Перри'))
