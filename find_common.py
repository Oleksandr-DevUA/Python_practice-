def find_common(numbers1, numbers2):
    common_list = []

    for num in numbers1:
        if num in numbers2 and num not in common_list:
            common_list.append(num)

    return common_list


result = find_common(
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7]
)
print(result)
