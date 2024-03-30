num=int(input("Enter Number:"))
fact=1
if num<0:
    print("No Factorial Number")
elif num==0:
    print("The Factorial Number")
else:
    for i in range(1,num+1):
              fact=fact*i
    print("The Factorial of",num,"Is",fact)
             
