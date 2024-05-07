#• Write a Python program to copy the contents of a file to another file.
a=open("tops.txt") :
b = a.read()
f= open("demo", "w") :
f = file.write(b)
file=open("result.txt"):
c = file.read()
print(c)
