numbers = [12, -5, 8, 0, -3, 15, 7, -10, 4, 6]

sum_number = 0
sum_number_negative = 0
max_number = None
sum_negative = 0
count = 0
digit = 0

for num in numbers:

    if num > 0:
        sum_number += num

    elif num < 0:
        sum_number_negative += num

    if num > 5:
        digit += 1

    if num % 2 == 0:
        if max_number is None or num > max_number:
            max_number = num


if num < 0:
    sum_negative += 1
    count += 1


print(f"Сума додатних чисел: {sum_number}")
print(f"Сума від'ємних чисел: {sum_number_negative}")
print(f"Найбільше парне число: {max_number}")
print(f"Кількість від'ємних чисел: {sum_negative}")
print(f"Кількість усіх чисел: {count}")
print(f"Кількість чисел, більших за 5: {digit}")
