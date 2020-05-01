date = input("Enter today's date (dd-mm)\n=> ")

date_split = date.split("-")

day = int(date_split[0])
month = str(date_split[1])

if month == '01':
    print(f"Days left: {31-day}")
elif month == '02':
    print(f"Days left: {30-day}")
elif month == '03':
    print(f"Days left: {31-day}")
elif month == '04':
    print(f"Days left: {30-day}")
elif month == '05':
    print(f"Days left: {31-day}")
elif month == '06':
    print(f"Days left: {30-day}")
elif month == '07':
    print(f"Days left: {31-day}")
elif month == '08':
    print(f"Days left: {31-day}")
elif month == '09':
    print(f"Days left: {30-day}")
elif month == '10':
    print(f"Days left: {31-day}")
elif month == '11':
    print(f"Days left: {30-day}")
elif month == '12':
    print(f"Days left: {31-day}")
