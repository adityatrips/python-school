n = list(map(float, input("Enter n\n=> ").split()))

first_interval = 0
second_interval = 0
third_interval = 0

for i in n:
  if i >= 26 and i <= 35:
    first_interval += 1
  if i >= 36 and i <= 45:
    second_interval += 1
  if i >= 46 and i <= 55:
    third_interval += 1

print(f"26-35={first_interval}")
print(f"36-45={second_interval}")
print(f"46-55={third_interval}")
