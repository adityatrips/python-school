a = input("Enter x\n=> ")
x = int(a)
exp = float(a)
n = int(input("Enter n\n=> "))


for i in range(1, n+1):
  exp = exp + ((x**n)/n)

print(exp)
