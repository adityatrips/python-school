p = input("ENTER A STRING\n=> ")
q = input("AGAIN PLEASE\n=> ")

if len(p) > len(q):
  print(q)
  for i in range(3):
    for j in range(i+1):
      print(p[j], end=' ')
    print()

elif len(q) > len(p):
  print(p)
