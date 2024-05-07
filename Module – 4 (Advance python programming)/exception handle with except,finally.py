# How Do You Handle Exceptions With Try/Except/Finally In Python? 
#Explain with coding snippets
try:
    x = 10 / 0  
except Exception as error:
    print("Exception caught :",error)
finally:
    print("This will always execute.")

