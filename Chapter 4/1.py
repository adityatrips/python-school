cm = float(input("Enter a length in centimetres\n=> "))
if cm > 0:
    inch = cm / 2.54
    print(f"{cm} in inches are {inch}")
else:
    print("Length can not be negative!")
