t = float(input("Enter the temperatures of the week separated by a space\n=> "))
t_s = t.split()
avg = (t_s[0]+t_s[1]+t_s[2]+t_s[3]+t_s[4]+t_s[5]+t_s[6])/7
print(f"Average temp for the week: {avg}")
