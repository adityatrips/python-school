def factorial_find(num):
  factorial = 1
  if num < 0:
    print("Factorial is not available for negative numbers")
  elif num == 0:
    return 1
  else:
    for i in range(1, num+1):
      factorial = factorial*i
    return factorial


n = int(input("Enter n\n=> "))
exp = 1

for i in range(1, n+1):
  exp += (1/factorial_find(n))

print(exp)
