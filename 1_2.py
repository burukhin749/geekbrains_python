cube_list = []
all_sum = 0

for i in range(1, 1000, 2):
    cube_list.append(i ** 3)

for num, sum in enumerate(cube_list):
    summa = 0
    while sum > 0:
        summa += sum % 10
        sum = sum // 10
    if summa % 7 == 0:
        all_sum += cube_list[num]

print(all_sum)

all_sum = 0

for i in range(len(cube_list)):
    cube_list[i] += 17

for num, sum in enumerate(cube_list):
    summa = 0
    while sum > 0:
        summa += sum % 10
        sum = sum // 10
    if summa % 7 == 0:
        all_sum += cube_list[num]

print (all_sum)