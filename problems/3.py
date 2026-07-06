N = int(input("Enter the range:"))
id = list(map(int,input().split()))
special = 0

for num in id:
    if num % 3 == 0 and num % 5 == 0:
        special = special + 1
print("The count of specialnumbers between 1 and N are: ",special)