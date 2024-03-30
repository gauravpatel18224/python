def isPalindrome(s):
    return s == s[::-1]
s=input("Enter Text:") 
#s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
