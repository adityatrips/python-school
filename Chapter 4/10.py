res = 0
nums = list(map(float, input("Enter values separated by a space\n=> ").split()))

for num in nums:
  res += num
print(res/len(nums))
