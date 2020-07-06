temp_s = int(input("Enter the time in seconds\n=> "))
temp_conv_min = temp_s // 60
temp_conv_sec = temp_s % 60
print(f"{temp_conv_min} minutes and {temp_conv_sec} seconds")
