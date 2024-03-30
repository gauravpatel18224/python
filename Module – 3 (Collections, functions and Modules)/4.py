li=[5,8,9,10,15,47]
def max():
    a=0

    for i in li:
        if(a<i):
            a=i
    print(a,"is the largest number")

def min():
    a=0
    for i in li:
        if(a>i):
            a=i 
    print(a," is the smallest number")   

def sum():
    a=0
    for i in li:
        a+=i
    print(a," is the sum of all numbers")   


min()
max()
sum()
