numbers = [5, 20, 12, 3, 18, 7, 15, 2]
max_num = 0
min_numbers = numbers[0]
max_two_num = 0

for num in numbers:
    if num > max_num:
        max_num = num

    elif min_numbers > num:
        min_numbers = num

for num in numbers:
    if num > max_two_num and num < max_num:
        max_two_num = num


print(max_two_num)