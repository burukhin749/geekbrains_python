t = '*'
print(f'{t*35}')

prices = [41.5, 56, 150.33, 19.8,
          241.99, 2.3, 43.3, 56.44,
          45.7, 34, 9.72, 98]

# Сортировка по возрастанию (одинаковые ID)
print(id(prices))
prices.sort()
print(id(prices))

for i in prices:
    r, kk = str(f"{i:.2f}").split('.')
    print(f"{r} руб {kk} коп,", end=" ")