def flatten_list(numbers):
    i = 0
    new_list = []

    while i < len(numbers):
        for digit in numbers[i]:
            new_list.append(digit)

        i += 1

    return new_list


result = flatten_list([[1, 2], [3, 4], [5, 6]])
print(result)
