lst = []
r = int(input("Enter how many rows?\n=> "))
c = int(input("Enter how many cols?\n=> "))
for i in range(r):
    row = []
    for j in range(c):
        el = int(input(f"Enter element at {i}, {j}: "))
        row.append(el)
    lst.append(row)

print('[')
for i in range(r):
    print('\t[ ', end=' ')
    for j in range(c):
        print(lst[i][j], end=' ')
    print(']')
print(']')
