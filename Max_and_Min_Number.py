Max_Number = 0 
Min_Number = 0


for i in range(10):
    Num = int(input("Number: "))

    if i == 0:
        Max_Number = Max_Number = Num

    else: 
        if Num > Max_Number:
            Max_Number = Num 
        
    
        if Num < Min_Number:
         Min_Number = Num  

    
    
count = Max_Number - Min_Number


print(f"{Max_Number}")
print(f"{Min_Number}")
print(f"{count}")
