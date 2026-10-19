def remove_duplicates(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list


result = remove_duplicates([2, 6, 2, 7, 28, 3, 4, 8, 8, 3, 8])
print(result)
