try:
    a=int(input("Enter value of a : "))
    b=int(input("Enter value of b : "))
    c=a/b
    print("Division : ",c)
except Exception as error:
    print("Exception caught : ",error)
finally:
    print("Finally block always execute ")
