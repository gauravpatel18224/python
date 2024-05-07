#• Can one block of except statements handle multiple exception?
try:
    n = int(input("Input a number: "))
    result = 10 / n
except Exception as error:
    print("Exception caught : ",error)
