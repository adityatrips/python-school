a = float(input("Enter side a\n=> "))
b = float(input("Enter side b\n=> "))
c = float(input("Enter side c\n=> "))

if (a+b > c) and (b+c > a) and (c+a > b):
    print("Triangle possible")
else:
    print("Triangle not possible")
