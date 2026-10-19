def get_average(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


def above_average(numbers):
    average = get_average(numbers)
    result = []

    for num in numbers:
        if num > average:
            result.append(num)

    return result


numbers = [24, 46, 11, 78, 43, 89, 87, 0]
print(above_average(numbers))
