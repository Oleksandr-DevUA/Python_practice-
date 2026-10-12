numbers = [3, 8, 3, 5, 8, 1, 5, 9, 1]
i = 0

while i < len(numbers):
    value = numbers[i]

    if numbers.count(value) > 1:
        while value in numbers:
            numbers.pop(numbers.index(value))
    else:
        i += 1

print(numbers)