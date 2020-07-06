x = int(input("Enter number to print odd number till that number in descending order\n=> "))

if x % 2 == 1:
    for i in range(x, 0, -2):
        print(i, end=' ')
elif x % 2 == 0:
    for i in range(x-1, 0, -2):
        print(i, end=' ')
