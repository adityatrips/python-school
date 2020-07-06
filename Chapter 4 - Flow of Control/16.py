def reverse(s):
  return s[::-1]


def isPalindrome(s):
  if reverse(s) == s:
    print("Palindrome")
  else:
    print("Not palindrome")


s = input("Enter a string\n=> ")

isPalindrome(s)
