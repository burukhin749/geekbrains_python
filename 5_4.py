numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

big = [numbers[num] for num in range(1, len(numbers)) if numbers[num] > numbers[num - 1]]

print(big)
