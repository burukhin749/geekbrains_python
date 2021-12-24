prices = [41.5, 56, 150.33, 19.8,
          241.99, 2.3, 43.3, 56.44,
          45.7, 34, 9.72, 98]

print(id(prices))

for i in prices:
    r, kk = str(f"{i:.2f}").split('.')
    print(f"{r} руб {kk} коп,", end=" ")

print('\n')
prices.sort()
print(id(prices))

for i in prices:
    r, kk = str(f"{i:.2f}").split('.')
    print(f"{r} руб {kk} коп,", end=" ")

print('\n')
prices_s = sorted(prices, reverse=True)
print(id(prices_s))

for i in prices_s:
    r, kk = str(f"{i:.2f}").split('.')
    print(f"{r} руб {kk} коп,", end=" ")

print('\n')

five_costs = prices[7:12]
for i in five_costs:
    r, kk = str(f"{i:.2f}").split('.')
    print(f"{r} руб {kk} коп,", end=" ")

