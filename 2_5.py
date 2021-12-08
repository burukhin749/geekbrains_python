prices = [41.5, 56, 150.33, 19.8, 241.99, 2.3, 43.3, 56.44, 45.7, 34, 9.72, 98]

print(f"\n\n{'*' * 35} А_1\n")

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {kop} коп,", end=" ")
