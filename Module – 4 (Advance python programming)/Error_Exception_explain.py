#• Explain Exception handling? What is an Error in Python

try:
    a=int(input("Enter A value : "))
    b=int(input("Enter B value : "))
    c=a/b
    print("Division : ",c)
except Exception as error:
    print("Exception caught : ",error)

