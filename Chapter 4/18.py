n = int(input("Enter n\n=> "))
m = int(input("Enter m\n=> "))

for i in range(1, n+1):
  if i % m == 0:
    if i % 2 == 0:
      print(f"{i}: Even")
    else:
      print(f"{i}: Odd")
