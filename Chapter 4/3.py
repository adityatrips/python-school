x = float(input("Enter x\n=> "))
y = float(input("Enter y\n=> "))

if x > y:
    if x-y == 0.001:
        print('Close')
    else:
        print('Not close')
else:
    if y-x == 0.001:
        print('Close')
    else:
        print('Not close')
