numbers = [4, 7, 4, 2, 7, 9, 2, 5, 9, 1]

for num in numbers:
    if numbers.count(num) > 1:
        numbers.remove(num)

print(numbers)


numbers = [4, 7, 4, 2, 7, 9, 2, 5, 9, 1]

i = 0
while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            numbers.pop(j)
        else:
            j += 1
    i += 1

print(numbers)