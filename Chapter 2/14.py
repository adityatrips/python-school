n = int(input("Enter a number 1-7\n=> "))
if n >= 8 or n < 0:
    print("Read the instructions")
else:
    print(f"{n}{n+1}{n+2}")
