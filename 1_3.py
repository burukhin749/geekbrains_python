for p in range(101):
    if p % 10 == 1 and p % 100 != 11:
        print(p, 'процент')
    elif 1 < p % 10 < 5 and not 11 < p % 100 < 15:
        print(p, 'процента')
    else:
        print(p, 'процентов')
