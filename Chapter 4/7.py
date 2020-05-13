from math import sqrt
x = float(input("Enter a number to check if it's square root is a prime or not\n=> "))
sqrt_x = sqrt(x)

for i in range(2, sqrt_x//2):
    if sqrt_x % i == 0:
        print("Not a prime")
    else:
        print("Prime")
