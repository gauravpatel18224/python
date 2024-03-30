def chars(a,b):
    A=b[:2]+a[2:]

    B=a[:2]+b[2:]

    return A+' '+B

print(chars('abc','xyz')) 
