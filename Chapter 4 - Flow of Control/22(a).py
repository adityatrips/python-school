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


x = int(input("Enter x\n=> "))

exp = x-((x**2)/factorial_find(2)) + ((x**3)/factorial_find(3)) + ((x**4) /
                                                                   factorial_find(4)) + ((x**5)/factorial_find(5)) + ((x**6)/factorial_find(6))

print(exp)
