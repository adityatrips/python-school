print("Enter the subject marks separated by a space!")
marks = input()
m_split = marks.split()
avg = (
    int(m_split[0])+int(m_split[1])+int(m_split[2]) +
    int(m_split[3])+int(m_split[4])
) / 5
print(f"Average: {avg}")
