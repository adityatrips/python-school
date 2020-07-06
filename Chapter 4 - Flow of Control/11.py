a = float(input("Enter the side a\n=> "))
b = float(input("Enter the side b\n=> "))
c = float(input("Enter the side c\n=> "))

if a == b == c:
  print("Equilateral Triangle")
elif a == b or b == c or c == a:
  print("Isosceles Triangle")
else:
  print("Scalene Triangle")
