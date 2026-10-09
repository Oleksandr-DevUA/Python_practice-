numbers = [4, 7, 2, 9, 6, 1, 8, 3, 5, 10]
Max_number = numbers[0]
Min_number = numbers[0]
for numbers in numbers:
    if numbers > Max_number:
        Max_number = numbers

    else:
        if  numbers < Min_number:
            Min_number = numbers

print(f"{Max_number}")
print(f"{Min_number}")
    

        
    