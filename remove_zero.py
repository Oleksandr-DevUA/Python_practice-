numbers = [0, 4, 0, 7, 2, 0, 9, 1]

i = 0

while i < len(numbers):
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
    else:
        i += 1

print(numbers)
