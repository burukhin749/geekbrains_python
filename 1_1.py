duration = int(input('Duration: '))  # Пользователь вводит число

days = duration // 86400  # Переводим секунды в дни
hours = duration // 3600 % 24  # Переводим секунды в часы
minutes = duration // 60 % 60  # Переводим секунды в минуты
seconds = duration % 60  # Находим остаток от общего числа секунд

print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
