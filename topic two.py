rows = int(input("Please enter the total number of rows:"))
number = 1
print("Flloyd's triangle")
for i in range(1, 1+rows):
    for j in range(1, i+1):
        print(number, end = '')
        number  = number + 1
    print()