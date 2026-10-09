numbers = [4, 7, 2, 9, 6, 1, 8, 3, 5, 10]
max_number = numbers[0]
min_numbers = numbers[0]
sum_number = 0 
Not_even_numbers = 0
even_numbers = 0

for num in numbers:
    if num > max_number:
        max_number = num
    else:
        if num < min_numbers:
            min_numbers = num   

    if num %2 ==0:
        even_numbers +=1
    else:
        Not_even_numbers +=1
    
for num in numbers:
    sum_number += num

print(f"{max_number}")
print(f"{min_numbers}")
print(f"{even_numbers}")
print(f"{Not_even_numbers}")
print(f"{sum_number}")
