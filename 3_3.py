def thesaurus(*args):
    names = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names:
            names[letter] = names[letter] + [i]
        else:
            names[letter] = [i]

    return names


print(thesaurus('Иван', 'Дмитрий', 'Олег', 'Пётр', 'Николай', 'Сергей',
                'Ольга', 'Анатолий', 'Артём', 'Алексей', 'Денис', 'Святослав',
                'Станислав', 'Инокентий', 'Альберт', 'Роман', 'Василиса', 'Надежда', ))
