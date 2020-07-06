nbr_of_items = int(input("Enter the number of items you're gonna buy\n=> "))
if nbr_of_items < 0:
    print(f"Items can't be negative")
elif nbr_of_items < 10:
    print(f"Charge is: {nbr_of_items*120}")
elif nbr_of_items >= 10 and nbr_of_items <= 99:
    print(f"Charge is: {nbr_of_items*100}")
else:
    print(f"Charge is: {nbr_of_items*70}")
